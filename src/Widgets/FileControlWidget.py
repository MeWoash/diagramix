from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
from DataControl.DiagramixDataController import DiagramixDataController
from Widgets.PlotWidgets import DiagramixPlot


class DiagramixFileWidget(QWidget):
    def __init__(self, parent: QWidget, diagramix_plot: DiagramixPlot) -> None:
        super().__init__()

        self.diagramix_plot_ref: DiagramixPlot = diagramix_plot
        self.data_controller: DiagramixDataController = diagramix_plot.data_controller
        self.create_layout()

    def create_layout(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # LOAD FILE
        self.file_input = QPushButton("Choose File")
        self.file_input.clicked.connect(self.file_input_clicked)
        self.main_layout.addWidget(self.file_input)

        self.file_input_label = QLabel("File:")
        self.main_layout.addWidget(self.file_input_label)

        # VIEW FILE
        self.view_table_button = QPushButton("View Table")
        self.view_table_button.setEnabled(False)
        self.view_table_button.clicked.connect(self.view_table_button_clicked)
        self.main_layout.addWidget(self.view_table_button)

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

    def view_table_button_clicked(self):
        window = QMainWindow(self)
        table = DiagramixTableView(self.data_controller.df)
        window.setWindowTitle("DataFrame Preview")
        window.setCentralWidget(table)
        window.show()