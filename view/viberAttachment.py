import Model.connection

class viberAppAtachment:
    def __init__(self,  viberAtachmentID):
        self._type = ''
        self._file=''
        self._viberMsgID=' '
        self.viberAtachmentID = viberAtachmentID
        self.results= []
        ex = Model.connection.conection.mycursor.callproc('viberattachment_proc', [viberAtachmentID, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           #self.investigationid=str(w[0])
           self.type=str(w[2])
           self.file=str(w[3])
           self.viberMsgID =str(w[1])

    @classmethod
    def FromData(cls, type, file, viberMsgID):
        cls.type = str(type)
        cls.file = str(file)
        cls.viberMsgID= str(viberMsgID)
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
        ex = Model.connection.conection.mycursor.callproc('proc_deleteviberMsg', [self._viberAtachmentID,])
        Model.connection.conection.mycursor.stored_results()


def getAllExaminers(self):
    viberAttachments = []
    ex = Model.connection.conection.mycursor.callproc('allViberAttachments_proc')

    for result in Model.connection.conection.mycursor.stored_results():
        for i in result.fetchall():
            viberAttachments .append(viberAppAtachment.FromData(i[0], i[1], i[2], i[3]))

    return viberAttachments

w=viberAppAtachment(1)


