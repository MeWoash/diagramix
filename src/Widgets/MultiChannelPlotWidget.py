from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt, QEvent
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, QMainWindow, \
    QTableWidget, QTableWidgetItem
from DataControl.DiagramixDataController import DiagramixDataController
from Widgets.PlotWidgets import DiagramixPlot


class DiagramixMultiChPlot(QWidget):
    def __init__(self, parent: QWidget, diagramix_plot: DiagramixPlot) -> None:
        super().__init__(parent)

        self.diagramix_plot_ref: diagramix_plot
