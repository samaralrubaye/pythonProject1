# importing various libraries
import email
import sys
from turtle import pd
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import matplotlib.pyplot as plt
import pandas as pd
from geopy.geocoders import Nominatim

from allWhatsApp import allWhatsApp
# main window
# which inherits QDialog


class Window(QDialog):
   
    # constructor
    def __init__(self,viber_summary = None,email_summary = None, whatsapp_summary = None):
        super(Window, self).__init__()
       
        # a figure instance to plot on
        self.figure = plt.figure()

      
        self.canvas = FigureCanvas(self.figure)

      
        self.toolbar = NavigationToolbar(self.canvas, self)

    

        if email_summary != None:
            self.plotemail(email_summary)
         
        if whatsapp_summary!= None:
            self.plotWhatsapp(whatsapp_summary)
        if viber_summary != None :
            self.plotViber(viber_summary)
           


      
       

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

    
      
        # setting layout to the main window
        self.setLayout(layout)
    
        
   
       

    # actionemai called by the push button
    def plotemail(self,email_summary):
        self.figure.clear()
         
        people = []
        comunication = []
        
        for i in email_summary:
            people.append(i.FirstName)
            comunication.append(i.SenderCount)
        print(people)
        for i in range(len(people)):
            plt.bar( people[i],comunication[i])
      
        plt.title('Amount of suspsous comunication per person', fontsize=14)
        plt.xlabel('people', fontsize=14)
        plt.ylabel('Comunication messages/Emails', fontsize=14)
        plt.grid(True)
          # put the figure inside the canavas
        self.canvas.draw()
       
        
    
    # actionemai called by the push button
    def plotViber(self,viber_summary):
            # clearing old figure
        self.figure.clear()
         
        people = []
        comunication = []
        for i in viber_summary:
            people.append(i.FirstName)
            comunication.append(i.SenderCount)
        for i in range(len(people)):
            plt.bar( people[i],comunication[i])
       
        plt.title('Amount of suspsous comunication per person', fontsize=14)
        plt.xlabel('people', fontsize=14)
        plt.ylabel('Comunication messages/Emails', fontsize=14)
        plt.grid(True)
          # put the figure inside the canavas
        self.canvas.draw()
    # action called by the push button
   
    

    def plotWhatsapp(self,whatsapp_summary):
        self.figure.clear()
        people = []
        comunication = []
        for i in whatsapp_summary:
            people.append(i.FirstName)
            comunication.append(i.SenderCount)
        print(comunication)
        print(people)
        for i in range(len(people)):
            plt.bar( people[i],comunication[i])
       
        plt.title('Amount of suspsous comunication per person', fontsize=14)
        plt.xlabel('people', fontsize=14)
        plt.ylabel('Comunication messages/Emails', fontsize=14)
        plt.grid(True)
          # put the figure inside the canavas
        self.canvas.draw()
    # action called by the push button
         
# 
          
   
   

        
   
    
        

# driver code
if __name__ == '__main__':
    
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Window()
    
    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())
