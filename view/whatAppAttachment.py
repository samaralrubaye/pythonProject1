import connection

class whatsAppAtachment:
    def __init__(self,  whatsAppAtachmentID= None):
        super(whatsAppAtachment,self).__init__()
        if whatsAppAtachmentID == None:
            return
        self._type = ''
        self._file=''
        self._whatsAppMsgID=' '
        self.whatsAppAtachmentID = whatsAppAtachmentID
        self.results= []
        ex = connection.conection.mycursor.callproc('whatsup_attachment_proc', [whatsAppAtachmentID, ])
        connection.conection.mycursor.stored_results()
        for result in connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           #self.investigationid=str(w[0])
           self.type=str(w[1])
           self.file=str(w[2])
           self.whatsAppMsgID =str(w[3])

   
    def FromData(self, type, file, whatsAppMsgID ):
        ex=whatsAppAtachment()
        ex.type = str(type)
        ex.file = str(file)
        ex.whatsAppAtachmentID= str(whatsAppMsgID)
        return ex


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
        ex = connection.conection.mycursor.callproc('proc_Deletewhatsup_attachment', [self._whatsAppAtachmentID, ])
        connection.conection.mycursor.stored_results()

    def getAllviberMessage(self):
        AllviberMessage=[]
        ex = connection.conection.mycursor.callproc('allwhatsAppMsg_proc')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                AllviberMessage.append(whatsAppAtachment.FromData(self,i[0],i[1],i[3]))

        return AllviberMessage



