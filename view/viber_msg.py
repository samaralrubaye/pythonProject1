import connection

class viberMassages:
    def __init__(self,  viberMsgID=None):
        super(viberMassages,self).__init__()
        if viberMsgID == None:
            return
        self._viberMsg = ''
        self._viber_longtude=' '
        self._viber_latitude=' '
        self._viber_msgDateTime = ' '
        self._viber_Number = ' '
        self._viber_readtime = ' '
        self.viberMsgID=viberMsgID
        self.results= []
        ex = connection.conection.mycursor.callproc('viber_msg_proc', [self.viber_Number, ])
        connection.conection.mycursor.stored_results()
        for result in connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           #self.investigationid=str(w[0])
           self.viber_Number = str(w[1])
           self._viberMsg=str(w[2])

           self._viber_longtude =str(w[3])
           self.viber_latitude = str(w[4])
           self._viberMsgIP = str(w[5])
           self._viber_msgDateTime=str(w[6])
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
    
   
    def FromData(self,viberMsg , viber_longtude,viber_latitude,viberMsgIP, viber_msgDateTime,viber_readtime ):
        ex=viberMassages()
        ex.viberMsg = str(viberMsg)
        ex.viber_latitude = str(viber_latitude)
        ex.viber_longtude = str(viber_longtude)
        ex.viberMsgIP = str(viberMsgIP)
        ex.viber_msgDateTime = str(viber_msgDateTime)
        ex.viber_readtime = str(viber_readtime)
        return ex


    def delete_vibermsg(self,ID):
        ex = connection.conection.mycursor.callproc('proc_deleteviberMsg', [self.viberMsgID,])
        connection.conection.mycursor.stored_results()

    def getAllviberMsg(self):
        Viber_msgs = []
        ex = connection.conection.mycursor.callproc('allViberMsgs_proc')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                Viber_msgs.append(viberMassages.FromData(self,i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

        return Viber_msgs





