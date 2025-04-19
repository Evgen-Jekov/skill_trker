from PyQt6.QtWidgets import QApplication
from app.GUI.main import MainWindow
from app.repository.db import Base, engine

def start():
    app = QApplication([])
    window = MainWindow()
    Base.metadata.create_all(bind=engine)
    app.exec()