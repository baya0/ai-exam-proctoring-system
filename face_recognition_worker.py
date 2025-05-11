# Standard library imports
import numpy as np

# Third-party imports
import torch
import cv2
from PIL import Image
import torchvision.transforms as transforms
from scipy.spatial.distance import cosine

# PySide6 imports
from PySide6.QtCore import QRunnable, QObject, Signal
from PySide6.QtGui import QImage
import logging
from scipy.stats import entropy

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class WorkerSignals(QObject):
    finished = Signal(object)
    error = Signal(str)

class FaceRecognitionWorker(QRunnable):
    def __init__(self, image, embeddings_dict, face_detector, embedding_model,anti_spoofing_model, device):
        super().__init__()
        self.image = image
        self.embeddings_dict = embeddings_dict
        self.face_detector = face_detector
        self.embedding_model = embedding_model
        self.anti_spoofing_model = anti_spoofing_model
        self.device = device
        self.signals = WorkerSignals()
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.threshold = 0.5 # Adjust this threshold as needed

class FaceRecognitionWorker(QRunnable):
    def __init__(self, image, embeddings_dict, face_detector, embedding_model, anti_spoofing_model, device):
        super().__init__()
        self.image = image
        self.embeddings_dict = embeddings_dict
        self.face_detector = face_detector
        self.embedding_model = embedding_model
        self.anti_spoofing_model = anti_spoofing_model
        self.device = device
        self.signals = WorkerSignals()
        self.threshold = 0.5  # Adjust this threshold as needed

    def run(self):
        try:
            result = self.perform_face_recognition()
            self.signals.finished.emit(result)
        except Exception as e:
            print(f"Error in face recognition: {str(e)}")
            self.signals.error.emit(str(e))

    def perform_face_recognition(self):
        img = self.image
        faces = self.face_detector.detect_faces(img)
        if len(faces) == 0:
            print("No face detected")
            return {"result": None, "details": {"max_similarity": 0, "threshold": self.threshold, "similarities": {}}}

        face = faces[0]
        x, y, w, h = face['box']
        face_img = img[y:y+h, x:x+w]

        # Anti-spoofing check
        if self.is_spoof(face_img):
            return {"result": "SPOOF", "details": "Spoof detected"}

        face_img = cv2.resize(face_img, (160, 160))
        face_img = torch.from_numpy(face_img.transpose((2, 0, 1))).float()
        face_img = face_img.unsqueeze(0).to(self.device)
        face_img = (face_img - 127.5) / 128.0  # Normalize to [-1, 1]

        with torch.no_grad():
            embedding = self.embedding_model(face_img).cpu().numpy().flatten()

        max_similarity = -1
        predicted_id = None
        similarities = {}

        for student_id, student_embeddings in self.embeddings_dict.items():
            avg_embedding = np.mean(student_embeddings, axis=0)
            similarity = 1 - cosine(embedding, avg_embedding)
            similarities[student_id] = similarity
            if similarity > max_similarity:
                max_similarity = similarity
                predicted_id = student_id

        details = {
            "max_similarity": max_similarity,
            "threshold": self.threshold,
            "similarities": similarities
        }

        if max_similarity > self.threshold:
            return {"result": int(predicted_id), "details": details}
        else:
            return {"result": None, "details": details}

    def run(self):
        try:
            result = self.perform_face_recognition()
            self.signals.finished.emit(result)
        except Exception as e:
            print(f"Error in face recognition: {str(e)}")
            self.signals.error.emit(str(e))

    def qimage_to_numpy(self, qimage):
        qimage = qimage.convertToFormat(QImage.Format_RGB888)
        width = qimage.width()
        height = qimage.height()
        ptr = qimage.constBits()
        arr = np.array(ptr).reshape(height, width, 3)  # Reshape the data
        return arr

    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def preprocess_for_anti_spoofing(self, face_img):
     # Resize the image to 160x160 
     face_img = cv2.resize(face_img, (160, 160))
    
     # Convert to RGB if it's not already
     if len(face_img.shape) == 2:
        face_img = cv2.cvtColor(face_img, cv2.COLOR_GRAY2RGB)
    
     # Normalize pixel values to [0, 1]
     face_img = face_img.astype(np.float32) / 255.0
    
     # Expand dimensions to create a batch of size 1
     face_img = np.expand_dims(face_img, axis=0)
    
     return face_img
    

    def check_anti_spoofing(self, face_img):
     logger.debug("Starting anti-spoofing check")
     resized_face = cv2.resize(face_img, (160, 160))
     resized_face = resized_face.astype("float") / 255.0
     resized_face = np.expand_dims(resized_face, axis=0)
    
     preds = self.anti_spoofing_model.predict(resized_face)
     confidence = preds[0][0]
     logger.debug(f"Anti-spoofing confidence: {confidence}")
    
     if confidence < 0.3:
        logger.debug("Definitely real")
        return True
     elif confidence > 0.7:
        logger.debug("Definitely spoof")
        return False
     else:
        logger.debug("Uncertain result, performing additional checks")
        
        # Check for unnatural edges
        edge_score = self.check_unnatural_edges(face_img)
        
        # Analyze texture patterns
        texture_score = self.analyze_texture_patterns(face_img)
        
        # Combine scores (you may need to adjust these thresholds)
        if edge_score > 0.7 and texture_score > 0.7:
            logger.debug("Additional checks suggest real face")
            return True
        else:
            logger.debug("Additional checks suggest spoof")
            return False
        

    def is_spoof(self, face_img):
        face_img = cv2.resize(face_img, (160, 160))
        face_img = face_img.astype(np.float32) / 255.0
        face_img = np.expand_dims(face_img, axis=0)
        prediction = self.anti_spoofing_model.predict(face_img)
        return prediction[0][0] > 0.5  # Adjust threshold as needed

    def check_unnatural_edges(self, image):
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     edges = cv2.Canny(gray, 100, 200)
    
    # Calculate the percentage of edge pixels
     edge_percentage = np.sum(edges > 0) / (edges.shape[0] * edges.shape[1])
    
    # Normalize the score (you may need to adjust these thresholds)
     edge_score = 1 - (edge_percentage / 0.1)  # Assuming 10% edges is the maximum for a real face
     edge_score = max(0, min(edge_score, 1))  # Clamp between 0 and 1
    
     logger.debug(f"Edge score: {edge_score}")
     return edge_score
 
    def analyze_texture_patterns(self, image):
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Compute Local Binary Pattern (LBP)
     lbp = self.local_binary_pattern(gray, 8, 1)
    
    # Calculate histogram of LBP
     hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, 10), range=(0, 9))
     hist = hist.astype("float")
     hist /= (hist.sum() + 1e-7)
    
    # Calculate entropy of the histogram
     texture_entropy = entropy(hist)
    
    # Normalize the score (you may need to adjust these thresholds)
     texture_score = 1 - (texture_entropy / 3)  # Assuming entropy of 3 is the maximum for a real face
     texture_score = max(0, min(texture_score, 1))  # Clamp between 0 and 1
    
     logger.debug(f"Texture score: {texture_score}")
     return texture_score

    def local_binary_pattern(self, image, n_points, radius):
     y_max, x_max = image.shape
     output = np.zeros((y_max, x_max), dtype=np.uint8)
     for x in range(radius, x_max - radius):
        for y in range(radius, y_max - radius):
            center = image[y, x]
            pixels = []
            for point in range(n_points):
                theta = point * (2 * np.pi / n_points)
                x_i = int(round(x + radius * np.cos(theta)))
                y_i = int(round(y + radius * np.sin(theta)))
                if x_i == x and y_i == y:
                    continue
                pixels.append(image[y_i, x_i] >= center)
            output[y, x] = sum([2**i for i, v in enumerate(pixels) if v])
     return output