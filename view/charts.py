
import matplotlib.pyplot as plt
 

class graphics:
    
         
    def piechart(self, Tasksss,my_labels):
        plt.pie(Tasksss,labels=my_labels,autopct='%1.1f%%')
        plt.title('My Tasks')
        plt.axis('equal')
        plt.show()

g=graphics()
Tasksss = [300,500,700]
my_labels = ['Tasks Pending','Tasks Ongoing','Tasks Completed']

#g.piechart(Tasksss, my_labels)