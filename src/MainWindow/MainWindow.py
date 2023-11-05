import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion

from CentralWidgets import StartScreenWidget, PlotScreenWidget


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diagramix")
        
        self.create_central_widgets()
        self.change_central_widget("start_screen_widget")

    def create_central_widgets(self):
        self.centralwidgets = {
            "start_screen_widget":StartScreenWidget.StartScreenWidget(),
            "plot_screen_widget":PlotScreenWidget.PlotScreenWidget()
        }

    def change_central_widget(self, widget: str):
        if widget not in self.centralwidgets.keys():
            print("Widget doesnt exist!")
        else:
            self.setCentralWidget(self.centralwidgets[widget])




