import sys
import unittest
from PyQt5 import QtCore, QtWidgets, QtTest
from login import *

app = QtWidgets.QApplication(sys.argv)

class test01:
    '''Test the margarita mixer GUI'''
    def setUp(self):
        self.form = ui_Dialog()

    def test_defaults(self):
        self.LblUserName.setText('watson')
        self.lnEditPassword.setText('watson123')
        QtTest.QTest.mouseClick(self.BtnLogin, QtCore.Qt.LeftButton)
  

if __name__ == "__main__":
    unittest.main()