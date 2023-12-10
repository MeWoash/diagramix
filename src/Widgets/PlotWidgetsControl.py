import typing
from PyQt6 import QtCore
from pyqtgraph import PlotWidget, GraphicsLayoutWidget, PlotItem
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit, QCheckBox, QFileDialog, QTableWidget, QTableWidgetItem, QMainWindow, QScrollArea, QComboBox, QColorDialog
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIntValidator, QColor, QPalette
from Widgets.PlotWidgets import DiagramixPlot, DiagramixPlotObject
from DataControl.DiagramixDataController import DiagramixDataController
import numpy as np

class DiagramixPlotControls(QWidget):
    """
    Main widget which stores other widgets that can configure Plot.

    Args:
        QWidget (_type_): _description_
    """

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
        self.subplot_control = DiagramixPlotSubplotGenerator(self)
        self.subplot_control.n_plots_input.setText(str(self.diagramix_plot_ref.n_subplots))
        self.subplot_control.n_max_columns_input.setText(str(self.diagramix_plot_ref.n_max_columns))
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

        #SIGNAL GENERATOR
        self.signal_generator = DiagramixSignalContainer(self, self.diagramix_plot_ref)
        self.main_layout.addWidget(self.signal_generator)

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
        self.clear_button.clicked.connect(self.clear_button_wrapper)
        self.main_layout.addWidget(self.clear_button, alignment=Qt.AlignmentFlag.AlignBottom)

    def clear_button_wrapper(self):
        self.diagramix_plot_ref.clear_plot_items()
        self.signal_generator.signal_table.clear_items()

    def file_input_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Wszystkie pliki (*);;Pliki CSV (*.csv);;Pliki TXT (*.txt)")
        load_succeeded = False
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

        self.clear_button_wrapper()
        
        self.diagramix_plot_ref.create_subplots()

        self.signal_generator.signal_generator.update_options()

class DiagramixPlotSubplotGenerator(QWidget):
    """
    Widget Used to generate Subplots

    Args:
        QWidget (_type_): _description_
    """
    def __init__(self, parent) -> None:
        super().__init__(parent)

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
    """
    Widget showing loaded data in table.

    Args:
        QTableWidget (_type_): _description_
    """

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

class DiagramixSignalContainer(QWidget):
    """
    Widget used to manage signals in subplots

    Args:
        QWidget (_type_): _description_
    """
    
    def __init__(self, parent: QWidget, diagramix_plot: DiagramixPlot) -> None:
        super().__init__(parent)
        self.diagramix_plot_ref:DiagramixPlot = diagramix_plot
        self.data_controller:DiagramixDataController = diagramix_plot.data_controller
        
        self.create_layout()

    def create_layout(self):
        """
        Creates main widget layout
        """
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.signal_table = DiagramixSignalTable(self)
        self.signal_generator = DiagramixSignalGenerator(self, self.signal_table, self.diagramix_plot_ref)

        signal_generator_label = QLabel("Signal Generator")
        self.main_layout.addWidget(signal_generator_label)

        self.main_layout.addWidget(self.signal_generator)

        signal_table_label = QLabel("Signal Table")
        self.main_layout.addWidget(signal_table_label)
        
        self.main_layout.addWidget(self.signal_table)


