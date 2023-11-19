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


    def draw(self):
        self.clear_plot_items()
        x=np.linspace(0,6.28,100)
        y=np.sin(x)

        for i in range(len(self.subplots)):
            plot_object = DiagramixPlotObject(self)
            plot_object.setData(x,np.cos(x)*np.sin(x*(i+1)))
            self.subplots[i].add_plot_data_item(plot_object)

            plot_object2 = DiagramixPlotObject(self)
            plot_object2.setData(x,np.sin(x)*np.cos(x*(i+1)))
            self.subplots[i].add_plot_data_item(plot_object2)

        self.synchronize_x_axes()
        self.synchronize_y_axes()

class DiagramixSubPlot(PlotItem):

    def __init__(self, parent=None, name=None, labels=None, title=None, viewBox=None, axisItems=None, enableMenu=True, **kargs):
        super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)
        self.plot_data_items = []

    def __del__(self):
        self.clear_plot_data_items()
        print("Deleted SubPlot")

    def add_plot_data_item(self, plot_data_item: PlotDataItem):
        self.plot_data_items.append(plot_data_item)
        self.addItem(plot_data_item)


    def clear_plot_data_items(self):
        self.plot_data_items.clear()
        self.clear()
        

class DiagramixPlotObject(PlotDataItem):

    def __init__(self, parent=None, name=None, labels=None, title=None, viewBox=None, axisItems=None, enableMenu=True, **kargs):
        super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)
        R=np.random.randint(0,256)
        G=np.random.randint(0,256)
        B=np.random.randint(0,256)
        self.setPen(R,G,B)

    def __del__(self):
        print("Deleted plot line")



        
            