import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QRadioButton, QButtonGroup)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # to pass and init var use super method
        self.setWindowTitle("My First GUI")
        self.setGeometry(800, 300, 500, 500)  # x, y width, height
        self.r1 = QRadioButton("Visa", self)
        self.r2 = QRadioButton("Master Card", self)
        self.r3 = QRadioButton("Gift Card", self)
        self.r4 = QRadioButton("In Store", self)
        self.r5 = QRadioButton("Online", self)

        self.bg1 = QButtonGroup(self)
        self.bg2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.r1.setGeometry(0, 0, 300, 50)
        self.r2.setGeometry(0, 50, 300, 50)
        self.r3.setGeometry(0, 100, 300, 50)
        self.r4.setGeometry(0, 150, 300, 50)
        self.r5.setGeometry(0, 200, 300, 50)
        # for a group format
        self.setStyleSheet("QRadioButton{"
                           "font-size:20px;"
                           "font-style:Arial;"
                           "padding:10px;"
                           "}")

        self.bg1.addButton(self.r1)
        self.bg1.addButton(self.r2)
        self.bg1.addButton(self.r3)
        self.bg2.addButton(self.r4)
        self.bg2.addButton(self.r5)

        self.r1.toggled.connect(self.radio_selected)
        self.r2.toggled.connect(self.radio_selected)
        self.r3.toggled.connect(self.radio_selected)
        self.r4.toggled.connect(self.radio_selected)
        self.r5.toggled.connect(self.radio_selected)

    def radio_selected(self):
        # print("You selected something")
        radio = self.sender()
        if radio.isChecked():
            print(f"{radio.text()} is selected")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
