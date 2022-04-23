# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\samar\Desktop\finalyearproject\pythonProject1\view\BookMark.2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from datetime import datetime
import os
from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_bookmark(object):
    def setupUi(self, bookmark):
        bookmark.setObjectName("bookmark")
        bookmark.resize(676, 446)
        self.label = QtWidgets.QLabel(bookmark)
        self.label.setGeometry(QtCore.QRect(50, 40, 401, 41))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(bookmark)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 90, 581, 231))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btn_AddNote = QtWidgets.QPushButton(bookmark)
        self.btn_AddNote.setGeometry(QtCore.QRect(70, 350, 93, 28))
        self.btn_AddNote.setObjectName("btn_AddNote")
        self.pushButton = QtWidgets.QPushButton(bookmark)
        self.pushButton.setGeometry(QtCore.QRect(500, 360, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(bookmark)
        QtCore.QMetaObject.connectSlotsByName(bookmark)
        self.btn_AddNote.clicked.connect(self.writeText)
        self.pushButton.clicked.connect(self.hidding)

    def retranslateUi(self, bookmark):
        _translate = QtCore.QCoreApplication.translate
        bookmark.setWindowTitle(_translate("bookmark", "Bookmark note"))
        self.label.setText(_translate("bookmark", "Add note to the bookmark"))
        self.btn_AddNote.setText(_translate("bookmark", "Done"))
        self.pushButton.setText(_translate("bookmark", "Cancle"))
        self.pushButton
    
    def writeText(self):
         desktop = os.path.join(os.path.join(os.environ['USERPROFILE']))
         now = datetime.now()
         now = int(now.strftime("%Y%m%d%H%M%S"))
   
         with open(str(desktop)+'/'+'Desktop/evidance'+'/'+"bookmarknote%d.txt"%now, 'w') as f:
            f.write(self.plainTextEdit.toPlainText())
            print() 
            f.close() 
         bookmark.close()
            
    def hidding(self):
        # bookmark = QtWidgets.QDialog()
        bookmark.close()
    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bookmark = QtWidgets.QDialog()
    ui = Ui_bookmark()
    ui.setupUi(bookmark)
    bookmark.show()
    sys.exit(app.exec_())
