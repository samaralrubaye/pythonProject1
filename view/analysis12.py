# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\samar\Desktop\finalyearproject\pythonProject1\view\analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import PIL.ImageGrab
from PyQt5.QtWebEngineWidgets import QWebEngineView
from GeographicalLocation import *
from cases import *

class Ui_DialogAnalysis(object):
    def __init__(self, ex = None):
        self.case =cases ()
        super(Ui_DialogAnalysis,self).__init__()
        if ex == None:
           return
        
        self.Case = ex           

   
    
    
    @property
    def Case(self):
        return self.case

    @Case.setter
    def Case(self, value):
        self.case = value

    def setupUi(self, DialogAnalysis):
        DialogAnalysis.setObjectName("DialogAnalysis")
        DialogAnalysis.resize(1482, 1003)
        self.tabWidgetBookMark = QtWidgets.QTabWidget(DialogAnalysis)
        self.tabWidgetBookMark.setGeometry(QtCore.QRect(290, 0, 1011, 1001))
        self.tabWidgetBookMark.setObjectName("tabWidgetBookMark")
        #geo location
        self.geoloctab = QtWidgets.QWidget()
        self.geoloctab.setObjectName("geoloctab")
        self.tabWidgetBookMark.addTab(self.geoloctab, "")
        # social engineering
        self.SocialNetworktab = QtWidgets.QWidget()
        self.SocialNetworktab.setObjectName("SocialNetworktab")
        self.lbl_Visualization = QtWidgets.QLabel(self.SocialNetworktab)
        self.lbl_Visualization.setGeometry(QtCore.QRect(14, 20, 971, 711))
        self.lbl_Visualization.setText("")
        self.lbl_Visualization.setPixmap(QtGui.QPixmap("c:\\Users\\samar\\Desktop\\finalyearproject\\pythonProject1\\view\\filename4.png"))
        self.lbl_Visualization.setScaledContents(True)
        self.lbl_Visualization.setObjectName("lbl_Visualization")
        self.groupBox_7 = QtWidgets.QGroupBox(self.SocialNetworktab)
        self.groupBox_7.setGeometry(QtCore.QRect(30, 780, 751, 80))
        self.groupBox_7.setObjectName("groupBox_7")
        self.btn_Circular_Layout = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_Circular_Layout.setGeometry(QtCore.QRect(30, 30, 93, 28))
        self.btn_Circular_Layout.setObjectName("btn_Circular_Layout")
        self.btn_Planer_Layout = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_Planer_Layout.setGeometry(QtCore.QRect(130, 30, 93, 28))
        self.btn_Planer_Layout.setObjectName("btn_Planer_Layout")
        self.btn_Random_Layout = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_Random_Layout.setGeometry(QtCore.QRect(230, 30, 93, 28))
        self.btn_Random_Layout.setObjectName("btn_Random_Layout")
        self.btn_Special_Layout = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_Special_Layout.setGeometry(QtCore.QRect(340, 30, 93, 28))
        self.btn_Special_Layout.setObjectName("btn_Special_Layout")
        self.tabWidgetBookMark.addTab(self.SocialNetworktab, "")
        #statistic
        self.statisictap = QtWidgets.QWidget()
        self.statisictap.setObjectName("statisictap")
        self.groupBox_4 = QtWidgets.QGroupBox(self.statisictap)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 790, 791, 80))
        self.groupBox_4.setObjectName("groupBox_4")
        self.btnPieChart = QtWidgets.QPushButton(self.groupBox_4)
        self.btnPieChart.setGeometry(QtCore.QRect(70, 20, 93, 28))
        self.btnPieChart.setObjectName("btnPieChart")
        self.btnBarChart = QtWidgets.QPushButton(self.groupBox_4)
        self.btnBarChart.setGeometry(QtCore.QRect(210, 20, 93, 28))
        self.btnBarChart.setObjectName("btnBarChart")
        self.checkBox_places = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_places.setGeometry(QtCore.QRect(410, 20, 81, 20))
        self.checkBox_places.setObjectName("checkBox_places")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_5.setGeometry(QtCore.QRect(530, 20, 81, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_6.setGeometry(QtCore.QRect(670, 20, 81, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.lbl_statistic = QtWidgets.QLabel(self.statisictap)
        self.lbl_statistic.setGeometry(QtCore.QRect(20, 20, 761, 751))
        self.lbl_statistic.setText("")
        self.lbl_statistic.setPixmap(QtGui.QPixmap("c:\\Users\\samar\\Desktop\\finalyearproject\\pythonProject1\\view\\barchart.png"))
        self.lbl_statistic.setScaledContents(True)
        self.lbl_statistic.setObjectName("lbl_statistic")
        self.tabWidgetBookMark.addTab(self.statisictap, "")
        self.tab_tap = QtWidgets.QWidget()
        self.tab_tap.setObjectName("tab_tap")
        self.label_5 = QtWidgets.QLabel(self.tab_tap)
        self.label_5.setGeometry(QtCore.QRect(-20, -10, 951, 871))
        self.label_5.setObjectName("label_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_tap)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 10, 961, 851))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidgetBookMark.addTab(self.tab_tap, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 0, 871, 1000))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textBrowser_3)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textBrowser_6)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.textBrowser_2)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.textBrowser_9)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.textBrowser_4)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.textBrowser_5)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.textBrowser_7)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.textBrowser_8)
        self.fileCommatLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.fileCommatLabel.setFont(font)
        self.fileCommatLabel.setObjectName("fileCommatLabel")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.fileCommatLabel)
        self.textBrowser = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.textBrowser)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.fileCommatLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.fileCommatLineEdit.setObjectName("fileCommatLineEdit")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.fileCommatLineEdit)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.toolButton = QtWidgets.QToolButton(self.formLayoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.toolButton)
        self.tabWidgetBookMark.addTab(self.tab, "")
        self.dockWidget_analysis = QtWidgets.QDockWidget(DialogAnalysis)
        self.dockWidget_analysis.setGeometry(QtCore.QRect(0, 0, 295, 902))
        self.dockWidget_analysis.setStyleSheet("q rgb(250, 235, 255)")
        self.dockWidget_analysis.setObjectName("dockWidget_analysis")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 211, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_Email = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Email.setGeometry(QtCore.QRect(30, 40, 81, 20))
        self.checkBox_Email.setObjectName("checkBox_Email")
        self.checkBox_WhatsApp = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_WhatsApp.setGeometry(QtCore.QRect(30, 70, 81, 20))
        self.checkBox_WhatsApp.setObjectName("checkBox_WhatsApp")

        self.checkBox_Viber = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Viber.setGeometry(QtCore.QRect(30, 110, 81, 20))
        self.checkBox_Viber.setObjectName("checkBox_Viber")
        #Keyword search
        self.lineEdit_serchKeyWord_ForChat = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.lineEdit_serchKeyWord_ForChat.setGeometry(QtCore.QRect(120, 90, 161, 31))
        self.lineEdit_serchKeyWord_ForChat.setObjectName("lineEdit_serchKeyWord_ForChat")
        self.btnKeyWordChat_2 = QtWidgets.QPushButton(self.dockWidgetContents_2)
        # key word serch
        self.btnKeyWordChat_2.setGeometry(QtCore.QRect(10, 90, 111, 31))
        self.btnKeyWordChat_2.setObjectName("btnKeyWordChat_2")
        #snapshot
        self.btnSnapshot = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnSnapshot.setGeometry(QtCore.QRect(20, 10, 61, 51))
        self.btnSnapshot.setObjectName("btnSnapshot")
        self.groupBox_3 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 640, 231, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_filterKeyWord = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_filterKeyWord.setGeometry(QtCore.QRect(10, 20, 201, 20))
        self.checkBox_filterKeyWord.setObjectName("checkBox_filterKeyWord")
        self.checkBox_FiterTimeDate = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_FiterTimeDate.setGeometry(QtCore.QRect(10, 50, 171, 20))
        self.checkBox_FiterTimeDate.setObjectName("checkBox_FiterTimeDate")
        #verify
        self.btnVerify = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnVerify.setGeometry(QtCore.QRect(40, 760, 141, 28))
        self.btnVerify.setObjectName("btnVerify")
        self.groupBox_5 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 300, 271, 101))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 20))
        self.label.setObjectName("label")
        #date
        self.dateEdit_dateFrom = QtWidgets.QDateEdit(self.groupBox_5)
        self.dateEdit_dateFrom.setGeometry(QtCore.QRect(80, 20, 110, 22))
        self.dateEdit_dateFrom.setObjectName("dateEdit_dateFrom")
        self.dateEdit_dateTo = QtWidgets.QDateEdit(self.groupBox_5)
        self.dateEdit_dateTo.setGeometry(QtCore.QRect(80, 60, 110, 22))
        self.dateEdit_dateTo.setObjectName("dateEdit_dateTo")
        self.groupBox_6 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 460, 241, 80))
        self.groupBox_6.setObjectName("groupBox_6")
        #lineedit sender
        self.lineEdit_Sender = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_Sender.setGeometry(QtCore.QRect(70, 20, 161, 22))
        self.lineEdit_Sender.setObjectName("lineEdit_Sender")
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_Recepian = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_Recepian.setGeometry(QtCore.QRect(70, 50, 161, 22))
        self.lineEdit_Recepian.setObjectName("lineEdit_Recepian")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 55, 21))
        self.label_4.setObjectName("label_4")
        self.dockWidget_analysis.setWidget(self.dockWidgetContents_2)


        self.retranslateUi(DialogAnalysis)
        self.tabWidgetBookMark.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(DialogAnalysis)

    def retranslateUi(self, DialogAnalysis):
        _translate = QtCore.QCoreApplication.translate
        DialogAnalysis.setWindowTitle(_translate("DialogAnalysis", "Analysis"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.geoloctab), _translate("DialogAnalysis", "Geolocation"))
        self.groupBox_7.setTitle(_translate("DialogAnalysis", "Virtualization  Social Network"))
        self.btn_Circular_Layout.setText(_translate("DialogAnalysis", "Circular layout"))
        self.btn_Planer_Layout.setText(_translate("DialogAnalysis", "Planer layout"))
        self.btn_Random_Layout.setText(_translate("DialogAnalysis", "Random layout"))
        self.btn_Special_Layout.setText(_translate("DialogAnalysis", "Spectral layout"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.SocialNetworktab), _translate("DialogAnalysis", "Social networ"))
        self.groupBox_4.setTitle(_translate("DialogAnalysis", "options"))
        self.btnPieChart.setText(_translate("DialogAnalysis", "Pie chart"))
        self.btnBarChart.setText(_translate("DialogAnalysis", "Bar chart"))
        self.checkBox_places.setText(_translate("DialogAnalysis", "Places"))
        self.checkBox_5.setText(_translate("DialogAnalysis", "People"))
        self.checkBox_6.setText(_translate("DialogAnalysis", "Dates"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.statisictap), _translate("DialogAnalysis", "statisic"))
        self.label_5.setText(_translate("DialogAnalysis", "TextLabel"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.tab_tap), _translate("DialogAnalysis", "chat"))
        self.label_10.setText(_translate("DialogAnalysis", "file name"))
        self.label_7.setText(_translate("DialogAnalysis", "from"))
        self.label_15.setText(_translate("DialogAnalysis", "Attachment"))
        self.label_12.setText(_translate("DialogAnalysis", "BCC"))
        self.label_11.setText(_translate("DialogAnalysis", "CC"))
        self.label_13.setText(_translate("DialogAnalysis", "from time"))
        self.label_14.setText(_translate("DialogAnalysis", "To Time"))
        self.fileCommatLabel.setText(_translate("DialogAnalysis", "File commat"))
        self.label_9.setText(_translate("DialogAnalysis", "Path"))
        self.label_8.setText(_translate("DialogAnalysis", "To"))
        self.toolButton.setText(_translate("DialogAnalysis", "..."))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.tab), _translate("DialogAnalysis", "Bookmark"))
        self.dockWidget_analysis.setWindowTitle(_translate("DialogAnalysis", "Analysis bar"))
        self.groupBox_2.setTitle(_translate("DialogAnalysis", "platForm"))
        self.checkBox_Email.setText(_translate("DialogAnalysis", "Email"))
        self.checkBox_WhatsApp.setText(_translate("DialogAnalysis", "WahatApp"))
        self.checkBox_Viber.setText(_translate("DialogAnalysis", "Viber"))
        self.btnKeyWordChat_2.setText(_translate("DialogAnalysis", "Search keyword"))
        self.btnSnapshot.setText(_translate("DialogAnalysis", "Snapshot"))
        self.groupBox_3.setTitle(_translate("DialogAnalysis", "Filter option"))
        self.checkBox_filterKeyWord.setText(_translate("DialogAnalysis", "Filter by  keyword only"))
        self.checkBox_FiterTimeDate.setText(_translate("DialogAnalysis", "Filter by Date and time only"))
        self.btnVerify.setText(_translate("DialogAnalysis", "verify"))
        self.groupBox_5.setTitle(_translate("DialogAnalysis", "Date filtering"))
        self.label_2.setText(_translate("DialogAnalysis", "To date"))
        self.label.setText(_translate("DialogAnalysis", "From date"))
        self.groupBox_6.setTitle(_translate("DialogAnalysis", "Sender recepian"))
        self.label_3.setText(_translate("DialogAnalysis", "Sender"))
        self.label_4.setText(_translate("DialogAnalysis", "recepian"))
        # add completer to the line editor
        name = ['apple', 'ape', 'boo', 'baa', 'bee']
        completer = QtWidgets.QCompleter(name)
        # put the completer in
        self.lineEdit_Recepian.setCompleter(completer)
         # put the completer in
        self.lineEdit_Sender.setCompleter(completer)
        # to date functionality
        self.dateEdit_dateFrom.setCalendarPopup(True)
        self.dateEdit_dateFrom.setMinimumDate(QtCore.QDate(2022, 2, 2))
        self.dateEdit_dateFrom.setMaximumDate(QtCore.QDate(2022, 3, 1))
        self.dateEdit_dateFrom.dateChanged.connect(self.fromlinedittopython)
        self.dateEdit_dateFrom.dateTimeChanged.connect(lambda: method(self))
        # to date functionality
        self.dateEdit_dateTo.setCalendarPopup(True)
        self.dateEdit_dateTo.setMinimumDate(QtCore.QDate(2022, 2, 2))
        self.dateEdit_dateTo.setMaximumDate(QtCore.QDate(2022, 3, 1))
        self.dateEdit_dateTo.dateChanged.connect(self.fromlinedittopython)
        self.dateEdit_dateTo.dateTimeChanged.connect(lambda: method(self))
        # btn screen shot
        self.btnSnapshot.clicked.connect(self.screenshoting)
       
         # btns for socialnetwork
        self.btn_Circular_Layout.clicked.connect(self.curcularlayout)
        self.btn_Planer_Layout.clicked.connect(self.planerlayout)
        self.btn_Random_Layout.clicked.connect(self.randomLayout)
        self.btn_Special_Layout.clicked.connect(self.spectralLayout)
        # btn for statistic
        self.btnBarChart.clicked.connect(self.barchart)
        self.btnPieChart.clicked.connect(self.piechart)
        self.checked()
        def method(self):
            print(self.dateEdit_dateTo.date())

    def fromlinedittopython(self):
        return self.dateEdit_dateTo.date().toPyDate

    def checked(self):
        if self.checkBox_Email.checkState() == 0:
            print('noemail')
        if self.checkBox_Email.checkState() == 2:
            print('email')
        if self.checkBox_WhatsApp.checkState() == 0:
            print('noWATSUP')
        if self.checkBox_WhatsApp.checkState() == 2:
            print(' WATSUP')
        if self.checkBox_WhatsApp.checkState() == 0:
            print('noWATSUP')
        if self.checkBox_Viber.checkState() == 2:
            print('WATSUP')
    def curcularlayout(self):
        self.lbl_Visualization.setPixmap(
            QtGui.QPixmap("C:\\Users\\samar\\Desktop\\finalyearproject\\pythonProject1\\view\\filename1.png"))

    def planerlayout(self):
        self.lbl_Visualization.setPixmap(
            QtGui.QPixmap("C:\\Users\\samar\\Desktop\\finalyearproject\\pythonProject1\\view\\filename2.png"))

    def randomLayout(self):
        self.lbl_Visualization.setPixmap(
            QtGui.QPixmap("C:\\Users\\samar\\Desktop\\finalyearproject\\pythonProject1\\view\\filename3.png"))

    def spectralLayout(self):
        self.lbl_Visualization.setPixmap(
            QtGui.QPixmap("C:\\Users\\samar\\Desktop\\finalyearproject\\pythonProject1\\view\\filename4.png"))

    # btn to draw the stastic
    def piechart(self):
        self.lbl_statistic.setPixmap(
            QtGui.QPixmap("C:\\Users\\samar\\Desktop\\finalyearproject\\pythonProject1\\view\\f.png"))

    def barchart(self):
        self.lbl_statistic.setPixmap(
            QtGui.QPixmap("C:\\Users\\samar\\Desktop\\finalyearproject\\pythonProject1\\view\\barchart.png"))

    def screenshoting(self):
        im = PIL.ImageGrab.grab()
        im.save('snapshot.png')
        im.show()
        fileFilter = 'PNG (*.png)'
        options = QtWidgets.QFileDialog.getSaveFileName(caption='select a file', directory=' ', filter=fileFilter,
                                                        initialFilter='PNG (*.png)')

        if options:
            im.save(str(options))

    def getsavefilename(self):
        fileFilter = 'PNG (*.png)'
        response = QtWidgets.QFileDialog.getSaveFileName(caption='select a file', directory='snapshot.png',
                                                         filter=fileFilter, initialFilter=' JPG (*.png) '
                                                         )
        response = QtWidgets.QFileDialog.DontUseNativeDialog
        response = QtWidgets.QFileDialog.saveFileContent(self.screenshoting)
        return response


    def grapaDate(self):
        self.dateEdit_dateTo.setDate()
        print("ddd")





     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAnalysis = QtWidgets.QDialog()
    ui = Ui_DialogAnalysis()
    ui.setupUi(DialogAnalysis)
    DialogAnalysis.show()
    sys.exit(app.exec_())
