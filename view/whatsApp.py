import connection

class whatsApp:
    def __init__(self, whatsAppNumber=None):
        super(whatsApp,self).__init__()
        if whatsAppNumber == None:
            return
        self._WhatsAppOs = ' '
        self._peopleId =' '
        self.whatsAppNumber = whatsAppNumber
        self.results= []
        ex = connection.conection.mycursor.callproc('whatsup_proc', [whatsAppNumber, ])
        connection.conection.mycursor.stored_results()
        for result in connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           self.WhatsAppOs=str(w[1])
           self.peopleId=str(w[2])

   
    def FromData(self, WhatsAppOs, peopleId):
        ex=whatsApp()
        ex.WhatsAppOs = str(WhatsAppOs)
        ex.peopleId = str(peopleId)
        return ex


    @property
    def WhatsAppOs(self):
        return self._WhatsAppOs

    @WhatsAppOs.setter
    def WhatsAppOs(self,value):
        self._WhatsAppOs=value


    @property
    def peopleId(self):
        return self._peopleId
    @peopleId.setter
    def peopleId(self,value):
        self._peopleId=value
    @property
    def whatsAppNumber(self):
        return self._whatsAppNumber
    @whatsAppNumber.setter
    def whatsAppNumber(self,value):
        self._whatsAppNumber=value

    def delete_vibermsg(self, ID):
        ex = connection.conection.mycursor.callproc('proc_deletwhatsup', [self.whatsAppNumber, ])
        connection.conection.mycursor.stored_results()


    def getAllWhatsApp(self):
        AllWhatsApp=[]
        ex = connection.conection.mycursor.callproc('allWhatApp')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                AllWhatsApp.append(whatsApp.FromData(self,i[0],i[1]))

        return AllWhatsApp

