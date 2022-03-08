from email.mime import application
from Analysis19 import Ui_DialogAnalysis
from GeographicalLocation import MyApp
import sys
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QRadioButton,
    QGroupBox,
    QPushButton,
    QGridLayout,
    QButtonGroup,
    QApplication,
    QTabWidget,QDialog)
from PyQt5.QtGui import QIcon

from PyQt5 import QtWidgets, QtCore, QtGui




class eventsActivator(QWidget):
    
    def __init__(self):
        
       analysis=Ui_DialogAnalysis()
     
       analysis..radioButton_viber.toggled.connect(lambda:self.viberdetails(analysis.radioButton_viber))
        
       # self.analysis.radioButton_whatsApp.toggled.connect(self.whatsApp)
       # self.analysis.radioButtonEmail.toggled.connect(self.email)
        
    def viberdetails(self):
        print("viber")   
    def whatsApp(self):
        print('whatsapp')
            
    def email(self):
        print('email')
    def show(self):
        print('show')
       
app = QApplication(sys.argv)
tabPage =eventsActivator()
tabPage.show()
app.exec_()
   

