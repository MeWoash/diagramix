from PyQt6.QtWidgets import QApplication
from Widgets.MainWindow import DiagramixMainWindow
import sys
import logging

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = DiagramixMainWindow()
    mainWindow.show()
    app.exec()
