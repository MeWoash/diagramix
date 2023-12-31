import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QToolBar
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion

from Widgets.MainPlotScreenWidget import PlotScreenWidget

# Subclass QMainWindow to customize your application's main window
class DiagramixMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diagramix")
        self.setMinimumSize(1200,600)
        # self.create_central_widgets()
        # self.create_toolbar()
        # self.change_central_widget("start_screen_widget")
        # self.change_toolbar("exit_button_stub")

        # GRAPH TEST
        self.main_plot_screen = PlotScreenWidget()
        self.setCentralWidget(self.main_plot_screen)
        


