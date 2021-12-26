from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QDateTimeEdit

import Analysis4



class functionality:
    sender_combobox = QtWidgets.QLineEdit(Analysis4.Ui_MainWindow)
    sender_combobox.setGeometry(QtCore.QRect(110, 70, 211, 22))
    dates = ['10-04-2020 ', '2020-04-10', '2020-04-10 12:47:00']
    sender_combobox.addItems(dates)
    cal = QDateTimeEdit()
    cal.setCalendarPopup(True)
    cal.setDisplayFormat("dd-mm-yy")
    cal.calendarWidget().setLocale(QLocale(QLocale.English))

    dateedit = QtWidgets.QDateEdit(calendarPopup=True)
    dateedit.setGeometry(QtCore.QRect(110, 70, 211, 22))
    dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
