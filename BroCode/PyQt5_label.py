import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # to pass and init var use super method
        self.setWindowTitle("My First GUI")
        self.setGeometry(800, 300, 500, 500)  # x, y width, height
        # PYQt5 Labels
        label = QLabel(self)
        label.setGeometry(0,0, label.width(), label.height())
        label.setGeometry( 0, 0, 500, 500)
        #label.setGeometry((self.width()-label.width())//2, (self.height()-label.height())//2,label.width(), label.height())


        self.setWindowIcon(QIcon("E:\PythonCourse\BroCode\pexels-nickcollins-1274609.jpg"))
        label = QLabel("Welcome", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: green;"
                            "background-color: yellow;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")  # stylesheet arg should end with ;
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
        label.setAlignment(Qt.AlignCenter)




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
