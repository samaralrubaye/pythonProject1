import connection
class whatsAppsummary:
    def __init__(self):
        self._firstName=''
        self._lastName=''
        self._whatsApp=''
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
    def WhatsApp(self):
            return self._whatsApp

    @WhatsApp.setter
    def WhatsApp(self, value):
            self._whatsApp= value
        
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
        


    def FromData(self, firstNme,lastName, whatsApp,senderCount,recepiantcount ):
            v=whatsAppsummary()
            v.FirstName = str(firstNme)
            v.LastName= str(lastName)
            v.WhatsApp=str(whatsApp)
            v.SenderCount=str(senderCount)
            v.Recepiantcount=str(recepiantcount)
            return v
        

    def getAllemailSummary(self,caseid):
            whatsaooarray=[]
            ex = connection.conection.mycursor.callproc('whatsappSummery',[caseid])

            for result in connection.conection.mycursor.stored_results():
                for i in result.fetchall():
                    whatsaooarray.append(whatsAppsummary.FromData(self,i[0],i[1],i[2],i[3],i[4])) 
            return whatsaooarray
