import sys
import time

import numpy as np
import sys

from xmlrpc.client import SYSTEM_ERROR
from matplotlib import widgets
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


import random

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        

        draw_circlar = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(draw_circlar)
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(draw_circlar, self))

        

        self._dynamic_ax = draw_circlar.figure.subplots()
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
       

       


    


if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    qapp.exec_()