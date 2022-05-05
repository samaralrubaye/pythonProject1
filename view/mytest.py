# from email.mime import application
# import json
# import sys
# import folium
# from matplotlib.pyplot import show

# import requests


# url = (
#     "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
# )
# data = json.loads(requests.get(f"{url}/vis1.json").text)
# m = folium.Map(location=[48.218871184761596, 11.624819877497147], zoom_start=15, tiles="Stamen Terrain")

# marker = folium.Marker(
#     location=[48.218871184761596, 11.624819877497147],
#     popup=folium.Popup(max_width=450).add_child(
#         folium.Vega(data, width=450, height=250)
#          ),
#        )

# marker.add_to(m)


import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QLabel, QFrame, QHBoxLayout, QVBoxLayout,QTableWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
from MyQwidgetItem import *

from allViber import allViber
from allEmail import allEmail
from allWhatsApp import allWhatsApp
class SplashScreen(QWidget):
    def __init__(self,cID = None,ctype = None,iID = None):
        super().__init__()
        self.caseid = cID        
        self.type = ctype
        self.itemid = iID
        self.setWindowTitle('Spash Screen Example')
        self.setFixedSize(1100, 500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.counter = 0
        self.n = 300 # total instance

        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(5)

    @property
    def ItemID(self):
        return self.itemid

    @ItemID.setter
    def ItemID(self, value):
        self.itemid = value
 

    @property
    def CaseID(self):
        return self.caseid

    @CaseID.setter
    def CaseID(self, value):
        self.caseid = value
 
 
    @property
    def Type(self):
        return self.type

    @Type.setter
    def Type(self, value):
        self.type = value

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        layout.addWidget(self.frame)

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')

        # center labels
        self.labelTitle.resize(self.width() - 10, 150)
        self.labelTitle.move(0, 40) # x, y
        self.labelTitle.setText('Please wait')
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.resize(self.width() - 10, 50)
        self.labelDescription.move(0, self.labelTitle.height())
        self.labelDescription.setObjectName('LabelDesc')
        self.labelDescription.setText('<strong>Working on Task #1</strong>')
        self.labelDescription.setAlignment(Qt.AlignCenter)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(100, self.labelDescription.y() + 130)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)

        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 50)
        self.labelLoading.move(0, self.progressBar.y() + 70)
        self.labelLoading.setObjectName('LabelLoading')
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelLoading.setText('loading...')




    def loading(self):
        self.progressBar.setValue(self.counter)

        if self.counter == int(self.n * 0.3):
            self.labelDescription.setText('<strong>Working on Task #2</strong>')
        elif self.counter == int(self.n * 0.6):
            self.labelDescription.setText('<strong>Working on Task #3</strong>')
        elif self.counter >= self.n:
            self.timer.stop()
            self.close()

            time.sleep(1)

            self.myApp = MyApp(self.caseid,self.Type,self.ItemID)
            self.myApp.show()

        self.counter += 1
class MyApp(QTableWidget):

    def __init__(self,cID = None,ctype = None,iID = None):
        super().__init__()
        self.caseid = cID        
        self.type = ctype
        self.itemid = iID
        self.title = 'PyQt5 - QTableWidget'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600
   
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
   
        self.createTable()
   
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
   
        #Show window
        self.show()

    @property
    def ItemID(self):
        return self.itemid

    @ItemID.setter
    def ItemID(self, value):
        self.itemid = value
 

    @property
    def CaseID(self):
        return self.caseid

    @CaseID.setter
    def CaseID(self, value):
        self.caseid = value
 
 
    @property
    def Type(self):
        return self.type

    @Type.setter
    def Type(self, value):
        self.type = value

    #Create table
    def createTable(self):
        self.title = 'PyQt5 table'
        self.left = 20000
        self.top = 200
        self.width = 1000
        self.height = 400
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderItem(0, MyQwidgetItem("Sender first Name"))
        self.tableWidget.setHorizontalHeaderItem(1, MyQwidgetItem("Sender last Name"))
        self.tableWidget.setHorizontalHeaderItem(2, MyQwidgetItem(" message"))
  
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,200)
        
        if (self.Type == 1):
         self.GetEmails(self.ItemID)
        
        if (self.Type == 2):
         self.WhatsApploading(self.ItemID)
         
        if (self.Type == 3):
         self.vibercall(self.ItemID)
      


    def GetEmails(self,senderID):
        #emails=allEmail.getAllEmails(self)
        
        emails=allEmail.getEmailsBySenderID(self,self.CaseID,senderID)

        row=0
        self.tableWidget.setRowCount(len(emails))
      
        for i in emails:
               
              # index = PyQt5.QtCore.QPersistentModelIndex(
               # self.tableWidget.model().index(row, 1))
            
            # row.setitem(row,1, QTableWidgetItem(i.FromEmail_lastname))

            # self.tableWidget.rowAt[i] = row

               fname =  MyQwidgetItem(i.FromEmail_firstName)
               fname.ID =i.FromEmail_ID
               self.tableWidget.setItem(row,0,fname)

               self.tableWidget.setItem(row,1, MyQwidgetItem(i.FromEmail_lastname))
               self.tableWidget.setItem(row,2, MyQwidgetItem(i.FromEmail_Email))
               self.tableWidget.setItem(row,3, MyQwidgetItem(i.FromEmail_content_text))
               self.tableWidget.setItem(row,4, MyQwidgetItem(i.FromEmail_timeDate))
               self.tableWidget.setItem(row,5, MyQwidgetItem(i.ToEmail_firstName))
               self.tableWidget.setItem(row,6, MyQwidgetItem(i.ToEmail_lastname))
               self.tableWidget.setItem(row,7, MyQwidgetItem(i.ToEmail_Email))
               self.tableWidget.setItem(row,8, MyQwidgetItem(i.ToEmail_timeDate))
               self.tableWidget.setItem(row,9, MyQwidgetItem(i.ToEmail_timeDate))
               self.tableWidget.setItem(row,10, MyQwidgetItem(i.BccEmail_Email))
               self.tableWidget.setItem(row,11, MyQwidgetItem(i.CcEmail_Email))
               row=row+1
            
               self.tableWidget.move(0,0)

    def vibercall(self, senderID):
        vibers=allViber.getVibersBySenderID(self,self.CaseID,senderID)
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
     
     
    def WhatsApploading(self, senderID):
          WhatsApps= allWhatsApp.getWhatsAppBySenderID(self,self.CaseID,senderID)
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


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        #LabelTitle {
            font-size: 60px;
            color: #93deed;
        }

        #LabelDesc {
            font-size: 30px;
            color: #c2ced1;
        }

        #LabelLoading {
            font-size: 30px;
            color: #e8e8eb;
        }

        QFrame {
            background-color: #2F4454;
            color: rgb(220, 220, 220);
        }

        QProgressBar {
            background-color: #DA7B93;
            color: rgb(200, 200, 200);
            border-style: none;
            border-radius: 10px;
            text-align: center;
            font-size: 30px;
        }

        QProgressBar::chunk {
            border-radius: 10px;
            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #1C3334, stop:1 #376E6F);
        }
    ''')
    
    splash = SplashScreen()
    splash.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
