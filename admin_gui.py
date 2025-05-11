# Standard library imports
import os
import shutil

# Third-party imports
import mysql.connector
import bcrypt

# PySide6 imports
from PySide6.QtWidgets import (
    QMainWindow, QMessageBox, QFileDialog, QListWidget, 
    QWidget, QVBoxLayout, QLabel, QRadioButton, QButtonGroup,
    QTableWidgetItem
)
from PySide6.QtCore import Qt

# Local imports
from ui.ui_AdminGui import Ui_AdminWindow

class AdminGui(QMainWindow):
    def __init__(self, app, ui_loader):
        super().__init__()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)
        self.app = app
        self.ui_loader = ui_loader
        self.exam_templates = {}

        
        self.initialize_ui()
        self.connect_signals()

    def initialize_ui(self):
        self.populate_student_ids()
        self.populate_exam_selectors()
        self.load_exam_templates()
        self.loadNotes()
        self.ui.cb30.setEnabled(True)
        self.ui.cb31.setEnabled(True)
        self.ui.cb20.setEnabled(True)
        self.ui.cb20.setEditable(False)
        self.ui.listWidget_2.setSelectionMode(QListWidget.SingleSelection)

    def connect_signals(self):
        # Connect buttons to functions
        self.ui.btn11.clicked.connect(self.save_student_details)
        self.ui.btn10.clicked.connect(self.add_student_pictures)
        self.ui.cb20.currentIndexChanged.connect(self.fetch_student_details)
        self.ui.btn20.clicked.connect(self.update_student_details)
        self.ui.btn21.clicked.connect(self.delete_student_details)
        self.ui.btn22.clicked.connect(self.edit_student_picture)
        self.ui.btn30.clicked.connect(self.save_marks_details)
        self.ui.btn31.clicked.connect(self.fetch_exam_marks)
        self.ui.btn32.clicked.connect(self.update_exam_marks)
        self.ui.btn33.clicked.connect(self.delete_exam_marks)
        self.ui.btn60.clicked.connect(self.add_question_to_template) 
        self.ui.cb70.currentIndexChanged.connect(self.update_template_view)
        self.ui.btn70.clicked.connect(self.delete_selected_question)
        self.ui.btn12.clicked.connect(self.add_user_photos)
        self.ui.btn23.clicked.connect(self.edit_user_photos)
        self.ui.logout_btn.clicked.connect(self.logout)
        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)



    def save_student_details(self):
        try:
            first_name = self.ui.tb11.text()
            last_name = self.ui.tb12.text()
            id_number = self.ui.tb10.text()
            password = self.ui.tb15.text()
            gender = self.ui.cb10.currentText()
            phone_number = self.ui.tb13.text()
            Email = self.ui.tb14.text()


            sql = """INSERT INTO users (user_type, first_name, last_name, id_number, password, gender,phone_number,Email) 
                     VALUES ('student', %s, %s, %s, %s, %s,%s,%s)"""
            self.app.cursor.execute(sql, (first_name, last_name, id_number, password, gender,phone_number,Email))
            self.app.connection.commit()

            QMessageBox.information(self, "Success", "Student details saved successfully!")
        except mysql.connector.Error as err:
             QMessageBox.critical(self, "Error", f"Failed to save: {err}")
           
           
    def add_student_pictures(self):
        try:
           # Open file dialog
           file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")

           if file_name:
            # Get student ID
            id_number = self.ui.cb20.currentText()

            # Connect to database if not already connected
            if not self.app.connection.isconnected():
                self.app.connection.connect()

            # Update profile picture URL in database
            sql = "UPDATE users SET profile_picture_url = %s WHERE id_number = %s AND user_type = 'student'"
            self.app.cursor.execute(sql, (file_name, id_number))
            self.app.connection.commit()

            # Update filenamelabel with the chosen file name
            self.ui.filenamelabel.setText(file_name)

            QMessageBox.information(self, "Success", "Student picture updated successfully!")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to update student picture: {err}")
        finally:
        # Close database connection if necessary
         if self.app.connection.isconnected():
            self.app.connection.close()
    
    def fetch_student_details(self, student_id):
     try:
        print(f"Fetching details for student ID: {student_id} (type: {type(student_id)})")
        query = "SELECT id_number, first_name, last_name FROM users WHERE id_number = %s AND user_type = 'student'"
        self.app.cursor.execute(query, (student_id,))
        result = self.app.cursor.fetchone()
        print(f"Query result: {result}")
        
        if result:
            self.ui.tb20.setText(result[1])  # first_name
            self.ui.tb21.setText(result[2])  # last_name
            # Populate other fields as needed
        else:
            self.ui.tb20.clear()
            self.ui.tb21.clear()
            # Clear other fields as needed
            
        return result
     except mysql.connector.Error as err:
        print(f"Error fetching student details: {err}")
        return None


    def populate_student_ids(self):
     try:
        sql = "SELECT id_number FROM users WHERE user_type = 'student'"
        self.app.cursor.execute(sql)
        student_ids = [str(row[0]) for row in self.app.cursor.fetchall()]
        self.ui.cb20.clear()
        self.ui.cb20.addItems(student_ids)
        print(f"Populated student IDs: {student_ids}")
     except mysql.connector.Error as err:
        QMessageBox.critical(self, "Error", f"Failed to fetch student IDs: {err}")
     

    def update_student_details(self):
        try:
         id_number = self.ui.cb20.currentText()
         first_name = self.ui.tb20.text()
         last_name = self.ui.tb21.text()
         new_password = self.ui.tb24.text()  
         gender = self.ui.cb21.currentText()
         phone_number = self.ui.tb22.text()
         email = self.ui.tb23.text()

        # Basic validation (replace with your specific requirements)
         if not all([first_name, last_name, email]):
            QMessageBox.critical(self, "Error", "Please fill in all required fields!")
            return

        # Check if user entered a new password
         if new_password:
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
         else:
            
            hashed_password = None  # Or retrieve the existing hashed password from the database

         sql = """UPDATE users SET first_name = %s, last_name = %s, 
                   gender = %s, password = %s, phone_number = %s, email = %s 
                   WHERE id_number = %s AND user_type = 'student'"""
         self.app.cursor.execute(sql, (first_name, last_name, gender, hashed_password, phone_number, email, id_number))
         self.app.connection.commit()
         QMessageBox.information(self, "Success", "Student details updated successfully!")

        except mysql.connector.Error as err:
         if err.errno == 1062:  # Handle duplicate entry error 
            QMessageBox.critical(self, "Error", "This ID number already exists!")
        else:
            QMessageBox.critical(self, "Error", f"Failed to update student details: {err}")



    def delete_student_details(self):
        try:
            id_number = self.ui.cb20.currentText()
            confirm = QMessageBox.question(self, "Confirm Deletion", 
                                           "Are you sure you want to delete this student?",
                                           QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                sql = "DELETE FROM users WHERE id_number = %s AND user_type = 'student'"
                self.app.cursor.execute(sql, (id_number,))
                self.app.connection.commit()
                QMessageBox.information(self, "Success", "Student deleted successfully!")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to delete student: {err}")

    def edit_student_picture(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            id_number = self.ui.cb20.currentText()
            try:
                sql = "UPDATE users SET profile_picture_url = %s WHERE id_number = %s AND user_type = 'student'"
                self.app.cursor.execute(sql, (file_name, id_number))
                self.app.connection.commit()
                QMessageBox.information(self, "Success", "Student picture updated successfully!")
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Error", f"Failed to update student picture: {err}")

    def save_marks_details(self):
     try:
        # Get student ID from tb30 QLineEdit
        student_id = self.ui.tb30.text()
        # Validate student ID (optional, but recommended)
        if not student_id.isdigit():
            QMessageBox.warning(self, "Warning", "Invalid student ID. Please enter a numeric ID.")
            return

        # Get selected exam name
        exam_name = self.ui.cb30.currentText()
        if not exam_name:
            QMessageBox.warning(self, "Warning", "Please select an exam.")
            return

        # Get exam marks from tb31 QLineEdit
        marks = self.ui.tb31.text()

        # Validate marks (optional, but recommended)
        try:
            marks = float(marks)  # Convert to float for numeric validation
            if marks < 0 or marks > 100:
                QMessageBox.warning(self, "Warning", "Invalid marks. Please enter a value between 0 and 100.")
                return
        except ValueError:
            QMessageBox.warning(self, "Warning", "Invalid marks. Please enter a numeric value.")
            return

        # Get exam ID from exam name
        self.app.cursor.execute("SELECT id FROM exams WHERE exam_name = %s", (exam_name,))
        exam_result = self.app.cursor.fetchone()
        if not exam_result:
            QMessageBox.warning(self, "Warning", "Selected exam not found.")
            return
        exam_id = exam_result[0]

        # Insert marks into database
        sql = "INSERT INTO studentexams (student_id, exam_id, marks) VALUES (%s, %s, %s)"
        self.app.cursor.execute(sql, (student_id, exam_id, marks))
        self.app.connection.commit()

        QMessageBox.information(self, "Success", "Marks saved successfully!")

     except mysql.connector.Error as err:
        self.app.connection.rollback()
        QMessageBox.critical(self, "Error", f"Failed to save marks: {err}")


    def populate_exam_comboboxes(self):
     try:
        query = "SELECT exam_name FROM exams"
        self.app.cursor.execute(query)
        exam_names = [row[0] for row in self.app.cursor.fetchall()]
        
        self.ui.cb30.clear()
        self.ui.cb31.clear()
        self.ui.cb30.addItems(exam_names)
        self.ui.cb31.addItems(exam_names)
     except mysql.connector.Error as err:
        print(f"Error populating exam ComboBoxes: {err}")

    def fetch_exam_marks(self):
     try:
        student_id = self.ui.tb32.text()
        exam_name = self.ui.cb31.currentText()

        if not student_id or not exam_name:
            QMessageBox.warning(self, "Warning", "Please enter a student ID and select an exam.")
            return

        # Get the exam ID from the exam_name
        self.app.cursor.execute("SELECT id FROM exams WHERE exam_name = %s", (exam_name,))
        exam_result = self.app.cursor.fetchone()
        if not exam_result:
            QMessageBox.warning(self, "Warning", "Exam not found.")
            return
        exam_id = exam_result[0]

        # Fetch the marks
        sql = "SELECT marks FROM studentexams WHERE student_id = %s AND exam_id = %s"
        self.app.cursor.execute(sql, (student_id, exam_id))
        result = self.app.cursor.fetchone()

        if result:
            self.ui.tb33.setText(str(result[0]))
            QMessageBox.information(self, "نجاح", "تم جلب العلامة")
        else:
            self.ui.tb33.clear()
            QMessageBox.information(self, "ملاحظة", "لم نعثر على علامة لهذا الطالب و الفحص ")

     except mysql.connector.Error as err:
        QMessageBox.critical(self, "Error", f"Failed to fetch marks: {err}")
    

    def update_exam_marks(self):
     try:
        student_id = self.ui.tb32.text()
        exam_name = self.ui.cb31.currentText()
        new_marks = self.ui.tb33.text()

        if not student_id or not exam_name or not new_marks:
            QMessageBox.warning(self, "تحذير", "الرجاء ادخال جميع المعلومات المطلوبة")
            return

        # Get the exam ID from the exam_name
        self.app.cursor.execute("SELECT id FROM exams WHERE exam_name = %s", (exam_name,))
        exam_result = self.app.cursor.fetchone()
        if not exam_result:
            QMessageBox.warning(self, "تحذير", "لم نعثر على امتحان")
            return
        exam_id = exam_result[0]

        sql = "UPDATE studentexams SET marks = %s WHERE student_id = %s AND exam_id = %s"
        self.app.cursor.execute(sql, (new_marks, student_id, exam_id))
        self.app.connection.commit()

        if self.app.cursor.rowcount > 0:
            QMessageBox.information(self, "نجاح", "تم تعديل العلامة")
        else:
            QMessageBox.information(self, "Info", "لم يحدث تغيرات ، ربما السجل غير موجود")

     except mysql.connector.Error as err:
        self.app.connection.rollback()
        QMessageBox.critical(self, "Error", f"Failed to update marks: {err}")

    def delete_exam_marks(self):
     try:
        student_id = self.ui.tb32.text()
        exam_name = self.ui.cb31.currentText()

        if not student_id or not exam_name:
            QMessageBox.warning(self, "تحذير", "ادخل رقم تعريف الطالب و اختر اسم الامتحان")
            return

        # Get the exam ID from the exam_name
        self.app.cursor.execute("SELECT id FROM exams WHERE exam_name = %s", (exam_name,))
        exam_result = self.app.cursor.fetchone()
        if not exam_result:
            QMessageBox.warning(self, "تحذير", "لم نعثر على امتحان")
            return
        exam_id = exam_result[0]

        confirm = QMessageBox.question(self, "تأكيد الحذف", 
                                       "هل أنت متأكد من حذف العلامة",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            sql = "DELETE FROM studentexams WHERE student_id = %s AND exam_id = %s"
            self.app.cursor.execute(sql, (student_id, exam_id))
            self.app.connection.commit()

            if self.app.cursor.rowcount > 0:
                self.ui.tb33.clear()
                QMessageBox.information(self, "نجاح", "تم حذف العلامة")
            else:
                QMessageBox.information(self, "ملاحظة", "لايوجد علامات لتحذف")

     except mysql.connector.Error as err:
        self.app.connection.rollback()
        QMessageBox.critical(self, "Error", f"Failed to delete marks: {err}")


    # Report module
    def update_reports_table(self):
      try:
        # ... connect to database ...

        # Prepare SQL query to retrieve notes 
        sql = "SELECT users.first_name, users.last_name, exams.exam_name, studentexams.note_text, studentexams.exam_date FROM studentexams JOIN users ON studentexams.student_id = users.id JOIN exams ON studentexams.exam_id = exams.id"
        self.cursor.execute(sql)
        notes_data = self.cursor.fetchall()  # Fetch all note records

        # Clear existing table data
        self.reports_table.setRowCount(0)

        # Iterate through notes data and populate table rows
        row_count = 0
        for row in notes_data:
            full_name = f"{row[0]} {row[1]}"  # Combine first and last name for display
            exam_name, note_text, exam_date = row[2:]  # Extract remaining data
            self.reports_table.insertRow(row_count)
            self.reports_table.setItem(row_count, 0, QTableWidgetItem(full_name))
            self.reports_table.setItem(row_count, 1, QTableWidgetItem(row[1]))  # Use student ID if needed
            self.reports_table.setItem(row_count, 2, QTableWidgetItem(exam_name))
            self.reports_table.setItem(row_count, 3, QTableWidgetItem(note_text))
            self.reports_table.setItem(row_count, 4, QTableWidgetItem(exam_date.strftime("%Y-%m-%d")))  # Format date for better readability
            row_count += 1

      except (mysql.connector.Error, Exception) as err:
        print("Error while fetching notes:", err)
        # not to forget add a message box to display an error message to the admin user here



     #view student videos module
      self.video_list = QListWidget()
    # Retrieve student IDs and populate combo box
      student_ids = self.get_student_ids()
      for student_id in student_ids:
       self.student_id_combo.addItem(student_id)
    # Connect combo box selection change to slot function
       self.student_id_combo.currentIndexChanged.connect(self.update_video_list)
    def get_student_ids(self):
     sql = "SELECT id_number FROM students"
     self.cursor.execute(sql)
     student_ids = [row[0] for row in self.cursor.fetchall()]  # Extract ID from each row
     return student_ids
 
    def update_video_list(self, index):
     selected_id = self.student_id_combo.currentText()
     sql = "SELECT video_title FROM student_videos WHERE student_id = %s"
     self.cursor.execute(sql, (selected_id,))
     video_titles = [row[0] for row in self.cursor.fetchall()]  # Extract title from each row
     self.video_list.clear()
     for title in video_titles:
        self.video_list.addItem(title)
    #/////////////////////////////////////////tab_6
    def populate_exam_selectors(self):
     try:
        query = "SELECT id, exam_name FROM exams"
        self.app.cursor.execute(query)
        exams = self.app.cursor.fetchall()
        
        # Clear existing items
        self.ui.cb30.clear()
        self.ui.cb31.clear()
        self.ui.cb60.clear()
        self.ui.cb70.clear()
        
        for exam_id, exam_name in exams:
            self.ui.cb30.addItem(exam_name, exam_id)
            self.ui.cb31.addItem(exam_name, exam_id)
            self.ui.cb60.addItem(exam_name, exam_id)
            self.ui.cb70.addItem(exam_name, exam_id)
        
        print(f"Populated exam selectors with {len(exams)} exams")
     except mysql.connector.Error as err:
        print(f"Error fetching exams: {err}")

    def add_question_to_template(self):
        exam_id = self.ui.cb60.currentData()
        exam_name = self.ui.cb60.currentText()
        question = self.ui.textEdit.toPlainText()
        options = [
            ('A', self.ui.tb60.text(), self.ui.sp60.value()),
            ('B', self.ui.tb61.text(), self.ui.sp61.value()),
            ('C', self.ui.tb62.text(), self.ui.sp62.value()),
            ('D', self.ui.tb63.text(), self.ui.sp63.value())
        ]
        correct_answer = self.ui.cb61.currentText()

        if not question or not all(option[1] for option in options):
            QMessageBox.warning(self, "Incomplete Data", "Please fill in all fields.")
            return

        template_item = f"Q: {question}\n"
        for letter, option_text, marks in options:
            template_item += f"{letter}: {option_text} (Marks: {marks})\n"
        template_item += f"Correct Answer: {correct_answer}"

        if exam_name not in self.exam_templates:
            self.exam_templates[exam_name] = []
        self.exam_templates[exam_name].append(template_item)

        self.save_question_to_database(exam_id, question, options, correct_answer)
        self.clear_template_fields()
        self.update_template_view()

    def clear_template_fields(self):
        self.ui.textEdit.clear()
        self.ui.tb60.clear()
        self.ui.tb61.clear()
        self.ui.tb62.clear()
        self.ui.tb63.clear()
        self.ui.sp60.setValue(0)
        self.ui.sp61.setValue(0)
        self.ui.sp62.setValue(0)
        self.ui.sp63.setValue(0)

    def save_question_to_database(self, exam_id, question_text, options, correct_answer):
     try:
        query = """INSERT INTO exam_templates 
                   (exam_id, question_text, option_a, option_b, option_c, option_d, correct_answer) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        option_values = [opt[1] for opt in options] + [''] * (4 - len(options))  # Pad with empty strings if less than 4 options
        self.app.cursor.execute(query, (exam_id, question_text, *option_values, correct_answer))
        self.app.connection.commit()
        QMessageBox.information(self, "نجاح", "تم حفظ السؤال بنجاح")
     except mysql.connector.Error as err:
        self.app.connection.rollback()
        QMessageBox.critical(self, "Database Error", f"Failed to save question: {err}")

    def load_exam_templates(self):
     try:
        query = """
        SELECT e.exam_name, et.question_text, et.correct_answer, 
               et.option_a, et.option_b, et.option_c, et.option_d
        FROM exams e
        JOIN exam_templates et ON e.id = et.exam_id
        ORDER BY e.exam_name, et.id
        """
        self.app.cursor.execute(query)
        results = self.app.cursor.fetchall()

        for exam_name, question_text, correct_answer, *options in results:
            if exam_name not in self.exam_templates:
                self.exam_templates[exam_name] = []
            
            template_item = f"Q: {question_text}\n"
            for letter, option_text in zip('ABCD', options):
                if option_text:
                    template_item += f"{letter}: {option_text}\n"
            template_item += f"الاجابة الصحيحة: {correct_answer}"
            
            self.exam_templates[exam_name].append(template_item)

     except mysql.connector.Error as err:
        QMessageBox.critical(self, "Database Error", f"Failed to load exam templates: {err}")
    

    def delete_selected_question(self):
        selected_items = self.ui.listWidget_2.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "لم يتم اختيار شيء", "الرجاء اختيار سؤال للحذف")
            return

        selected_item = selected_items[0]
        question_text = selected_item.text().split('\n')[0][3:]  # Extract question text
        exam_name = self.ui.cb70.currentText()

        reply = QMessageBox.question(self, 'تأكيد الحذف',
                                     f"هل أنت متأكد من حذف السؤال\n\n{question_text}",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.delete_question_from_database(exam_name, question_text)
            self.update_template_view()

    def delete_question_from_database(self, exam_name, question_text):
        try:
            # Get exam_id
            self.app.cursor.execute("SELECT id FROM exams WHERE exam_name = %s", (exam_name,))
            exam_id = self.app.cursor.fetchone()[0]

            # Delete options first (due to foreign key constraint)
            self.app.cursor.execute("""
                DELETE o FROM options o
                JOIN questions q ON o.question_id = q.id
                WHERE q.exam_id = %s AND q.question_text = %s
            """, (exam_id, question_text))

            # Then delete the question
            self.app.cursor.execute("""
                DELETE FROM questions
                WHERE exam_id = %s AND question_text = %s
            """, (exam_id, question_text))

            self.app.connection.commit()

            # Remove from local storage
            self.exam_templates[exam_name] = [q for q in self.exam_templates[exam_name] 
                                              if not q.startswith(f"Q: {question_text}")]

            QMessageBox.information(self, "نجاح", "تم حذف السؤال بنجاح")
        except mysql.connector.Error as err:
            self.app.connection.rollback()
            QMessageBox.critical(self, "Database Error", f"Failed to delete question: {err}")

    def update_template_view(self):
        self.ui.listWidget_2.clear()
        selected_exam = self.ui.cb70.currentText()
        if selected_exam in self.exam_templates:
            self.ui.listWidget_2.addItems(self.exam_templates[selected_exam])


    def logout(self):
        # Implement logout functionality here
        reply = QMessageBox.question(self, 'تسجيل الخروج', 'هل أنت متأكد من  تسجيل الخروج؟',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()  # Close the AdminGui window
            self.app.logout()  # Call a method in SharedApp to handle logout

    def closeEvent(self, event):
        super().closeEvent(event)

    def add_user_photos(self):
        student_id = self.ui.cb20.currentText()
        if not student_id:
            QMessageBox.warning(self, "تحذير", "الرجاء اختيار طالب")
            return

        photo_paths = []
        for _ in range(3):  # Allow selecting up to 3 photos
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(self, "Select Photo", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
            if file_path:
                photo_paths.append(file_path)
            else:
                break  # User cancelled selection

        if not photo_paths:
            return  # No photos selected

        destination_folder = r"C:\Users\ASUS\Desktop\done\studentdata\students_picture"
        os.makedirs(destination_folder, exist_ok=True)

        stored_paths = []
        for i, photo_path in enumerate(photo_paths):
            file_name = f"{student_id}_photo_{i+1}{os.path.splitext(photo_path)[1]}"
            destination_path = os.path.join(destination_folder, file_name)
            shutil.copy2(photo_path, destination_path)
            stored_paths.append(destination_path)

        try:
            # Delete existing photos for this user
            delete_query = "DELETE FROM user_photos WHERE user_id = %s"
            self.app.cursor.execute(delete_query, (student_id,))

            # Insert new photo paths
            insert_query = "INSERT INTO user_photos (user_id, photo_url) VALUES (%s, %s)"
            self.app.cursor.executemany(insert_query, [(student_id, path) for path in stored_paths])
            
            self.app.connection.commit()
            QMessageBox.information(self, "Success", f"{len(stored_paths)} photo(s) added successfully!")
            
            # Update the filenamelabel_4 with the new paths
            self.ui.filenamelabel_4.setText("\n".join(stored_paths))
        
        except mysql.connector.Error as err:
            self.app.connection.rollback()
            QMessageBox.critical(self, "Error", f"Failed to add photos: {err}")

    def edit_user_photos(self):
        student_id = self.ui.cb20.currentText()
        if not student_id:
            QMessageBox.warning(self, "Warning", "Please select a student first.")
            return

        try:
            # Fetch existing photo paths
            query = "SELECT photo_url FROM user_photos WHERE user_id = %s"
            self.app.cursor.execute(query, (student_id,))
            existing_photos = self.app.cursor.fetchall()

            photo_paths = []
            for i in range(3):
                if i < len(existing_photos):
                    file_path, _ = QFileDialog.getOpenFileName(self, f"Edit Photo {i+1}", existing_photos[i][0], "Image Files (*.png *.jpg *.jpeg *.bmp)")
                else:
                    file_path, _ = QFileDialog.getOpenFileName(self, f"Add Photo {i+1}", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
                
                if file_path:
                    photo_paths.append(file_path)
                elif i < len(existing_photos):
                    photo_paths.append(existing_photos[i][0])  # Keep existing photo if no new one selected
                else:
                    break  # User cancelled selection for a new photo

            destination_folder = r"C:\Users\ASUS\Desktop\done\studentdata\students_picture"
            os.makedirs(destination_folder, exist_ok=True)

            stored_paths = []
            for i, photo_path in enumerate(photo_paths):
                if photo_path not in [p[0] for p in existing_photos]:  # Only copy if it's a new photo
                    file_name = f"{student_id}_photo_{i+1}{os.path.splitext(photo_path)[1]}"
                    destination_path = os.path.join(destination_folder, file_name)
                    shutil.copy2(photo_path, destination_path)
                    stored_paths.append(destination_path)
                else:
                    stored_paths.append(photo_path)  # Keep existing path

            # Delete existing photos for this user
            delete_query = "DELETE FROM user_photos WHERE user_id = %s"
            self.app.cursor.execute(delete_query, (student_id,))

            # Insert updated photo paths
            insert_query = "INSERT INTO user_photos (user_id, photo_url) VALUES (%s, %s)"
            self.app.cursor.executemany(insert_query, [(student_id, path) for path in stored_paths])
            
            self.app.connection.commit()
            QMessageBox.information(self, "Success", f"Photos updated successfully!")
            
            # Update the filenamelabel_3 with the new paths
            self.ui.filenamelabel_3.setText("\n".join(stored_paths))

        except mysql.connector.Error as err:
            self.app.connection.rollback()
            QMessageBox.critical(self, "Error", f"Failed to update photos: {err}")
    

    def loadNotes(self):
        try:
            query = """
            SELECT u.id_number, u.first_name, u.last_name, e.exam_name, e.exam_date, se.note_text
            FROM studentexams se
            JOIN users u ON se.student_id = u.id_number
            JOIN exams e ON se.exam_id = e.id
            WHERE se.note_text IS NOT NULL AND se.note_text != ''
            ORDER BY e.exam_date DESC
            """
            self.app.cursor.execute(query)
            notes = self.app.cursor.fetchall()
            

            self.ui.notestable.setRowCount(len(notes))
            for row, note in enumerate(notes):
                student_id, first_name, last_name, exam_name, exam_date, note_text = note
                self.ui.notestable.setItem(row, 0, QTableWidgetItem(str(student_id)))
                self.ui.notestable.setItem(row, 1, QTableWidgetItem(f"{first_name} {last_name}"))
                self.ui.notestable.setItem(row, 2, QTableWidgetItem(exam_name))
                self.ui.notestable.setItem(row, 3, QTableWidgetItem(exam_date.strftime("%Y-%m-%d %H:%M:%S")))
                self.ui.notestable.setItem(row, 4, QTableWidgetItem(note_text))

            self.ui.notestable.resizeColumnsToContents()
        except mysql.connector.Error as err:
            print(f"Error loading notes: {err}")
            QMessageBox.critical(self, "Error", "Failed to load notes. Please try again.")


    def closeEvent(self, event):
     reply = QMessageBox.question(self, 'اغلاق النافذة', 'هل انت متأكد ؟',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
     if reply == QMessageBox.Yes:
        event.accept()
        super().closeEvent(event)
     else:
        event.ignore()