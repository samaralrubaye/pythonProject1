
from operator import truediv
import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import pandas as pd
import os
from allViber import allViber

from allWhatsApp import allWhatsApp
from allEmail import allEmail
import os
from mytable import *
from MyQwidgetItem import MyQwidgetItem
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
        self.tableWidget = MyTableWidget()
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
       
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Sender first Name"))
        self.tableWidget.setHorizontalHeaderItem(1,  QTableWidgetItem("Sender last Name"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Sender Email"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("The Email text"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Time sent"))
        self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem("Reciepeant Firt Name"))
        self.tableWidget.setHorizontalHeaderItem(6, QTableWidgetItem("Reciepeant last Name"))
        self.tableWidget.setHorizontalHeaderItem(7, QTableWidgetItem("Reciepeant Email"))
        self.tableWidget.setHorizontalHeaderItem(8, QTableWidgetItem("time recieved"))
        self.tableWidget.setHorizontalHeaderItem(9, QTableWidgetItem("stats"))
        self.tableWidget.setHorizontalHeaderItem(10, QTableWidgetItem("Bcc"))
        self.tableWidget.setHorizontalHeaderItem(11, QTableWidgetItem("cc"))
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
        
        row=0
        self.tableWidget.setRowCount(len(emails))
      
        for i in emails:
               
              # index = PyQt5.QtCore.QPersistentModelIndex(
               # self.tableWidget.model().index(row, 1))
               x = QTableWidget.row(self.tableWidget,QTableWidgetItem(i.FromEmail_lastname))
               if x == True:
                   print('test')
                   print(x)
                   print('test')
            # row.setitem(row,1, QTableWidgetItem(i.FromEmail_lastname))

            # self.tableWidget.rowAt[i] = row

               test =  MyQwidgetItem(i.FromEmail_firstName)
               test.ID = i.FromEmail_firstName
               self.tableWidget.setMyItem(row,0,test)
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
    def buttonCVS_clicked(self):
         

          desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\evidance')
          rowcount=self.tableWidget.rowCount()
          columncount=self.tableWidget.columnCount()
          senderfirtstname=[]
          senderlaststname=[]
          SenderEmail=[]
          TheEmailtext=[]
          Timesent=[]
          TheEmailtext=[]
          ReciepeantFirtName =[]
          ReciepeantlastName=[]
          ReciepeantEmail=[]
          #self.tableWidget.cellClicked.connect(self.gosomewhere)
          self.tableWidget.DoubleClicked(self.gosomewhere)
         # connect(self.gosomewhere)

          
          for row  in range(rowcount):
              senderfirtstname.append(self.tableWidget.item(row,0).text())
              senderlaststname.append(self.tableWidget.item(row,1).text())
              SenderEmail.append(self.tableWidget.item(row,2).text())
              TheEmailtext.append(self.tableWidget.item(row,3).text())
              Timesent.append(self.tableWidget.item(row,4).text())
              ReciepeantFirtName.append(self.tableWidget.item(row,5).text())
              ReciepeantEmail.append(self.tableWidget.item(row,6).text())
              ReciepeantFirtName.append(self.tableWidget.item(row,7).text())
              
              
              

       
                   
          SenderEmail=[]
          #data = {'Sender first Name':senderfirtstname ,'Sender last Name': senderlaststname,'The Email text': TheEmailtext,'Time sent':Timesent ,
               # 'Reciepeant Firt Name':ReciepeantFirtName ,'Reciepeant last Name': ReciepeantlastName,'Reciepeant Email': ReciepeantEmail,'Time sent':Timesent ,   
              #  'Sent Time': Timesent}
          data = {'Sender first Name':senderfirtstname ,'Sender last Name': senderlaststname,'the sender email':SenderEmail,'The Email text': TheEmailtext,
                'Reciepeant Firt Name': ReciepeantFirtName,'Reciepeant last Name': ReciepeantlastName,'Reciepeant Email': ReciepeantEmail,'Time sent':Timesent ,   
                'Sent Time': Timesent}

          print(SenderEmail)
          
          print(Timesent)
          print(ReciepeantFirtName)
          print(ReciepeantlastName)

          print('senderfirtstname' + str(len(senderfirtstname)))
          print('senderlaststname' + str(len(senderlaststname)))
          print('SenderEmail' + str(len(SenderEmail)))
          print(' SenderEmail' + str(len( SenderEmail)))
          print(' TheEmailtext' + str(len( TheEmailtext)))
          print(' Timesent' + str(len( Timesent)))
          print(' ReciepeantFirtName' + str(len( ReciepeantFirtName)))
          print(' ReciepeantlastName' + str(len( ReciepeantlastName)))
          print('  ReciepeantEmail' + str(len(  ReciepeantEmail))) 
      
         # print(data)  

          #df = pd.DataFrame(data, columns= ['Sender first Name', 'Sender last Name', 'The Email text','Time sent', 'Reciepeant last Name','Time sent', 'Sent Time'])
          df = pd.DataFrame(data, columns= ['Sender first Name', 'Sender last Name','sender email ','The Email text'])
         # pd.read_excel(desktop+'\export_dataframe.xls',index_col='Name')        
          df.to_csv (desktop+'\export_dataframe.csv',index = False, header=True)
         # df.to_excel (desktop+'\export_dataframe.xls',index = False, header=True)
          print (df)
        #  print(desktop)
    #https://stackoverflow.com/questions/14588479/retrieving-cell-data-from-a-selected-cell-in-a-tablewidget    
    def gosomewhere(self):
        print('happy')
   
     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = emaildetails()
    sys.exit(app.exec_())  
