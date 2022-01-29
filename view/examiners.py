import connection
#from PYTHONPROJECT1.Model import connection
#import sys
#sys.path.append('\Users\samar\Desktop\finalyearproject\pythonProject1\Model')

class ExaMiners:
    def __init__(self,  userid =None):
        super(ExaMiners,self).__init__()
        if userid == None:
            return
        self._firstName = ''
        self._LastName=''
        self.userid = userid
        self._examinerPassword=' '
        self.results= []
        ex = connection.conection.mycursor.callproc('examiners_proc', [userid, ])
        connection.conection.mycursor.stored_results()
        for result in connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           self.firstName=str(w[1])
           self.lastName=str(w[2])
           self.password= str(w[3])




       

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
        return self._userid
    @userId.setter
    def userId(self,value):
        self._userid=value
    
    @property
    def examinerPassword(self):
        return self._examinerPassword
    
    @examinerPassword.setter
    def examinerPassword(self,value):
        self._examinerPassword=value

    def printing(self):
        print(self.firstName)

    # mycursor.execute('SELECT idviber_msg,viber_Latitude, vlongitude FROM viber_msg')
    def Details(self):
        w = connection.conection.mycursor.callproc('procExaminerDetails')
        connection.conection.mycursor.stored_results()

        for result in connection.conection.mycursor.stored_results():
            temp = result.fetchall()
            return temp

    def fulName(self):
         return self.firstName+" "+self.lastName
    print(fulName)
    

    def createNewExaminer(self,fname,lname):
        ex = connection.conection.mycursor.callproc('proc_addExaminer', [self.firstName,self.lastName])
        connection.conection.mycursor.stored_results()

    def update_Examiner(self,ID,fname,lname):
        ex = connection.conection.mycursor.callproc('proc_updateExaminer', [self.userid,self.firstName,self.lastName, self.examinerPassword])
        connection.conection.mycursor.stored_results()

    def delete_Examiner(self,ID):
        ex = connection.conection.mycursor.callproc('deleteviber_proc', [self.userid,])
        connection.conection.mycursor.stored_results()

    def fromData(self,fname,lname,id):
        ex= ExaMiners()
        ex.firstName = str(fname)
        ex.lastName = str(lname)
        ex.userId = id

        return ex


    def getAllExaminers(self):
        examiners=[]
        ex = connection.conection.mycursor.callproc('Examiners')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                examiners.append(ExaMiners.fromData(self,i[0],i[1],i[2]))

        return examiners
    
    def anotherlogin(self,  name,examinerPassword):
     
         args =[name,examinerPassword]
         w = connection.conection.mycursor.callproc('ExaminerLogINproc', args)
         connection.conection.mycursor.stored_results()
         
         ex = ExaMiners()

         for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                ex = ExaMiners.fromData(self,i[1],i[2],i[0])
             
         return ex
      
           






    