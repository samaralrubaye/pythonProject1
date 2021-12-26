import Model.connection


class viber:
    def __init__(self, viberNamber):
        self._viberOs = ' '
        self._peopleID = ' '
        self.viberNamber =viberNamber
        self.results = []
        ex = Model.connection.conection.mycursor.callproc('viber_proc', [viberNamber, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
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
    def delete_email(self,ID):
        ex = Model.connection.conection.mycursor.callproc('proc_deleteViber', [self.viberNamber])
        Model.connection.conection.mycursor.stored_results()


w = viber(10101010)

print(w.peopleID)