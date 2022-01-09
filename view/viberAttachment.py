import connection

class viberAppAtachment:
    def __init__(self,  viberAtachmentID=None):
        self._type = ''
        self._file=''
        self._viberMsgID=' '
        self.viberAtachmentID = viberAtachmentID
        self.results= []
        ex = connection.conection.mycursor.callproc('viberattachment_proc', [viberAtachmentID, ])
        connection.conection.mycursor.stored_results()
        for result in connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           #self.investigationid=str(w[0])
           self.type=str(w[2])
           self.file=str(w[3])
           self.viberMsgID =str(w[1])

    

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
    def viberMsgID(self):
        return self._viberMsgID

    @viberMsgID.setter
    def viberMsgID(self, value):
        self._viberMsgID = value
    @property
    def viberAtachmentID(self):
        return self._viberAtachmentID
    @viberAtachmentID.setter
    def viberAtachmentID(self,value):
        self._viberAtachmentID=value

    def delete_viberAttachment(self,ID):
        ex = connection.conection.mycursor.callproc('proc_deleteviberMsg', [self._viberAtachmentID,])
        connection.conection.mycursor.stored_results()
   
    def FromData(self, type, file, viberMsgID):
        ex=viberAppAtachment()
        ex.type = str(type)
        ex.file = str(file)
        ex.viberMsgID= str(viberMsgID)
        return ex

    def getAllExaminers(self):
        viberAttachments = []
        ex = connection.conection.mycursor.callproc('allViberAttachments_proc')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                viberAttachments .append(viberAppAtachment.FromData(i[0], i[1], i[2], i[3]))

        return viberAttachments




