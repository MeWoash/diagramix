from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from Widgets.PlotWidgets import DiagramixPlot
from Widgets.PlotWidgetsControl import DiagramixPlotControls
from Widgets.FileControlWidget import DiagramixFileWidget


class DiagramixTabBar(QTabWidget):

    def __init__(self, parent: QWidget, diagramix_plot: DiagramixPlot) -> None:
        super().__init__()

        self.diagramix_plot_ref: DiagramixPlot = diagramix_plot
        self.create_layout()


    def create_layout(self):
        self.setTabPosition(QTabWidget.TabPosition.North)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        diagramix_file_control = DiagramixFileWidget(None, self.diagramix_plot_ref)
        diagramix_plot_control = DiagramixPlotControls(None, self.diagramix_plot_ref)
        self.addTab(diagramix_file_control, "Importyyyyyyyyyyyyyyyyyyyy")
        self.addTab(diagramix_plot_control, "Edit")

    def __del__(self):
        pass
