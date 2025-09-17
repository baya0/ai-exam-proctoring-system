# AI-Based Remote Exam Proctoring System

An intelligent desktop application for remote exam supervision using face recognition, anti-spoofing, and behavioral analysis techniques. Designed with privacy and real-time performance in mind, built using Python and PyQt.

---
## Features
- Face Recognition & Verification
  - Uses FaceNet and Siamese Neural Networks for accurate identity verification.
  - Matches live webcam feed with stored reference image.

- Anti-Spoofing Detection
  - Employs a transfer learning model to detect photo/video spoof attempts.
  - Ensures only real human faces are accepted.

- Behavioral Monitoring
  - Eye and mouth movement detection using OpenCV.
  - Head pose estimation and gaze direction analysis.
  - Alerts on abnormal or suspicious behavior (e.g. looking away, talking, multiple faces).

- Object Detection
  - YOLOv5 model for detecting unauthorized devices (e.g., phones, tablets).
  - Flags when more than one person is detected.

- Audio Analysis
  - Monitors ambient sound to detect possible cheating via speech.

- User Interface
  - Built with PyQt6 for exam-taker and supervisor interfaces.
  - Provides live alerts and logs for invigilators.

---

## Technologies Used

| Component            | Tool/Library         |
|----------------------|----------------------|
| Language             | Python               |
| GUI Framework        | PyQt6                |
| Face Detection       | MTCNN                |
| Face Recognition     | FaceNet + SNN        |
| Anti-Spoofing        | Transfer Learning (e.g., MobileNet) |
| Behavior Detection   | OpenCV               |
| Object Detection     | YOLOv5               |
| Sound Analysis       | PyAudio / Librosa    |

---

## System Architecture

assets/


---


## requirements 
# Core GUI Framework
PySide6>=6.7.0

# Database
mysql-connector-python>=8.0.0

# Computer Vision and Image Processing
opencv-python>=4.8.0
Pillow>=10.0.0
albumentations>=1.3.0

# Machine Learning and Deep Learning
torch>=2.0.0
torchvision>=0.15.0
tensorflow>=2.13.0
scipy>=1.11.0
numpy>=1.24.0

# Face Recognition and Detection
facenet-pytorch>=2.5.0
mtcnn>=0.1.1
dlib>=19.24.0

# Object Detection
ultralytics>=8.0.0

# Audio Processing
sounddevice>=0.4.6

# Security
bcrypt>=4.0.0

# Optional (for test files)
PyQt6>=6.5.0

---

## Screenshots
assests/screenshots/
- Login verification page
- Live face detection with status
- Alerting system in GUI
- Admin dashboard or control panel

---

## Project Scope

This system was developed as a final year graduation project for the Faculty of Mechanical and Electrical Engineering – Damascus University (2023-2024).

---
## Author 
Location: Syria   
LinkedIn: [https://www.linkedin.com/in/bayan-abo-razmeh-59b8a11a6]  
GitHub: [https://github.com/baya0]

---
