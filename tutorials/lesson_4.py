# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QWidget,
#     QVBoxLayout,
#     QHBoxLayout,
#     QGridLayout,
#     QStackedLayout,
# )
# from PyQt6.QtGui import QPalette, QColor


# class Color(QWidget):
#     def __init__(self, color):
#         super(Color, self).__init__()

#         self.setAutoFillBackground(True)

#         palette = self.palette()
#         palette.setColor(QPalette.ColorRole.Window, QColor(color))
#         self.setPalette(palette)


# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super(MainWindow, self).__init__()

# #         self.setWindowTitle("My App")

# #         layout1 = QHBoxLayout()
# #         layout2 = QVBoxLayout()
# #         layout3 = QVBoxLayout()

# #         layout1.setContentsMargins(0, 0, 0, 0)
# #         layout1.setSpacing(20)

# #         layout2.addWidget(Color("red"))
# #         layout2.addWidget(Color("yellow"))
# #         layout2.addWidget(Color("purple"))

# #         layout1.addLayout(layout2)

# #         layout1.addWidget(Color("green"))

# #         layout3.addWidget(Color("red"))
# #         layout3.addWidget(Color("purple"))

# #         layout1.addLayout(layout3)

# #         widget = QWidget()
# #         widget.setLayout(layout1)
# #         self.setCentralWidget(widget)


# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super(MainWindow, self).__init__()

# #         self.setWindowTitle("My App")

# #         layout = QGridLayout()

# #         layout.addWidget(Color("red"), 0, 0)
# #         layout.addWidget(Color("green"), 1, 0)
# #         layout.addWidget(Color("blue"), 1, 1)
# #         layout.addWidget(Color("purple"), 2, 1)


# #         widget = QWidget()
# #         widget.setLayout(layout)
# #         self.setCentralWidget(widget)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         layout = QStackedLayout()

#         layout.addWidget(Color("red"))
#         layout.addWidget(Color("green"))
#         layout.addWidget(Color("blue"))
#         layout.addWidget(Color("yellow"))

#         layout.setCurrentIndex(3)

#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()

# import sys

# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import (
#     QApplication,
#     QHBoxLayout,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QStackedLayout,
#     QVBoxLayout,
#     QWidget,
# )

# from layout_colorwidget import Color


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         pagelayout = QVBoxLayout()
#         button_layout = QHBoxLayout()
#         self.stacklayout = QStackedLayout()

#         pagelayout.addLayout(button_layout)
#         pagelayout.addLayout(self.stacklayout)

#         btn = QPushButton("red")
#         btn.pressed.connect(self.activate_tab_1)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("red"))

#         btn = QPushButton("green")
#         btn.pressed.connect(self.activate_tab_2)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("green"))

#         btn = QPushButton("yellow")
#         btn.pressed.connect(self.activate_tab_3)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("yellow"))

#         widget = QWidget()
#         widget.setLayout(pagelayout)
#         self.setCentralWidget(widget)

#     def activate_tab_1(self):
#         self.stacklayout.setCurrentIndex(0)

#     def activate_tab_2(self):
#         self.stacklayout.setCurrentIndex(1)

#     def activate_tab_3(self):
#         self.stacklayout.setCurrentIndex(2)


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
)

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)
        tabs.setDocumentMode(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
