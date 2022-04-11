import connection
class emailsummary:
    def __init__(self):
        self._firstName=''
        self._lastName=''
        self._email=''
        self._senderCount=''
        self._recepiantcount=''

    @property
    def FirstName(self):
        return self._firstName

    @FirstName.setter
    def FirstName (self, value):
        self._firstName= value
        

    @property
    def LastName(self):
        return self._lastName

    @LastName.setter
    def LastName(self, value):
             self._lastName= value
        
    @property
    def Email(self):
            return self._email

    @Email.setter
    def Email(self, value):
            self._email= value
        
    @property
    def SenderCount(self):
            return self._senderCount

    @SenderCount.setter
    def SenderCount(self, value):
             self._senderCount= value
        

    @property
    def Recepiantcount(self):
            return self._recepiantcount

    @Recepiantcount.setter
    def Recepiantcount(self, value):
             self._recepiantcount= value
        


    def FromData(self, firstNme,lastName, email,senderCount,recepiantcount ):
            v=emailsummary()
            v.FirstName = str(firstNme)
            v.LastName= str(lastName)
            v.Email=str(email)
            v.SenderCount=str(senderCount)
            v.Recepiantcount=str(recepiantcount)
            return v
        

    def getAllemailSummary(self,caseid, datefrom,dateto, textcontent,txtsender,txtresipain):
            emailarray=[]
            ex = connection.conection.mycursor.callproc('emailSummery',[textcontent,datefrom,dateto,caseid,txtsender,txtresipain])

            for result in connection.conection.mycursor.stored_results():
                for i in result.fetchall():
                    emailarray.append(emailsummary.FromData(self,i[0],i[1],i[2],i[3],i[4])) 
            return emailarray