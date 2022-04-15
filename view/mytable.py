from typing import overload
from PyQt5.QtWidgets import *


from MyQwidgetItem import MyQwidgetItem

class MyTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(400)
        self.setColumnCount(1)
        self.setColumnWidth(0, 400)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.itemClicked.connect(self.handleItemClick)
        

    def handleItemClick(self, item):
        try:
             print(str(item.ID))
        except:
            print('tt')
        
       
    #     self.cellClicked.connect(lambda:self.cell_was_clicked(self.currentRow(),self.currentColumn()))
    #     print(type(self.currentRow()))
    #     print(type(self.currentColumn()))
  

    # def cell_was_clicked(self, row, column):
    #         item = self.itemAt(self,row, column)
    #         print(type(self.currentRow()))
    #         print(type(self.currentColumn()))
    #         self.ID = item.text()
        
