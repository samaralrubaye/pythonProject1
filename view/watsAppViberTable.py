import csv
from datetime import datetime
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import pandas as pd
from allViber import allViber
from allWhatsApp import allWhatsApp
from mytable import *
from MyQwidgetItem import MyQwidgetItem



class ViberWatsAppTable(QWidget):

    def __init__(self,  WhatsApps=None,Vibers=None,cID = None):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 200
        self.top = 0
        self.width = 1500
        self.height = 900
        self.type = 0
        self.caseid = cID
        if WhatsApps != None:
           self.type = 2
           
        if Vibers != None:
           self.type = 3
           
        self.initUI()
        if WhatsApps != None:
           self.WhatsApploading(WhatsApps)
           self.buttonCVS.clicked.connect(self.buttonCVS_clicked)
           
        if Vibers != None:
           self.vibercall(Vibers)
           self.buttonCVS.clicked.connect(self.buttonCVS_clicked)
        
        
    
    @property
    def Type(self):
        return self.type

    @Type.setter
    def Type(self, value):
        self.type = value


    @property
    def caseId(self):
        return self.caseid

    @caseId.setter
    def caseId(self, value):
        self.caseid = value
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
      #  self.createTable()
        # self.tableWidget = MyTableWidget()
        
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.tableWidget = MyTableWidget(self.caseId,self.Type)
        
        self.buttonCVS = QPushButton()
        self.buttonCVS.setText("Export as a CVS")
        self.buttonCVS.move(64,32)
        self.layout.addWidget(self.buttonCVS) 
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
        self.show()
     

   # def createTable(self):
       # Create table
      
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Sender first Name"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Sender last Name"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Number"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("The message"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Time sent"))
        self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem("Reciepeant Firt Name"))
        self.tableWidget.setHorizontalHeaderItem(6, QTableWidgetItem("Reciepeant last Name"))
        self.tableWidget.setHorizontalHeaderItem(7, QTableWidgetItem("Recipeant Number"))
        self.tableWidget.setHorizontalHeaderItem(8, QTableWidgetItem("time recieved"))
        self.tableWidget.setHorizontalHeaderItem(9, QTableWidgetItem("stats"))
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,200)
        self.tableWidget.setColumnWidth(3,500)
        self.tableWidget.setColumnWidth(4,200)
        self.tableWidget.setColumnWidth(5,200)
        self.tableWidget.setColumnWidth(6,200)
        self.tableWidget.setColumnWidth(7,200)
        self.tableWidget.setColumnWidth(8,200)
        #self.vibercall()
        
    
    def vibercall(self, vibers):
        #vibers=allViber.getAllVibers(self,88888,'2000/1/1','4000/1/1','')
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
     
     
    def WhatsApploading(self, WhatsApps):
         # WhatsApps= allWhatsApp.getAllWhatsApp(self,88888,'2000/1/1','4000/1/1','')
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
    def buttonCVS_clicked(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']))
        now = datetime.now()
        now = int(now.strftime("%Y%m%d%H%M%S"))
        f = open(str(desktop)+'/'+'Desktop/evidance'+'/'+"chatdata%d.csv"%now, "a", newline="")  # open csv file
        print(desktop)
        c = csv.writer(f) 
        rowcount=self.tableWidget.rowCount()
         

        c.writerow(
              [str('sender_firt_tname'),
             str('SenderlastName'),str('Sender number'),str('The message'),str('Time sent'),
              str('Reciepeant Firt Name'),str('Reciepeant last Name'), str('Recipeant Number'), str('Sending_dateTime')])  
        for row  in range(rowcount):
                c.writerow(
              [str(self.tableWidget.item(row,0).text()), str(self.tableWidget.item(row,1).text()), str(self.tableWidget.item(row,2).text()),
              str(self.tableWidget.item(row,3).text()), str(self.tableWidget.item(row,4).text()), str(self.tableWidget.item(row,5).text()), str(self.tableWidget.item(row,6).text())
              ,str(self.tableWidget.item(row,7).text()),str(self.tableWidget.item(row,8).text())]) 
              


              

       

   

     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ViberWatsAppTable()
    sys.exit(app.exec_())  
