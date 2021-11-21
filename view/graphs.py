import numpy as np
from numpy.random import rand
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import Model.connection
import viber

class graph:
    list=[]
    df=pd.read_sql('SELECT msgdates FROM dataforensic.viber_msg', con=Model.connection.conection.mydb)
    rf=pd.DataFrame(df)
    print('kk',rf.values.tolist())
    def inputx(self):
        x=[1,2,3,5]
        return x
    def inputy(self):
        y = [2000, 300, 4000, 400]
        return y

   # plt.plot(x,y)
   # plt.savefig('dd.png')
    def barchart(self):
        plt.bar(g.inputx(), g.inputy())
        plt.savefig('barchart.png')
    def piechart(self):
        plt.pie(g.inputx())
        plt.savefig('f.png')

g=graph()


g.barchart()
g.piechart()





