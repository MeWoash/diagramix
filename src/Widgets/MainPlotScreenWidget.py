import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QIntValidator
from Widgets.PlotWidgets import DiagramixPlot
from Widgets.PlotWidgetsControl import DiagramixPlotControls

class PlotScreenWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.diagramix_plot = DiagramixPlot()
        self.diagramix_plot_controls = DiagramixPlotControls(self.diagramix_plot, self)

        self.main_layout.addWidget(self.diagramix_plot_controls)
        self.main_layout.addWidget(self.diagramix_plot)



        