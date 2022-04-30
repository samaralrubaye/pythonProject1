import sys
import sys
import time
from typing import overload
from PyQt5.QtWidgets import *

from mytable import *
from MyQwidgetItem import MyQwidgetItem

import csv
from datetime import datetime
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot,QTimer
import pandas as pd

from viber import viber

from viberSummary import vibersummary
from allEmail import allEmail
from allWhatsApp import allWhatsApp

from allViber import allViber




class MyTableWidget(QTableWidget):
    def __init__(self,cID = None,ctype = None):
        super().__init__()
        
         
        self.caseid = cID        
        self.type = ctype
        # self.setMinimumWidth(400)
        # self.setColumnCount(1)
        # self.setColumnWidth(0, 400)
        # self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.itemClicked.connect(self.handleItemClick)
   
    @property
    def CaseID(self):
        return self.caseid

    @CaseID.setter
    def CaseID(self, value):
        self.caseid = value
 
 
    @property
    def Type(self):
        return self.type

    @Type.setter
    def Type(self, value):
        self.type = value

    def initUI(self):
        self.title = 'PyQt5 table'
        self.left = 20000
        self.top = 200
        self.width = 1000
        self.height = 400
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
      
        
        self.buttonCVS = QPushButton()
        self.btnclose = QPushButton()
        self.buttonCVS.setText("Import as a CVS")
        self.btnclose.setText("close") 
        self.buttonCVS.move(64,32)
        self.layout.addWidget(self.buttonCVS) 
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget( self.btnclose)  
        self.setLayout(self.layout) 
        self.show()
        self.btnclose.clicked.connect(self.hidding)
        

    def handleItemClick(self, item):
        try:
            # self.progressBar.setValue(self.counter)
            # if self.counter == int(self.n * 0.3):
            #     self.labelDescription.setText('<strong>Working on Task #2</strong>')
            # elif self.counter == int(self.n * 0.6):
            #     self.labelDescription.setText('<strong>Working on Task #3</strong>')
            # elif self.counter >= self.n:
            #  self.timer.stop()
            #  self.close()

            #  time.sleep(1)

            # self.SplashScreen= SplashScreen()
            # self.SplashScreen.show()

            #  self.counter += 1
         
             
             self.title = 'PyQt5 table'
             self.left = 20000
             self.top = 200
             self.width = 1000
             self.height = 400
             self.initUI()
             self.tableWidget.setRowCount(10)
             self.tableWidget.setColumnCount(10)
             self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Sender first Name"))
             self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Sender last Name"))
             self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem(" message"))
  
             self.tableWidget.setColumnWidth(0,200)
             self.tableWidget.setColumnWidth(1,200)
             self.tableWidget.setColumnWidth(2,200)
             
             if (self.Type == 1):
              self.GetEmails(item.ID)
        
             if (self.Type == 2):
              self.WhatsApploading(item.ID)
              
             if (self.Type == 3):
              self.vibercall(item.ID)
            #  pop=summary(self,item.ID)
            #  pop.show()
            #  pop=checking()
            #  pop.show()
        except:
            print('tt')

    def GetEmails(self,senderID):
        #emails=allEmail.getAllEmails(self)
        
        emails=allEmail.getEmailsBySenderID(self,self.CaseID,senderID)

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
               
    def vibercall(self, senderID):
        vibers=allViber.getVibersBySenderID(self,self.CaseID,senderID)
        row=0
        self.tableWidget.setRowCount(len(vibers))
        for j in vibers:
            fname =  MyQwidgetItem(j.FromViber_Msg_FirstName)
            fname.ID =j.FromViber_Msg_ID
            self.tableWidget.setItem(row,0,fname)
          
            self.tableWidget.setItem(row,1, MyQwidgetItem(j.FromViber_Msg_LastName))
            self.tableWidget.setItem(row,2, MyQwidgetItem(j.FromViber_Msg_number))
            self.tableWidget.setItem(row,3, MyQwidgetItem(j.ToViber_Msg))
            self.tableWidget.setItem(row,4, MyQwidgetItem(j.ToViber_Msg_DateandTime))
            self.tableWidget.setItem(row,5, MyQwidgetItem(j.ToViber_Msg_FirstName))
            self.tableWidget.setItem(row,6, MyQwidgetItem(j.ToViber_Msg_LastName))
            self.tableWidget.setItem(row,7, MyQwidgetItem(j.ToViber_Msg_number))
            self.tableWidget.setItem(row,8, MyQwidgetItem(j.ToViber_Msg))
            row=row+1
            self.tableWidget.move(0,0)
     
     
    def WhatsApploading(self, senderID):
          WhatsApps= allWhatsApp.getWhatsAppBySenderID(self,self.CaseID,senderID)
          row=0
          self.tableWidget.setRowCount(len(WhatsApps))
          for j in WhatsApps:
            fname =  MyQwidgetItem(j.FromWhatsApp_Msg_FirstName)
            fname.ID =j.FromWhatsApp_Msg_ID
            self.tableWidget.setItem(row,0,fname)
            self.tableWidget.setItem(row,1, MyQwidgetItem(j.FromWhatsApp_Msg_LastName))
            self.tableWidget.setItem(row,2, MyQwidgetItem(j.FromWhatsApp_Msg_number))
            self.tableWidget.setItem(row,3, MyQwidgetItem(j.FromWhatsApp_Msg))
            self.tableWidget.setItem(row,4, MyQwidgetItem(j.FromWhatsApp_Msg_DateandTime))
            self.tableWidget.setItem(row,5, MyQwidgetItem(j.ToWhatsApp_Msg_FirstName))
            self.tableWidget.setItem(row,6, MyQwidgetItem(j.ToWhatsApp_Msg_LastName))
            self.tableWidget.setItem(row,7, MyQwidgetItem(j.ToWhatsApp_Msg_number))
            self.tableWidget.setItem(row,8, MyQwidgetItem(j.ToWhatsApp_Msg_DateandTime))
            row=row+1   
            self.tableWidget.move(0,0)


    def hidding(self):
        # bookmark = QtWidgets.QDialog()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyTableWidget()
    sys.exit(app.exec_())  
    #sys.exit(app.exec_())
        
       
    #     self.cellClicked.connect(lambda:self.cell_was_clicked(self.currentRow(),self.currentColumn()))
    #     print(type(self.currentRow()))
    #     print(type(self.currentColumn()))
  

    # def cell_was_clicked(self, row, column):
    #         item = self.itemAt(self,row, column)
    #         print(type(self.currentRow()))
    #         print(type(self.currentColumn()))
    #         self.ID = item.text()
        
