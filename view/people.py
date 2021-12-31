
import Model.connection

class People:
    def __init__(self,  peopleid):
        self._firstName = ''
        self._LastName=''
        self.userid = peopleid
        self.results= []
        ex = Model.connection.conection.mycursor.callproc('people_proc', [peopleid, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           self.firstName=str(w[1])
           self.lastName=str(w[2])

    @classmethod
    def FromData(cls, fname, lname):
        cls.firstName = str(fname)
        cls.lastName = str(lname)
        return cls




    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self,value):
        self._firstName=value


    @property
    def lastName(self):
        return self._LastName
    @lastName.setter
    def lastName(self,value):
        self._LastName=value
    @property
    def peopleid(self):
        return self._peopleid
    @peopleid.setter
    def peopleid(self,value):
        self._peopleid=value

    def printing(self):
        print(self.firstName)

    def delete_email(self,ID):
        ex = Model.connection.conection.mycursor.callproc('PROC_delete_people', [self._peopleid])
        Model.connection.conection.mycursor.stored_results()

    def getAllPeople(self):
        allpeople = []
        ex = Model.connection.conection.mycursor.callproc('Examiners')

        for result in Model.connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                allpeople.append(People.FromData(i[0], i[1]))
        return allpeople


#w.printing()




