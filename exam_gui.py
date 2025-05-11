import sys
import os
import traceback
import json
from datetime import datetime
from queue import Queue
import cv2
import threading
import sounddevice as sd
import mysql.connector
import numpy as np
import queue

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, 
    QRadioButton, QButtonGroup, QMessageBox, QGraphicsScene, QHBoxLayout
)
from PySide6.QtCore import Slot, Qt, QTimer, QDateTime,QThread, Signal
from PySide6.QtGui import QPixmap, QImage, QFont

from ui.ui_doexam import Ui_examwidgete
from camera_thread import CameraThread
from proctoring_system import ProctorSystem



class VideoRecorder(QThread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.is_recording = False

    def run(self):
        cap = cv2.VideoCapture(0)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.filename, fourcc, 20.0, (width, height))
        self.is_recording = True

        while self.is_recording:
            ret, frame = cap.read()
            if ret:
                out.write(frame)

        cap.release()
        out.release()

    def stop(self):
        self.is_recording = False
        self.wait()


class ExamGui(QWidget):
    def __init__(self, app, exam_id, student_id,camera_thread):
        print(f"ExamGui __init__ called with: app={app}, exam_id={exam_id}, student_id={student_id}, camera_thread={camera_thread}")
        super().__init__()
        print("Initializing ExamGui")
        self.app = app
        self.ui = Ui_examwidgete()
        self.ui.setupUi(self)
        self.cursor = app.connection.cursor() 
        self.exam_id = exam_id
        self.student_id = student_id
        self.student_exam_id = None
        self.camera_thread =  camera_thread
        print(f"Exam ID: {exam_id}, Student ID: {student_id}")
        self.note_edit = self.ui.note_edit

        
        self.warning_count = 0
        self.max_warnings = 3
        self.warn_label = self.ui.warnlabel  

        self.video_recorder = None
        self.video_path = None
        self.proctoring_queue = Queue()

        self.proctoring_system = ProctorSystem()
        self.proctoring_system.result_ready.connect(self.handle_proctoring_result)

        if self.ui.scrollAreaWidgetContents.layout() is None:
            self.ui.scrollAreaWidgetContents.setLayout(QVBoxLayout())
            self.ui.scrollAreaWidgetContents.setLayoutDirection(Qt.RightToLeft)
        
        self.setupComponents()      
        self.setupCamera()
        self.connectSignals()
        self.loadExamTemplate()
        self.start_exam()


            # Audio setup
        self.audio_queue = queue.Queue()
        self.audio_thread = threading.Thread(target=self.audio_capture_thread, daemon=True)
        self.audio_thread.start()

    def setupComponents(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.remaining_time = 900  # 15 minutes in seconds
        self.timer.start(1000)  # Update every second   

    def updateTimer(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.timer.stop()
            self.submit_exam()
        else:
            minutes, seconds = divmod(self.remaining_time, 60)
            self.ui.lcdNumber.display(f"{minutes:02d}:{seconds:02d}")

    def connectSignals(self):
        self.ui.submitBtn.clicked.connect(self.on_submit_button_clicked)
        self.ui.noteBtn.clicked.connect(self.submitNote)

    def setupCamera(self):
        self.camera_thread.change_pixmap_signal.connect(self.updateCameraView)
        self.scene = QGraphicsScene()
        self.ui.camera_label.setScene(self.scene)


    @Slot(QImage)
    def updateCameraView(self, image):
     try:
        if image is None:
            print("Received None image in updateCameraView")
            return

        pixmap = QPixmap.fromImage(image)
        self.scene.clear()
        self.scene.addPixmap(pixmap)
        self.ui.camera_label.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
        
        frame = self.qimage_to_numpy(image)
        if frame is None:
            print("Failed to convert QImage to numpy array")
            return

        audio_data = self.get_audio_data()
        result = self.proctoring_system.update_frame(frame, audio_data)
        if isinstance(result, dict) and "error" in result:
            print(f"Error in proctoring: {result['error']}")
     except Exception as e:
        print(f"Error in updateCameraView: {str(e)}")
        import traceback
        traceback.print_exc()

    @staticmethod
    def qimage_to_numpy(qimage):
     try:
        qimage = qimage.convertToFormat(QImage.Format_RGB888)
        width = qimage.width()
        height = qimage.height()
        buffer = qimage.constBits()
        if buffer is None:
            print("Failed to get image buffer")
            return None
        img_array = np.frombuffer(buffer, np.uint8).reshape((height, width, 3)).copy()
        return img_array
     except Exception as e:
        print(f"Error in qimage_to_numpy: {e}")
        return None

    def audio_capture_thread(self):
     def audio_callback(indata, frames, time, status):
        if status:
            print(f"Audio callback status: {status}", file=sys.stderr)
        try:
            self.audio_queue.put(indata.copy())
        except Exception as e:
            print(f"Error in audio callback: {e}")
 
     try:
        with sd.InputStream(callback=audio_callback, 
                            channels=1, 
                            samplerate=self.proctoring_system.sample_rate):
            while True:
                sd.sleep(1000)  # Sleep for 1 second
     except Exception as e:
        print(f"Error in audio capture thread: {e}")

    def get_audio_data(self):
     try:
        return self.audio_queue.get_nowait()
     except queue.Empty:
        # If no audio data is available, return silence
        return np.zeros((int(self.proctoring_system.sample_rate), 1), dtype=np.float32)
     except Exception as e:
        print(f"Error in get_audio_data: {e}")
        return np.zeros((int(self.proctoring_system.sample_rate), 1), dtype=np.float32)

    def start_exam(self):
        try:
            query = """
            INSERT INTO studentexams (student_id, exam_id, start_time)
            VALUES (%s, %s, NOW())
            """
            self.app.cursor.execute(query, (self.student_id, self.exam_id))
            self.student_exam_id = self.app.cursor.lastrowid
            self.app.connection.commit()
            print(f"Exam started. student_exam_id: {self.student_exam_id}")
            
            # Start video recording
            video_dir = "exam_videos"
            os.makedirs(video_dir, exist_ok=True)
            self.video_path = os.path.join(video_dir, f"exam_{self.student_exam_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi")
            self.video_recorder = VideoRecorder(self.video_path)
            self.video_recorder.start()
            
            self.proctoring_system.start_proctoring()
            
            # Initialize and start proctoring thread
            self.proctoring_system.result_ready.connect(self.handle_proctoring_result)
            self.proctoring_system.start_proctoring()

        except mysql.connector.Error as err:
            print(f"Error starting exam: {err}")
            QMessageBox.critical(self, "Error", f"Failed to start exam: {err}")
        except Exception as e:
            print(f"Unexpected error in start_exam: {e}")
            print(f"Error traceback: {traceback.format_exc()}")
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {str(e)}")

    def loadExamTemplate(self):
        try:
            query = """
            SELECT id, question_text, option_a, option_b, option_c, option_d
            FROM exam_templates
            WHERE exam_id = %s
            ORDER BY id
            """
            self.cursor.execute(query, (self.exam_id,))
            questions = self.cursor.fetchall()
            print(f"Fetched {len(questions)} questions")

            layout = self.ui.scrollAreaWidgetContents.layout()
            
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            for index, question in enumerate(questions, start=1):
                self.create_question_widget(layout, index, *question)

        except mysql.connector.Error as err:
            print(f"Error loading exam template: {err}")
            QMessageBox.critical(self, "Error", f"Failed to load exam template: {err}")

    def create_question_widget(self, layout, question_number, question_id, question_text, option_a, option_b, option_c, option_d):
        question_widget = QWidget()
        question_layout = QVBoxLayout(question_widget)

        question_label = QLabel(f"Question {question_number}:\n{question_text}")
        question_layout.addWidget(question_label)

        button_group = QButtonGroup(question_widget)
        button_group.setProperty("question_id", question_id)
        button_group.setProperty("question_number", question_number)
        options = [
            ('A', option_a),
            ('B', option_b),
            ('C', option_c),
            ('D', option_d)
        ]
        for i, (letter, option_text) in enumerate(options):
            radio_button = QRadioButton(f"{letter}. {option_text}")
            question_layout.addWidget(radio_button)
            button_group.addButton(radio_button, i)

        layout.addWidget(question_widget)

    def collect_answers(self):
        answers = {}
        layout = self.ui.scrollAreaWidgetContents.layout()
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, QWidget):
                button_group = widget.findChild(QButtonGroup)
                if button_group and button_group.checkedButton():
                    question_id = button_group.property("question_id")
                    question_number = button_group.property("question_number")
                    answer = button_group.checkedButton().text()[0]
                    answers[question_id] = answer
                    print(f"Question {question_number} (ID: {question_id}): {answer}")
        return answers

    def submit_exam(self, terminated=False):
        if self.student_exam_id is None:
            print("Error: Exam was not properly started.")
            return

        notes = self.note_edit.toPlainText()
        answers = self.collect_answers()
        score = self.calculate_score(answers) if not terminated else 0
    
        try:
            query = """
            UPDATE studentexams
            SET note_text = %s, marks = %s, terminated_due_to_cheating = %s, end_time = NOW()
            WHERE id = %s
            """
            self.app.cursor.execute(query, (notes, score, terminated, self.student_exam_id))
            self.app.connection.commit()
            
            if not terminated:
                QMessageBox.information(self, "Success", f"Exam submitted successfully! Your score: {score}")
            
            self.save_proctoring_data()
            self.stop_recording()
            self.close()
        except mysql.connector.Error as err:
            print(f"Error submitting exam: {err}")
            QMessageBox.critical(self, "Error", f"Failed to submit exam. Error: {err}")

    def save_proctoring_data(self):
        if self.student_exam_id is None:
            print("Error: student_exam_id is not set")
            return

        proctoring_results = self.proctoring_system.get_current_results()
        try:
            # Save overall proctoring summary
            summary_query = """
            INSERT INTO proctoringdata (student_exam_id, timestamp, data_type, data_value)
            VALUES (%s, %s, %s, %s)
            """
            self.app.cursor.execute(summary_query, (
                self.student_exam_id, 
                datetime.now().isoformat(), 
                "proctoring_summary", 
                json.dumps(proctoring_results)
            ))
            self.app.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error saving proctoring summary: {err}")
              
    def handle_proctoring_result(self, result):
     if "warnings" in result and result["warnings"]:
        for warning in result["warnings"]:
            self.warning_count += 1
            warning_message = f"Warning {self.warning_count}/{self.max_warnings}: {warning}"
            self.display_warning(warning_message)
            print(f"Warning: {warning}")  # For debugging
            
            if self.warning_count >= self.max_warnings:
                self.end_exam_due_to_cheating()
                return  # Exit the method to prevent further processing
        
        self.save_proctoring_event(result)
    
    # Process other proctoring results if needed
     if "gaze_direction" in result:
        print(f"Gaze direction: {result['gaze_direction']}")
     if "head_movement" in result:
        print(f"Head movement: {result['head_movement']}")
     if "detected_objects" in result:
        print(f"Detected objects: {result['detected_objects']}")
     if "audio_class" in result:
        print(f"Audio class: {result['audio_class']}")


    def save_proctoring_event(self, result):
        try:
            query = """
            INSERT INTO proctoringdata (student_exam_id, timestamp, data_type, data_value)
            VALUES (%s, %s, %s, %s)
            """
            for warning in result["critical_warnings"]:
                self.app.cursor.execute(query, (
                    self.student_exam_id,
                    datetime.now().isoformat(),
                    "critical_warning",
                    warning
                ))
            self.app.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error saving proctoring event: {err}")



    def display_warning(self, message):
     self.warn_label.setText(message)
     self.warn_label.setStyleSheet("color: red; font-weight: bold;")
     print(f"Displaying warning: {message}")  # Add this line for debugging
     QTimer.singleShot(5000, self.clear_warning)  # Clear warning after 5 seconds

    def clear_warning(self):
     self.warn_label.clear()
     self.warn_label.setStyleSheet("")

    def end_exam_due_to_cheating(self):
     self.proctoring_system.stop_proctoring()
     self.display_warning("The exam has been terminated due to multiple violations.")
     self.submit_exam(terminated=True)
     self.save_proctoring_data()  # Save final proctoring data
     QTimer.singleShot(5000, self.close)  # Close the exam window after 5 seconds

    def on_submit_button_clicked(self):
        self.proctoring_system.stop_proctoring()
        self.submit_exam(terminated=False)

    def calculate_score(self, answers):
        score = 0
        correct_answers = self.get_correct_answers()
        print(f"Correct answers: {correct_answers}")
        print(f"Student answers: {answers}")
        
        for question_id, answer in answers.items():
            if question_id in correct_answers:
                if answer == correct_answers[question_id]:
                    score += 1
                    print(f"Correct answer for question ID {question_id}")
                else:
                    print(f"Incorrect answer for question ID {question_id}. Given: {answer}, Correct: {correct_answers[question_id]}")
            else:
                print(f"No correct answer found for question ID {question_id}")
        
        final_score = (score / len(correct_answers)) * 100 if correct_answers else 0
        print(f"Final score: {final_score}")
        return final_score
    
    def get_correct_answers(self):
        try:
            query = """
            SELECT id, correct_answer 
            FROM exam_templates
            WHERE exam_id = %s
            ORDER BY id
            """
            self.app.cursor.execute(query, (self.exam_id,))
            return {row[0]: row[1] for row in self.app.cursor.fetchall()}
        except mysql.connector.Error as err:
            print(f"Error fetching correct answers: {err}")
            return {}

    def submitNote(self):
        note_text = self.note_edit.toPlainText()
        if not note_text:
            QMessageBox.warning(self, "Empty Note", "Please enter a note before submitting.")
            return

        try:
            query = """
            UPDATE studentexams
            SET note_text = %s
            WHERE id = %s
            """
            self.app.cursor.execute(query, (note_text, self.student_exam_id))
            self.app.connection.commit()
            QMessageBox.information(self, "Success", "Note submitted successfully!")
            self.note_edit.clear()
        except mysql.connector.Error as err:
            print(f"Error submitting note: {err}")
            QMessageBox.critical(self, "Error", f"Failed to submit note: {err}")

    def closeEvent(self, event):
     print("ExamGui closeEvent called")
     if hasattr(self, 'proctoring_system'):
        self.proctoring_system.stop_proctoring()
     if hasattr(self, 'camera_thread') and self.camera_thread:
        self.camera_thread.change_pixmap_signal.disconnect(self.updateCameraView)
     if hasattr(self, 'video_recorder') and self.video_recorder:
        self.video_recorder.stop()
     if hasattr(self, 'audio_thread'):
        self.audio_thread.join(timeout=1)  # Give the audio thread 1 second to finish
     super().closeEvent(event)


    def stop_recording(self):
        if self.video_recorder:
            self.video_recorder.stop()

    def __del__(self):
        print("ExamGui is being deleted")
        self.closeEvent(None)