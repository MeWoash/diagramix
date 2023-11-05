import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion

class PlotScreenWidget(QWidget):

    def __init__(self):
        super().__init__()

        