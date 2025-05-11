import os ,time
from typing import List, Tuple
import pickle
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
import traceback

# PySide6 imports
from PySide6.QtWidgets import (
    QDialog, QLabel, QMessageBox, QVBoxLayout, 
    QComboBox, QDialogButtonBox, QGraphicsScene
)
from PySide6.QtCore import Qt, Slot, QTimer, QThreadPool,QThread,Signal
from PySide6.QtGui import QImage, QPixmap

# Local imports
from ui.ui_catch_pic import Ui_Form
from face_recognition_worker import FaceRecognitionWorker
from exam_gui import ExamGui
from tensorflow.keras.models import model_from_json

class EmbeddingLoader(QThread):
    finished = Signal(object)
    progress = Signal(int, int)  # current, total
    error = Signal(str)

    def __init__(self, app, device, embedding_model):
        super().__init__()
        self.app = app
        self.device = device
        self.embedding_model = embedding_model
        self.cache_file = "embeddings_cache.pkl"
        self.timeout = 300000  # 5 minutes timeout

    def run(self):
        try:
            embeddings = self.load_embeddings()
            print(f"Embeddings in EmbeddingLoader before emitting: {len(embeddings)}")
            self.finished.emit(embeddings)
        except Exception as e:
            print(f"Error in EmbeddingLoader: {str(e)}")
            self.error.emit(str(e))

    def load_embeddings(self):
        # Check if cache exists and is not older than 24 hours
        if os.path.exists(self.cache_file) and (time.time() - os.path.getmtime(self.cache_file) < 86400):
            print("Loading embeddings from cache...")
            with open(self.cache_file, 'rb') as f:
                embeddings_dict = pickle.load(f)
            print(f"Loaded {len(embeddings_dict)} embeddings from cache")
            return embeddings_dict

        print("Cache not found or outdated. Loading embeddings from database...")
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
         total_students = self.app.cursor.rowcount
         print(f"Total students found in database: {total_students}")
         for id_number, photo_url in self.app.cursor.fetchall():
            print(f"Processing student {id_number}: {photo_url}")
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
                        print(f"Embedding added for student {id_number}")
                else:
                    print(f"Warning: No face detected for student {id_number}: {photo_url}")
            else:
                print(f"Warning: File not found for student {id_number}: {photo_url}")
        
         print(f"Embeddings loaded for {len(embeddings_dict)} students")

                 # Save embeddings to cache
         with open(self.cache_file, 'wb') as f:
            pickle.dump(embeddings_dict, f)
         print(f"Saved {len(embeddings_dict)} embeddings to cache")
        except mysql.connector.Error as err:
         print(f"Error loading embeddings: {err}")



        return embeddings_dict


