# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\samar\Desktop\finalyearproject\pythonProject1\view\analysisnew.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAnalysis(object):
    def setupUi(self, DialogAnalysis):
        DialogAnalysis.setObjectName("DialogAnalysis")
        DialogAnalysis.resize(1477, 1003)
        self.tabWidgetBookMark = QtWidgets.QTabWidget(DialogAnalysis)
        self.tabWidgetBookMark.setGeometry(QtCore.QRect(290, 0, 1201, 941))
        self.tabWidgetBookMark.setStyleSheet("border-left-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"selection-color: rgb(170, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.tabWidgetBookMark.setObjectName("tabWidgetBookMark")
        self.geoloctab = QtWidgets.QWidget()
        self.geoloctab.setObjectName("geoloctab")
        self.tabWidgetBookMark.addTab(self.geoloctab, "")
        self.SocialNetworktab = QtWidgets.QWidget()
        self.SocialNetworktab.setObjectName("SocialNetworktab")
        self.tabWidgetBookMark.addTab(self.SocialNetworktab, "")
        self.statisictap = QtWidgets.QWidget()
        self.statisictap.setObjectName("statisictap")
        self.tabWidgetBookMark.addTab(self.statisictap, "")
        self.chat_tap = QtWidgets.QWidget()
        self.chat_tap.setObjectName("chat_tap")
        self.tableWidget = QtWidgets.QTableWidget(self.chat_tap)
        self.tableWidget.setGeometry(QtCore.QRect(0, -30, 1161, 921))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tabWidgetBookMark.addTab(self.chat_tap, "")
        self.tab_bookmark = QtWidgets.QWidget()
        self.tab_bookmark.setObjectName("tab_bookmark")
        self.tabWidgetBookMark.addTab(self.tab_bookmark, "")
        self.dockWidget_analysis = QtWidgets.QDockWidget(DialogAnalysis)
        self.dockWidget_analysis.setGeometry(QtCore.QRect(0, 0, 295, 941))
        self.dockWidget_analysis.setStyleSheet("\n"
        "alternate-background-color: rgb(243, 247, 255);\n"
          "")
        self.dockWidget_analysis.setObjectName("dockWidget_analysis")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 370, 211, 151))
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
        self.lineEdit_serchKeyWord_ForChat.setGeometry(QtCore.QRect(110, 60, 161, 31))
        self.lineEdit_serchKeyWord_ForChat.setObjectName("lineEdit_serchKeyWord_ForChat")
        self.btnKeyWordChat_2 = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnKeyWordChat_2.setGeometry(QtCore.QRect(10, 60, 111, 31))
        self.btnKeyWordChat_2.setStyleSheet("background-color: rgb(222, 223, 255);")
        self.btnKeyWordChat_2.setObjectName("btnKeyWordChat_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 530, 221, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_filterKeyWord = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_filterKeyWord.setGeometry(QtCore.QRect(10, 20, 201, 20))
        self.checkBox_filterKeyWord.setObjectName("checkBox_filterKeyWord")
        self.checkBox_FiterTimeDate = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_FiterTimeDate.setGeometry(QtCore.QRect(10, 40, 171, 20))
        self.checkBox_FiterTimeDate.setObjectName("checkBox_FiterTimeDate")
        self.checkBox_senderRecipeant = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_senderRecipeant.setGeometry(QtCore.QRect(10, 60, 201, 20))
        self.checkBox_senderRecipeant.setObjectName("checkBox_senderRecipeant")
        self.btnVerify = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnVerify.setGeometry(QtCore.QRect(10, 740, 211, 41))
        self.btnVerify.setStyleSheet("background-color: rgb(222, 223, 255);")
        self.btnVerify.setObjectName("btnVerify")
        self.groupBox_5 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 260, 271, 101))
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
        self.groupBox_6.setGeometry(QtCore.QRect(20, 130, 241, 80))
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
        self.label_casename.setGeometry(QtCore.QRect(100, 30, 81, 20))
        self.label_casename.setText("")
        self.label_casename.setObjectName("label_casename")
        self.label_6 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_6.setGeometry(QtCore.QRect(40, 30, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_13.setGeometry(QtCore.QRect(200, 30, 55, 16))
        self.label_13.setObjectName("label_13")
        self.btnSnapshot = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnSnapshot.setGeometry(QtCore.QRect(10, 640, 211, 41))
        self.btnSnapshot.setStyleSheet("background-color: rgb(222, 223, 255);")
        self.btnSnapshot.setObjectName("btnSnapshot")
        self.btnClear = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnClear.setGeometry(QtCore.QRect(10, 690, 211, 41))
        self.btnClear.setAutoFillBackground(False)
        self.btnClear.setStyleSheet("background-color: rgb(222, 223, 255);\n"
        "")
        self.btnClear.setObjectName("btnClear")
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 800, 211, 41))
        self.pushButton.setStyleSheet("background-color: rgb(222, 223, 255);")
        self.pushButton.setObjectName("pushButton")
        self.dockWidget_analysis.setWidget(self.dockWidgetContents_2)

        self.retranslateUi(DialogAnalysis)
        self.tabWidgetBookMark.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(DialogAnalysis)

    def retranslateUi(self, DialogAnalysis):
        _translate = QtCore.QCoreApplication.translate
        DialogAnalysis.setWindowTitle(_translate("DialogAnalysis", "Dialog"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.geoloctab), _translate("DialogAnalysis", "Geolocation"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.SocialNetworktab), _translate("DialogAnalysis", "Social networ"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.statisictap), _translate("DialogAnalysis", "statisic"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DialogAnalysis", "Sender first name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DialogAnalysis", "Sender last name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DialogAnalysis", "Recepiant number"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("DialogAnalysis", "Reciepiant first name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("DialogAnalysis", "Recipeant last name "))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("DialogAnalysis", "Text message"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.chat_tap), _translate("DialogAnalysis", "chat"))
        self.tabWidgetBookMark.setTabText(self.tabWidgetBookMark.indexOf(self.tab_bookmark), _translate("DialogAnalysis", "Bookmark"))
        self.dockWidget_analysis.setWindowTitle(_translate("DialogAnalysis", "Analysis bar"))
        self.groupBox_2.setTitle(_translate("DialogAnalysis", "plat form"))
        self.radioButtonEmail.setText(_translate("DialogAnalysis", "Email"))
        self.radioButton_whatsApp.setText(_translate("DialogAnalysis", "WhatsApp"))
        self.radioButton_viber.setText(_translate("DialogAnalysis", "Viber"))
        self.btnKeyWordChat_2.setText(_translate("DialogAnalysis", "Search keyword"))
        self.groupBox_3.setTitle(_translate("DialogAnalysis", "Filter option"))
        self.checkBox_filterKeyWord.setText(_translate("DialogAnalysis", "Filter by  keyword only"))
        self.checkBox_FiterTimeDate.setText(_translate("DialogAnalysis", "Filter by Date and time only"))
        self.checkBox_senderRecipeant.setText(_translate("DialogAnalysis", "Filter by sender and recipiant"))
        self.btnVerify.setText(_translate("DialogAnalysis", "verify"))
        self.groupBox_5.setTitle(_translate("DialogAnalysis", "Date filtering"))
        self.label_2.setText(_translate("DialogAnalysis", "To date"))
        self.label.setText(_translate("DialogAnalysis", "From date"))
        self.groupBox_6.setTitle(_translate("DialogAnalysis", "Sender recepiant"))
        self.label_3.setText(_translate("DialogAnalysis", "Sender"))
        self.label_4.setText(_translate("DialogAnalysis", "recepiant"))
        self.label_6.setText(_translate("DialogAnalysis", "This is"))
        self.label_13.setText(_translate("DialogAnalysis", "case!"))
        self.btnSnapshot.setText(_translate("DialogAnalysis", "add evedence Item"))
        self.btnClear.setText(_translate("DialogAnalysis", "clear"))
        self.pushButton.setText(_translate("DialogAnalysis", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAnalysis = QtWidgets.QDialog()
    ui = Ui_DialogAnalysis()
    ui.setupUi(DialogAnalysis)
    DialogAnalysis.show()
    sys.exit(app.exec_())
