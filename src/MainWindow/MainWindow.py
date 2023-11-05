import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QToolBar
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion

from Toolbars import ExitWidget
from CentralWidgets import StartScreenWidget, PlotScreenWidget


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diagramix")
        
        self.create_central_widgets()
        self.create_toolbar()
        self.change_central_widget("start_screen_widget")
        self.change_toolbar("exit_button_stub")

    def create_central_widgets(self):
        self.centralwidgets = {
            "start_screen_widget": StartScreenWidget.StartScreenWidget(),
            "plot_screen_widget": PlotScreenWidget.PlotScreenWidget()
        }

    def change_central_widget(self, widget: str):
        if widget not in self.centralwidgets.keys():
            print("Widget doesnt exist!")
        else:
            self.setCentralWidget(self.centralwidgets[widget])

    def create_toolbar(self):
         self.toolbars = {
             "exit_button_stub": Toolbars.ExitWidget()
         }

    def change_toolbar(self, toolbar: str):
        if toolbar not in self.toolbars.keys():
            print("Widget doesnt exist!")
        else:
            self.addToolBar(self.toolbars[toolbar])