class TakePic(QDialog):
    def __init__(self, app, ui_loader, camera_thread,exam_id,logged_in_student_id):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.app = app
        self.ui_loader = ui_loader
        self.exam_id = exam_id
        self.logged_in_student_id = logged_in_student_id
        self.camera_thread = camera_thread
        self.thread_pool = QThreadPool() 
        self.setup_anti_spoofing() 
        print(f"TakePic initialized with camera_thread: {self.camera_thread}")

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f"Using device: {self.device}")
        
        self.setup_ui()
        self.setup_camera()
        self.setup_face_recognition()
        self.setup_anti_spoofing()
        self.start_embedding_loader()
        self.embeddings_dict = {}
        self.embeddings_loaded = False


    def setup_ui(self):
        self.scene = QGraphicsScene()
        self.ui.camerav.setScene(self.scene)
        
        self.loading_indicator = QLabel("Loading face recognition data...", self)
        self.loading_indicator.setAlignment(Qt.AlignCenter)
        self.loading_indicator.setStyleSheet("background-color: rgba(0, 0, 0, 128); color: white; font-weight: bold;")
        self.loading_indicator.setGeometry(self.rect())

        self.progress_label = QLabel("Loading embeddings: 0%", self)
        self.progress_label.setAlignment(Qt.AlignCenter)
        self.progress_label.setStyleSheet("background-color: rgba(0, 0, 0, 128); color: white; font-weight: bold;")
        self.progress_label.setGeometry(self.rect())
        self.progress_label.hide()

        self.ui.okBtn.clicked.connect(self.handle_ok)
        self.ui.cancelBtn.clicked.connect(self.handle_cancel)
        self.ui.okBtn.setEnabled(False)  # Disable the OK button initially

    def setup_anti_spoofing(self):
        root_dir = os.getcwd()
        json_file_path = os.path.join(root_dir, 'proctor', 'FaceAntispoofing', 'antispoofing_models', 'antispoofing_model.json')
        weights_file_path = os.path.join(root_dir, 'proctor', 'FaceAntispoofing', 'antispoofing_models', 'antispoofing_model.h5')

        with open(json_file_path, 'r') as json_file:
            loaded_model_json = json_file.read()
        
        self.anti_spoofing_model = model_from_json(loaded_model_json)
        self.anti_spoofing_model.load_weights(weights_file_path)
        print("Anti-spoofing model loaded from disk")


    def setup_camera(self):
        self.camera_thread.change_pixmap_signal.connect(self.update_image)
        self.camera_thread.error_signal.connect(self.handle_camera_error)
        self.camera_thread.start_camera()

    def setup_face_recognition(self):
        self.embedding_model = InceptionResnetV1(pretrained='vggface2').eval().to(self.device)
        self.face_detector = MTCNN()
        self.embeddings_dict = {}
        
 #starts a separate thread for loading face embeddings from the database
    def start_embedding_loader(self):
        self.embedding_loader = EmbeddingLoader(self.app, self.device, self.embedding_model)
        self.embedding_loader.finished.connect(self.on_embeddings_loaded)
        self.embedding_loader.progress.connect(self.update_progress)
        self.embedding_loader.error.connect(self.handle_embedding_error)
        self.embedding_loader.start()
        self.progress_label.show()
        print("Embedding loader started")

    def update_progress(self, current, total):
        percentage = int((current / total) * 100)
        self.progress_label.setText(f"Loading embeddings: {percentage}%")

    def handle_embedding_error(self, error_message):
        self.progress_label.hide()
        QMessageBox.warning(self, "Error", f"Failed to load embeddings: {error_message}")
        self.ui.okBtn.setEnabled(True)  # Enable the button to allow retrying

    def on_embeddings_loaded(self, embeddings):
        print(f"Received embeddings in TakePic: {len(embeddings)}")
        if isinstance(embeddings, dict):
         self.embeddings_dict = embeddings
         self.embeddings_loaded = True
         self.progress_label.hide()
         self.loading_indicator.hide()
         self.ui.okBtn.setEnabled(True)
         print(f"Embeddings loaded: {len(self.embeddings_dict)} students")
         QMessageBox.information(self, "Success", "Face recognition data loaded successfully!")
        else:
         print(f"Received unexpected type for embeddings: {type(embeddings)}")
         self.handle_embedding_error("Received invalid embeddings data")

         
    def update_image(self, image):
        pixmap = QPixmap.fromImage(image)
        self.scene.clear()
        self.scene.addPixmap(pixmap)
        self.ui.camerav.setSceneRect(pixmap.rect())

    def handle_camera_error(self, error_message):
        QMessageBox.critical(self, "Camera Error", f"Camera error: {error_message}")
        self.close()

    def handle_ok(self):
     self.check_embedding_status()
     if not self.embeddings_loaded or len(self.embeddings_dict) == 0:
        QMessageBox.warning(self, "Warning", "Face recognition data is not loaded yet. Please wait and try again.")
        return
     print(f"Current embeddings: {len(self.embeddings_dict)}")

     self.ui.okBtn.setEnabled(False)
     self.loading_indicator.setText("يتم التعرف على الوجه الرجاء الانتظار .....")
     self.loading_indicator.show()
     
