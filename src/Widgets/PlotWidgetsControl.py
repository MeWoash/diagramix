import typing
from PyQt6 import QtCore
from pyqtgraph import PlotWidget, GraphicsLayoutWidget, PlotItem
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit, QCheckBox, QFileDialog, QTableWidget, QTableWidgetItem, QMainWindow
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIntValidator
from Widgets.PlotWidgets import DiagramixPlot
from DataControl.DiagramixDataController import DiagramixDataController

class DiagramixPlotControls(QWidget):

    def __init__(self, parent: QWidget, diagramix_plot: DiagramixPlot) -> None:
        super().__init__(parent)

        self.diagramix_plot_ref:DiagramixPlot = diagramix_plot
        self.data_controller:DiagramixDataController = diagramix_plot.data_controller
        self.create_layout()


    def create_layout(self):
        
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # MAIN LABEL
        self.main_layout.addWidget(QLabel("Control Graph"), alignment=Qt.AlignmentFlag.AlignTop)

        # SUBPLOTS OPTION
        self.subplot_control = DiagramixPlotSubplotGenerator()
        self.subplot_control.n_plots_input.setText(str(self.diagramix_plot_ref.n_subplots))
        # self.subplot_control.n_plots_input.textChanged.connect(lambda x: self.diagramix_plot_ref.set_n_subplots(int(x)))
        self.subplot_control.n_max_columns_input.setText(str(self.diagramix_plot_ref.n_max_columns))
        # self.subplot_control.n_max_columns_input.textChanged.connect(lambda x: self.diagramix_plot_ref.set_n_max_columns(int(x)))
        self.subplot_control.generate_button.clicked.connect(self.generate_subplots_clicked)
        self.main_layout.addWidget(self.subplot_control, alignment=Qt.AlignmentFlag.AlignTop)

        #LOAD FILE
        self.file_input = QPushButton("Choose File")
        self.file_input.clicked.connect(self.file_input_clicked)
        self.main_layout.addWidget(self.file_input)

        self.file_input_label = QLabel("File:")
        self.main_layout.addWidget(self.file_input_label)

        #VIEW FILE
        self.view_table_button = QPushButton("View Table")
        self.view_table_button.setEnabled(False)
        self.view_table_button.clicked.connect(self.view_table_button_clicked)
        self.main_layout.addWidget(self.view_table_button)


        #PLOT CHECKBOXES
        self.sync_x_axes_btn = QCheckBox("Sync X axes")
        self.sync_x_axes_btn.stateChanged.connect(self.sync_x_state_changed)
        self.sync_x_axes_btn.setCheckState(Qt.CheckState.Unchecked)
        self.main_layout.addWidget(self.sync_x_axes_btn)

        self.sync_y_axes_btn = QCheckBox("Sync Y axes")
        self.sync_y_axes_btn.stateChanged.connect(self.sync_y_state_changed)
        self.sync_y_axes_btn.setCheckState(Qt.CheckState.Unchecked)
        self.main_layout.addWidget(self.sync_y_axes_btn)

        self.main_layout.addStretch(20)

        #CLEAR BUTTON
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.diagramix_plot_ref.clear_plot_items)
        self.main_layout.addWidget(self.clear_button, alignment=Qt.AlignmentFlag.AlignBottom)

        # DRAW BUTTON
        self.draw_button = QPushButton("Draw")
        self.draw_button.clicked.connect(self.diagramix_plot_ref.draw)
        self.main_layout.addWidget(self.draw_button, alignment=Qt.AlignmentFlag.AlignBottom)

    def file_input_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Wszystkie pliki (*);;Pliki CSV (*.csv);;Pliki TXT (*.txt)")
        if file_name:
            self.input_file_path = file_name
            self.file_input_label.setText(f"File: {file_name}")
            load_succeeded = self.data_controller.load_file(file_path=file_name)

        self.view_table_button.setEnabled(load_succeeded)

    def sync_x_state_changed(self, state):
        if state == Qt.CheckState.Unchecked.value or state == Qt.CheckState.PartiallyChecked.value:
            self.diagramix_plot_ref.sync_x_axes = False
        if state == Qt.CheckState.Checked.value:
            self.diagramix_plot_ref.sync_x_axes = True
        self.diagramix_plot_ref.synchronize_x_axes()

    def sync_y_state_changed(self, state):
        if state == Qt.CheckState.Unchecked.value or state == Qt.CheckState.PartiallyChecked.value:
            self.diagramix_plot_ref.sync_y_axes = False
        if state == Qt.CheckState.Checked.value:
            self.diagramix_plot_ref.sync_y_axes = True
        self.diagramix_plot_ref.synchronize_y_axes()

    def view_table_button_clicked(self):
        window = QMainWindow(self)
        table = DiagramixTableView(self.data_controller.df)
        window.setWindowTitle("DataFrame Preview")
        window.setCentralWidget(table)
        window.show()

    def generate_subplots_clicked(self):
        n_subplots = int(self.subplot_control.n_plots_input.text())
        n_max_columns = int(self.subplot_control.n_max_columns_input.text())
        
        self.diagramix_plot_ref.set_n_subplots(n_subplots)
        self.diagramix_plot_ref.set_n_max_columns(n_max_columns)

        self.diagramix_plot_ref.clear_subplots() 
        self.diagramix_plot_ref.create_subplots()

class DiagramixPlotSubplotGenerator(QWidget):
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

        self.generate_button = QPushButton("Generate")
        self.main_layout.addWidget(self.generate_button, 2, 0, 1, 2)


class DiagramixTableView(QTableWidget):

    def __init__(self, df):
        super().__init__()
        self.df = df
        self.populate_table()

    def populate_table(self):
        # Set the number of rows and columns
        self.setRowCount(self.df.shape[0])
        self.setColumnCount(self.df.shape[1])

        # Set the column headers
        # self.setHorizontalHeaderLabels(self.df.columns)
        
        # Populate the table with data
        for row in range(self.df.shape[0]):
            for col in range(self.df.shape[1]):
                item = QTableWidgetItem(str(self.df.iloc[row, col]))
                self.setItem(row, col, item)
                item.setFlags(item.flags()^(QtCore.Qt.ItemFlag.ItemIsSelectable|QtCore.Qt.ItemFlag.ItemIsEditable))




    