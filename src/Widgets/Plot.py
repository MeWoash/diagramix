from pyqtgraph import PlotWidget, GraphicsLayoutWidget
import pyqtgraph as pg
import numpy as np
import math


class DiagramixPlot(GraphicsLayoutWidget):

    def __init__(self):
        super().__init__()

        x=np.linspace(0,6.28,100)
        y=np.sin(x)

        self.create_subplots(4,3)

        for i in range(len(self.subplots)):
            self.subplots[i].plot(x,np.cos(x)*np.sin(x*(i+1)))

        self.sync_axes(True)

    def create_subplots(self, n_subplots, max_columns=2):
        self.subplots = []
        n_rows = (n_subplots + max_columns - 1) // max_columns

        plot_widget = pg.PlotWidget()
        for i in range(n_subplots):
            row = i // max_columns
            col = i % max_columns
            self.subplots.append(self.addPlot(row=row, col=col))


    def sync_axes(self, sync_axes_bool: bool):
        for i in range(1, len(self.subplots)):
            self.subplots[i].setXLink(self.subplots[0])
            self.subplots[i].setYLink(self.subplots[0])
        
            