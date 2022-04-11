from PyQt5.QtWidgets import *

class MyQwidgetItem(QTableWidgetItem):
    

    @property
    def ID(self):
        return self.id

    @ID.setter
    def ID(self, value):
        self.id = value