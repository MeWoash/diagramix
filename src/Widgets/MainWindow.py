import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QToolBar
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion

from Widgets import StartScreenWidget, MainPlotScreenWidget, ExitWidget

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diagramix")
        
        # self.create_central_widgets()
        # self.create_toolbar()
        # self.change_central_widget("start_screen_widget")
        # self.change_toolbar("exit_button_stub")

        # GRAPH TEST
        self.main_plot_screen = MainPlotScreenWidget.PlotScreenWidget()
        self.setCentralWidget(self.main_plot_screen)


