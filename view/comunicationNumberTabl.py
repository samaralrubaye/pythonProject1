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

    def __init__(self,viber_summary = None,whatsapp_summary = None):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 200
        self.top = 0
        self.width = 1500
        self.height = 900
        self.initUI()
        if whatsapp_summary!= None:
           self.WhatsApploading(whatsapp_summary)
           
        if viber_summary != None :
             self.vibercall(viber_summary)
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
      #  self.createTable()
        self.tableWidget = MyTableWidget()
        self.buttonCVS = QPushButton()
        self.buttonCVS.setText("Import as a CVS")
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
            test =  MyQwidgetItem(j.FirstName)
            test.ID =j.FirstName
            self.tableWidget.setItem(row,0,(test))
            self.tableWidget.setItem(row,1, QTableWidgetItem(j.LastName))
            self.tableWidget.setItem(row,2, QTableWidgetItem(j.ViberNumbr))
            self.tableWidget.setItem(row,3, QTableWidgetItem(j.SenderCount))
            self.tableWidget.setItem(row,4, QTableWidgetItem(j.Recepiantcount))
            
            
            row=row+1
            self.tableWidget.move(0,0)
     
     
    def WhatsApploading(self, whatsapp_summary):
         
          row=0
          self.tableWidget.setRowCount(len(whatsapp_summary))
          for j in whatsapp_summary:
            test =  MyQwidgetItem(j.FirstName)
            test.ID =j.FirstName
            self.tableWidget.setItem(row,0, QTableWidgetItem(test))
            self.tableWidget.setItem(row,1, QTableWidgetItem(j.LastName))
            self.tableWidget.setItem(row,2, QTableWidgetItem(j.WhatsApp))
            self.tableWidget.setItem(row,3, QTableWidgetItem(j.SenderCount))
            self.tableWidget.setItem(row,4, QTableWidgetItem(j.Recepiantcount))
            
            
            row=row+1   
            self.tableWidget.move(0,0)
    def buttonCVS_clicked(self):
         

          desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\evidance')
          rowcount=self.tableWidget.rowCount()
         
          senderfirtstname=[]
          senderlaststname=[]
          contact=[]
          senderCount=[]
          RecepiantCount=[]
         
         
          
          for row  in range(rowcount):
              senderfirtstname.append(self.tableWidget.item(row,0).text())
              senderlaststname.append(self.tableWidget.item(row,1).text())
              contact.append(self.tableWidget.item(row,2).text())
              senderCount.append(self.tableWidget.item(row,3).text())
              RecepiantCount.append(self.tableWidget.item(row,4).text())
              senderfirtstname.remove(senderfirtstname[0])

          print(contact)
                   
          
          data = {'Sender first Name':senderfirtstname ,'Sender last Name': 
          senderlaststname,'Contact':contact, 'Number of messages sent': senderCount, 'Number of message recived':RecepiantCount}



          df = pd.DataFrame(data, columns= ['Sender first Name', 'Sender last Name','Contact ','Number of messages sent','Number of message recived'])
               
          df.to_csv (desktop+'\export_dataframe.csv',index = False, header=True)
        
          print (df)
      
        

     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = comunicationNumberTable()
    sys.exit(app.exec_())  
