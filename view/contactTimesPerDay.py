import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from allViber import allViber

from allWhatsApp import allWhatsApp

class cantactTimesperDate(QWidget):

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
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Domain name"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Number of send Items"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("the date the items sent"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Number of send Items"))
        self.tableWidget.setItem(0,4, QTableWidgetItem("the date the items sent"))
       
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,200)
        self.tableWidget.setColumnWidth(3,200)
        self.tableWidget.setColumnWidth(4,200)
        
        #self.vibercall()
       # self.WhatsApploading()
  
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
            self.tableWidget.setItem(row,4, QTableWidgetItem(j.ToWhatsApp_Msg_DateandTime))
            self.tableWidget.setItem(row,5, QTableWidgetItem(j.FromWhatsApp_Msg_FirstName))
            self.tableWidget.setItem(row,6, QTableWidgetItem(j.ToWhatsApp_Msg_LastName))
            self.tableWidget.setItem(row,7, QTableWidgetItem(j.ToWhatsApp_Msg_number))
            self.tableWidget.setItem(row,8, QTableWidgetItem(j.ToWhatsApp_Msg_DateandTime))
            row=row+1   
            self.tableWidget.move(0,0)

     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = cantactTimesperDate()
    sys.exit(app.exec_())  
