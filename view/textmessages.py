
from operator import truediv
import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import pandas as pd
import os
from allViber import allViber
import csv

from allWhatsApp import allWhatsApp
from allEmail import allEmail
import os
from mytable import *
from MyQwidgetItem import MyQwidgetItem
from datetime import datetime


class emaildetails(QWidget):
    

    def __init__(self,emails=None):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 200
        self.top = 0
        self.width = 1500
        self.height = 900
        self.initUI()
        if emails != None:
           self.allEmails(emails)
           
          
        self.buttonCVS.clicked.connect(self.buttonCVS_clicked)
        
       
       
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
      #  self.createTable()
        self.tableWidget = MyTableWidget()
        self.buttonCVS = QPushButton()
        self.buttonCVS.setText("export as a CVS")
        self.buttonCVS.move(64,32)
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonCVS)
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
        self.show()
        
        
        
   # def createTable(self):
       # Create table
      
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(12)
       
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Sender first Name"))
        self.tableWidget.setHorizontalHeaderItem(1,  QTableWidgetItem("Sender last Name"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Sender Email"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("The Email text"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Time sent"))
        self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem("Reciepeant Firt Name"))
        self.tableWidget.setHorizontalHeaderItem(6, QTableWidgetItem("Reciepeant last Name"))
        self.tableWidget.setHorizontalHeaderItem(7, QTableWidgetItem("Reciepeant Email"))
        self.tableWidget.setHorizontalHeaderItem(8, QTableWidgetItem("time recieved"))
        self.tableWidget.setHorizontalHeaderItem(9, QTableWidgetItem("stats"))
        self.tableWidget.setHorizontalHeaderItem(10, QTableWidgetItem("Bcc"))
        self.tableWidget.setHorizontalHeaderItem(11, QTableWidgetItem("cc"))
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,200)
        self.tableWidget.setColumnWidth(3,500)
        self.tableWidget.setColumnWidth(4,200)
        self.tableWidget.setColumnWidth(5,200)
        self.tableWidget.setColumnWidth(6,200)
        self.tableWidget.setColumnWidth(7,200)
        self.tableWidget.setColumnWidth(8,200)
        self.tableWidget.setColumnWidth(9,200)
        self.tableWidget.setColumnWidth(10,200)
        self.tableWidget.setColumnWidth(11,200)
        #self.allEmails()
        
        #self.WhatsApploading()
    
   
    def allEmails(self,emails):
        #emails=allEmail.getAllEmails(self)
        
        row=0
        self.tableWidget.setRowCount(len(emails))
      
        for i in emails:
               
              # index = PyQt5.QtCore.QPersistentModelIndex(
               # self.tableWidget.model().index(row, 1))
            
            # row.setitem(row,1, QTableWidgetItem(i.FromEmail_lastname))

            # self.tableWidget.rowAt[i] = row

               fname =  MyQwidgetItem(i.FromEmail_firstName)
               fname.ID =i.FromEmail_ID
               self.tableWidget.setItem(row,0,fname)

               self.tableWidget.setItem(row,1, MyQwidgetItem(i.FromEmail_lastname))
               self.tableWidget.setItem(row,2, MyQwidgetItem(i.FromEmail_Email))
               self.tableWidget.setItem(row,3, MyQwidgetItem(i.FromEmail_content_text))
               self.tableWidget.setItem(row,4, MyQwidgetItem(i.FromEmail_timeDate))
               self.tableWidget.setItem(row,5, MyQwidgetItem(i.ToEmail_firstName))
               self.tableWidget.setItem(row,6, MyQwidgetItem(i.ToEmail_lastname))
               self.tableWidget.setItem(row,7, MyQwidgetItem(i.ToEmail_Email))
               self.tableWidget.setItem(row,8, MyQwidgetItem(i.ToEmail_timeDate))
               self.tableWidget.setItem(row,9, MyQwidgetItem(i.ToEmail_timeDate))
               self.tableWidget.setItem(row,10, MyQwidgetItem(i.BccEmail_Email))
               self.tableWidget.setItem(row,11, MyQwidgetItem(i.CcEmail_Email))
               row=row+1
        

     
     
    

       
        self.tableWidget.move(0,0)
    def buttonCVS_clicked(self):
          desktop = os.path.join(os.path.join(os.environ['USERPROFILE']))
          now = datetime.now()
          now = int(now.strftime("%Y%m%d%H%M%S"))
          f = open(str(desktop)+'/'+'Desktop/evidance'+'/'+"Emaildata%d.csv"%now, "a", newline="")  # open csv file
          print(desktop)
          c = csv.writer(f)   
          

          
          rowcount=self.tableWidget.rowCount()
       

          c.writerow(
              [str('Sender first Name'), str('Sender last Name'), str('the sender email'),
              str('The Email text'), str('Reciepeant Firt Name'), str('Reciepeant last Name'), str('Reciepeant Email')
              ,str('Time sent')]) 
         
          for row  in range(rowcount):
          
              c.writerow(
              [str(self.tableWidget.item(row,0).text()), str(self.tableWidget.item(row,1).text()), str(self.tableWidget.item(row,2).text()),
              str(self.tableWidget.item(row,3).text()), str(self.tableWidget.item(row,4).text()), str(self.tableWidget.item(row,5).text()), str(self.tableWidget.item(row,6).text())
              ,str(self.tableWidget.item(row,7).text())]) 


        

    
  
   
     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = emaildetails()
    sys.exit(app.exec_())  
