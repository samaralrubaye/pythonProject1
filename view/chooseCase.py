# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cases.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import examiner
from PyQt5 import QtCore, QtGui, QtWidgets
import examiners
import Examiner
import Model



class Ui_FormCases(object):
    def setupUi(self, FormCases):
        FormCases.setObjectName("FormCases")
        FormCases.resize(825, 320)
        self.label = QtWidgets.QLabel(FormCases)
        self.label.setGeometry(QtCore.QRect(54, 70, 171, 20))
        self.label.setObjectName("label")
        self.lb_examinerName = QtWidgets.QLabel(FormCases)
        self.lb_examinerName.setGeometry(QtCore.QRect(210, 80, 55, 16))
        self.lb_examinerName.setText("")
        self.lb_examinerName.setObjectName("lb_examinerName")
        self.label_3 = QtWidgets.QLabel(FormCases)
        self.label_3.setGeometry(QtCore.QRect(330, 70, 71, 16))
        self.label_3.setObjectName("label_3")
        self.comboBoxcases = QtWidgets.QComboBox(FormCases)
        self.comboBoxcases.setGeometry(QtCore.QRect(40, 160, 721, 22))
        self.comboBoxcases.setObjectName("comboBoxcases")
        cases=[]
        print(Examiner.Ui_Dialog.findExaminerID)
        for i in range(2):
            cases.append(str(Examiner.Ui_Dialog.bein(self)[0][1]))

        self.comboBoxcases.addItems(cases)
        self.ptnNext = QtWidgets.QPushButton(FormCases)
        self.ptnNext.setGeometry(QtCore.QRect(710, 240, 93, 28))
        self.ptnNext.setObjectName("ptnNext")
        self.btnBack = QtWidgets.QPushButton(FormCases)
        self.btnBack.setGeometry(QtCore.QRect(50, 240, 93, 28))
        self.btnBack.setObjectName("btnBack")


        self.retranslateUi(FormCases)
        QtCore.QMetaObject.connectSlotsByName(FormCases)


    def retranslateUi(self, FormCases):
        _translate = QtCore.QCoreApplication.translate
        FormCases.setWindowTitle(_translate("FormCases", "Cases"))
        self.label.setText(_translate("FormCases", "choose one of"))
        self.label_3.setText(_translate("FormCases", "cases"))
        self.ptnNext.setText(_translate("FormCases", "Next"))
        self.btnBack.setText(_translate("FormCases", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormCases = QtWidgets.QWidget()
    ui = Ui_FormCases()
    ui.setupUi(FormCases)
    FormCases.show()
    sys.exit(app.exec_())
