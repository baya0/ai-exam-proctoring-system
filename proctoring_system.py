import cv2
import numpy as np
import dlib
from collections import deque
from datetime import datetime
from ultralytics import YOLO
from scipy.spatial import distance
import sounddevice as sd
from PySide6.QtCore import QThread, Signal,Qt,QObject,QMutex, QMutexLocker
import tensorflow as tf
import time
import os
import torch
import librosa
import sounddevice as sd



class ProctorThread(QThread):
    result_ready = Signal(dict)

    def __init__(self, proctor_system):
        super().__init__()
        self.proctor_system = proctor_system
        self.running = True
        self.mutex = QMutex()
        self.frame_data = None
        self.audio_data = None

    def run(self):
        while self.running:
            with QMutexLocker(self.mutex):
                frame = self.frame_data
                audio = self.audio_data

            if frame is not None and audio is not None:
                result = self.proctor_system.analyze_frame(frame, audio)
                self.result_ready.emit(result)

            self.msleep(33)  # Approximately 30 FPS

    def stop(self):
        self.running = False

    def update_data(self, frame, audio):
        with QMutexLocker(self.mutex):
            self.frame_data = frame
            self.audio_data = audio



class AudioClassifier(QObject):
    audio_result = Signal(str, float)
    def __init__(self):
        super().__init__()


        print("Attempting to load model...")
        model_path = 'proctor/yamnet-tensorflow2-yamnet-v1'
        print(f"Model path: {model_path}")
        print(f"Directory contents: {os.listdir(model_path)}")
        self.model = tf.saved_model.load(model_path)
        print("Model loaded successfully")
        self.sample_rate = 16000
        self.duration = 10  # Duration of each audio sample in seconds
        self.audio_thread = None
        self.latest_result = ("Unknown", 0.0)
        
        # Load class names
        with open('proctor/yamnet-tensorflow2-yamnet-v1/assets/yamnet_class_map.csv', 'r') as f:
            self.class_names = [line.strip().split(',')[2] for line in f][1:]

    def classify_audio(self):
        audio_data = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='float32')
        sd.wait()
        audio_data = audio_data.flatten()

        audio_data = tf.reshape(audio_data, [-1])

        if len(audio_data) < self.sample_rate * self.duration:
            audio_data = tf.pad(audio_data, [[0, self.sample_rate * self.duration - len(audio_data)]])
        elif len(audio_data) > self.sample_rate * self.duration:
            audio_data = audio_data[:self.sample_rate * self.duration]

        try:
            scores, embeddings, spectrogram = self.model(audio_data)
            scores = scores.numpy()
            class_scores = np.mean(scores, axis=0)
            top_class_index = np.argmax(class_scores)
            inferred_class = self.class_names[top_class_index]

            return inferred_class, class_scores[top_class_index]
        except Exception as e:
            print(f"Error during audio classification: {e}")
            return "Unknown", 0.0

    def _audio_processing_loop(self):
        while True:
            inferred_class, confidence = self.classify_audio()
            self.latest_result = (inferred_class, confidence)
            QThread.msleep(1000)  # Sleep for 1 second

    def get_latest_result(self):
        with self.lock:
            return self.latest_result

    def start_audio_processing(self):
        if self.audio_thread is None or not self.audio_thread.isRunning():
            self.audio_thread = QThread()
            self.moveToThread(self.audio_thread)
            self.audio_thread.started.connect(self._audio_processing_loop)
            self.audio_thread.start()



    def stop_audio_processing(self):
     if self.audio_thread and self.audio_thread.isRunning():
        self.audio_thread.quit()
        self.audio_thread.wait()

