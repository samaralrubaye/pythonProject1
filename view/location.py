import Model.connection
f = open("script.js", "w")  # open the script file

Model.connection.conection.mycursor.execute('SELECT idviber_msg,viber_Latitude, vlongitude FROM viber_msg')
viber_msgs = Model.connection.conection.mycursor.fetchall()


class location :

    def __init__(self ,marker,longitude,latitude ):
        self.longitude=longitude
        self.latitude=latitude
        self.marker=marker



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



    # def addlocation(self):  # define add function that pass the id and the longitude and latitude
    #      global f
    #      self.f.write(" var marker_%d = L.marker([%d,%d],{}).addTo(map_732aa9293105477e92a5a9c8432b1001);"%(self.marker, self.longitude, self.latitude))
    #     # the js script body with passing the variables to it.

def add(marker_ID, longitude, latitude):  # define add function that pass the id and the longitude and latitude

    f.write(" var marker_%d = L.marker([%d,%d],{}).addTo(map_732aa9293105477e92a5a9c8432b1001);"%(marker_ID, longitude, latitude))


loc=[]

for i in range(len(viber_msgs)):
    loc.append(location(int(list(viber_msgs[i])[0]),float(list(viber_msgs[i])[1]),float(list(viber_msgs[i])[2])))
    # loc[i].addlocation()

for i in range(len(loc)):
    add(loc[i].getmarker(), loc[i].getlogtude(), loc[i].getlatitude())

f.close()