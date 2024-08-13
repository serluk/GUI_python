from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6 import uic

from instructor import Instructor


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("login_form_work.ui", self)

        self.ui.btn_login_object.clicked.connect(self.authenticate)

        self.show()

    def authenticate(self):
        login = self.login_object.text()
        password = self.password_object.text()
        if login == 'ABC' and password == '123' and self.ui.instructor_object.isChecked():
            # QMessageBox.information(self, 'Success', "You're logged in as instructor!")
            Instructor()
            self.close()
        elif login == 'ABC' and password == '123' and self.ui.student_object.isChecked():
            QMessageBox.information(self, 'Success', "You're logged in as student!")
        else:
            QMessageBox.critical(self, 'Error', "Invalid email or password.")

if __name__ == "__main__":
    app = QApplication([])
    window = Login()
    app.exec()
