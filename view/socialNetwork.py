import email
import sys
from turtle import clear
from xmlrpc.client import SYSTEM_ERROR
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5.QtWidgets import QApplication
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
    

    def __init__(self,vibers = None,emails = None,watsap = None):
        super(SocialNetwork, self).__init__()
        
        self.figures = plt.figure()
        self.canvases = FigureCanvas(self.figures)
        self.toolbars = NavigationToolbar(self.canvases, self)

       
        
        if emails != None:
          self.allemails(emails)
          self.draw_circlar(G_symmetric_emails)
        if watsap!= None:
           self.allwatsapp(watsap)
           self.draw_circlar(G_symmetric_watsapp)
        if vibers != None :
             self.allviper(vibers)
             self.draw_circlar(G_symmetric_viper)

        
      
        
      
        
    
        verticalLayout = QVBoxLayout()

        # adding tool bar to theverticalLayout
        verticalLayout.addWidget(self.toolbars)

        # adding canvas to theverticalLayout
        verticalLayout.addWidget(self.canvases)

     

        # settingverticalLayout to the main window
        self.setLayout(verticalLayout)

    
    def allemails(self,emails):
        
        for i in emails:
           G_symmetric_emails.add_edge(i.FromEmail_firstName,i.ToEmail_firstName) 
    
    def allwatsapp(self,watsap):
       
        for i in watsap:
           G_symmetric_watsapp.add_edge(i.FromWhatsApp_Msg_FirstName,i.ToWhatsApp_Msg_LastName)
    
    def allviper(self, Vibers):
        
        for i in Vibers: 
           G_symmetric_viper.add_edge(i.FromViber_Msg_FirstName,i.ToViber_Msg_FirstName) 


    # drawing in circularverticalLayout
    def draw_circlar(self, GS):
        
        nx.draw_networkx(GS)
        #plt.savefig("filename1.png")
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
