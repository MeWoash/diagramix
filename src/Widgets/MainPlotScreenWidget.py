import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QIntValidator
from Widgets.PlotWidgets import DiagramixPlot
from Widgets.PlotWidgetsControl import DiagramixPlotControls

class PlotScreenWidget(QWidget):

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.diagramix_plot = DiagramixPlot(self)
        self.diagramix_plot_controls = DiagramixPlotControls(self, self.diagramix_plot)

        self.main_layout.addWidget(self.diagramix_plot_controls)
        self.main_layout.setStretch(0, 1)
        self.main_layout.addWidget(self.diagramix_plot)
        self.main_layout.setStretch(1, 10)




        