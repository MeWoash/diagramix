import typing
from PyQt6 import QtCore
from pyqtgraph import PlotWidget, GraphicsLayoutWidget, PlotItem
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit, QCheckBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIntValidator
from Widgets.PlotWidgets import DiagramixPlot


class DiagramixPlotSubplotControl(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)


        self.main_layout.addWidget(QLabel("Number of plots"), 0, 0)
        self.n_plots_input = QLineEdit()
        self.n_plots_input.setValidator(QIntValidator(1,10))
        self.main_layout.addWidget(self.n_plots_input, 1, 0)

        self.main_layout.addWidget(QLabel("Number of columns"), 0, 1)
        self.n_max_columns_input = QLineEdit()
        self.n_max_columns_input.setValidator(QIntValidator(1,10))
        self.main_layout.addWidget(self.n_max_columns_input, 1, 1)

class DiagramixPlotControls(QWidget):

    def __init__(self, diagramix_plot: DiagramixPlot) -> None:
        super().__init__()
        self.diagramix_plot_ref = diagramix_plot

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # MAIN LABEL
        self.main_layout.addWidget(QLabel("Control Graph"), alignment=Qt.AlignmentFlag.AlignTop)

        # SUBPLOTS OPTION
        self.subplot_control = DiagramixPlotSubplotControl()
        self.subplot_control.n_plots_input.setText(str(self.diagramix_plot_ref.n_subplots))
        self.subplot_control.n_plots_input.textChanged.connect(lambda x: self.diagramix_plot_ref.set_n_subplots(int(x)))
        self.subplot_control.n_max_columns_input.setText(str(self.diagramix_plot_ref.n_max_columns))
        self.subplot_control.n_max_columns_input.textChanged.connect(lambda x: self.diagramix_plot_ref.set_n_max_columns(int(x)))
        self.main_layout.addWidget(self.subplot_control, alignment=Qt.AlignmentFlag.AlignTop)

        #PLOT CHECKBOXES
        self.sync_x_axes_btn = QCheckBox("Sync X axes")
        self.sync_x_axes_btn.stateChanged.connect(self.diagramix_plot_ref.sync_x_state_changed)
        self.sync_x_axes_btn.setCheckState(Qt.CheckState.Unchecked)
        self.main_layout.addWidget(self.sync_x_axes_btn)

        self.sync_y_axes_btn = QCheckBox("Sync Y axes")
        self.sync_y_axes_btn.stateChanged.connect(self.diagramix_plot_ref.sync_y_state_changed)
        self.sync_y_axes_btn.setCheckState(Qt.CheckState.Unchecked)
        self.main_layout.addWidget(self.sync_y_axes_btn)

        #CLEAR BUTTON
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.diagramix_plot_ref.clear_subplots)
        self.main_layout.addWidget(self.clear_button, alignment=Qt.AlignmentFlag.AlignBottom)

        # DRAW BUTTON
        self.draw_button = QPushButton("Draw")
        self.draw_button.clicked.connect(self.diagramix_plot_ref.draw)
        self.main_layout.addWidget(self.draw_button, alignment=Qt.AlignmentFlag.AlignBottom)



    