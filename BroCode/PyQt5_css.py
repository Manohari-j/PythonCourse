import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.b1 = QPushButton("#1")
        self.b2 = QPushButton("#2")
        self.b3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.b1)
        hbox.addWidget(self.b2)
        hbox.addWidget(self.b3)

        central_widget.setLayout(hbox)

        self.b1.setObjectName("b1")
        self.b2.setObjectName("b2")
        self.b3.setObjectName("b3")

        # for all the buttons
        # padding inside, margin: around the widget
        self.setStyleSheet("""
            QPushButton{
                font-size:40px;
                font-family:Arial;
                padding:15px 75px;
                margin:25px;
                border:3px solid;
                border-radius:15px;
            }
            QPushButton#b1{
                background-color: red;
            }
            QPushButton#b2{
                background-color: yellow;
            }
            QPushButton#b3{
                background-color: green;          
            }
            QPushButton#b1:hover{
                background-color: pink;
            }
            QPushButton#b2:hover{
                background-color: brown;
            }
            QPushButton#b3:hover{
                background-color: blue;
            }
        """)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())