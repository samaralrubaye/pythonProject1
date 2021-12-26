import Model.connection

class viberAppAtachment:
    def __init__(self,  viberAppAtachmentID):
        self._type = ''
        self._file=''
        self._whatsAppMsgID=' '
        self.viberAppAtachmentID = viberAppAtachmentID
        self.results= []
        ex = Model.connection.conection.mycursor.callproc('whatsup_attachment_proc', [viberAppAtachmentID, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           #self.investigationid=str(w[0])
           self.type=str(w[1])
           self.file=str(w[2])
           self.whatsAppMsgID =str(w[3])



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




w=viberAppAtachment(1)


