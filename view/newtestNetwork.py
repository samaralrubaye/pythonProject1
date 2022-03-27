from matplotlib import widgets
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
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


import warnings; warnings.simplefilter('ignore')
class SocialNetworkTest(QDialog):

    def __init__(self,vibers = None,emails = None,watsap = None):
        super(SocialNetworkTest, self).__init__()
        if emails != None:
          self.draw_circlar
        if watsap!= None:
           self.draw_circlar
        if vibers != None :
             self.draw_circlar
        self.figures = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figures'it takes the
        # 'figures' instance as a parameter to __init__
        self.canvases = FigureCanvas(self.figures)

       
        # it takes the Canvas widget and a parent
        self.toolbars = NavigationToolbar(self.canvases, self)
       

    def theSenderName(self, emails):
        for i in emails:
            print(i.FromEmail_firstName )
            return i.FromEmail_firstName + i.FromEmail_firstName

    def therecepianName(self, emails):
        for i in emails:
             return i.FromEmail_firstName+ i.FromEmail_firstName

    def Gettinginfo(self):
        G_symmetric = nx.Graph()
        print(self.therecepianName)
        G_symmetric.add_edge(self.theSenderName, self.therecepianName)
        return G_symmetric
    def drawNetwork(self):
         plt.clf()
         nx.info(self.Gettinginfo())
         plt.figure(figsize=(5, 5))
         nx.draw_networkx(self.Gettinginfo())
        
        





    # drawing in circular layout
    def draw_circlar(self):
        nx.draw_circular(self.Gettinginfo(), with_labels=True)
        plt.savefig("filename1.png")
        plt.show()
        self.canvases.draw()
        plt.clf() 





#sn= SocialNetworkTest("sara","L","samar","A")
#print(sn.draw_circlar())