class DiagramixSignalGenerator(QWidget):
    """
    Widget used to add signals

    Args:
        QWidget (_type_): _description_
    """
    def __init__(self, parent, signal_table ,diagramix_plot: DiagramixPlot) -> None:
        super().__init__(parent)
        self.signal_table = signal_table
        self.diagramix_plot_ref:DiagramixPlot = diagramix_plot
        self.data_controller:DiagramixDataController = diagramix_plot.data_controller

        self.create_layout()
        
    def create_layout(self):
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.signal_name_input_label = QLabel("Name")
        self.main_layout.addWidget(self.signal_name_input_label, 0, 0)
        self.signal_name_input = QLineEdit()
        self.main_layout.addWidget(self.signal_name_input, 0, 1)

        self.x_data_box_label = QLabel("X")
        self.main_layout.addWidget(self.x_data_box_label, 1, 0)
        self.x_data_box = QComboBox()
        self.main_layout.addWidget(self.x_data_box, 1, 1)

        self.y_data_box_label = QLabel("Y")
        self.main_layout.addWidget(self.y_data_box_label, 2, 0)
        self.y_data_box = QComboBox()
        self.main_layout.addWidget(self.y_data_box, 2, 1)

        self.color_label = QLabel("Color")
        self.main_layout.addWidget(self.color_label, 3, 0)
        self.color_button = QPushButton()
        self.main_layout.addWidget(self.color_button, 3, 1)

        self.subplot_label = QLabel("Subplot")
        self.main_layout.addWidget(self.subplot_label, 4, 0)
        self.subplot_box = QComboBox()
        self.main_layout.addWidget(self.subplot_box, 4, 1)

        R=np.random.randint(0,256)
        G=np.random.randint(0,256)
        B=np.random.randint(0,256)
        color = QColor(R, G, B)
        self.color_button.setStyleSheet(f'background-color: rgb({color.red()}, {color.green()}, {color.blue()});')
        self.color_button.clicked.connect(self.color_button_clicked)
        
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_button_clicked)
        self.main_layout.addWidget(self.add_button, 5, 0, 1, 2)

        self.update_options()

    def update_options(self):
        self.subplot_box.clear()
        self.subplot_box.addItems([str(i) for i in range(self.diagramix_plot_ref.n_subplots)])

    def color_button_clicked(self):
        color = QColorDialog.getColor()
        self.color_button.setStyleSheet(f'background-color: rgb({color.red()}, {color.green()}, {color.blue()});')

    def add_button_clicked(self):

        x=np.linspace(0,6.28,100)
        y=np.sin(x)
        plot_number = int(self.subplot_box.currentText())
        subplot_parent =  self.diagramix_plot_ref.subplots[plot_number]
        plot_object = DiagramixPlotObject(x, y, subplot_number=plot_number, subplot_parent=subplot_parent)
        subplot_parent.add_plot_data_item(plot_object)

        #CLEAR
        self.clear_data()

        plot_object_table = DiagramixSignalTableObject(self.signal_table, plot_object)
        self.signal_table.add_item(plot_object_table)

        

    def clear_data(self):
        self.signal_name_input.clear()
        self.x_data_box.clear()
        self.y_data_box.clear()
        
        R=np.random.randint(0,256)
        G=np.random.randint(0,256)
        B=np.random.randint(0,256)
        color = QColor(R, G, B)
        self.color_button.setStyleSheet(f'background-color: rgb({color.red()}, {color.green()}, {color.blue()});')


class DiagramixSignalTable(QScrollArea):
    """
    Widget displaying added signals

    Args:
        QScrollArea (_type_): _description_
    """

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        self.scroll_area_widget = QWidget()
        self.setWidget(self.scroll_area_widget)

        self.scroll_area_layout = QVBoxLayout()
        self.scroll_area_widget.setLayout(self.scroll_area_layout)

    def add_item(self, item):
        self.scroll_area_layout.addWidget(item)

    def clear_items(self):
        for i in reversed(range(self.scroll_area_layout.count())): 
            self.scroll_area_layout.itemAt(i).widget().setParent(None)
    
class DiagramixSignalTableObject(QWidget):
    counter = 0
    def __init__(self, parent, plot_object_ref: DiagramixPlotObject) -> None:
        super().__init__(parent)
        self.plot_object_ref: DiagramixPlotObject = plot_object_ref
        self.id = DiagramixSignalTableObject.counter
        DiagramixSignalTableObject.counter += 1

        self.create_layout()


    def create_layout(self):
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.id_label = QLabel(f"#{self.id}")
        self.main_layout.addWidget(self.id_label, 0, 0)

        self.id_subplot = QLabel(f"Subplot: {self.plot_object_ref.subplot_number}")
        self.main_layout.addWidget(self.id_subplot, 0, 1)

        self.delete_button = QPushButton(f"Delete")
        self.delete_button.clicked.connect(self.delete_clicked)
        self.main_layout.addWidget(self.delete_button, 0, 2)

    def delete_clicked(self):
        self.plot_object_ref.prepare_deleting()
        self.plot_object_ref.deleteLater()
        self.deleteLater()
        
        


    



    