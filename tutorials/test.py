import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QCheckBox,
    QComboBox,
    QListWidget,
    QLineEdit,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QSlider,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QRadioButton,
    QGroupBox,
    QProgressBar,
    QCalendarWidget,
    QTabWidget,
    QFormLayout,
    QDateEdit,
    QDateTimeEdit,
    QDial,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow):
    # def __init__(self):
    #     super(MainWindow, self).__init__()

    #     self.setWindowTitle("My App")

    #     widget = QLabel("Hello")
    #     font = widget.font()
    #     font.setPointSize(30)
    #     widget.setFont(font)
    #     widget.setAlignment(
    #         Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
    #     )
    #     widget.setPixmap(QPixmap("test.jpg"))
    #     widget.setScaledContents(True)
    #     self.setCentralWidget(widget)
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # Combobox
        # widget = QComboBox()
        # widget.addItems(["One", "Two", "Three"])

        # # Sends the current index (position) of the selected item.
        # widget.currentIndexChanged.connect(self.index_changed)

        # # There is an alternate signal to send the text.
        # widget.currentTextChanged.connect(self.text_changed)

        # widget.setEditable(True)
        # widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)\

        #     widget = QListWidget()
        #     widget.addItems(["One", "Two", "Three"])

        #     widget.currentItemChanged.connect(self.index_changed)
        #     widget.currentTextChanged.connect(self.text_changed)

        #     self.setCentralWidget(widget)

        # def index_changed(self, i):  # Not an index, i is a QListWidgetItem
        #     print(i.text())

        # def text_changed(self, s):  # s is a str
        #     print(s)

        #     widget = QLineEdit()
        #     widget.setMaxLength(10)
        #     widget.setPlaceholderText("Enter your text")

        #     # widget.setReadOnly(True) # uncomment this to make readonly

        #     widget.returnPressed.connect(self.return_pressed)
        #     widget.selectionChanged.connect(self.selection_changed)
        #     widget.textChanged.connect(self.text_changed)
        #     widget.textEdited.connect(self.text_edited)
        #     widget.setInputMask("000.000.000.000;_")

        #     self.setCentralWidget(widget)

        # def return_pressed(self):
        #     print("Return pressed!")
        #     self.centralWidget().setText("BOOM!")

        # def selection_changed(self):
        #     print("Selection changed")
        #     print(self.centralWidget().selectedText())

        # def text_changed(self, s):
        #     print("Text changed...")
        #     print(s)

        # def text_edited(self, s):
        #     print("Text edited...")
        #     print(s)

        #     widget = QSpinBox()
        #     widget.setMinimum(-10)
        #     widget.setMaximum(3)

        #     widget.setPrefix("$")
        #     widget.setSuffix("c")
        #     widget.setSingleStep(3)
        #     widget.valueChanged.connect(self.value_changed)
        #     widget.textChanged.connect(self.value_changed_str)
        #     widget.lineEdit().setReadOnly(True)

        #     self.setCentralWidget(widget)

        # def value_changed(self, i):
        #     print(i)

        # def value_changed_str(self, s):
        #     print(s)

        #     widget = QSlider(Qt.Orientation.Horizontal)
        #     widget.setMinimum(-10)
        #     widget.setMaximum(3)

        #     widget.setSingleStep(3)

        #     widget.valueChanged.connect(self.value_changed)
        #     widget.sliderMoved.connect(self.slider_position)
        #     widget.sliderPressed.connect(self.slider_pressed)
        #     widget.sliderReleased.connect(self.slider_released)

        #     self.setCentralWidget(widget)

        # def value_changed(self, i):
        #     print(i)

        # def slider_position(self, p):
        #     print("position", p)

        # def slider_pressed(self):
        #     print("Pressed!")

        # def slider_released(self):
        #     print("Released!")

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released!")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
