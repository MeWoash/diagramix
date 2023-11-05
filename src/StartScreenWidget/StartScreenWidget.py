import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion

class StartScreenWidget(QWidget):

    def __init__(self):
        super().__init__()

        input_file_path = None

        layout = QVBoxLayout()

        # Adding logo 
        logo_label = QLabel()
        logo_pixmap = QPixmap("img/logo.png").scaled(400, 400, Qt.AspectRatioMode.IgnoreAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignHCenter)


        # Adding input button
        file_input = QPushButton("Wybierz ścieżkę pliku")
        file_input.clicked.connect(self.load_file)
        layout.addWidget(file_input, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Adding input label
        self.input_label = QLabel("Plik: ")
        layout.addWidget(self.input_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Adding input button
        self.start_btn = QPushButton("Start")
        self.start_btn.setEnabled(False)
        self.start_btn.clicked.connect(self.start_btn_clicked)
        layout.addWidget(self.start_btn, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)
        self.setGeometry(100, 100, 800, 600)



    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Wszystkie pliki (*);;Pliki CSV (*.csv);;Pliki TXT (*.txt)")
        if file_name:
            self.input_file_path = file_name
            self.input_label.setText(f"Plik {file_name}")
            self.start_btn.setEnabled(True)

    def start_btn_clicked(self):
        #TODO replace startScreenWidget with plotWidget
        pass