
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import pandas as pd
import os
from allViber import allViber

from allWhatsApp import allWhatsApp
from allEmail import allEmail
import os
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
        self.tableWidget = QTableWidget()
        self.buttonCVS = QPushButton()
        self.buttonCVS.setText("Import as a CVS")
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
        self.tableWidget.setItem(0,0, QTableWidgetItem("Sender first Name"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Sender last Name"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Sender Email"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("The Email text"))
        self.tableWidget.setItem(0,4, QTableWidgetItem("Time sent"))
        self.tableWidget.setItem(0,5, QTableWidgetItem("Reciepeant Firt Name"))
        self.tableWidget.setItem(0,6, QTableWidgetItem("Reciepeant last Name"))
        self.tableWidget.setItem(0,7, QTableWidgetItem("Reciepeant Email"))
        self.tableWidget.setItem(0,8, QTableWidgetItem("time recieved"))
        self.tableWidget.setItem(0,9, QTableWidgetItem("stats"))
        self.tableWidget.setItem(0,10, QTableWidgetItem("Bcc"))
        self.tableWidget.setItem(0,11, QTableWidgetItem("cc"))
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
        
        row=1
        self.tableWidget.setRowCount(len(emails))
      
        for i in emails:
               self.tableWidget.setItem(row,0, QTableWidgetItem(i.FromEmail_firstName))
               self.tableWidget.setItem(row,1, QTableWidgetItem(i.FromEmail_lastname))
               self.tableWidget.setItem(row,2, QTableWidgetItem(i.FromEmail_Email))
               self.tableWidget.setItem(row,3, QTableWidgetItem(i.FromEmail_content_text))
               self.tableWidget.setItem(row,4, QTableWidgetItem(i.FromEmail_timeDate))
               self.tableWidget.setItem(row,5, QTableWidgetItem(i.ToEmail_firstName))
               self.tableWidget.setItem(row,6, QTableWidgetItem(i.ToEmail_lastname))
               self.tableWidget.setItem(row,7, QTableWidgetItem(i.ToEmail_Email))
               self.tableWidget.setItem(row,8, QTableWidgetItem(i.ToEmail_timeDate))
               self.tableWidget.setItem(row,9, QTableWidgetItem(i.ToEmail_timeDate))
               self.tableWidget.setItem(row,10, QTableWidgetItem(i.BccEmail_Email))
               self.tableWidget.setItem(row,11, QTableWidgetItem(i.CcEmail_Email))
               row=row+1
     
     
    

       
        self.tableWidget.move(0,0)
    def buttonCVS_clicked(self,emails):
         

          desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


          for i in emails:
              data = {'Sender first Name': [i.FromEmail_firstName],
             'Sender last Name': [i.FromEmail_lastname],'Sender Email': [i.FromEmail_Email],'The Email text': [i.FromEmail_content_text],'Time sent': [i.FromEmail_timeDate],
              'Reciepeant Firt Name': [i.ToEmail_firstName],'Reciepeant last Name': [i.ToEmail_lastname],'Reciepeant Email': [i.ToEmail_Email],'Time sent': [i.FromEmail_timeDate],   
               'Sent Time': [i.ToEmail_timeDate] }

          df = pd.DataFrame(data, columns= ['Product', 'Price'])

          df.to_csv ( desktop+'\export_dataframe.csv', index = False, header=True)

         # print (df)
          print(desktop)
        
   
   
     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = emaildetails()
    sys.exit(app.exec_())  
