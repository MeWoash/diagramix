import typing
from PyQt6 import QtCore
from pyqtgraph import PlotWidget, GraphicsLayoutWidget
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import QSize, Qt
import pyqtgraph as pg
import numpy as np
import math


class DiagramixPlot(GraphicsLayoutWidget):

    def __init__(self):
        super().__init__()
        self.n_subplots = 1
        self.n_max_columns = 1

        # self.create_subplots(self.n_subplots, self.n_max_columns)
        # self.sync_axes(True)


    def set_n_subplots(self, n_subplots):
        self.n_subplots = n_subplots
    
    def set_n_max_columns(self, n_max_columns):
        self.n_max_columns = n_max_columns

    def create_subplots(self, n_subplots, max_columns=2):
        self.subplots = []

        for i in range(n_subplots):
            row = i // max_columns
            col = i % max_columns
            self.subplots.append(self.addPlot(row=row, col=col))

    def sync_axes(self, sync_axes_bool: bool):
        for i in range(1, len(self.subplots)):
            self.subplots[i].setXLink(self.subplots[0])
            self.subplots[i].setYLink(self.subplots[0])

    def draw(self):
        self.create_subplots(self.n_subplots, self.n_max_columns)
        x=np.linspace(0,6.28,100)
        y=np.sin(x)
        for i in range(len(self.subplots)):
            self.subplots[i].plot(x,np.cos(x)*np.sin(x*(i+1)))

class DiagramixPlotControls(QWidget):

    def __init__(self, diagramix_plot: DiagramixPlot) -> None:
        super().__init__()
        self.diagramix_plot_ref = diagramix_plot

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # MAIN LABEL
        self.main_layout.addWidget(QLabel("Control Graph"), alignment=Qt.AlignmentFlag.AlignTop)

        # SUBPLOTS OPTION
        

        # DRAW BUTTON
        self.draw_button = QPushButton("Draw")
        self.draw_button.clicked.connect(self.diagramix_plot_ref.draw)
        self.main_layout.addWidget(self.draw_button, alignment=Qt.AlignmentFlag.AlignBottom)
        
            