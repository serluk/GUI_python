from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


class Instructor(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("instructor.ui", self)

        self.show()