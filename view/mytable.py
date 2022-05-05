import sys
import sys
import time
from typing import overload
from PyQt5.QtWidgets import *

from mytable import *
from MyQwidgetItem import MyQwidgetItem

import csv
from datetime import datetime
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot,QTimer
import pandas as pd

from viber import viber


from mytest import SplashScreen




class MyTableWidget(QTableWidget):
    def __init__(self,cID = None,ctype = None):
        super().__init__()
        
         
        self.caseid = cID        
        self.type = ctype
        # self.setMinimumWidth(400)
        # self.setColumnCount(1)
        # self.setColumnWidth(0, 400)
        # self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.itemClicked.connect(self.handleItemClick)
   
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

    def handleItemClick(self, item):
        try:
            
             self.SplashScreen= SplashScreen(self.CaseID,self.Type,item.ID)
             self.SplashScreen.show()

        except:
            print('tt')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyTableWidget()
    sys.exit(app.exec_())  
        
