import email
import sys
from xmlrpc.client import SYSTEM_ERROR
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from allEmail import allEmail
import random
from time import sleep

from allViber import allViber
from allWhatsApp import allWhatsApp
G_symmetric_emails = nx.Graph()
G_symmetric_watsapp = nx.Graph()
G_symmetric_viper = nx.Graph()
class SocialNetwork(QDialog):
    

    def __init__(self, parent=None):
        super(SocialNetwork, self).__init__(parent)
        
        self.figures = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figures'it takes the
        # 'figures' instance as a parameter to __init__
        self.canvases = FigureCanvas(self.figures)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbars = NavigationToolbar(self.canvases, self)

        # Just some button connected to 'plot' method
       # self.button3 = QPushButton('draw_random')
        # Just some button connected to 'plot' method
       # self.button4 = QPushButton('draw_random')
        
        self.allemails()
        self.allwatsapp()
        self.allviper()
        self.draw_circlar(G_symmetric_emails)
        sleep(2)
        self.draw_circlar(G_symmetric_watsapp)
        sleep(2)
        self.draw_circlar(G_symmetric_viper)
        # adding action to the button
      #  self.button3.clicked.connect(self.draw_random)
        # adding action to the button
       # self.button4.clicked.connect(self.draw_random)

        # creating a Vertical BoxverticalLayout
        verticalLayout = QVBoxLayout()

        # adding tool bar to theverticalLayout
        verticalLayout.addWidget(self.toolbars)

        # adding canvas to theverticalLayout
        verticalLayout.addWidget(self.canvases)

        # adding push button to theverticalLayout
        #verticalLayout.addWidget(self.button3)
      # adding push button to theverticalLayout
       # verticalLayout.addWidget(self.button4)

        # settingverticalLayout to the main window
        self.setLayout(verticalLayout)
        
        
   # def theSenderName(self):
       # for i in email:
         #  return i.fromEmail_lastname + i.fromEmail_lastname

   # def therecepianName(self, fname, lname):
      #  for i in email:
          #  return fname+ lname
   # def therecepianName(self):
        #for i in email:
       # return 'sera' + 'l'
    
    def allemails(self):
        
        emails=allEmail.getAllEmails(self)
        for i in emails:
           # print(i.toEmail_firstName)
           self.Gettinginfo(i.FromEmail_firstName,i.ToEmail_firstName,G_symmetric_emails)
       # self.Gettinginfo('samar','sami','sara','loscomb')
    
    def allwatsapp(self):
        WhatsApps= allWhatsApp.getAllWhatsApp(self)
        
        for i in WhatsApps:
           # print(i.toEmail_firstName)
           self.Gettinginfo(i.FromWhatsApp_Msg_FirstName,i.ToWhatsApp_Msg_LastName,G_symmetric_watsapp)
       # self.Gettinginfo('samar','sami','sara','loscomb')
    
    def allviper(self):
        Vibers=allViber.getAllVibers(self)
       
        for i in Vibers:
           # print(i.toEmail_firstName)
           self.Gettinginfo(i.FromViber_Msg_FirstName,i.ToViber_Msg_FirstName,G_symmetric_viper)
       # self.Gettinginfo('samar','sami','sara','loscomb')

    def Gettinginfo(self,fnamesender,fnamerecepiant,G_symmetric):
        
    
        
        #should be like this
       # print(self.theSenderName)
       # print(self.therecepianName)
    #    G_symmetric.add_edge(self.fnamesender, self.fnamerecepiant)
        
                               
        G_symmetric.add_edge(fnamesender, fnamerecepiant)
        
        
    


    def drawNetwork(self):
         nx.info(self.Get)
         plt.figures(figsize=(5, 5))
         nx.draw_networkx(self.Gettinginfo)
         plt.show()
         #plt.savefig("filename.png")
         plt.clf()

     



    # drawing in circularverticalLayout
    def draw_circlar(self, GS):
        self.figures.clear()
        # print(self.allemails)
        nx.draw_networkx(GS)
        plt.savefig("filename1.png")
        self.canvases.draw()



    # drawing in planarverticalLayout
    def drawplanar(self):
        self.figures.clear()
        nx.draw_planar(self.Gettinginfo, with_labels=True)
        plt.savefig("filename2.png")
        self.canvases.draw()



    # drawing in randomverticalLayout
    def draw_random(self):
        self.figures.clear()
        nx.draw_random(self.Gettinginfo(), with_labels=True)
        plt.savefig("filename3.png")
        self.canvases.draw()



    # drawing in spectralverticalLayout
    def draw_spectral(self):
        self.figures.clear()
        nx.draw_spectral( self.Gettinginfo(), with_labels=True)
        plt.savefig("filename4.png")
        self.canvases.draw()

   



    



 

# driver code
if __name__ == '__main__':
    
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    social = SocialNetwork()
    
    # showing the window
    social.show()

    # loop
    sys.exit(app.exec_())
