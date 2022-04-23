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

class comunicationNumberTable(QWidget):

    def __init__(self,viber_summary = None,whatsapp_summary = None,cID = None):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 200
        self.top = 0
        self.width = 1500
        self.height = 900
        self.type = 0
        self.caseid = cID
        if whatsapp_summary != None:
           self.type = 2
           
        if viber_summary != None:
           self.type = 3
        self.initUI()
        if whatsapp_summary!= None:
           self.WhatsApploading(whatsapp_summary)
           
        if viber_summary != None :
             self.vibercall(viber_summary)
        
    
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
        self.tableWidget = MyTableWidget(self.caseId,self.Type)
        self.buttonCVS = QPushButton()
        self.buttonCVS.setText("Export as a CVS")
        self.buttonCVS.move(64,32)
        # Add box layout, add table to box layout and add box layout to widget
       
        
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonCVS)
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
        self.show()
        self.buttonCVS.clicked.connect(self.buttonCVS_clicked)
      
      
     
        
     

   # def createTable(self):
       # Create table
      
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(5)
    
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Contact"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("the date the items sent"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Number of sent"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("the date the items recived"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Number of receieved"))
       
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,200)
        
        #self.vibercall()
       # self.WhatsApploading()
  
    def vibercall(self,viber_summary):
        
        row=0
        self.tableWidget.setRowCount(len(viber_summary))
        for j in viber_summary:
            fname =  MyQwidgetItem(j.FirstName)
            # change the quiry    fname.ID =j.FirstName_ID
            fname.ID =j.Sender_ID
            self.tableWidget.setItem(row,0,fname)
            
            
            self.tableWidget.setItem(row,1, MyQwidgetItem(j.LastName))
            self.tableWidget.setItem(row,2, MyQwidgetItem(j.ViberNumbr))
            self.tableWidget.setItem(row,3, MyQwidgetItem(j.SenderCount))
            self.tableWidget.setItem(row,4, MyQwidgetItem(j.Recepiantcount))
            row=row+1
            self.tableWidget.move(0,0)
     
     
    def WhatsApploading(self, whatsapp_summary):
         
          row=0
          self.tableWidget.setRowCount(len(whatsapp_summary))
          for j in whatsapp_summary:
                 fname =  MyQwidgetItem(j.FirstName)
                 # change the quiry    fname.ID =j.FirstName_ID
                 fname.ID =j.Sender_ID
                 self.tableWidget.setItem(row,0,fname)
                 self.tableWidget.setItem(row,1, MyQwidgetItem(j.LastName))
                 self.tableWidget.setItem(row,2, MyQwidgetItem(j.WhatsApp))
                 self.tableWidget.setItem(row,3, MyQwidgetItem(j.SenderCount))
                 self.tableWidget.setItem(row,4, MyQwidgetItem(j.Recepiantcount))
                 row=row+1   
                 self.tableWidget.move(0,0)

    def buttonCVS_clicked(self):
          desktop = os.path.join(os.path.join(os.environ['USERPROFILE']))
          now = datetime.now()
          now = int(now.strftime("%Y%m%d%H%M%S"))
          f = open(str(desktop)+'/'+'Desktop/evidance'+'/'+"chatdataCalculation%d.csv"%now, "a", newline="")  # open csv file
          print(desktop)
          c = csv.writer(f) 
          rowcount=self.tableWidget.rowCount()
         
         
          c.writerow([ str('Sender first Name'), str('Sender last Name'),str('Contact'), str('Number of messages sent'),str( 'Number of message recived')])
          
          for row  in range(rowcount):
              c.writerow(
              [str(self.tableWidget.item(row,0).text()), str(self.tableWidget.item(row,1).text()), str(self.tableWidget.item(row,2).text()),
              str(self.tableWidget.item(row,3).text()), str(self.tableWidget.item(row,4).text())]) 

          
        

     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = comunicationNumberTable()
    sys.exit(app.exec_())  
