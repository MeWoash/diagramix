from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt, QEvent
from PyQt6.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from Widgets.PlotWidgets import DiagramixPlot
from Widgets.PlotWidgetsControl import DiagramixPlotControls
from Widgets.FileControlWidget import DiagramixFileWidget
from Widgets.MultiChannelPlotWidget import DiagramixMultiChPlot


class DiagramixTabBar(QTabWidget):

    def __init__(self, parent: QWidget, diagramix_plot: DiagramixPlot) -> None:
        super().__init__()

        self.diagramix_plot_ref: DiagramixPlot = diagramix_plot
        self.create_layout()

    def create_layout(self):
        self.setTabPosition(QTabWidget.TabPosition.North)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        diagramix_plot_control = DiagramixPlotControls(None, self.diagramix_plot_ref)
        diagramix_multi_ch = DiagramixMultiChPlot(None, self.diagramix_plot_ref)
        self.diagramix_file_control = DiagramixFileWidget(None, self.diagramix_plot_ref)
        self.diagramix_file_control.enabler.connect(self.enable_edit)
        self.addTab(self.diagramix_file_control, "File Import")
        self.addTab(diagramix_plot_control, "Graph Edit")
        self.addTab(diagramix_multi_ch, "Multi Channel plotting")
        self.setTabEnabled(1, False)
        self.setTabEnabled(2, False)
        # self.enable_edit()

    def enable_edit(self):
        self.setTabEnabled(1, True)
        self.setTabEnabled(2, True)

    def __del__(self):
        pass
