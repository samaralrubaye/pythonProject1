# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\samar\Desktop\finalyearproject\pythonProject1\view\analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from cgi import test
from genericpath import exists
from operator import index
from pickle import TRUE
from re import T
from Takeasnapshot import *
#from unittest import case
from xmlrpc.client import TRANSPORT_ERROR
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QGridLayout
from PyQt5 import QtCore, QtGui, QtWidgets
import PIL.ImageGrab
from PyQt5.QtWebEngineWidgets import QWebEngineView
from folium import Figure
from matplotlib import axis
#from GeographicalLocation import *
from cases import *
from newtestNetwork import SocialNetworkTest

from socialNetwork import SocialNetwork
from testview import Window
from snapshot import*

 
from peoples import People

from viber import viber
from GeographicalLocation import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg 
from audioop import add
from mimetypes import init
import sys

#from additem1 import Ui_Evidance
from allEmail import *
from allViber import allViber
from emailSummary import *
from whatsappSummary import *
from viberSummary import *



from textmessages import *
#from socialNetworkWhatapp import SocialNetworkWhatapp
from comunicationNumberTabl import comunicationNumberTable
from contactTimesPerDay import cantactTimesperDate
from GeographicalLocation import MyApp


from watsAppViberTable import ViberWatsAppTable

#from textmessages import Ui_TextmsgeTable



CustomObjectRole=QtCore.Qt.UserRole + 1

