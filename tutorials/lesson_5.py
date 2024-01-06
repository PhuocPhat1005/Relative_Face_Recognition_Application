import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QToolBar,
    QStatusBar,
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__intit__()
        self.setWindowTitle("My Awesome App")
