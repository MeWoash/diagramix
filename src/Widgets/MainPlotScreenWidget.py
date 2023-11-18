import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QIntValidator
from Widgets import PlotWidgets

class PlotScreenWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.diagramix_plot = PlotWidgets.DiagramixPlot()
        self.diagramix_plot_controls = PlotWidgets.DiagramixPlotControls(self.diagramix_plot)

        self.main_layout.addWidget(self.diagramix_plot_controls)
        self.main_layout.addWidget(self.diagramix_plot)



        