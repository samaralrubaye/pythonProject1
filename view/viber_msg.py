import Model.connection

class viberMassages:
    def __init__(self,  viberMsgID):
        self._viberMsg = ''
        self._viber_longtude=' '
        self._viber_latitude=' '
        self._viber_msgDateTime = ' '
        self._viber_Number = ' '
        self._viber_readtime = ' '
        self.viberMsgID=viberMsgID
        self.results= []
        ex = Model.connection.conection.mycursor.callproc('viber_msg_proc', [self.viber_Number, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           #self.investigationid=str(w[0])
           self.viber_Number = str(w[1])
           self._viberMsg=str(w[2])

           self._viber_longtude =str(w[3])
           self.viber_latitude = str(w[4])
           self._viberMsgIP = str(w[5])
           self._viber_msgDateTime=str(w[5])
           self.viber_readtime=str(w[9])

           self.viber_readtime=str(w[10])

    @property
    def viber_msgDateTime(self):
        return self._viber_msgDateTime

    @viber_msgDateTime.setter
    def viber_msgDateTime(self, value):
        self._viber_msgDateTime = value

    @property
    def viber_readtime(self):
        return self._viber_readtime

    @viber_readtime.setter
    def viber_readtime(self, value):
        self._viber_readtime = value

    @property
    def viber_Number(self):
        return self._viber_Number

    @viber_Number.setter
    def viber_Number(self, value):
        self._viber_Number = value

    @property
    def viberMsg(self):
        return self._viberMsg

    @viberMsg.setter
    def viberMsg(self, value):
        self._viberMsg = value

    @property
    def viber_longtude(self):
        return self._viber_longtude

    @viber_longtude.setter
    def viber_longtude(self,value):
        self._viber_longtude=value


    @property
    def viber_latitude(self):
        return self._viber_latitude
    @viber_latitude.setter
    def viber_latitude(self,value):
        self._viber_latitude=value

    @property
    def viberMsgIP(self):
        return self._viberMsgIP

    @viberMsgIP.setter
    def viberMsgIP(self, value):
        self._viberMsgIP = value
    @property
    def viberMsgID(self):
        return self._viberMsgID
    @viberMsgID.setter
    def viberMsgID(self,value):
        self._viberMsgID=value
    def createNew(self,IP,longTude,latiTude,msg_time,number,reading_time):
        ex = Model.connection.conection.mycursor.callproc('addviber_proc', [IP,longTude,latiTude,msg_time,number,reading_time])
        Model.connection.conection.mycursor.stored_results()
    def update_viber(self,ID,IP,longTude,latiTude,msg_time,number,reading_time):
        ex = Model.connection.conection.mycursor.callproc('updateviber_proc', [ID,IP,longTude,latiTude,msg_time,number,reading_time])
        Model.connection.conection.mycursor.stored_results()

    def delete_viber(self,ID):
        ex = Model.connection.conection.mycursor.callproc('deleteviber_proc', [ID,])
        Model.connection.conection.mycursor.stored_results()





w=viberMassages(189)
print(w.whatsAppMsgID)



