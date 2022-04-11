import connection
class vibersummary:
    def __init__(self):
        self._firstName=''
        self._lastName=''
        self._viberNumbr=''
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
    def ViberNumbr(self):
            return self._viberNumbr

    @ViberNumbr.setter
    def ViberNumbr(self, value):
            self._viberNumbr= value
        
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
        


    def FromData(self, firstNme,lastName, viberNumbr,senderCount,recepiantcount ):
            v=vibersummary()
            v.FirstName = str(firstNme)
            v.LastName= str(lastName)
            v.ViberNumbr=str(viberNumbr)
            v.SenderCount=str(senderCount)
            v.Recepiantcount=str(recepiantcount)
            return v
        

    def getAllViberSummary(self,caseid, datefrom,dateto, textcontent,txtsender,txtresipain):
            Viberarray=[]
            ex = connection.conection.mycursor.callproc('vberSummery',[textcontent,datefrom,dateto,caseid,txtsender,txtresipain])

            for result in connection.conection.mycursor.stored_results():
                for i in result.fetchall():
                    Viberarray.append(vibersummary.FromData(self,i[0],i[1],i[2],i[3],i[4])) 
            return Viberarray