class ProctorSystem(QObject):
    result_ready = Signal(dict)


    def __init__(self):
        super().__init__()

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f"Using device: {self.device}")
        self.face_detector = dlib.get_frontal_face_detector()
        self.landmark_predictor = dlib.shape_predictor("proctor/models/shape_predictor_68_face_landmarks.dat")
        self.yolo_model = YOLO('proctor/models/yolov5s.pt')
        self.yolo_model.to(self.device)

        self.gaze_history = deque(maxlen=150)  # 5 seconds at 30 FPS
        self.face_history = deque(maxlen=30)  # 1 second at 30 FPS
        self.mouth_aspect_ratio_history = deque(maxlen=90)  # 3 seconds at 30 FPS
        self.no_face_counter = 0
        self.speaking_counter = 0
        self.object_history = {obj: deque(maxlen=90) for obj in ['cell phone', 'laptop', 'book']}  # 3 seconds at 30 FPS
        self.multiple_people_history = deque(maxlen=90)  # 3 seconds at 30 FPS
        self.audio_history = deque(maxlen=30)  # 30 seconds of audio history

        self.gaze_threshold = 0.3
        self.head_movement_threshold_x = 10
        self.head_movement_threshold_y = 8
        self.head_rotation_threshold = 15
        self.mouth_aspect_ratio_threshold = 0.6
        self.mouth_movement_threshold = 0.1
        self.object_detection_threshold = 0.3
        self.object_warning_threshold = 60  # 2 seconds at 30 FPS
        self.mouth_movement_warning_threshold = 80  # About 3 seconds at 30 FPS
        self.warning_count = 0
        self.max_warnings = 3

        self.sample_rate = 44100
        self.audio_duration = 1  # 1 second of audio
        self.audio_classifier = AudioClassifier()

        self.is_proctoring = False
        self.proctoring_results = {
            "start_time": None,
            "end_time": None,
            "total_frames": 0,
            "frames_with_face": 0,
            "critical_warnings": [],
            "potential_cheating_frames": 0,
            "frame_details": []
        }

        self.proctor_thread = ProctorThread(self)
        self.proctor_thread.result_ready.connect(self.handle_proctoring_result)

    def start_proctoring(self):
        self.is_proctoring = True
        self.proctoring_results["start_time"] = datetime.now().isoformat()
        self.audio_classifier.start_audio_processing()
        self.proctor_thread.start()
        print("Proctoring started")


    def stop_proctoring(self):
        self.is_proctoring = False
        self.proctoring_results["end_time"] = datetime.now().isoformat()
        self.proctor_thread.stop()
        self.proctor_thread.wait()
        self.audio_classifier.stop_audio_processing()
        print("Proctoring stopped")

    def update_frame(self, frame, audio):
     if frame is None or audio is None:
        print("Received None frame or audio in update_frame")
        return

     try:
        self.proctor_thread.update_data(frame, audio)
     except Exception as e:
        print(f"Error in update_frame: {e}")
        import traceback
        traceback.print_exc()


    def analyze_frame(self, frame, audio_data):

     try:
        if not self.is_proctoring:
            return {}

        frame_result = {
            "timestamp": datetime.now().isoformat(),
            "face_detected": False,
            "gaze_direction": None,
            "head_movement": None,
            "detected_objects": [],
            "warnings": [],
        }

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector(gray)

        if faces:
            frame_result["face_detected"] = True
            landmarks = self.landmark_predictor(gray, faces[0])

            gaze_result = self.detect_gaze(gray, landmarks)
            frame_result["gaze_direction"] = gaze_result
            self.gaze_history.append(gaze_result)

            head_result = self.detect_head_movement(landmarks, frame)
            frame_result["head_movement"] = head_result

            mouth_result = self.detect_speaking(landmarks)
            if mouth_result:
                frame_result["warnings"].append("Speaking detected")

            object_result = self.detect_objects_and_people(frame)
            frame_result["detected_objects"], person_count = object_result
            self.handle_multiple_people_detection(person_count, frame_result)
            self.handle_object_detection(frame_result["detected_objects"], frame_result)

        else:
            self.no_face_counter += 1
            if self.no_face_counter >= 150:  # 5 seconds at 30 FPS
                frame_result["warnings"].append("No face detected for 5 seconds")

        audio_result = self.analyze_audio(audio_data)
        frame_result["audio_class"] = audio_result
        frame_result["audio_confidence"] = 1.0  # or calculate a confidence score if possible
        self.audio_history.append(audio_result)
        self.check_sustained_audio_events(frame_result)

        self.update_proctoring_results(frame_result)

        return frame_result
     except Exception as e:
        print(f"Error in analyze_frame: {str(e)}")
        import traceback
        traceback.print_exc()
        return {"error": str(e)}
    


    def detect_gaze(self, gray, landmarks):
     left_eye = self.get_eye_aspect_ratio(torch.tensor([(landmarks.part(n).x, landmarks.part(n).y) for n in range(36, 42)], device=self.device))
     right_eye = self.get_eye_aspect_ratio(torch.tensor([(landmarks.part(n).x, landmarks.part(n).y) for n in range(42, 48)], device=self.device))
     ear = (left_eye + right_eye) / 2.0
     gaze_ratio = self.get_gaze_ratio(gray, landmarks)

     if ear < 0.2:
        return "blinking"
     elif gaze_ratio <= 0.8:
        return "right"
     elif gaze_ratio > 1.2:
        return "left"
     else:
        return "center"
        


    def get_eye_aspect_ratio(self, eye_landmarks):
        # GPU accelerated EAR calculation
        vert_dist1 = torch.norm(eye_landmarks[1] - eye_landmarks[5])
        vert_dist2 = torch.norm(eye_landmarks[2] - eye_landmarks[4])
        horiz_dist = torch.norm(eye_landmarks[0] - eye_landmarks[3])
        return (vert_dist1 + vert_dist2) / (2.0 * horiz_dist)

    def get_gaze_ratio(self, gray, landmarks):
        # This method remains CPU-bound due to OpenCV operations
        left_eye_region = self.get_eye_region(landmarks, [36, 37, 38, 39, 40, 41])
        right_eye_region = self.get_eye_region(landmarks, [42, 43, 44, 45, 46, 47])
        
        left_eye_frame = self.isolate_eye(gray, left_eye_region)
        right_eye_frame = self.isolate_eye(gray, right_eye_region)
        
        left_ratio = self.calculate_gaze_ratio(left_eye_frame)
        right_ratio = self.calculate_gaze_ratio(right_eye_frame)
        
        return (left_ratio + right_ratio) / 2

    def get_eye_region(self, landmarks, eye_points):
        return np.array([(landmarks.part(point).x, landmarks.part(point).y) for point in eye_points])

    def isolate_eye(self, gray, eye_region):
        height, width = gray.shape
        mask = np.zeros((height, width), np.uint8)
        cv2.fillPoly(mask, [eye_region], 255)
        eye = cv2.bitwise_and(gray, gray, mask=mask)
        
        margin = 5
        min_x = np.min(eye_region[:, 0]) - margin
        max_x = np.max(eye_region[:, 0]) + margin
        min_y = np.min(eye_region[:, 1]) - margin
        max_y = np.max(eye_region[:, 1]) + margin
        
        return eye[min_y:max_y, min_x:max_x]

    def calculate_gaze_ratio(self, eye_frame):
        height, width = eye_frame.shape
        
        left_side = eye_frame[0:height, 0:int(width/2)]
        right_side = eye_frame[0:height, int(width/2):width]
        
        left_side_avg = cv2.mean(left_side)[0]
        right_side_avg = cv2.mean(right_side)[0]
        
        if left_side_avg == 0:
            gaze_ratio = 0.1  # looking right
        elif right_side_avg == 0:
            gaze_ratio = 2  # looking left
        else:
            gaze_ratio = left_side_avg / right_side_avg
        return gaze_ratio

    def check_sustained_gaze(self):
     if len(self.gaze_history) >= 90:  # 3 seconds at 30 FPS
        away_count = self.gaze_history.count("left") + self.gaze_history.count("right")
        return away_count >= 80  # If looking away for more than ~2.7 seconds out of 3
     return False
 
    def detect_head_movement(self, landmarks, frame):
     try:
        face_points = torch.tensor([(p.x, p.y) for p in landmarks.parts()], device=self.device, dtype=torch.float32)
        self.face_history.append(face_points)
    
        if len(self.face_history) < 2:
            return "initializing"
    
        prev_points = self.face_history[-2]
        current_points = face_points
    
        movement = current_points - prev_points
        movement_x = torch.mean(movement[:, 0].float())
        movement_y = torch.mean(movement[:, 1].float())
    
        left_eye = torch.mean(current_points[36:42].float(), dim=0)
        right_eye = torch.mean(current_points[42:48].float(), dim=0)
        current_angle = torch.atan2(right_eye[1] - left_eye[1], right_eye[0] - left_eye[0])
        prev_left_eye = torch.mean(prev_points[36:42].float(), dim=0)
        prev_right_eye = torch.mean(prev_points[42:48].float(), dim=0)
        prev_angle = torch.atan2(prev_right_eye[1] - prev_left_eye[1], prev_right_eye[0] - prev_left_eye[0])
        rotation = torch.degrees(current_angle - prev_angle)
    
        if (torch.abs(movement_x) > self.head_movement_threshold_x or
            torch.abs(movement_y) > self.head_movement_threshold_y or
            torch.abs(rotation) > self.head_rotation_threshold):
            return "movement"
    
        return "stable"
     except Exception as e:
        print(f"Error in detect_head_movement: {e}")
        return "error"
    

    def detect_objects_and_people(self, frame):
     try:
        results = self.yolo_model(frame)
        detected_objects = []
        person_count = 0
        for r in results:
            for det in r.boxes.data.tolist():
                *xyxy, conf, cls = det
                if conf > self.object_detection_threshold:
                    cls_name = self.yolo_model.names[int(cls)].lower()
                    if cls_name == 'person':
                        person_count += 1
                    elif cls_name in self.object_history:
                        detected_objects.append(cls_name)
        return detected_objects, person_count
     except Exception as e:
        print(f"Error in object detection: {e}")
        return [], 0

    def handle_multiple_people_detection(self, person_count, frame_result):
        self.multiple_people_history.append(1 if person_count > 1 else 0)
        if sum(self.multiple_people_history) >= self.object_warning_threshold:
            warning = f"Multiple people detected for {self.object_warning_threshold/30:.1f} seconds"
            frame_result["warnings"].append(warning)
            self.multiple_people_history = deque([0] * 90, maxlen=90)

    def handle_object_detection(self, detected_objects, frame_result):
        for obj in self.object_history:
            if obj in detected_objects:
                self.object_history[obj].append(1)
            else:
                self.object_history[obj].append(0)
            
            if sum(self.object_history[obj]) >= self.object_warning_threshold:
                warning = f"{obj.capitalize()} detected for {self.object_warning_threshold/30:.1f} seconds"
                frame_result["warnings"].append(warning)
                self.object_history[obj] = deque([0] * 90, maxlen=90)

    def detect_speaking(self, landmarks):
     try:
        mouth_landmarks = torch.tensor([(p.x, p.y) for p in landmarks.parts()[48:68]], device=self.device, dtype=torch.float32)
    
        A = torch.norm(mouth_landmarks[2] - mouth_landmarks[10])
        B = torch.norm(mouth_landmarks[4] - mouth_landmarks[8])
        C = torch.norm(mouth_landmarks[0] - mouth_landmarks[6])
    
        aspect_ratio = (A + B) / (2.0 * C)
        self.mouth_aspect_ratio_history.append(aspect_ratio.item())
    
        if len(self.mouth_aspect_ratio_history) < 30:
            return False
    
        avg_ratio = np.mean(self.mouth_aspect_ratio_history)
        max_ratio = np.max(self.mouth_aspect_ratio_history)
    
        is_open = aspect_ratio > self.mouth_aspect_ratio_threshold
        is_movement = (max_ratio - avg_ratio) > self.mouth_movement_threshold
    
        return is_open or is_movement
     except Exception as e:
        print(f"Error in detect_speaking: {e}")
        return False
    
    def analyze_audio(self, audio_data):
     if len(audio_data.shape) > 1:
        audio_data = np.mean(audio_data, axis=1)

     spectral_centroid = librosa.feature.spectral_centroid(y=audio_data, sr=self.sample_rate)
     zero_crossing_rate = librosa.feature.zero_crossing_rate(audio_data)

     if np.mean(spectral_centroid) > 3000 and np.mean(zero_crossing_rate) > 0.1:
        return "speech"
     else:
        return "background"

    def check_sustained_audio_events(self, frame_result):
        if self.check_sustained_audio("Speech"):
            frame_result["warnings"].append("Sustained speech detected for 10 seconds")

        if self.check_sustained_audio("Turn, page"):
            frame_result["warnings"].append("Sustained page turning detected for 5 seconds")

    def check_sustained_audio(self, audio_class, duration=10):
     if len(self.audio_history) >= duration:
        return sum(1 for audio in self.audio_history[-duration:] if audio.lower() == audio_class.lower()) >= duration * 0.8
     return False
 
    def update_proctoring_results(self, frame_result):
        self.proctoring_results["total_frames"] += 1
        if frame_result["face_detected"]:
            self.proctoring_results["frames_with_face"] += 1
        if frame_result["warnings"]:
            self.proctoring_results["potential_cheating_frames"] += 1
        self.proctoring_results["frame_details"].append(frame_result)

    def get_current_results(self):
        return self.proctoring_results
    

    def handle_proctoring_result(self, result):
        self.result_ready.emit(result)



