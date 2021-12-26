
import Model.connection

class PeoPle:
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




w=PeoPle(5)
print(w.firstName)
print(w.userid)
print(w.lastName)

#w.printing()




