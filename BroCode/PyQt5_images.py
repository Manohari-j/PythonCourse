import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)

#
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # to pass and init var use super method
        self.setWindowTitle("My First GUI")
        self.setGeometry(800, 300, 500, 500)  # x, y width, height
        label = QLabel(self)
        #label.setGeometry(0, 0, label.width(), label.height())
        label.setGeometry(0, 0, 500, 400)

        # PYQt5 Images
        pixmap = QPixmap("E:\PythonCourse\BroCode\pexels-nickcollins-1274609.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
