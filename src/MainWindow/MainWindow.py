import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    #Class variables
    #
    #
    #
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diagramix")


