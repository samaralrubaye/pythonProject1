import csv
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import pandas as pd

from allViber import allViber

from allWhatsApp import allWhatsApp

class cantactTimesperDate(QWidget):

    def __init__(self,email_summary = None):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 200
        self.top = 0
        self.width = 1500
        self.height = 900
        self.initUI() 
        if email_summary!= None:
           self.emailcall(email_summary)
           
        
            
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
              #  self.createTable()
        self.tableWidget = QTableWidget()
        self.buttonCVS = QPushButton()
        self.buttonCVS.setText("Import as a CVS")
        self.buttonCVS.move(64,32)
        
      #  self.createTable()
       
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
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
        self.tableWidget.setItem(0,0, QTableWidgetItem("First name"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Last name"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Email"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Number of sent emails"))
        self.tableWidget.setItem(0,4, QTableWidgetItem("Number of recived emails"))
       
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,200)
        self.tableWidget.setColumnWidth(3,200)
        self.tableWidget.setColumnWidth(4,200)
        
  
  
    def emailcall(self,email_summary):
        
        row=1
        self.tableWidget.setRowCount(len(email_summary))
        for j in email_summary:
            self.tableWidget.setItem(row,0, QTableWidgetItem(j.FirstName))
            self.tableWidget.setItem(row,1, QTableWidgetItem(j.LastName))
            self.tableWidget.setItem(row,2, QTableWidgetItem(j.Email))
            self.tableWidget.setItem(row,3, QTableWidgetItem(j.SenderCount))
            self.tableWidget.setItem(row,4, QTableWidgetItem(j.Recepiantcount))
           
            row=row+1
            self.tableWidget.move(0,0)

    def buttonCVS_clicked(self):
         

          desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\evidance')
          rowcount=self.tableWidget.rowCount()
         
          senderfirtstname=[]
          senderlaststname=[]
          Email=[]
          number_of_emailssent=[]
          number_of_emails_recived=[]
         
         
          
          for row  in range(rowcount):
              senderfirtstname.append(self.tableWidget.item(row,0).text())
              senderlaststname.append(self.tableWidget.item(row,1).text())
              Email.append(self.tableWidget.item(row,2).text())
              number_of_emailssent.append(self.tableWidget.item(row,3).text())
              number_of_emails_recived.append(self.tableWidget.item(row,4).text())
              
        #   print(Email)
       
                   
       
          data = {'Sender first Name':senderfirtstname ,'Sender last Name': 
          senderlaststname,'Email': Email, 'number_of_emailssent': number_of_emailssent,
           'number_of_emails_recived':number_of_emails_recived}

        

         

          
          df = pd.DataFrame(data, columns= ['Sender first Name', 'Sender last Name','Email ','Number of emails sent', 'Number of emails recived'])
          
          df.to_csv (desktop+'\export_dataframe.csv',index = False, header=True)
        
          print (df)
       
        
 
     
    
           

     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = cantactTimesperDate()
    sys.exit(app.exec_())  
