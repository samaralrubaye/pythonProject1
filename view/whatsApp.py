import Model.connection

class whatsApp:
    def __init__(self, whatsAppNumber):
        self._WhatsAppOs = ' '
        self._peopleId =' '
        self.whatsAppNumber = whatsAppNumber
        self.results= []
        ex = Model.connection.conection.mycursor.callproc('whatsup_proc', [whatsAppNumber, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           self.WhatsAppOs=str(w[1])
           self.peopleId=str(w[2])



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
        ex = Model.connection.conection.mycursor.callproc('proc_deletwhatsup', [self.whatsAppNumber, ])
        Model.connection.conection.mycursor.stored_results()




w = whatsApp(11111111)
print(w.peopleId)