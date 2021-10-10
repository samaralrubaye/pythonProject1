import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('Email Forensic Tool')
        # self.inituI()
        # WILL PUT ALL THE CHANGE IN THIS CLASS

    # def inituI(self):
    # self.label = QtWidgets.QLabel(self)
    # self.label.setText("my first label")
    # self.label.move(100, 70)
    # self.b1 = QtWidgets.QPushButton(self)
    # self.b1.setText("ff")
    # self.b1.clicked.connect(self.clicked)
    # self.move(55, 50)

    def window(self):
        # get the app setup
        app = QApplication(sys.argv)
        win = MyWindow()
        win.show()
        sys.exit(app.exec_())

    def clicked(self):
        self.label.setText("youchanged")


ns = MyWindow()
ns.window()
