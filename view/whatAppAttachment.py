import Model.connection

class whatsAppAtachment:
    def __init__(self,  whatsAppAtachmentID):
        self._type = ''
        self._file=''
        self._whatsAppMsgID=' '
        self.whatsAppAtachmentID = whatsAppAtachmentID
        self.results= []
        ex = Model.connection.conection.mycursor.callproc('whatsup_attachment_proc', [whatsAppAtachmentID, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           #self.investigationid=str(w[0])
           self.type=str(w[1])
           self.file=str(w[2])
           self.whatsAppMsgID =str(w[3])

    @classmethod
    def FromData(cls, type, file, whatsAppMsgID ):
        cls.type = str(type)
        cls.file = str(file)
        cls.whatsAppAtachmentID= str(whatsAppMsgID)
        return cls


    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,value):
        self._type=value


    @property
    def file(self):
        return self._file
    @file.setter
    def file(self,value):
        self._file=value

    @property
    def whatsAppMsgID(self):
        return self._whatsAppMsgID

    @whatsAppMsgID.setter
    def whatsAppMsgID(self, value):
        self._whatsAppMsgID = value
    @property
    def whatsAppAtachmentID(self):
        return self._whatsAppAtachmentID
    @whatsAppAtachmentID.setter
    def whatsAppAtachmentID(self,value):
        self._whatsAppAtachmentID=value

    def delete_vibermsg(self, ID):
        ex = Model.connection.conection.mycursor.callproc('proc_Deletewhatsup_attachment', [self._whatsAppAtachmentID, ])
        Model.connection.conection.mycursor.stored_results()

    def getAllviberMessage(self):
        AllviberMessage=[]
        ex = Model.connection.conection.mycursor.callproc('allwhatsAppMsg_proc')

        for result in Model.connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                AllviberMessage.append(whatsAppAtachment.FromData(i[0],i[1],i[3]))

        return AllviberMessage



