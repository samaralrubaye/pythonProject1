import connection


class viber:
    def __init__(self, viberNamber=None):
        super(viber,self).__init__()
        if viberNamber == None:
            return
        self._viberOs = ' '
        self._peopleID = ' '
        self.viberNamber =viberNamber
        self.results = []
        ex = connection.conection.mycursor.callproc('viber_proc', [viberNamber, ])
        connection.conection.mycursor.stored_results()
        for result in connection.conection.mycursor.stored_results():
            w = result.fetchall()[0]
            self.viberOs = str(w[1])
            self.peopleID = str(w[2])

  


    @property
    def viberOs(self):
        return self._viberOs

    @viberOs.setter
    def viberOs(self, value):
        self._viberOs = value

    @property
    def peopleID(self):
        return self._peopleID

    @peopleID.setter
    def peopleID(self, value):
        self._peopleID = value

    @property
    def viberNamber(self):
        return self._viberNamber

    @viberNamber.setter
    def viberNamber(self, value):
        self._viberNamber = value
    def delete_viber(self,ID):
        ex = connection.conection.mycursor.callproc('proc_deleteViber', [self.viberNamber])
        connection.conection.mycursor.stored_results()
  
    def FromData(self,viberOs ,peopleID ):
        ex=viber()
        ex.viberOs = str(viberOs)
        ex.peopleID = str(peopleID)
        return ex

    def getAllVibers(self):
        Vibers=[]
        ex = connection.conection.mycursor.callproc('allvibers_proc')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                Vibers.append(viber.FromData(self,i[0],i[1]))

        return Vibers
    def selectAllViber(self):
        ex = connection.conection.mycursor.callproc('selectALLViber')
        connection.conection.mycursor.stored_results()
        


