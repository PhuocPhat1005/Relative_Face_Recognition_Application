from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QTextEdit,
    QMenu,
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction

# Only needed for access to command line arguments
import sys
from random import choice

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]


# Subclass QMainWindow to customize your application's main window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

# self.button_is_checked = True

# self.n_times_clicked = 0

# self.setWindowTitle("My App")

# self.label = QLabel()

# self.button = QPushButton("Press Me!")
# self.setFixedSize(QSize(400, 300))

# self.input = QLineEdit()
# self.input.textChanged.connect(self.label.setText)

# layout = QVBoxLayout()
# layout.addWidget(self.input)
# layout.addWidget(self.label)

# container = QWidget()
# container.setLayout(layout)

# QPushButton.clicked is a signal, it can be connected to a function
# self.button.setCheckable(True)
# self.button.clicked.connect(self.the_button_was_clicked)
# self.windowTitleChanged.connect(self.the_window_title_changed)

# Receiving data from a signal
# button.clicked.connect(self.the_button_was_toggled)

# self.button.released.connect(self.the_button_was_released)

# self.button.setChecked(self.button_is_checked)

# Set the central widget of the Window.
# self.setCentralWidget(self.button)
# self.setCentralWidget(container)

# def the_button_was_clicked(self):
#     print("Clicked.")
#     new_window_title = choice(window_titles)
#     print("Setting title: " + new_window_title)
#     self.setWindowTitle(new_window_title)

# self.button.setText("You already clicked me.")
# self.button.setEnabled(False)

# Also change the window title.
# self.setWindowTitle("My Oneshot App")

# def the_button_was_released(self):
#     # print("Checked?", checked)
#     # self.button_is_checked = checked
#     self.button_is_checked = self.button.isChecked()
#     print(self.button_is_checked)

# def the_window_title_changed(self, window_title):
#     print("Window title changed:" + window_title)
#     if window_title == "Something went wrong":
#         self.button.setDisabled(True)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.label = QLabel("Click in this window")
        # self.setCentralWidget(self.label)
        self.show()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    # def contextMenuEvent(self, e):
    #     context = QMenu(self)
    #     context.addAction(QAction("test 1", self))
    #     context.addAction(QAction("test 2", self))
    #     context.addAction(QAction("test 3", self))
    #     context.exec(e.globalPos())

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))

    def mousePressEvent(self, event):
        print("Mouse pressed!")
        super().mousePressEvent(event)

    #     if e.button() == Qt.MouseButton.LeftButton:
    #         # handle the left-button press in here
    #         self.label.setText("mousePressEvent LEFT")

    #     elif e.button() == Qt.MouseButton.MiddleButton:
    #         # handle the middle-button press in here.
    #         self.label.setText("mousePressEvent MIDDLE")

    #     elif e.button() == Qt.MouseButton.RightButton:
    #         # handle the right-button press in here.
    #         self.label.setText("mousePressEvent RIGHT")

    # def mouseReleaseEvent(self, e):
    #     if e.button() == Qt.MouseButton.LeftButton:
    #         self.label.setText("mouseReleaseEvent LEFT")

    #     elif e.button() == Qt.MouseButton.MiddleButton:
    #         self.label.setText("mouseReleaseEvent MIDDLE")

    #     elif e.button() == Qt.MouseButton.RightButton:
    #         self.label.setText("mouseReleaseEvent RIGHT")

    # def mouseDoubleClickEvent(self, e):
    #     if e.button() == Qt.MouseButton.LeftButton:
    #         self.label.setText("mouseDoubleClickEvent LEFT")

    #     elif e.button() == Qt.MouseButton.MiddleButton:
    #         self.label.setText("mouseDoubleClickEvent MIDDLE")

    #     elif e.button() == Qt.MouseButton.RightButton:
    #         self.label.setText("mouseDoubleClickEvent RIGHT")


class CustomButton(QPushButton):
    def mousePressEvent(self, e):
        e.accept()


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
# window = QWidget()
# window = QPushButton("Push me")
# window = QMainWindow()
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.
