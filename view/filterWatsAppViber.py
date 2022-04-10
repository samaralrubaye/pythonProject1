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

    def __init__(self,  WhatsApps=None,Vibers=None):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 200
        self.top = 0
        self.width = 1500
        self.height = 900
        self.initUI()
        if WhatsApps != None:
           self.WhatsApploading(WhatsApps)
           self.buttonCVS.clicked.connect(self.buttonCVS_clicked)
           
        if Vibers != None:
           self.vibercall(Vibers)
           self.buttonCVS.clicked.connect(self.buttonCVS_clicked)
        
        
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
      #  self.createTable()
        self.tableWidget = MyTableWidget()
        
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.tableWidget = MyTableWidget()
        
        self.buttonCVS = QPushButton()
        self.buttonCVS.setText("Import as a CVS")
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
            test =  MyQwidgetItem(j.FromViber_Msg_FirstName)
            test.ID =j.FromViber_Msg_FirstName
            self.tableWidget.setItem(row,0,(test))
            self.tableWidget.setItem(row,0, QTableWidgetItem(j.FromViber_Msg_FirstName))
            self.tableWidget.setItem(row,1, QTableWidgetItem(j.FromViber_Msg_LastName))
            self.tableWidget.setItem(row,2, QTableWidgetItem(j.FromViber_Msg_number))
            self.tableWidget.setItem(row,3, QTableWidgetItem(j.ToViber_Msg))
            self.tableWidget.setItem(row,4, QTableWidgetItem(j.ToViber_Msg_DateandTime))
            self.tableWidget.setItem(row,5, QTableWidgetItem(j.ToViber_Msg_FirstName))
            self.tableWidget.setItem(row,6, QTableWidgetItem(j.ToViber_Msg_LastName))
            self.tableWidget.setItem(row,7, QTableWidgetItem(j.ToViber_Msg_number))
            self.tableWidget.setItem(row,8, QTableWidgetItem(j.ToViber_Msg))
            row=row+1
            self.tableWidget.move(0,0)
     
     
    def WhatsApploading(self, WhatsApps):
         # WhatsApps= allWhatsApp.getAllWhatsApp(self,88888,'2000/1/1','4000/1/1','')
          row=0
          self.tableWidget.setRowCount(len(WhatsApps))
          for j in WhatsApps:
            test =  MyQwidgetItem(j.FromWhatsApp_Msg_FirstName)
            test.ID =j.FromWhatsApp_Msg_FirstName
            self.tableWidget.setItem(row,0,(test))
            self.tableWidget.setItem(row,0, QTableWidgetItem(j.FromWhatsApp_Msg_FirstName))
            self.tableWidget.setItem(row,1, QTableWidgetItem(j.FromWhatsApp_Msg_LastName))
            self.tableWidget.setItem(row,2, QTableWidgetItem(j.FromWhatsApp_Msg_number))
            self.tableWidget.setItem(row,3, QTableWidgetItem(j.FromWhatsApp_Msg))
            self.tableWidget.setItem(row,4, QTableWidgetItem(j.FromWhatsApp_Msg_DateandTime))
            self.tableWidget.setItem(row,5, QTableWidgetItem(j.ToWhatsApp_Msg_FirstName))
            self.tableWidget.setItem(row,6, QTableWidgetItem(j.ToWhatsApp_Msg_LastName))
            self.tableWidget.setItem(row,7, QTableWidgetItem(j.ToWhatsApp_Msg_number))
            self.tableWidget.setItem(row,8, QTableWidgetItem(j.ToWhatsApp_Msg_DateandTime))
            row=row+1   
            self.tableWidget.move(0,0)
    def buttonCVS_clicked(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\evidance')
        rowcount=self.tableWidget.rowCount()
         
        sender_firt_name=[]
        sender_last_name=[]
        Sender_contact=[]
        message=[]
        sending_Time=[]
        Recipiant_First_name=[]
        Recepiant_Last_Name=[]
        Recepiant_contact=[]
        Sending_dateTime=[]
         
         
          
        for row  in range(rowcount):
              sender_firt_name.append(self.tableWidget.item(row,0).text())
              sender_last_name.append(self.tableWidget.item(row,1).text())
              Sender_contact.append(self.tableWidget.item(row,2).text())
              message.append(self.tableWidget.item(row,3).text())
              sending_Time.append(self.tableWidget.item(row,4).text())
              Recipiant_First_name.append(self.tableWidget.item(row,5).text())
              Recepiant_Last_Name.append(self.tableWidget.item(row,6).text())
              Recepiant_contact.append(self.tableWidget.item(row,7).text())
              Sending_dateTime.append(self.tableWidget.item(row,8).text())

              data = {'sender_firt_tname': sender_firt_name ,
             'SenderlastName': sender_last_name,'Sender number': Sender_contact,'The message': message,'Time sent': sending_Time ,
              'Reciepeant Firt Name': Recipiant_First_name,'Reciepeant last Name': Recepiant_Last_Name,'Recipeant Number': Recepiant_contact,'Sending_dateTime': Sending_dateTime}

        df = pd.DataFrame(data, columns= ['sender_firt_name', 'sender_last_name','Sender_contact','Number','Recipiant_First_name','Recepiant_Last_Name','Recepiant_contact','Sending_dateTime'])

        df.to_csv ( desktop+'\export_dataframe.csv', index = False, header=True)

        print(desktop)

   

     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ViberWatsAppTable()
    sys.exit(app.exec_())  
