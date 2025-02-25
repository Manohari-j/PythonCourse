import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # to pass and init var use super method
        self.setWindowTitle("My First GUI")
        self.setGeometry(800, 300, 500, 500)  # x, y width, height
        self.button = QPushButton("Click Me!", self)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):

        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click) # signal is clicked and should be connected to a slot

        self.label.setGeometry(170,300, 200,100)
        self.label.setStyleSheet("font-size:50px;")

    def on_click(self):
        # print("Button Clicked!")
        # self.button.setText("Clicked!")
        # self.button.setDisabled(True)
        self.label.setText("GoodBye!")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
