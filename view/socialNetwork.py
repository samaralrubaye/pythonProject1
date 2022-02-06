import sys
from xmlrpc.client import SYSTEM_ERROR
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import random
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
        self.draw_circlar()
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

    def theSenderName(self):
        return self.senderFirstNam + self.SenerLastName

    def therecepianName(self):
        return self.recepianFisrtName + self.RecepianLastName

    def Gettinginfo(self):
        G_symmetric = nx.Graph()
        G_symmetric.add_edge(self.theSenderName, self.therecepianName)
        return G_symmetric
    def drawNetwork(self):
         nx.info(self.Gettinginfo())
         plt.figures(figsize=(5, 5))
         nx.draw_networkx(self.Gettinginfo)
         plt.show()
         plt.savefig("filename.png")
         plt.clf()

     



    # drawing in circularverticalLayout
    def draw_circlar(self):
        self.figures.clear()
        nx.draw_circular(self.Gettinginfo(), with_labels=True)
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
