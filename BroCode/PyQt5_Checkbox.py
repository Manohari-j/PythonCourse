import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QCheckBox)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # to pass and init var use super method
        self.setWindowTitle("My First GUI")
        self.setGeometry(800, 300, 500, 500)  # x, y width, height
        self.checkbox = QCheckBox("Do you like food? ",self)

        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size:20px;"
                                    "font-family:Arial;")

        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self,state):

        if state == Qt.Checked:
            print("You like food")
        else:
            print("You don't like food")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
