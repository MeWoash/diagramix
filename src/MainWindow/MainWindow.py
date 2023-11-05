import sys
from StartScreenWidget import StartScreenWidget
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diagramix")
        start_screen_widget = StartScreenWidget.StartScreenWidget()
        self.setCentralWidget(start_screen_widget)




