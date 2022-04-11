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
     
        

    def handleItemClick(self, item):
        print(str(item.ID))

    def setMyItem(self, row: int, column: int, item: MyQwidgetItem) -> None: 
        self.setItem(row,column,item)
        
        self.itemClicked.connect(lambda:self.handleItemClick(item))
