import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)
import sys
from turtle import pd
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        # Create a QGridLayout instance
        layout = QGridLayout()
        # Add widgets to the layout
        # constructor
   

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to 'plot' method
        self.button = QPushButton('Plot')
        # Just some button connected to 'plot' method
        self.button2 = QPushButton('Plot2')

        # adding action to the button
        self.button.clicked.connect(self.plot)
        # adding action to the button
        self.button2.clicked.connect(self.plot2)

        # creating a Vertical Box layout
       

        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        layout.addWidget(self.button)
      # adding push button to the layout
        layout.addWidget(self.button2)

        # setting layout to the main window
        layout.addWidget(self.canvas, 0, 0, 0, 1 ,0,2)
        layout.addWidget(QPushButton("Button at (0, 0)"), 5, 0)
        layout.addWidget(QPushButton("Button2 at (0, 1)"), 5, 1)
       
        # Set the layout on the application's window
        self.setLayout(layout)

    # action called by the push button
    def plot(self):
          Country = ['USA','Canada','Germany','UK','France']
          GDP_Per_Capita = [45000,42000,52000,49000,47000]
          # clearing old figure
          self.figure.clear()
          New_Colors = ['green','blue','purple','brown','teal']
          plt.bar(Country, GDP_Per_Capita, color=New_Colors)
          plt.title('Amount of suspsous comunication per country', fontsize=14)
          plt.xlabel('Country', fontsize=14)
          plt.ylabel('Comunication messages/Emails', fontsize=14)
          plt.grid(True)
          # put the figure inside the canavas
          self.canvas.draw()
    # action called by the push button
   
    def plot2(self):
         Tasks = [300,500,700]
         # clearing old figure
         self.figure.clear()
         my_labels = 'Tasks Pending','Tasks Ongoing','Tasks Completed'
         plt.pie(Tasks,labels=my_labels,autopct='%1.1f%%')
         plt.title('My Tasks')
         plt.axis('equal')
         # put the figure inside the canavas
         self.canvas.draw()


       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())