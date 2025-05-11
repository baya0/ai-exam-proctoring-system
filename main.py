from PySide6.QtWidgets import QApplication
from shared_app import SharedApp
from main_window import MainWindow
import sys
import mysql.connector
if __name__ == "__main__":
    app = SharedApp(sys.argv)

    try:
        app.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="bayan",
            database="neww"
        )
        
        app.cursor = app.connection.cursor()
    except mysql.connector.Error as err:
        print("Database error:", err)
        sys.exit(1)
   
    def close_connection():
        if app.connection:
            app.cursor.close()
            app.connection.close()

    app.aboutToQuit.connect(close_connection)
    main_window = MainWindow(app)
    app.set_main_window(main_window)  
    main_window.show()

    sys.excepthook = lambda type, value, traceback: print(f"Uncaught exception: {value}")
    sys.exit(app.exec())


