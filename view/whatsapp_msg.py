import Model.connection

class whatsAppMassages:
    def __init__(self,  whatsAppMsgID):
        self._whatsAppMsg = ''
        self._whatsAppMsgIP=''
        self._whatsApp_longtude=' '
        self._whatsApp_latitude=' '
        self._whatsApp_msgDateTime = ' '
        self._whatsApp_Number = ' '
        self._whatsApp_readtime = ' '
        self.whatsAppMsgID = whatsAppMsgID
        self.results= []
        ex = Model.connection.conection.mycursor.callproc('whatsup_msg_proc', [whatsAppMsgID, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           #self.investigationid=str(w[0])
           self._whatsAppMsg=str(w[1])
           self._whatsAppMsgIP=str(w[2])
           self._whatsApp_latitude =str(w[3])
           self._whatsApp_longtude = str(w[4])
           self._whatsApp_msgDateTime=str(w[5])
           self.whatsApp_Number=str(w[6])
           self._whatsApp_readtime=str(w[10])

    @classmethod
    def FromData(cls, whatsAppMsg, whatsAppMsgIP, whatsApp_latitude, whatsApp_longtude, whatsApp_msgDateTime, whatsApp_readtime  ):
        cls.whatsAppMsg = str(whatsAppMsg)
        cls.whatsAppMsgIP = str(whatsAppMsgIP)
        cls.whatsApp_latitude = str(whatsApp_latitude)
        cls.whatsApp_longtude = str(whatsApp_longtude)
        cls.whatsApp_msgDateTime = str(whatsApp_msgDateTime)
        cls. whatsApp_readtime=str( whatsApp_readtime)

        return cls

    @property
    def whatsApp_readtime(self):
        return self._whatsApp_readtime

    @whatsApp_readtime.setter
    def whatsApp_readtime(self, value):
        self._whatsApp_readtime = value

    @property
    def whatsApp_Number(self):
        return self._whatsApp_Number

    @whatsApp_Number.setter
    def whatsApp_Number(self, value):
        self._whatsApp_Number = value

    @property
    def whatsApp_msgDateTime(self):
        return self._whatsApp_msgDateTime

    @whatsApp_msgDateTime.setter
    def whatsApp_msgDateTime(self, value):
        self._whatsApp_msgDateTime = value

    @property
    def whatsApp_latitude(self):
        return self._whatsApp_latitude

    @whatsApp_latitude.setter
    def whatsApp_latitude(self,value):
        self._whatsApp_latitude=value


    @property
    def whatsApp_longtude(self):
        return self._whatsApp_longtude
    @whatsApp_longtude.setter
    def whatsApp_longtude(self,value):
        self._whatsApp_longtude=value

    @property
    def whatsAppMsgIp(self):
        return self._whatsAppMsgIp

    @whatsAppMsgIp.setter
    def whatsAppMsgIp(self, value):
        self._whatsAppMsgIp = value
    @property
    def whatsAppMsgID(self):
        return self._whatsAppMsgID
    @whatsAppMsgID.setter
    def whatsAppMsgID(self,value):
        self. _whatsAppMsgID=value



    def getAllWhatsApp_msg(self):
        AllWhatsApp_msg=[]
        ex = Model.connection.conection.mycursor.callproc('Examiners')

        for result in Model.connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                AllWhatsApp_msg.append(whatsAppMassages.FromData(i[0],i[1],i[3], i[4], i[5], i[6], i[10]))

        return AllWhatsApp_msg





