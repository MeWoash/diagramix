from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainWindow = MainWindow.MainWindow()
    mainWindow.show()
    app.exec()
