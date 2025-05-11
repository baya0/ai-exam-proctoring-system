from PySide6.QtWidgets import QApplication
from camera_thread import CameraThread




class SharedApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.main_window = None
        self.new_window = None
        self.connection = None
        self.cursor = None
        self.camera_thread = CameraThread()
        self.classifier = None
        self.label_encoder = None
        self.exam_gui = None
        self.Admin_Gui = None
        self.take_pic_window = None

    def set_main_window(self, window):
        self.main_window = window

    def set_new_window(self, window):
        self.new_window = window

    def set_main_window_visible(self, visible):
        if self.main_window:
            self.main_window.setVisible(visible)

    def set_Admin_Gui(self, window):
        self.Admin_Gui = window

    def set_Admin_Gui_visible(self, visible):
        if self.Admin_Gui:
            self.Admin_Gui.setVisible(visible)

    def set_take_pic_window(self, window):
        self.take_pic_window = window

    def set_exam_gui(self, exam_gui):
        self.exam_gui = exam_gui

    def logout(self):
        print("Logout process started")
        windows_to_close = [self.new_window, self.Admin_Gui, self.exam_gui, self.take_pic_window]
        for window in windows_to_close:
            if window:
                print(f"Closing window: {window.__class__.__name__}")
                window.close()
        
        # Reset window references
        self.new_window = None
        self.Admin_Gui = None
        self.exam_gui = None
        self.take_pic_window = None
        
        # Show the login window again
        if self.main_window:
            self.main_window.show()
            try:
                self.main_window.ui.idLine.clear()
                self.main_window.ui.passLine.clear()
            except AttributeError:
                print("Warning: Unable to clear login fields. UI elements might be missing.")
        
        print("Logout completed")