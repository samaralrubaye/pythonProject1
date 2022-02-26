import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from allViber import allViber

from allWhatsApp import allWhatsApp

class ViberWatsAppTable(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 200
        self.top = 0
        self.width = 1500
        self.height = 900
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
      #  self.createTable()
        self.tableWidget = QTableWidget()
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
        self.show()
     

   # def createTable(self):
       # Create table
      
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(9)
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
        self.WhatsApploading()
  
    def vibercall(self):
        vibers=allViber.getAllVibers(self)
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
     
     
    def WhatsApploading(self):
          WhatsApps= allWhatsApp.getAllWhatsApp(self)
          row=1
          self.tableWidget.setRowCount(len(WhatsApps))
          for j in WhatsApps:
            self.tableWidget.setItem(row,0, QTableWidgetItem(j.FromWhatsApp_Msg_FirstName))
            self.tableWidget.setItem(row,1, QTableWidgetItem(j.FromWhatsApp_Msg_LastName))
            self.tableWidget.setItem(row,2, QTableWidgetItem(j.FromWhatsApp_Msg_number))
            self.tableWidget.setItem(row,3, QTableWidgetItem(j.FromWhatsApp_Msg))
            self.tableWidget.setItem(row,4, QTableWidgetItem(j.FromWhatsApp_Msg_DateandTime))
            self.tableWidget.setItem(row,5, QTableWidgetItem(j.FromWhatsApp_Msg_FirstName))
            self.tableWidget.setItem(row,6, QTableWidgetItem(j.ToWhatsApp_Msg_LastName))
            self.tableWidget.setItem(row,7, QTableWidgetItem(j.ToWhatsApp_Msg_number))
            self.tableWidget.setItem(row,8, QTableWidgetItem(j.ToWhatsApp_Msg_DateandTime))
            row=row+1   
            self.tableWidget.move(0,0)

     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ViberWatsAppTable()
    sys.exit(app.exec_())  
