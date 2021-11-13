

import Model.connection

lists=[]
class location:


    def __init__(self ,longitude,latitude, marker):
        self.longitude=longitude
        self.latitude=latitude
        self.marker=marker
        self.f = open("script.js", "w")  # open the script file

    Model.connection.conection.mycursor.execute('SELECT idviber_msg,viber_Latitude, vlongitude FROM viber_msg')
    viber_msgs = Model.connection.conection.mycursor.fetchall()

    #lists = list(viber_msgs)

        # for email in emails:

    #print(lists)


    #for i in range(len(lists)):
      #  print(lists[0][0])
       # print(lists[0][1])
       # print(lists[0][2])



    def getlogtude(self):
        return self.longitude
    def getlatitude(self):
        return self.latitude
    def getmarker(self):
        return self.marker



    def addlocation(self):  # define add function that pass the id and the longitude and latitude

         self.f.write(" var marker_%d = L.marker([%d,%d],{}).addTo(map_732aa9293105477e92a5a9c8432b1001);"%(self.marker, self.longitude, self.latitude))
        # the js script body with passing the variables to it.


loc=[]
lists=Model.connection.conection.viber_msgs
print(lists)
#loc= location(3.333333,4.444444,5.343)
print(len(lists))
print(type(lists))
for i in range(len(lists)):
    loc.append(location(lists[i][0],lists[i][1], lists[i][2]))
    print(loc[i].longitude())


#laca=location()

#loc=location(3.3333333,4.44444,5.55555)

#loc.addlocation()
#print(loc.getlatitude())
#print(loc.getlogtude())
#print(loc.getmarker())


#loc.f.close()
