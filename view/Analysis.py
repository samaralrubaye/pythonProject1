# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(754, 544)
        self.ToDateTime = QtWidgets.QDateTimeEdit(Dialog)
        self.ToDateTime.setGeometry(QtCore.QRect(350, 70, 194, 22))
        self.ToDateTime.setObjectName("ToDateTime")
        self.FromDateTme = QtWidgets.QDateTimeEdit(Dialog)
        self.FromDateTme.setGeometry(QtCore.QRect(90, 70, 194, 22))
        self.FromDateTme.setObjectName("FromDateTme")
        self.degreeDistributionSpinBox = QtWidgets.QSpinBox(Dialog)
        self.degreeDistributionSpinBox.setGeometry(QtCore.QRect(170, 130, 251, 22))
        self.degreeDistributionSpinBox.setObjectName("degreeDistributionSpinBox")
        self.lnKeyword = QtWidgets.QLineEdit(Dialog)
        self.lnKeyword.setGeometry(QtCore.QRect(90, 20, 201, 31))
        self.lnKeyword.setObjectName("lnKeyword")
        self.Btn_Disply = QtWidgets.QPushButton(Dialog)
        self.Btn_Disply.setGeometry(QtCore.QRect(220, 440, 111, 41))
        self.Btn_Disply.setObjectName("Btn_Disply")
        self.Btn_Verify = QtWidgets.QPushButton(Dialog)
        self.Btn_Verify.setGeometry(QtCore.QRect(20, 440, 151, 41))
        self.Btn_Verify.setObjectName("Btn_Verify")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 70, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 70, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 240, 131, 141))
        self.groupBox.setObjectName("groupBox")
        self.checkBoxEmail = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxEmail.setGeometry(QtCore.QRect(10, 20, 121, 20))
        self.checkBoxEmail.setObjectName("checkBoxEmail")
        self.checkBox_Viber = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Viber.setGeometry(QtCore.QRect(10, 60, 81, 20))
        self.checkBox_Viber.setObjectName("checkBox_Viber")
        self.checkBox_whatsapp = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_whatsapp.setGeometry(QtCore.QRect(10, 110, 91, 20))
        self.checkBox_whatsapp.setObjectName("checkBox_whatsapp")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 125, 141, 31))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 250, 261, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_KeyWord = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_KeyWord.setGeometry(QtCore.QRect(10, 20, 191, 20))
        self.checkBox_KeyWord.setObjectName("checkBox_KeyWord")
        self.checkBox_DataTime = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_DataTime.setGeometry(QtCore.QRect(10, 60, 171, 20))
        self.checkBox_DataTime.setObjectName("checkBox_DataTime")
        self.checkBox_DegreeOfDistirbution = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_DegreeOfDistirbution.setGeometry(QtCore.QRect(10, 100, 211, 20))
        self.checkBox_DegreeOfDistirbution.setObjectName("checkBox_DegreeOfDistirbution")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(280, 190, 31, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_Sender = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Sender.setGeometry(QtCore.QRect(80, 190, 181, 22))
        self.lineEdit_Sender.setObjectName("lineEdit_Sender")
        self.lineEdit_recepian = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_recepian.setGeometry(QtCore.QRect(330, 190, 201, 22))
        self.lineEdit_recepian.setObjectName("lineEdit_recepian")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(510, 260, 141, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioGioLocation = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioGioLocation.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.radioGioLocation.setObjectName("radioGioLocation")
        self.radioPlotGraphic = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioPlotGraphic.setGeometry(QtCore.QRect(10, 50, 111, 20))
        self.radioPlotGraphic.setObjectName("radioPlotGraphic")
        self.radioSocialNetwork = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioSocialNetwork.setGeometry(QtCore.QRect(10, 90, 131, 20))
        self.radioSocialNetwork.setObjectName("radioSocialNetwork")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Btn_Disply.setText(_translate("Dialog", "Disply"))
        self.Btn_Verify.setText(_translate("Dialog", "Verify the Data"))
        self.label.setText(_translate("Dialog", "From"))
        self.label_2.setText(_translate("Dialog", "To"))
        self.label_3.setText(_translate("Dialog", "Keyword"))
        self.groupBox.setTitle(_translate("Dialog", "PlatForm"))
        self.checkBoxEmail.setText(_translate("Dialog", "Email"))
        self.checkBox_Viber.setText(_translate("Dialog", "Viber"))
        self.checkBox_whatsapp.setText(_translate("Dialog", "WhatsAAP"))
        self.label_4.setText(_translate("Dialog", "Degree of distribution"))
        self.groupBox_2.setTitle(_translate("Dialog", "Filter Options"))
        self.checkBox_KeyWord.setText(_translate("Dialog", "Filter Keyword "))
        self.checkBox_DataTime.setText(_translate("Dialog", "Filter Date and Time"))
        self.checkBox_DegreeOfDistirbution.setText(_translate("Dialog", "Filter the Degree of the disterbutiob"))
        self.label_5.setText(_translate("Dialog", "From"))
        self.label_6.setText(_translate("Dialog", "To"))
        self.groupBox_3.setTitle(_translate("Dialog", "Disply options"))
        self.radioGioLocation.setText(_translate("Dialog", "Geolocation"))
        self.radioPlotGraphic.setText(_translate("Dialog", " Plot a graph"))
        self.radioSocialNetwork.setText(_translate("Dialog", "Social Network"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())