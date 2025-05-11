import os
from typing import List, Tuple

# Third-party imports
import numpy as np
import cv2
import torch
import torchvision.transforms as transforms
from PIL import Image
from scipy.spatial.distance import cosine
import albumentations as A
from mtcnn import MTCNN
from facenet_pytorch import InceptionResnetV1
import mysql.connector

# PySide6 imports
from PySide6.QtWidgets import (
    QDialog, QLabel, QMessageBox, QVBoxLayout, 
    QComboBox, QDialogButtonBox, QGraphicsScene
)
from PySide6.QtCore import Qt, Slot, QTimer, QThreadPool
from PySide6.QtGui import QImage, QPixmap

# Local imports
from ui.ui_catch_pic import Ui_Form
from face_recognition_worker import FaceRecognitionWorker
from exam_gui import ExamGui



class TakePic(QDialog):
    def __init__(self, app, ui_loader, camera_thread):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.app = app
        self.ui_loader = ui_loader
        self.camera_thread = camera_thread
        self.thread_pool = QThreadPool()
        self.scene = QGraphicsScene()
        self.ui.camerav.setScene(self.scene)
        self.camera_thread.change_pixmap_signal.connect(self.update_image)
        self.camera_thread.error_signal.connect(self.handle_camera_error)
        self.camera_thread.change_pixmap_signal.connect(self.update_image)
        self.camera_thread.start_camera()

        # Initialize the embedding model
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.embedding_model = InceptionResnetV1(pretrained='vggface2').eval().to(self.device)

        self.face_detector = MTCNN()
        
        # Load embeddings and assign to app
        self.embeddings_dict= self.load_embeddings()


        # Add this line to create the loading indicator
        self.loading_indicator = QLabel("جاري التعرف على الوجه...", self)
        self.loading_indicator.setAlignment(Qt.AlignCenter)
        self.loading_indicator.setStyleSheet("background-color: rgba(0, 0, 0, 128); color: white; font-weight: bold;")
        self.loading_indicator.hide()  # Hide it initially

    


    def handle_camera_error(self, error_message):
        QMessageBox.critical(self, "Camera Error", f"Camera error: {error_message}")
        self.close()

    @Slot(QImage)
    def update_image(self, image):
        pixmap = QPixmap.fromImage(image)
        self.scene.clear()
        self.scene.addPixmap(pixmap)
        self.ui.camerav.setSceneRect(pixmap.rect())  # Adjust the view to fit the image
    
    def closeEvent(self, event):
        self.camera_thread.stop_camera()
        super().closeEvent(event)

            # this method to position the loading indicator
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.loading_indicator.setGeometry(self.rect())

        self.ui.cancelBtn.clicked.connect(self.handle_cancel)
        self.ui.okBtn.clicked.connect(self.handle_ok)

        self.camera_thread.change_pixmap_signal.connect(self.update_image)

        self.scene = QGraphicsScene()
        self.ui.camerav.setScene(self.scene)

        self.embeddings_dict = self.load_embeddings()
        self.threshold = 0.5  # Adjust as needed

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message, QMessageBox.Ok)



    def handle_ok(self):
     self.ui.okBtn.setEnabled(False)
     self.loading_indicator.show()

     if not self.scene.items():
        self.show_error_message("No image captured!")
        self.ui.okBtn.setEnabled(True)
        self.loading_indicator.hide()
        return

     image = self.scene.items()[0].pixmap().toImage()
     worker = FaceRecognitionWorker(image, self.embeddings_dict, 
                                       self.face_detector, self.embedding_model)
     worker.signals.finished.connect(self.handle_recognition_result)
     worker.signals.error.connect(self.handle_recognition_error)

     self.recognition_timer = QTimer(self)
     self.recognition_timer.setSingleShot(True)
     self.recognition_timer.timeout.connect(self.handle_recognition_timeout)
     self.recognition_timer.start(30000)  # 30 seconds timeout

     self.thread_pool.start(worker)
    

    def handle_recognition_timeout(self):
        self.thread_pool.clear()  # Stop the worker
        self.ui.okBtn.setEnabled(True)
        self.loading_indicator.hide()
        self.show_error_message("Face recognition timed out. Please try again.")


    def handle_recognition_result(self, result):
     self.recognition_timer.stop()
     self.ui.okBtn.setEnabled(True)
     self.loading_indicator.hide()
    
     print(f"Recognition result: {result} (type: {type(result)})")
    
     if result is not None:
        if isinstance(result, (int, np.integer)):
            result = int(result)  # Convert numpy.int32 to standard Python int
            print(f"Recognized student ID: {result}")
            # Fetch student details from database
            student_details = self.fetch_student_details(result)
            
            print(f"Fetched student details: {student_details}")
            
            if student_details:
                try:
                    id_number, first_name, last_name = student_details
                    QMessageBox.information(self, "Recognition Successful", f"Welcome, {first_name} {last_name}!")
                    self.open_exam_gui(id_number)
                except Exception as e:
                    print(f"Error unpacking student details: {e}")
                    self.show_error_message(f"Error processing student details: {str(e)}")
            else:
                self.show_error_message("Failed to fetch student details. Please try again.")
        else:
            print(f"Unexpected result type: {type(result)}")
            self.show_error_message("Unexpected error occurred. Please try again.")
     else:
        print("Face not recognized")
        self.show_error_message("Face not recognized! Please try again.")
    
     
    def fetch_student_details(self, student_id):
     try:
        query = "SELECT id_number, first_name, last_name FROM users WHERE id_number = %s AND user_type = 'student'"
        self.app.cursor.execute(query, (student_id,))
        result = self.app.cursor.fetchone()
        print(f"Raw database result: {result}")
        return result
     except mysql.connector.Error as err:
        print(f"Error fetching student details: {err}")
        return None
     except Exception as e:
        print(f"Unexpected error in fetch_student_details: {e}")
        return None
     
    def open_exam_gui(self, student_id):
     print(f"Opening exam GUI for student ID: {student_id}")
     try:
        available_exams = self.fetch_available_exams(student_id)
        print(f"Available exams: {available_exams}")
        
        if available_exams:
            exam_id = self.show_exam_selection_dialog(available_exams)
            print(f"Selected exam ID: {exam_id}")
            if exam_id:
                try:
                    self.exam_gui = ExamGui(self.app, exam_id, student_id) 
                    self.exam_gui.show()
                    self.close()
                    
                except Exception as e:
                    print(f"Error opening ExamGui: {e}")
                    QMessageBox.critical(self, "Error", f"Failed to open exam: {str(e)}")
            else:
                print("No exam selected")
        else:
            print("No available exams")
            QMessageBox.information(self, "No Exams", "There are no available exams for you at this time.")
     except Exception as e:
        print(f"Error in open_exam_gui: {e}")
        QMessageBox.critical(self, "Error", f"An unexpected error occurred: {str(e)}")



    def fetch_available_exams(self, student_id):
     print(f"Fetching available exams for student ID: {student_id}")
     try:
        query = """
        SELECT e.id, e.exam_name 
        FROM exams e
        LEFT JOIN studentexams se ON e.id = se.exam_id AND se.student_id = %s
        WHERE se.id IS NULL
        """
        self.app.cursor.execute(query, (student_id,))
        exams = self.app.cursor.fetchall()
        print(f"Fetched exams: {exams}")
        return exams
     except mysql.connector.Error as err:
        print(f"Error fetching available exams: {err}")
        return []

    def show_exam_selection_dialog(self, available_exams):
     print("Showing exam selection dialog")
     dialog = QDialog(self)
     dialog.setWindowTitle("Select Exam")
     layout = QVBoxLayout()

     combo_box = QComboBox()
     for exam_id, exam_name in available_exams:
        combo_box.addItem(exam_name, exam_id)
     layout.addWidget(combo_box)

     button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
     button_box.accepted.connect(dialog.accept)
     button_box.rejected.connect(dialog.reject)
     layout.addWidget(button_box)

     dialog.setLayout(layout)

     if dialog.exec_() == QDialog.Accepted:
        selected_exam_id = combo_box.currentData()
        print(f"Selected exam ID: {selected_exam_id}")
        return selected_exam_id
     print("No exam selected")
     return None

    def handle_recognition_error(self, error_message):
        self.recognition_timer.stop()
        self.ui.okBtn.setEnabled(True)
        self.loading_indicator.hide()
        self.show_error_message(f"Error: {error_message}")
     

    def handle_cancel(self):
        self.reject()


    def load_embeddings(self):
     embeddings_dict = {}
    
    # Define augmentations
     augmentations = A.Compose([
        A.RandomBrightnessContrast(p=0.5),
        A.RandomRotate90(p=0.5),
        A.HorizontalFlip(p=0.5),
        A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.1, rotate_limit=15, p=0.5),
     ])
  
     transform = transforms.Compose([
        transforms.Resize((160, 160)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
     ])

     face_detector = MTCNN()
 
     try:
        query = "SELECT u.id_number, p.photo_url FROM users u JOIN user_photos p ON u.id_number = p.user_id WHERE u.user_type = 'student'"
        self.app.cursor.execute(query)
        for id_number, photo_url in self.app.cursor.fetchall():
            if os.path.isfile(photo_url):
                img = cv2.imread(photo_url)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
                faces = face_detector.detect_faces(img)
                if len(faces) > 0:
                    face = faces[0]
                    x, y, w, h = face['box']
                    face_img = img[y:y+h, x:x+w]
                    
                    # Apply augmentations
                    for _ in range(3):  # Create 3 augmented versions of each image
                        augmented = augmentations(image=face_img)
                        aug_face_img = augmented['image']
                        
                        aug_face_img = Image.fromarray(aug_face_img)
                        aug_face_img = transform(aug_face_img).unsqueeze(0).to(self.device)
                        
                        with torch.no_grad():
                            embedding = self.embedding_model(aug_face_img).cpu().numpy().flatten()
                        
                        if id_number not in embeddings_dict:
                            embeddings_dict[id_number] = []
                        embeddings_dict[id_number].append(embedding)
                else:
                    print(f"Warning: No face detected for student {id_number}: {photo_url}")
            else:
                print(f"Warning: File not found for student {id_number}: {photo_url}")
     except mysql.connector.Error as err:
        print(f"Error loading embeddings: {err}")
    
     return embeddings_dict