class Ui_DialogAnalysis(object):
   # def additemWindo(self):
      #  self.window = QtWidgets.QDialog() 
      #  self.ui= Ui_Evidance()
      #  self.ui.setupUi(self.window)
       # DialogAnalysis.hide()
       # self.window.show()
       
    def __init__(self, SelectedCase = None):
        self.case =cases()
        super(Ui_DialogAnalysis,self).__init__()
        if SelectedCase == None:
           return
        
        self.Case = SelectedCase 
        
         
        self.activepeople = People()  
     
       
       

    @property
    def Case(self):
        return self.case

    @Case.setter
    def Case(self, value):
        self.case = value

    @property
    def Activepeople(self):
        return self.activepeople
    @Activepeople.setter
    def Activepeople(self, value):
        self.activepeople = value
    def setupUi(self, DialogAnalysis):
        DialogAnalysis.setObjectName("DialogAnalysis")
        DialogAnalysis.resize(1477, 1003)
        self.tabWidgetBookMark = QtWidgets.QTabWidget(DialogAnalysis)
        self.tabWidgetBookMark.setGeometry(QtCore.QRect(290, 0, 1201, 941))
        self.tabWidgetBookMark.setStyleSheet("border-left-color: rgb(243, 247, 255);\n"
       "border-color: rgb(0, 0, 0);\n"
        "selection-color: rgb(222, 223, 255);\n"
         "background-color: rgb(255, 255, 255);")
        self.tabWidgetBookMark.setObjectName("tabWidgetBookMark")
        self.geoloctab = QtWidgets.QWidget()
        self.geoloctab.setObjectName("geoloctab")
       
        self.SocialNetworktab = QtWidgets.QWidget()
       
      
        self.statisictap = QtWidgets.QWidget()
        self.statisictap.setObjectName("statisictap")
        
        self.chat_tap = QtWidgets.QWidget()
        self.chat_tap.setObjectName("chat_tap")
       
        self.tab_bookmark = QtWidgets.QWidget()
        self.tab_bookmark.setObjectName("tab_bookmark")
        self.tabWidgetBookMark.addTab(self.tab_bookmark, "")
        self.dockWidget_analysis = QtWidgets.QDockWidget(DialogAnalysis)
        self.dockWidget_analysis.setGeometry(QtCore.QRect(0, 0, 295, 941))
        self.dockWidget_analysis.setStyleSheet("\n""background-color: rgb(243, 247, 255);")
        self.dockWidget_analysis.setObjectName("dockWidget_analysis")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 100, 211, 151 ))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButtonEmail = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonEmail.setGeometry(QtCore.QRect(30, 30, 95, 20))
        self.radioButtonEmail.setObjectName("radioButtonEmail")
        self.radioButton_whatsApp = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_whatsApp.setGeometry(QtCore.QRect(30, 60, 95, 20))
        self.radioButton_whatsApp.setObjectName("radioButton_whatsApp")
        self.radioButton_viber = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_viber.setGeometry(QtCore.QRect(30, 100, 95, 20))
        self.radioButton_viber.setObjectName("radioButton_viber")
        self.lineEdit_serchKeyWord_ForChat = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.lineEdit_serchKeyWord_ForChat.setGeometry(QtCore.QRect(100, 420, 181, 31))
        self.lineEdit_serchKeyWord_ForChat.setObjectName("lineEdit_serchKeyWord_ForChat")
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_5.setGeometry(QtCore.QRect(20, 420, 71, 31))
        self.label_5.setStyleSheet("background-color: rgb(222, 223, 255);")
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 270, 221, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_filterKeyWord = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_filterKeyWord.setGeometry(QtCore.QRect(10, 20, 201, 20))
        self.checkBox_filterKeyWord.setObjectName("checkBox_filterKeyWord")
        self.checkBox_FiterTimeDate = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_FiterTimeDate.setGeometry(QtCore.QRect(10, 40, 171, 20))
        self.checkBox_FiterTimeDate.setObjectName("checkBox_FiterTimeDate")
    
        self.checkBox_sender = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_sender.setGeometry(QtCore.QRect(10, 60, 201, 20))
        self.checkBox_sender.setObjectName("checkBox_sender")
     
       
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(10, 80, 141, 20))
        self.checkBox.setObjectName("checkBox")
        self.btnVerify = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnVerify.setGeometry(QtCore.QRect(20, 740, 111, 41))
        self.btnVerify.setStyleSheet("background-color: rgb(222, 223, 255);")
        self.btnVerify.setObjectName("btnVerify")
        self.groupBox_5 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 570, 271, 101))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 20))
        self.label.setObjectName("label")
        self.dateEdit_dateFrom = QtWidgets.QDateEdit(self.groupBox_5)
        self.dateEdit_dateFrom.setGeometry(QtCore.QRect(80, 20, 110, 22))
        self.dateEdit_dateFrom.setObjectName("dateEdit_dateFrom")
        self.dateEdit_dateTo = QtWidgets.QDateEdit(self.groupBox_5)
        self.dateEdit_dateTo.setGeometry(QtCore.QRect(80, 60, 110, 22))
        self.dateEdit_dateTo.setObjectName("dateEdit_dateTo")
        self.groupBox_6 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_6.setGeometry(QtCore.QRect(30, 470, 251, 80))
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_Sender = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_Sender.setGeometry(QtCore.QRect(70, 20, 161, 22))
        self.lineEdit_Sender.setObjectName("lineEdit_Sender")
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_Recepian = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_Recepian.setGeometry(QtCore.QRect(70, 50, 161, 22))
        self.lineEdit_Recepian.setObjectName("lineEdit_Recepian")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 55, 21))
        self.label_4.setObjectName("label_4")
        self.label_casename = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_casename.setGeometry(QtCore.QRect(80, 40, 51, 16))
        self.label_casename.setText("")
        self.label_casename.setObjectName("label_casename")
        self.label_6 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_6.setGeometry(QtCore.QRect(30, 40, 41, 16))
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_13.setGeometry(QtCore.QRect(150, 40, 55, 16))
        self.label_13.setObjectName("label_13")
        self.btnSnapshot = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnSnapshot.setGeometry(QtCore.QRect(140, 740, 131, 41))
        self.btnSnapshot.setStyleSheet("background-color: rgb(222, 223, 255);")
        self.btnSnapshot.setObjectName("btnSnapshot")
        self.btnClear = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnClear.setGeometry(QtCore.QRect(140, 790, 131, 41))
        self.btnClear.setAutoFillBackground(False)
        self.btnClear.setStyleSheet("background-color: rgb(222, 223, 255);\n"
"")
        self.btnClear.setObjectName("btnClear")
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 790, 111, 41))
        self.pushButton.setStyleSheet("background-color: rgb(222, 223, 255);")
        self.pushButton.setObjectName("pushButton")
        self.btnshowResult = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnshowResult.setGeometry(QtCore.QRect(30, 690, 241, 41))
        self.btnshowResult.setStyleSheet("background-color: rgb(222, 223, 255);")
        self.btnshowResult.setObjectName("btnshowResult")
        self.dockWidget_analysis.setWidget(self.dockWidgetContents_2)
        self.label_casename.setText(self.case.caseName)
        self.retranslateUi(DialogAnalysis)
        self.tabWidgetBookMark.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(DialogAnalysis)
        
        
           # print(i.ToEmail_logtude)
  #  def fff(self):
      #  emails=allEmail.getAllEmails(self)
      #  for i in emails:
         #   print(i.toEmail_latitude)
            #print(i.toEmail_logtude)
           # MyApp.cordinate(self,i.fromEmail_latitude, i.fromEmail_latitude)
               
        

    def retranslateUi(self, DialogAnalysis):
        _translate = QtCore.QCoreApplication.translate
        DialogAnalysis.setWindowTitle(_translate("DialogAnalysis", "The Holmes Tool Kit (THTK)"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.geoloctab), _translate("DialogAnalysis", "Geolocation"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.SocialNetworktab), _translate("DialogAnalysis", "Social networ"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.statisictap), _translate("DialogAnalysis", "statisic"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.chat_tap), _translate("DialogAnalysis", "chat"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.tab_bookmark), _translate("DialogAnalysis", "Bookmark"))
        self.dockWidget_analysis.setWindowTitle(_translate("DialogAnalysis", "Analysis bar"))
        self.groupBox_2.setTitle(_translate("DialogAnalysis", "Plat form"))
        self.radioButtonEmail.setText(_translate("DialogAnalysis", "Email"))
        self.radioButton_whatsApp.setText(_translate("DialogAnalysis", "WhatsApp"))
        self.radioButton_viber.setText(_translate("DialogAnalysis", "Viber"))
        self.groupBox_3.setTitle(_translate("DialogAnalysis", "Filter option"))
        self.checkBox_filterKeyWord.setText(_translate("DialogAnalysis", "Filter by  keyword only"))
        self.checkBox_FiterTimeDate.setText(_translate("DialogAnalysis", "Filter by Date and time only"))
        self.btnVerify.setText(_translate("DialogAnalysis", "verify"))
        self.groupBox_5.setTitle(_translate("DialogAnalysis", "Date filtering"))
        self.label_2.setText(_translate("DialogAnalysis", "To date"))
        self.label.setText(_translate("DialogAnalysis", "From date"))
        self.groupBox_6.setTitle(_translate("DialogAnalysis", "Sender recepiant"))
        self.label_3.setText(_translate("DialogAnalysis", "Sender"))
        self.label_4.setText(_translate("DialogAnalysis", "Recepiant"))
        self.label_6.setText(_translate("DialogAnalysis", "This is"))
        self.label_13.setText(_translate("DialogAnalysis", "case!"))
        self.btnSnapshot.setText(_translate("DialogAnalysis", "Add evedence Item"))
        self.btnClear.setText(_translate("DialogAnalysis", "Clear"))
        self.btnClear.clicked.connect(self.clearalltaps)
       
        self.checkBox_sender.setText(_translate("DialogAnalysis", "Filter by sender"))
        self.checkBox.setText(_translate("DialogAnalysis", "Filter by recepiant"))

        self.btnshowResult.setText(_translate("DialogAnalysis", "Show result"))
        self.pushButton.setText(_translate("DialogAnalysis", "Back"))
        self.label_5.setText(_translate("DialogAnalysis", "   Keyword"))
        #self.btnSnapshot.clicked.connect(self.additemWindo)
        name=['cute','jumbo','ccccc']
        completer = QtWidgets.QCompleter(name)
        # put the completer in
        self.lineEdit_Recepian.setCompleter(completer)

         # put the completer in
        self.lineEdit_Sender.setCompleter(completer)
       
        #getting the value
        self.lineEdit_Recepian.textChanged.connect(self.selectedRecepean)
        self.lineEdit_Sender.textChanged.connect(self.selectedSender)
        self.dateEdit_dateFrom.setCalendarPopup(True)
        self.dateEdit_dateFrom.setMinimumDate(QtCore.QDate(2000, 2, 2))
        self.dateEdit_dateFrom.setMaximumDate(QtCore.QDate(4000, 3, 1))
       # self.dateEdit_dateFrom.dateChanged.connect(self.fromlinedittopython)
        
        # to date functionality
        self.dateEdit_dateTo.setStyleSheet("\n""background-color: rgb(222, 223, 255);")
        self.dateEdit_dateTo.setCalendarPopup(True)
        self.dateEdit_dateTo.setMinimumDate(QtCore.QDate(2000, 2, 2))
        self.dateEdit_dateTo.setMaximumDate(QtCore.QDate(4000, 3, 1))
      #  self.dateEdit_dateTo.dateChanged.connect(self.fromlinedittopython)
       # self.todate=self.dateEdit_dateTo.dateTimeChanged.connect(lambda: DateTo(self).toPyDate)

        
         # to date functionality
        self.dateEdit_dateFrom.setStyleSheet("\n""background-color: rgb(222, 223, 255);")
        self.dateEdit_dateFrom.setCalendarPopup(True)
        self.dateEdit_dateFrom.setMinimumDate(QtCore.QDate(2000, 2, 2))
        self.dateEdit_dateFrom.setMaximumDate(QtCore.QDate(4000, 3, 1))
        #    check box
        # self.checkBox_FiterTimeDate.stateChanged.connect(self.checked)
        # self.checkBox_filterKeyWord.stateChanged.connect(self.checked)
        # self.checkBox_senderRecipeant.stateChanged.connect(self.checked)
        self.checkBox_FiterTimeDate.toggled.connect(self.checked)
        self.checkBox_filterKeyWord.toggled.connect(self.checked)
        self.checkBox_sender.toggled.connect(self.checked)
        self.checkBox.toggled.connect(self.checked)
        self.btnshowResult.clicked.connect(self.btnstate)
        self.btnSnapshot.clicked.connect(self.on_click)
        
       

          # activing radio button 
        # def allResult(self): 
        #      self.radioButton_viber.toggled.connect(lambda:self.btnstate(self.radioButton_viber))
        #      self.radioButton_whatsApp.toggled.connect(lambda:self.btnstate(self.radioButton_whatsApp))
    def on_click(self):
        import os
        path = self.getdirectory()
        for el in path:
            if os.path.exists(el):
                time.sleep(2)
                img = ImageGrab.grab()
                time_now = time.strftime("%Y%m%d%h%M%S")
                name = f"screen{time_now}"
                img.save(f"{path}/{name}.png", "png")
                name_img = name
                
                break
            else:
                try:
                    os.mkdir(path)
                except OSError:
                    time.sleep(2)
                    img = ImageGrab.grab()
                    time_now = time.strftime("%Y%m%d%h%M%S")
                    name = f"screen{time_now}"
                    img.save(f"{path}/{name}.png", "png")
                    name_img = name
                    
                    break
                else:
                    time.sleep(2)
                    img = ImageGrab.grab()
                    time_now = time.strftime("%Y%m%d%h%M%S")
                    name = f"screen{time_now}"
                    img.save(f"{path}/{name}.png", "png")
                    name_img = name
                   

                    break

    def getdirectory(self):
         response = QtWidgets.QFileDialog.getExistingDirectory(caption='Select folder')
         print(response)
         return response


            #      self.radioButtonEmail.toggled.connect(lambda:self.btnstate(self.radioButtonEmail))

    def clearalltaps(self):
       
        for i in range(self.tabWidgetBookMark.count()-1):
            self.tabWidgetBookMark.removeTab(i)
            i=i-1 
            self.tabWidgetBookMark.removeTab(0)
    
    def selectedRecepean(self):
        print(self.lineEdit_Recepian.text())
      #print(self.lineEdit_Recepian.selectedText())
    def selectedSender(self):
         print(self.lineEdit_Sender.text())
        #print(self.lineEdit_Sender.selectedText())
    def grapaDate(self):
            self.dateEdit_dateTo.setDate()
            print("ddd")
        # selct the to date
  
      # select the from date
    def checked(self):
        #ALL TRUE
        if self.checkBox_filterKeyWord.checkState() == 2 and self.checkBox_FiterTimeDate.checkState() == 2 and self.checkBox.checkState() == 2 and self.checkBox_sender.checkState() == 2:
            print('shecked')
            self.lineEdit_serchKeyWord_ForChat.setEnabled(True)
            self.dateEdit_dateFrom.setEnabled(True)
            self.dateEdit_dateTo.setEnabled(True)
            self.lineEdit_Recepian.setEnabled(True)
            self.lineEdit_Sender.setEnabled(True)
            # T T T F
        if  self.checkBox_filterKeyWord.checkState() == 2 and self.checkBox_FiterTimeDate.checkState() == 2 and self.checkBox.checkState()==2 and self.checkBox_sender.checkState()==0:
            print('shecked')
            self.lineEdit_serchKeyWord_ForChat.setEnabled(True)
     
            self.dateEdit_dateFrom.setEnabled(True)
            self.dateEdit_dateTo.setEnabled(True)
            self.lineEdit_Recepian.setEnabled(True)
            self.lineEdit_Sender.setEnabled(False)
            # T T F F ?
        if  self.checkBox_filterKeyWord.checkState() == 2 and self.checkBox_FiterTimeDate.checkState() == 2 and self.checkBox.checkState()== 0 and self.checkBox_sender.checkState()== 0:
            print('shecked')
            self.lineEdit_serchKeyWord_ForChat.setEnabled(True)
            self.dateEdit_dateFrom.setEnabled(True)
            self.dateEdit_dateTo.setEnabled(True)
            self.lineEdit_Recepian.setEnabled(False)
            self.lineEdit_Sender.setEnabled(False)
            # T F F F

        if  self.checkBox_filterKeyWord.checkState() == 2 and self.checkBox_FiterTimeDate.checkState() == 0 and self.checkBox.checkState()==0 and self.checkBox_sender.checkState()==0:
            print('shecked')
            self.lineEdit_serchKeyWord_ForChat.setEnabled(True)
          
            self.dateEdit_dateFrom.setEnabled(False)
            self.dateEdit_dateTo.setEnabled(False)
            self.lineEdit_Recepian.setEnabled(False)
            self.lineEdit_Sender.setEnabled(False)
            # F F F F
        if  self.checkBox_filterKeyWord.checkState() == 0 and self.checkBox_FiterTimeDate.checkState() == 0 and self.checkBox.checkState()==0 and self.checkBox_sender.checkState()==0:
            print('shecked')
            self.lineEdit_serchKeyWord_ForChat.setEnabled(False)
          
            self.dateEdit_dateFrom.setEnabled(False)
            self.dateEdit_dateTo.setEnabled(False)
            self.lineEdit_Recepian.setEnabled(False)
            self.lineEdit_Sender.setEnabled(False)
            #F F F T
        if  self.checkBox_filterKeyWord.checkState() == 0 and self.checkBox_FiterTimeDate.checkState() == 0 and self.checkBox.checkState()==0 and self.checkBox_sender.checkState()==2:
            print('shecked')
            self.lineEdit_serchKeyWord_ForChat.setEnabled(False)
           
            self.dateEdit_dateFrom.setEnabled(False)
            self.dateEdit_dateTo.setEnabled(False)
            self.lineEdit_Recepian.setEnabled(False)
            self.lineEdit_Sender.setEnabled(True)
            #F F T T
        if  self.checkBox_filterKeyWord.checkState() == 0 and self.checkBox_FiterTimeDate.checkState() == 0 and self.checkBox.checkState()==2 and self.checkBox_sender.checkState()==2:
            print('shecked')
            self.lineEdit_serchKeyWord_ForChat.setEnabled(False)
     
            self.dateEdit_dateFrom.setEnabled(False)
            self.dateEdit_dateTo.setEnabled(False)
            self.lineEdit_Recepian.setEnabled(True)
            self.lineEdit_Sender.setEnabled(True)
            # F T T T
        if  self.checkBox_filterKeyWord.checkState() == 0 and self.checkBox_FiterTimeDate.checkState() == 2 and self.checkBox.checkState()==2 and self.checkBox_sender.checkState()==2:
               print('shecked')
               self.lineEdit_serchKeyWord_ForChat.setEnabled(False)
               self.dateEdit_dateFrom.setEnabled(True)
               self.dateEdit_dateTo.setEnabled(True)
               self.lineEdit_Recepian.setEnabled(True)
               self.lineEdit_Sender.setEnabled(True)
            # F T F F
        if  self.checkBox_filterKeyWord.checkState() == 0 and self.checkBox_FiterTimeDate.checkState() == 2 and self.checkBox.checkState()==0 and self.checkBox_sender.checkState()==0:
            print('shecked')
            self.lineEdit_serchKeyWord_ForChat.setEnabled(False)
     
            self.dateEdit_dateFrom.setEnabled(True)
            self.dateEdit_dateTo.setEnabled(True)
            self.lineEdit_Recepian.setEnabled(False)
            self.lineEdit_Sender.setEnabled(False)
            # F F T F
        if  self.checkBox_filterKeyWord.checkState() == 0 and self.checkBox_FiterTimeDate.checkState() == 0 and self.checkBox.checkState() == 2 and self.checkBox_sender.checkState() == 0:
               print('shecked')
               self.lineEdit_serchKeyWord_ForChat.setEnabled(False)
               self.dateEdit_dateFrom.setEnabled(False)
               self.dateEdit_dateTo.setEnabled(False)
               self.lineEdit_Recepian.setEnabled(True)
               self.lineEdit_Sender.setEnabled(False)
         # F T T F
        if  self.checkBox_filterKeyWord.checkState() == 0 and self.checkBox_FiterTimeDate.checkState() == 2 and self.checkBox.checkState()==2 and self.checkBox_sender.checkState()==0:
               print('shecked')
               self.lineEdit_serchKeyWord_ForChat.setEnabled(False)
               self.dateEdit_dateFrom.setEnabled(True)
               self.dateEdit_dateTo.setEnabled(True)
               self.lineEdit_Recepian.setEnabled(True)
               self.lineEdit_Sender.setEnabled(False)
        # T F F T
        if  self.checkBox_filterKeyWord.checkState() == 2 and self.checkBox_FiterTimeDate.checkState() == 0 and self.checkBox.checkState()==0 and self.checkBox_sender.checkState()==2:
               print('shecked')
               self.lineEdit_serchKeyWord_ForChat.setEnabled(True)
               self.dateEdit_dateFrom.setEnabled(False)
               self.dateEdit_dateTo.setEnabled(False)
               self.lineEdit_Recepian.setEnabled(False)
               self.lineEdit_Sender.setEnabled(True)
                # F T F T
        if  self.checkBox_filterKeyWord.checkState() == 0 and self.checkBox_FiterTimeDate.checkState() == 2 and self.checkBox.checkState()==0 and self.checkBox_sender.checkState()==2:
               print('shecked')
               self.lineEdit_serchKeyWord_ForChat.setEnabled(False)
               self.dateEdit_dateFrom.setEnabled(True)
               self.dateEdit_dateTo.setEnabled(True)
               self.lineEdit_Recepian.setEnabled(False)
               self.lineEdit_Sender.setEnabled(True)
                # T F T F
        if  self.checkBox_filterKeyWord.checkState() == 2 and self.checkBox_FiterTimeDate.checkState() == 0 and self.checkBox.checkState()==2 and self.checkBox_sender.checkState()==0:
               print('shecked')
               self.lineEdit_serchKeyWord_ForChat.setEnabled(True)
               self.dateEdit_dateFrom.setEnabled(False)
               self.dateEdit_dateTo.setEnabled(False)
               self.lineEdit_Recepian.setEnabled(True)
               self.lineEdit_Sender.setEnabled(False)
             
                # T F T T
        if  self.checkBox_filterKeyWord.checkState() == 2 and self.checkBox_FiterTimeDate.checkState() == 0 and self.checkBox.checkState()==2 and self.checkBox_sender.checkState()==2:
               print('shecked')
               self.lineEdit_serchKeyWord_ForChat.setEnabled(True)
               self.dateEdit_dateFrom.setEnabled(False)
               self.dateEdit_dateTo.setEnabled(False)
               self.lineEdit_Recepian.setEnabled(True)
               self.lineEdit_Sender.setEnabled(True)
           # T T F T ?
        if  self.checkBox_filterKeyWord.checkState() == 2 and self.checkBox_FiterTimeDate.checkState() == 2 and self.checkBox.checkState()==0 and self.checkBox_sender.checkState()==2:
               print('shecked')
               self.lineEdit_serchKeyWord_ForChat.setEnabled(True)
               self.dateEdit_dateFrom.setEnabled(True)
               self.dateEdit_dateTo.setEnabled(True)
               self.lineEdit_Recepian.setEnabled(False)
               self.lineEdit_Sender.setEnabled(True)
        
        
        
        
        
        
    #SocialNetwork.draw_circlar(G_symmetric_watsapp)


        
    def btnstate(self):
        mText=""
        mseander=""
        mrespian=""
        mFromDate='0001/1/1'
        mToDate= '9999/1/1'
        if self.checkBox_filterKeyWord.checkState() == 2 :
           mText=self.lineEdit_serchKeyWord_ForChat.text()
           
        if self.checkBox_sender.checkState() == 2 :
           mseander=self.lineEdit_Sender.text()
          
        
        if  self.checkBox_FiterTimeDate.checkState() == 2 :
            mFromDate=self.dateEdit_dateFrom.date().toString('yyyy/MM/dd')
            mToDate= self.dateEdit_dateTo.date().toString('yyyy/MM/dd')
        if  self.checkBox.checkState() == 2 :
            mFromDate=self.lineEdit_Recepian.text()
           

       
          
        if self.radioButton_whatsApp.isChecked():
           
           
            WhatsApps= allWhatsApp.getAllWhatsApp(self,
            self.case.caseId
            ,str( mFromDate)
                ,str(mToDate) , mText,mseander,mrespian)
            
               
           
            self.clearalltaps() 
            self.tabWidgetBookMark.addTab(SocialNetwork(None,None,WhatsApps),"SocialNetworktab")
            self.tabWidgetBookMark.addTab(MyApp(None,None,WhatsApps), "Geographical location")
            self.tabWidgetBookMark.addTab(ViberWatsAppTable( WhatsApps, None),"Comunication")
            whatsapp_summary=whatsAppsummary.getwhatsappSummary(self,
            self.case.caseId
            ,str( mFromDate)
                ,str(mToDate) , mText,mseander,mrespian)
            self.tabWidgetBookMark.addTab(comunicationNumberTable(None,whatsapp_summary),"Comunication Analysis")
           # self.tabWidgetBookMark.addTab(SocialNetworkTest(None,None,WhatsApps),"SocialNetworktab")
            self.tabWidgetBookMark.addTab(Window(None,None,whatsapp_summary),"statisic")

            
        if self.radioButton_viber.isChecked():               
       
                self.clearalltaps()
               
                
    
                vibers=allViber.getAllVibers(self,
                self.case.caseId
                ,str( mFromDate)
                ,str(mToDate) , mText,mseander,mrespian)
                
                self.tabWidgetBookMark.addTab(SocialNetwork(vibers,None,None),"SocialNetworktab")
                self.tabWidgetBookMark.addTab(MyApp(vibers,None,None), "Geographical location")
                self.tabWidgetBookMark.addTab(ViberWatsAppTable(None,vibers),"Comunication")
                viber_summary=vibersummary.getAllViberSummary(self,
            self.case.caseId
            ,str( mFromDate)
                ,str(mToDate) , mText,mseander,mrespian)
                self.tabWidgetBookMark.addTab(comunicationNumberTable(viber_summary,None),"Comunication Analysis")
              #  self.tabWidgetBookMark.addTab(SocialNetworkTest(vibers,None,None),"SocialNetworktab")
                self.tabWidgetBookMark.addTab(Window(viber_summary,None, None),"statisic")

        if self.radioButtonEmail.isChecked():
                #'email for social network
                self.clearalltaps()
                      
                emails=allEmail.getAllEmails(self,
                 self.case.caseId
                 ,str( mFromDate)
                ,str(mToDate) , mText,mseander,mrespian)

                self.tabWidgetBookMark.addTab(SocialNetwork(None,emails,None),"SocialNetworktab")
                self.tabWidgetBookMark.addTab(MyApp(None,emails,None), "Geographical location")
                self.tabWidgetBookMark.addTab(emaildetails(emails),'EmailComunication')
                email_summary=emailsummary.getAllemailSummary(self,
            self.case.caseId
            ,str( mFromDate)
                ,str(mToDate) , mText,mseander,mrespian)
                self.tabWidgetBookMark.addTab(cantactTimesperDate(email_summary),"DataTime")
                self.tabWidgetBookMark.addTab(Window(None,email_summary,None),"statisic")
      
            
    def checkedInputs(self):
        if self.checkBox_filterKeyWord.checkState() == 2 and self.checkBox_FiterTimeDate.checkState() == 2 and self.checkBox_sender.checkState()==2 and self.checkBox.checkState()==2 :
           mText=self.lineEdit_serchKeyWord_ForChat.text()
           mFromDate=self.dateEdit_dateFrom.date()
           mToDate= self.dateEdit_dateTo.date()
           mrespian= self.lineEdit_Recepian.text()

        if  self.checkBox_filterKeyWord.checkState() == 2 and self.checkBox_FiterTimeDate.checkState() == 2 and self.checkBox_sender.checkState()==0:
            mText=self.lineEdit_serchKeyWord_ForChat.text()
            mFromDate=self.dateEdit_dateFrom.date()
            mToDate= '4000/2/2'
        if  self.checkBox_filterKeyWord.checkState() == 2 and self.checkBox_FiterTimeDate.checkState() == 0 and self.checkBox_sender.checkState()==0:
             mText=self.lineEdit_serchKeyWord_ForChat.text()
             mFromDate='2000/2/2'
             mToDate= '4000/2/2'
        if  self.checkBox_filterKeyWord.checkState() == 0 and self.checkBox_FiterTimeDate.checkState() == 2 and self.checkBox_sender.checkState()==2:
            mText=' '
            mFromDate=self.dateEdit_dateFrom.date()
            mToDate= self.dateEdit_dateTo.date()
        if  self.checkBox_filterKeyWord.checkState() == 0 and self.checkBox_FiterTimeDate.checkState() == 0 and self.checkBox_sender.checkState()==2:
             mText=' '
             mFromDate='2000/2/2'
             mToDate= self.dateEdit_dateTo.date()      
  
            
        

    
     
 
      
     #  select a recepian
    
    
     #grapping the date from the line edit to python program   
  

def fromlinedittopython(self):
        return self.dateEdit_dateTo.date().toPyDate()
    
    

def DateFrom(self):
          return self.dateEdit_dateFrom.date().toPyDate()   
    # #select the sender

def DateTo(self):
        return self.dateEdit_dateTo.date().toPyDate()

        
      #  the check button activity

   
   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAnalysis = QtWidgets.QDialog()
    ui = Ui_DialogAnalysis()
    ui.setupUi(DialogAnalysis)
    DialogAnalysis.show()
    sys.exit(app.exec_())