# Main execution (for testing purposes)
if __name__ == "__main__":
    proctor = ProctorSystem()
    proctor.start_proctoring()
    
    print("Initializing camera...")
    cap = cv2.VideoCapture(0)  # Use camera index 0 (usually the default camera)
    
    # Wait for the camera to initialize
    time.sleep(2)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        proctor.stop_proctoring()
        exit()
    
    print("Camera opened successfully. Starting frame processing...")
    start_time = time.time()
    frame_count = 0
    
    try:
        while time.time() - start_time < 60:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break
            
            frame_count += 1
            print(f"\nProcessing frame {frame_count}")
            
            try:
                _, frame_result = proctor.analyze_frame(frame)
                
                # Print frame analysis results
                print(f"Face detected: {frame_result['face_detected']}")
                print(f"Gaze direction: {frame_result['gaze_direction']}")
                print(f"Head movement: {frame_result['head_movement']}")
                print(f"Detected objects: {frame_result['detected_objects']}")
                print(f"Audio class: {frame_result.get('audio_class', 'Unknown')} (Confidence: {frame_result.get('audio_confidence', 0.0):.2f})")
                
                if frame_result["warnings"]:
                    print(f"Warnings: {frame_result['warnings']}")
                
            except Exception as e:
                print(f"Error processing frame: {str(e)}")
            
            # Add a small delay to reduce CPU usage
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("Interrupted by user")
    
    print("\nStopping proctoring and releasing resources...")
    cap.release()
    
    proctor.stop_proctoring()
    results = proctor.get_current_results()
    print("\nProctoring summary:")
    print(f"Total frames processed: {results['total_frames']}")
    print(f"Frames with face detected: {results['frames_with_face']}")
    print(f"Potential cheating frames: {results['potential_cheating_frames']}")
    print(f"Start time: {results['start_time']}")
    print(f"End time: {results['end_time']}")
    
    # Print the last 5 frame details
    print("\nLast 5 frame details:")
    for frame_detail in results['frame_details'][-5:]:
        print(frame_detail)