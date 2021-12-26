import Model.connection

class ExaMiners:
    def __init__(self,  userid):
        self._firstName = ''
        self._LastName=''
        self.userid = userid
        self.results= []
        ex = Model.connection.conection.mycursor.callproc('examiners_proc', [userid, ])
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
    def userId(self):
        return self.userid
    @userId.setter
    def userId(self,value):
        self.userid=value

    def printing(self):
        print(self.firstName)

    # mycursor.execute('SELECT idviber_msg,viber_Latitude, vlongitude FROM viber_msg')
    def Details(self):
        w = Model.connection.conection.mycursor.callproc('procExaminerDetails')
        Model.connection.conection.mycursor.stored_results()

        for result in Model.connection.conection.mycursor.stored_results():
            temp = result.fetchall()
            return temp

    def fulName(self,fname, lastname):
         return w.firstName+" "+w.lastName

    def bein(self,ID):
       w = Model.connection.conection.mycursor.callproc('casesforinvestigators',[self.userid,])
       Model.connection.conection.mycursor.stored_results()
       cases = []
       mf = []
       for result in Model.connection.conection.mycursor.stored_results():
           temp = result.fetchall()
           return temp

    def createNewExaminer(self,fname,lname):
        ex = Model.connection.conection.mycursor.callproc('proc_addExaminer', [self.firstName,self.lastName])
        Model.connection.conection.mycursor.stored_results()

    def update_Examiner(self,ID,fname,lname):
        ex = Model.connection.conection.mycursor.callproc('proc_updateExaminer', [self.userid,self.firstName,self.lastName])
        Model.connection.conection.mycursor.stored_results()

    def delete_Examiner(self,ID):
        ex = Model.connection.conection.mycursor.callproc('deleteviber_proc', [self.userid,])
        Model.connection.conection.mycursor.stored_results()




w=ExaMiners(456)
print(w.firstName)
print(w.userid)
print(w.lastName)
print(w.fulName)
#w.printing()



