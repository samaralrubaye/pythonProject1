

import csv
from datetime import datetime
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from mysqlx import Row
import pandas as pd
import os
from allViber import allViber

from allWhatsApp import allWhatsApp
from allEmail import allEmail
import os
from mytable import *
from MyQwidgetItem import MyQwidgetItem


class emaildetails(QWidget):

    def __init__(self, emails=None):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 200
        self.top = 0
        self.width = 1500
        self.height = 900
        self.initUI()
        if emails != None:
            self.allEmails(emails)

        

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

      #  self.createTable()
        self.tableWidget = MyTableWidget()
        self.buttonCVS = QPushButton()
        self.buttonCVS.setText("Import as a CVS")
        self.buttonCVS.move(64, 32)
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonCVS)
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.show()
       

   # def createTable(self):
       # Create table

        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)

        self.tableWidget.setHorizontalHeaderItem(
            0, QTableWidgetItem("Sender first Name"))
        self.tableWidget.setHorizontalHeaderItem(
            1,  QTableWidgetItem("Sender last Name"))
        self.tableWidget.setHorizontalHeaderItem(
            2, QTableWidgetItem("Sender Email"))

        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)

        # self.allEmails()

        # self.WhatsApploading()

        self.tableWidget.insertRow
        
        test =MyQwidgetItem('1')
        test.ID = 111
        test2 =MyQwidgetItem('2')
        test2.ID = 222
        test3 =MyQwidgetItem('3')
        test3.ID = 333
        self.tableWidget.setItem(1, 0, test)
        self.tableWidget.setItem(1, 1, test2)
        self.tableWidget.setItem(1, 2, test3)
        
        self.tableWidget.move(0, 0)
      
    #     self.tableWidget.cellClicked.connect(lambda:self.cell_was_clicked(self.tableWidget.currentRow(),self.tableWidget.currentColumn()))
    #     print(type(self.tableWidget.currentRow()))
    #     print(type(self.tableWidget.currentColumn()))
  

    # def cell_was_clicked(self, row, column):
    #         item = self.tableWidget.itemAt(self,row, column)
    #         print(type(self.tableWidget.currentRow()))
    #         print(type(self.tableWidget.currentColumn()))
    #         self.ID = item.text()
        

    

      
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = emaildetails()
    sys.exit(app.exec_())



