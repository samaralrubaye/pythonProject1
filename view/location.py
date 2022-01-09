import connection

f = open("script.js", "w")  # open the script file

connection.conection.mycursor.execute('SELECT idviber_msg,viber_Latitude, vlongitude FROM viber_msg')
viber_msgs = connection.conection.mycursor.fetchall()

import sys
from PyQt5.QtCore import QUrl, QUrlQuery
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

class location :





    def __init__(self ,marker,longitude,latitude ):
        self.longitude=longitude
        self.latitude=latitude
        self.marker=marker









        # for email in emails:

    #print(lists)


    #for i in range(len(lists)):
      #  print(lists[0][0])
       # print(lists[0][1])
       # print(lists[0][2])



    def getlogtude(self):
        return self.longitude
    def getlatitude(self):
        return self.latitude
    def getmarker(self):
        return self.marker



    # def addlocation(self):  # define add function that pass the id and the longitude and latitude
    #      global f
    #      self.f.write(" var marker_%d = L.marker([%d,%d],{}).addTo(map_732aa9293105477e92a5a9c8432b1001);"%(self.marker, self.longitude, self.latitude))
    #     # the js script body with passing the variables to it.

def add(marker_ID, longitude, latitude):  # define add function that pass the id and the longitude and latitude

    f.write(" var marker_%d = L.marker([%d,%d],{}).addTo(map_732aa9293105477e92a5a9c8432b1001);"%(marker_ID, longitude, latitude))


loc=[]

for i in range(len(viber_msgs)):
    loc.append(location(int(list(viber_msgs[i])[0]),float(list(viber_msgs[i])[1]),float(list(viber_msgs[i])[2])))
    # loc[i].addlocation()

for i in range(len(loc)):
    add(loc[i].getmarker(), loc[i].getlogtude(), loc[i].getlatitude())

    print(1)


f.close()

app = QApplication(sys.argv)

web = QWebEngineView()

web.load(QUrl("http://localhost:63342/pythonProject1/view/test.html?_ijt=iva7ln3q8i8p1hdoa8dsbundsv&_ij_reload=RELOAD_ON_SAVE"))
url = QUrl.fromLocalFile(r"C:\Users\samar\PycharmProjects\pythonProject1\view\test.html")
   # url = QUrl.fromLocalFile(r"test.html")
   # s=open("test.html")
    #url = QUrl.setUrl(r"view/test.html")
web.load(url)
web.show()

sys.exit(app.exec_())