import typing
from PyQt6 import QtCore
from pyqtgraph import GraphicsLayoutWidget, PlotItem, PlotDataItem
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QCheckBox
from PyQt6.QtCore import QSize, Qt
from DataControl.DiagramixDataController import DiagramixDataController
import pyqtgraph as pg
import numpy as np
import math


class DiagramixPlot(GraphicsLayoutWidget):

    def __init__(self, parent=None, show=False, size=None, title=None, **kargs):
        super().__init__(parent, show, size, title, **kargs)

        self.data_controller = DiagramixDataController()
        self.all_data_items = []
        self.n_subplots = 1
        self.n_max_columns = 1
        self.subplots: [DiagramixSubPlot] = []
        self.sync_x_axes = False
        self.sync_y_axes = False

    def __del__(self):
        self.clear_subplots()

    def set_n_subplots(self, n_subplots):
        self.n_subplots = n_subplots
    
    def set_n_max_columns(self, n_max_columns):
        self.n_max_columns = n_max_columns

    def clear_subplots(self):
        self.subplots.clear()
        self.clear()

    def create_subplots(self):
        for i in range(self.n_subplots):
            row = i // self.n_max_columns
            col = i % self.n_max_columns
            p = DiagramixSubPlot()
            self.subplots.append(p)
            self.addItem(p, row=row, col=col)
            p.setParentItem(self.centralWidget)

    def synchronize_x_axes(self):
        if self.sync_x_axes == True:
            for i in range(1, len(self.subplots)):
                self.subplots[i].setXLink(self.subplots[0])
        else: 
            for i in range(1, len(self.subplots)):
                self.subplots[i].setXLink(None)

    def synchronize_y_axes(self):
        if self.sync_y_axes == True:
            for i in range(1, len(self.subplots)):
                self.subplots[i].setYLink(self.subplots[0])
        else: 
            for i in range(1, len(self.subplots)):
                self.subplots[i].setYLink(None)

    def clear_plot_items(self):
        for p in self.subplots:
            p.clear_plot_data_items()
            self.removeItem(p)
        self.subplots.clear()
            

class DiagramixSubPlot(PlotItem):

    def __init__(self, parent=None, name=None, labels=None, title=None, viewBox=None, axisItems=None, enableMenu=True, **kargs):
        super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)
        print("Created DiagramixSubPlot")

    def __del__(self):
        print("Deleted DiagramixSubPlot")

    def add_plot_data_item(self, plot_data_item: PlotDataItem):
        self.addItem(plot_data_item)

    def remove_plot_data_item(self, item):
        self.removeItem(item)
        item.deleteLater()

    def clear_plot_data_items(self):
        self.clear()
        

class DiagramixPlotObject(PlotDataItem):

    def __init__(self, x: np.ndarray, y: np.ndarray, subplot_number: int, subplot_parent:DiagramixSubPlot, RGB:list  = None, parent=None, name=None, labels=None, title=None, viewBox=None, axisItems=None, enableMenu=True, **kargs):
        super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)
        if RGB == None:
            self.RGB = [np.random.randint(0,256),
                        np.random.randint(0,256),
                        np.random.randint(0,256)]
        else:
            self.RGB = RGB

        self.subplot_number: int = subplot_number
        self.subplot_parent: DiagramixSubPlot = subplot_parent
        self.x = x
        self.y = y
        self.setPen(*self.RGB)
        self.update_data()
        print(f"Created DiagramixPlotObject")

    def update_data(self):
        self.setData(self.x, self.y)

    def prepare_deleting(self):
        self.subplot_parent.remove_plot_data_item(self)

    def __del__(self):
        self.subplot_parent.remove_plot_data_item(self)
        print("Deleted DiagramixPlotObject")



        
            