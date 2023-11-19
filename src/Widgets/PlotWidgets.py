import typing
from PyQt6 import QtCore
from pyqtgraph import GraphicsLayoutWidget, PlotItem, PlotDataItem
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QCheckBox
from PyQt6.QtCore import QSize, Qt
import pyqtgraph as pg
import numpy as np
import math


class DiagramixPlot(GraphicsLayoutWidget):

    def __init__(self):
        super().__init__()
        self.n_subplots = 1
        self.n_max_columns = 1
        self.subplots = []
        self.sync_x_axes = False
        self.sync_y_axes = False

    def __del__(self):
        self.clear_subplots()

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
            p = DiagramixSubPlot()
            self.subplots.append(p)
            self.addItem(p, row=row, col=col)

    def sync_x_state_changed(self, state):
        if state == Qt.CheckState.Unchecked.value or state == Qt.CheckState.PartiallyChecked.value:
            self.sync_x_axes = False
        if state == Qt.CheckState.Checked.value:
            self.sync_x_axes = True
        self.synchronize_x_axes()

    def synchronize_x_axes(self):
        if self.sync_x_axes == True:
            for i in range(1, len(self.subplots)):
                self.subplots[i].setXLink(self.subplots[0])
        else: 
            for i in range(1, len(self.subplots)):
                self.subplots[i].setXLink(None)

    def sync_y_state_changed(self, state):
        if state == Qt.CheckState.Unchecked.value or state == Qt.CheckState.PartiallyChecked.value:
            self.sync_y_axes = False
        if state == Qt.CheckState.Checked.value:
            self.sync_y_axes = True
        self.synchronize_y_axes()

    def synchronize_y_axes(self):
        if self.sync_y_axes == True:
            for i in range(1, len(self.subplots)):
                self.subplots[i].setYLink(self.subplots[0])
        else: 
            for i in range(1, len(self.subplots)):
                self.subplots[i].setYLink(None)

    def draw(self):
        self.clear_subplots()
        self.create_subplots(self.n_subplots, self.n_max_columns)
        x=np.linspace(0,6.28,100)
        y=np.sin(x)

        for i in range(len(self.subplots)):
            plot_object = DiagramixPlotObject()
            plot_object.setData(x,np.cos(x)*np.sin(x*(i+1)))
            self.subplots[i].add_plot_data_item(plot_object)

    
        self.synchronize_x_axes()
        self.synchronize_y_axes()

class DiagramixSubPlot(PlotItem):

    def __init__(self, parent=None, name=None, labels=None, title=None, viewBox=None, axisItems=None, enableMenu=True, **kargs):
        super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)
        self.plot_data_items = []

    def __del__(self):
        self.clear_plot_data_items()

    def add_plot_data_item(self, plot_data_item: PlotDataItem):
        self.plot_data_items.append(plot_data_item)
        self.addItem(plot_data_item)

    def clear_plot_data_items(self):
        for p in self.plot_data_items:
            del p
        self.plot_data_items.clear()
        self.clear()
        

class DiagramixPlotObject(PlotDataItem):

    def __init__(self, parent=None, name=None, labels=None, title=None, viewBox=None, axisItems=None, enableMenu=True, **kargs):
        super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)



        
            