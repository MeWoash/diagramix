from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from Widgets.PlotWidgets import DiagramixPlot
from Widgets.PlotWidgetsControl import DiagramixPlotControls
from Widgets.FileControlWidget import DiagramixControlWidget


class DiagramixTabBar(QTabWidget):

    def __init__(self, parent: None):
        super().__init__()

        self.diagramix_plot = DiagramixPlot(self)
        self.create_layout()


    def create_layout(self):
        self.setTabPosition(QTabWidget.TabPosition.North)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.addTab(DiagramixControlWidget(None), "Importyyyyyyyyyyyyyyyyyyyy")
        self.addTab(DiagramixPlotControls(None, self.diagramix_plot), "Edit")

    def __del__(self):
        pass
