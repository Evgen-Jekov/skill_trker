from PyQt6.QtWidgets import QApplication
from app.GUI.main import MainWindow

def start():
    app = QApplication([])
    window = MainWindow()
    app.exec()