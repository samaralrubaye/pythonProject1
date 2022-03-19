import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import pandas as pd

from allViber import allViber

from allWhatsApp import allWhatsApp

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
           self.buttonCVS.clicked.connect(self.buttonCVS_clicked_whatsapp)
           
        if Vibers != None:
           self.vibercall(Vibers)
           self.buttonCVS.clicked.connect(self.buttonCVS_clicked_viber)
        
        
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
      #  self.createTable()
        self.tableWidget = QTableWidget()
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
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
        self.tableWidget.setItem(0,0, QTableWidgetItem("Sender first Name"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Sender last Name"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Number"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("The message"))
        self.tableWidget.setItem(0,4, QTableWidgetItem("Time sent"))
        self.tableWidget.setItem(0,5, QTableWidgetItem("Reciepeant Firt Name"))
        self.tableWidget.setItem(0,6, QTableWidgetItem("Reciepeant last Name"))
        self.tableWidget.setItem(0,7, QTableWidgetItem("Recipeant Number"))
        self.tableWidget.setItem(0,8, QTableWidgetItem("time recieved"))
        self.tableWidget.setItem(0,9, QTableWidgetItem("stats"))
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
        row=1
        self.tableWidget.setRowCount(len(vibers))
        for j in vibers:
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
          row=1
          self.tableWidget.setRowCount(len(WhatsApps))
          for j in WhatsApps:
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
    def buttonCVS_clicked_whatsapp(self,WhatsApps):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


        for i in WhatsApps:
              data = {'Sender first Name': [i.FromWhatsApp_Msg_FirstName],
             'Sender last Name': [i.FromViber_Msg_LastName],'Number': [i.FromWhatsApp_Msg_number],'The message': [i.FromWhatsApp_Msg],'Time sent': [i.FromWhatsApp_Msg_DateandTime],
              'Reciepeant Firt Name': [i.ToWhatsApp_Msg_FirstName],'Reciepeant last Name': [i.ToWhatsApp_Msg_LastName],'Recipeant Number': [i.ToWhatsApp_Msg_number],'Time sent': [i.ToViber_Msg],   
               'read status': [i.ToViber_Msg] }

        df = pd.DataFrame(data, columns= ['Sender first Name', 'Sender last Name','Number','Reciepeant Firt Name','Reciepeant last Name','Recipeant Number','Time sent','read status'])

        df.to_csv ( desktop+'\export_dataframe.csv', index = False, header=True)

        print(desktop)

    def buttonCVS_clicked_viber(self,Vibers):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


        for i in Vibers:
              data = {'Sender first Name': [i.FromViber_Msg_FirstName],
             'Sender last Name': [i.FromWhatsApp_Msg_LastName],'Number': [i.FromViber_Msg_number],'The message': [i.FromWhatsApp_Msg],'Time sent': [i.ToViber_Msg_DateandTime],
              'Reciepeant Firt Name': [i.ToWhatsApp_Msg_FirstName],'Reciepeant last Name': [i.ToViber_Msg_FirstName],'Recipeant Number': [i.ToViber_Msg_number],'Time sent': [i.ToWhatsApp_Msg_DateandTime],   
               'read status': [i.ToWhatsApp_Msg_DateandTime] }

        df = pd.DataFrame(data, columns= ['Sender first Name', 'Sender last Name','Number','Reciepeant Firt Name','Reciepeant last Name','Recipeant Number','Time sent','read status'])

        df.to_csv ( desktop+'\export_dataframe.csv', index = False, header=True)

        print(desktop)

     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ViberWatsAppTable()
    sys.exit(app.exec_())  
