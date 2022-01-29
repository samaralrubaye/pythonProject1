
import connection

class People:
    def __init__(self,  peopleid= None):
        super(People,self).__init__()
        if peopleid == None:
            return

        self._firstName = ''
        self._LastName=''
        self.userid = peopleid
        self.results= []
        ex = connection.conection.mycursor.callproc('people_proc', [peopleid, ])
        connection.conection.mycursor.stored_results()
        for result in connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           self.firstName=str(w[1])
           self.lastName=str(w[2])

    
    def FromData(self,userid, fname, lname):
        ex=People()
        ex.firstName = str(fname)
        ex.lastName = str(lname)
        ex.userid= str(userid)
        return ex




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
   
    def fullName(fname,lname):
        return fname+lname

    def printing(self):
        print(self.firstName)

    def delete_email(self,ID):
        ex = connection.conection.mycursor.callproc('PROC_delete_people', [self._userid])
        connection.conection.mycursor.stored_results()

    def getAllPeople(self):
        allpeople = []
        ex = connection.conection.mycursor.callproc('allpeople_proc')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                allpeople.append(People.FromData(i[0],[1],i[2]))
        return allpeople


#w.printing()




