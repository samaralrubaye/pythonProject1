import networkx as nx
import matplotlib.pyplot as plt

import warnings; warnings.simplefilter('ignore')
class SocialNetwork:

    def __init__(self,senderFirstName,SenerLastName,recepianFisrtName, RecepianLastName):
       self.senderFirstNam = senderFirstName
       self.SenerLastName = SenerLastName
       self.recepianFisrtName = recepianFisrtName
       self.RecepianLastName = RecepianLastName

    def theSenderName(self):
        return self.senderFirstNam + self.SenerLastName

    def therecepianName(self):
        return self.recepianFisrtName + self.RecepianLastName

    def Gettinginfo(self):
        G_symmetric = nx.Graph()
        G_symmetric.add_edge(sn.theSenderName(), sn.therecepianName())
        return G_symmetric
    def drawNetwork(self):
         nx.info(sn.Gettinginfo())
         plt.figure(figsize=(5, 5))
         nx.draw_networkx(sn.Gettinginfo())
         plt.show()
         plt.savefig("filename.png")
         plt.clf()





    # drawing in circular layout
    def draw_circlar(self):
        nx.draw_circular(sn.Gettinginfo(), with_labels=True)
        plt.savefig("filename1.png")



    # drawing in planar layout
    def drawplanar(self):
        nx.draw_planar(sn.Gettinginfo(), with_labels=True)
        plt.savefig("filename2.png")



    # drawing in random layout
    def draw_random(self):
        nx.draw_random(sn.Gettinginfo(), with_labels=True)
        plt.savefig("filename3.png")



    # drawing in spectral layout
    def draw_spectral(self):
        nx.draw_spectral( sn.Gettinginfo(), with_labels=True)
        plt.savefig("filename4.png")





    def Digraph(self):
        G_asymmetric = nx.DiGraph()
        G_asymmetric.add_edge('v','z')
    def drawdraw(self):
        nx.spring_layout(sn.Digraph())
        nx.draw_networkx(sn.Digraph())



    # drawing in circular layout
    def Circular_layout(self):
        nx.draw_circular(sn.Digraph(), with_labels=True)
        plt.savefig("filename7.png")

    # clearing the current plot
    plt.clf()

    # drawing in planar layout
    def planner_layout(self):
        nx.draw_planar(sn.Digraph(), with_labels=True)
        plt.savefig("filename8.png")

    # clearing the current plot
    plt.clf()

    # drawing in random layout
    def random_layout(self):
        nx.draw_random(sn.Digraph(), with_labels=True)
        plt.savefig("filename9.png")

    # clearing the current plot
    plt.clf()

    # drawing in spectral layout
    def specral_Layout(self):
        nx.draw_spectral(sn.Digraph(), with_labels=True)
        plt.savefig("filename10.png")
    def clearingPlot(self):
    # clearing the current plot
        plt.clf()

    # drawing in spring layout
    def draw_spring(self):
        nx.draw_spring(sn.Digraph(), with_labels=True)
        plt.savefig("filename15.png")



    # drawing in shell layout
    def shell_layout(self):
        nx.draw_shell(sn.Digraph(), with_labels=True)
        plt.savefig("filename16.png")

    # clearing the current plot
    plt.clf()
sn= SocialNetwork("qqq","dfdf","EEEE","gggg")
print(sn.theSenderName())
print(sn.therecepianName())
print(sn.Gettinginfo())
print(sn.drawNetwork())
print(sn.draw_circlar())
print(sn.draw_random())
print(sn.draw_spectral())
print(sn.drawplanar())
print(sn.Digraph())
print(sn.drawdraw())
#print(sn.planner_layout())
#print(sn.random_layout())
#print(sn.shell_layout())
#print(sn.specral_Layout())


