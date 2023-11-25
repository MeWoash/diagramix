from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout


class DiagramixControlWidget(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.create_layout()

    def create_layout(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # LOAD FILE
        self.file_input = QPushButton("Choose File")
        # self.file_input.clicked.connect(self.file_input_clicked)
        self.main_layout.addWidget(self.file_input)

        self.file_input_label = QLabel("File:")
        self.main_layout.addWidget(self.file_input_label)

    # def file_input_clicked(self):
    #     file_name, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Wszystkie pliki (*);;Pliki CSV (*.csv);;Pliki TXT (*.txt)")
    #     if file_name:
    #         self.input_file_path = file_name
    #         self.file_input_label.setText(f"File: {file_name}")
    #         load_succeeded = self.data_controller.load_file(file_path=file_name)
    #
    #     self.view_table_button.setEnabled(load_succeeded)