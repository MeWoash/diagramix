import typing
from PyQt6 import QtCore
from pyqtgraph import GraphicsLayoutWidget
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QCheckBox
from PyQt6.QtCore import QSize, Qt
from Widgets import PlotWidgetsUtility
import pyqtgraph as pg
import numpy as np
import math


class DiagramixPlot(GraphicsLayoutWidget):

    def __init__(self):
        super().__init__()
        self.n_subplots = 1
        self.n_max_columns = 1
        self.subplots = []
        self.sync_axes = False


    def set_n_subplots(self, n_subplots):
        self.n_subplots = n_subplots
    
    def set_n_max_columns(self, n_max_columns):
        self.n_max_columns = n_max_columns

    def clear_subplots(self):
        for p in self.subplots:
            del p
        self.subplots.clear()
        self.clear()

    def create_subplots(self, n_subplots, max_columns=2):
        
        for i in range(n_subplots):
            row = i // max_columns
            col = i % max_columns
            self.subplots.append(self.addPlot(row=row, col=col))

    def sync_state_changed(self, state):
        if state == Qt.CheckState.Unchecked.value or state == Qt.CheckState.PartiallyChecked.value:
            self.sync_axes = False
        if state == Qt.CheckState.Checked.value:
            self.sync_axes = True
        self.synchronize_axes()

    def synchronize_axes(self):
        if self.sync_axes == True:
            for i in range(1, len(self.subplots)):
                self.subplots[i].setXLink(self.subplots[0])
                self.subplots[i].setYLink(self.subplots[0])
        else: 
            for i in range(1, len(self.subplots)):
                self.subplots[i].setXLink(None)
                self.subplots[i].setYLink(None)

    def draw(self):
        self.clear_subplots()
        self.create_subplots(self.n_subplots, self.n_max_columns)
        x=np.linspace(0,6.28,100)
        y=np.sin(x)
        for i in range(len(self.subplots)):
            self.subplots[i].plot(x,np.cos(x)*np.sin(x*(i+1)))

        self.synchronize_axes()

class DiagramixPlotControls(QWidget):

    def __init__(self, diagramix_plot: DiagramixPlot) -> None:
        super().__init__()
        self.diagramix_plot_ref = diagramix_plot

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # MAIN LABEL
        self.main_layout.addWidget(QLabel("Control Graph"), alignment=Qt.AlignmentFlag.AlignTop)

        # SUBPLOTS OPTION
        self.subplot_control = PlotWidgetsUtility.DiagramixPlotSubplotControl()
        self.subplot_control.n_plots_input.setText(str(self.diagramix_plot_ref.n_subplots))
        self.subplot_control.n_plots_input.textChanged.connect(lambda x: self.diagramix_plot_ref.set_n_subplots(int(x)))
        self.subplot_control.n_max_columns_input.setText(str(self.diagramix_plot_ref.n_max_columns))
        self.subplot_control.n_max_columns_input.textChanged.connect(lambda x: self.diagramix_plot_ref.set_n_max_columns(int(x)))
        self.main_layout.addWidget(self.subplot_control, alignment=Qt.AlignmentFlag.AlignTop)

        #PLOT CHECKBOXES
        self.sync_axes_btn = QCheckBox("Sync axes")
        self.sync_axes_btn.stateChanged.connect(self.diagramix_plot_ref.sync_state_changed)
        self.sync_axes_btn.setCheckState(Qt.CheckState.Unchecked)
        self.main_layout.addWidget(self.sync_axes_btn)

        # DRAW BUTTON
        self.draw_button = QPushButton("Draw")
        self.draw_button.clicked.connect(self.diagramix_plot_ref.draw)
        self.main_layout.addWidget(self.draw_button, alignment=Qt.AlignmentFlag.AlignBottom)

        
            