#Checks if an image has been captured. If not, it shows an error message and re-enables the OK button.
     try:
            image = self.camera_thread.get_latest_frame()
            if image is None:
                self.show_error_message("لم يتم التقاط صورة !")
                self.ui.okBtn.setEnabled(True)
                self.loading_indicator.hide()
                return

            print(f"Number of embeddings before recognition: {len(self.embeddings_dict)}")
            worker = FaceRecognitionWorker(image, self.embeddings_dict, 
                                           self.face_detector, self.embedding_model, self.anti_spoofing_model, self.device)  
            worker.signals.finished.connect(self.on_face_recognition_finished)
            worker.signals.error.connect(self.handle_recognition_error)

            self.recognition_timer = QTimer(self)
            self.recognition_timer.setSingleShot(True)
            self.recognition_timer.timeout.connect(self.handle_recognition_timeout)
            self.recognition_timer.start(60000)  # 60 seconds timeout

            self.thread_pool.start(worker)
     except Exception as e:
            self.show_error_message(f"An error occurred: {str(e)}")
            self.ui.okBtn.setEnabled(True)
            self.loading_indicator.hide()

    def on_face_recognition_finished(self, result):
     self.recognition_timer.stop()
     self.loading_indicator.hide()
     self.ui.okBtn.setEnabled(True)

     # Log detailed results to terminal
     print(f"Face recognition result: {result}")

     if result["result"] == "SPOOF":
        QMessageBox.warning(self, "تحذير", "محاولة تزييف")
     elif result["result"] is not None:
        recognized_id = result["result"]
        max_similarity = result["details"]["max_similarity"]
        threshold = result["details"]["threshold"]
        
        print(f"Face recognized: Student ID {recognized_id}")
        print(f"Max similarity: {max_similarity:.4f}, Threshold: {threshold:.4f}")
        print(f"Similarities: {result['details']['similarities']}")
        
        if str(recognized_id) == str(self.logged_in_student_id):
            student_details = self.fetch_student_details(recognized_id)
            if student_details:
                id_number, first_name, last_name = student_details
                QMessageBox.information(self, "تم التعرف", f"أهلاً, {first_name} {last_name}!")
                self.open_exam_gui(id_number)
                self.accept() 
            else:
                QMessageBox.warning(self, "Warning", f"Student details not found for ID: {recognized_id}")
        else:
            QMessageBox.warning(self, "وصول ممنوع", "الوجه الذي تم التعرف عليه غير مسموحه له بالوصول")
     else:
        print("Face not recognized")
        print(f"Similarities: {result['details']['similarities']}")
        print(f"Threshold: {result['details']['threshold']:.4f}")
        QMessageBox.warning(self, "تحذير", "لم يتم التعرف على الوجه يرجى المحاولة لاحقاً")

        
    def handle_recognition_error(self, error_message):
        self.loading_indicator.hide()
        self.ui.okBtn.setEnabled(True)
        QMessageBox.critical(self, "خطأ", f"خطأ في عملية التعرف: {error_message}")

    def fetch_student_details(self, student_id):
        try:
            query = "SELECT id_number, first_name, last_name FROM users WHERE id_number = %s AND user_type = 'student'"
            self.app.cursor.execute(query, (student_id,))
            result = self.app.cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error fetching student details: {e}")
            return None
        

    def open_exam_gui(self, student_id):
     try:
        print(f"Attempting to open ExamGui with parameters:")
        print(f"  app: {self.app}")
        print(f"  exam_id: {self.exam_id}")
        print(f"  student_id: {student_id}")
        print(f"  camera_thread: {self.camera_thread}")
        
        self.exam_gui = ExamGui(self.app, self.exam_id, student_id, self.camera_thread)
        print("ExamGui instance created successfully")
        
        self.app.set_exam_gui(self.exam_gui)
        print("ExamGui set in app")
        
        self.exam_gui.setAttribute(Qt.WA_DeleteOnClose)
        self.exam_gui.show()
        print("ExamGui shown")
        
        self.camera_thread.change_pixmap_signal.disconnect(self.update_image)
        print("Camera thread disconnected from TakePic")
        
        self.close()
        print("TakePic window closed")
     except Exception as e:
        print(f"Error in open_exam_gui: {e}")
        print(f"Error type: {type(e)}")
        print(f"Error traceback: {traceback.format_exc()}")
        QMessageBox.critical(self, "Error", f"An unexpected error occurred: {str(e)}")

    def handle_cancel(self):
        self.reject()

    def handle_recognition_timeout(self):
     self.thread_pool.clear()  # Stop the worker
     self.ui.okBtn.setEnabled(True)
     self.loading_indicator.hide()
     QMessageBox.warning(self, "Timeout", "Face recognition timed out. Please try again.")

    def show_error_message(self, message):
     QMessageBox.critical(self, "Error", message, QMessageBox.Ok)


    def check_embedding_status(self):
     print(f"Current embeddings: {len(self.embeddings_dict)}")
     print(f"Embeddings loaded status: {self.embeddings_loaded}")