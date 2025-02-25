import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # to pass and init var use super method
        self.setWindowTitle("My First GUI")
        self.setGeometry(800, 300, 500, 500)  # x, y width, height
        # PYQt5 Labels label = QLabel(self) label.setGeometry(0,0, label.width(), label.height()) label.setGeometry(
        # 0, 0, 500, 500) label.setGeometry((self.width()-label.width())//2, (self.height()-label.height())//2,
        # label.width(), label.height())

        # PYQt5 Images
        # pixmap = QPixmap("E:\PythonCourse\BroCode\pexels-nickcollins-1274609.jpg")
        # label.setPixmap(pixmap)
        # label.setScaledContents(True)
        # self.setWindowIcon(QIcon("E:\PythonCourse\BroCode\pexels-nickcollins-1274609.jpg"))
        # label = QLabel("Welcome", self)
        # label.setFont(QFont("Arial", 30))
        # label.setGeometry(0, 0, 500, 100)
        # label.setStyleSheet("color: green;"
        #                     "background-color: yellow;"
        #                     "font-weight: bold;"
        #                     "font-style: italic;"
        #                     "text-decoration: underline;")  # stylesheet arg should end with ;
        # label.setAlignment(Qt.AlignTop) # vertical top
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignVCenter)

        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignLeft)
        #
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignCenter)
        self.initUI()

        # PYQt5 Layouts : Layouts cannot be added in main window init

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        l1 = QLabel("#1", self)
        l2 = QLabel("#2", self)
        l3 = QLabel("#3", self)
        l4 = QLabel("#4", self)
        l5 = QLabel("#5", self)

        l1.setStyleSheet("background-color: red;")
        l2.setStyleSheet("background-color: yellow;")
        l3.setStyleSheet("background-color: green;")
        l4.setStyleSheet("background-color: blue;")
        l5.setStyleSheet("background-color: orange;")

        # vbox = QVBoxLayout()
        # vbox.addWidget(l1)
        # vbox.addWidget(l2)
        # vbox.addWidget(l3)
        # vbox.addWidget(l4)
        # vbox.addWidget(l5)

        # central_widget.setLayout(vbox)
        # hbox = QHBoxLayout()
        # hbox.addWidget(l1)
        # hbox.addWidget(l2)
        # hbox.addWidget(l3)
        # hbox.addWidget(l4)
        # hbox.addWidget(l5)
        #
        # central_widget.setLayout(hbox)

        grid = QGridLayout()
        grid.addWidget(l1,0,0)
        grid.addWidget(l2,0,1)
        grid.addWidget(l3,0,2)
        grid.addWidget(l4,1,0)
        grid.addWidget(l5,1,1)

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
