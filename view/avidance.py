import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PIL import ImageGrab


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'How To Take Screenshot using Python and PyQt5'
        self.left = 250
        self.top = 250
        self.width = 200
        self.height = 90
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        """
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        """

        self.button = QPushButton('&Take screenshot', self)
        self.button.move(20, 20)

        self.setWindowIcon(QIcon('icon.png'))

        self.button.clicked.connect(self.on_click)
        self.show()
    #button.clicked.connect(self.on_click) binds signal of a button ( clicked ) to a slot self.on_click . 
    #@pyqtSlot()
    def on_click(self):
        import os
        path = self.getdirectory()
        for el in path:
            if os.path.exists(el):
                time.sleep(2)
                img = ImageGrab.grab()
                time_now = time.strftime("%Y%m%d%h%M%S")
                name = f"screen{time_now}"
                img.save(f"{path}/{name}.png", "png")
                name_img = name
                QMessageBox.question(self, 'Screenshot make!', f"Screenshot save in directory {path}/" + name_img,QMessageBox.Ok,QMessageBox.Ok)
                break
            else:
                try:
                    os.mkdir(path)
                except OSError:
                    time.sleep(2)
                    img = ImageGrab.grab()
                    time_now = time.strftime("%Y%m%d%h%M%S")
                    name = f"screen{time_now}"
                    img.save(f"{path}/{name}.png", "png")
                    name_img = name
                    QMessageBox.question(self, 'Screenshot make!', f"Screenshot save in directory {path}/" + name_img,QMessageBox.Ok,QMessageBox.Ok)
                    break
                else:
                    time.sleep(2)
                    img = ImageGrab.grab()
                    time_now = time.strftime("%Y%m%d%h%M%S")
                    name = f"screen{time_now}"
                    img.save(f"{path}/{name}.png", "png")
                    name_img = name
                    QMessageBox.question(self, 'Screenshot make!', f"Screenshot save in directory {path}/" + name_img,QMessageBox.Ok,QMessageBox.Ok)

                    break

    def getdirectory(self):
        response = QtWidgets.QFileDialog.getExistingDirectory(caption='Select folder')
        print(response)
        return response


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())