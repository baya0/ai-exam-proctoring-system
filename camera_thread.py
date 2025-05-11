import cv2
from PySide6.QtCore import QThread, Signal,Qt
from PySide6.QtGui import QImage
import numpy as np
import threading

class CameraThread(QThread):
    change_pixmap_signal = Signal(QImage)
    error_signal = Signal(str)

    def __init__(self, camera_index=0):
        super().__init__()
        self.camera_index = camera_index
        self.running = False
        self.latest_frame = None
        self.frame_lock = threading.Lock()

    def run(self):
        self.running = True
        cap = cv2.VideoCapture(self.camera_index)
        while self.running:
            ret, frame = cap.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                p = convert_to_qt_format.scaled(640, 480, Qt.AspectRatioMode.KeepAspectRatio)
                self.change_pixmap_signal.emit(p)
                with self.frame_lock:
                    self.latest_frame = frame
            else:
                self.error_signal.emit("Failed to capture frame")
                self.msleep(33)  # ~30 fps
        cap.release()

    def start_camera(self):
        if not self.isRunning():
            self.start()

    def stop_camera(self):
        self.running = False
        self.wait()

    def get_latest_frame(self):
        with self.frame_lock:
            return self.latest_frame.copy() if self.latest_frame is not None else None