import connection
class allWhatsApp:
    def __init__(self):
        self._FromWhatsApp_Msg_FirstName=' '
        self._FromWhatsApp_Msg_LastName=' '
        self._FromWhatsApp_Msg_Latitude=' '
        self._FromWhatsApp_Msg_Longtude=' '
        self._FromWhatsApp_Msg_IP=' '
        self._FromWhatsApp_Msg_DateandTime=' '
        self._FromWhatsApp_Msg_number=' '
        self._FromWhatsApp_Msg=' '

        self._toWhatsApp_Msg_FirstName=' '
        self._toWhatsApp_Msg_LastName=' '
        self._toWhatsApp_Msg_Latitude_=' '
        self._toWhatsApp_Msg_Longtude=' '
        self._toWhatsApp_Msg_IP=' '
        self._toWhatsApp_Msg_DateandTime=' '
        self._toWhatsApp_Msg_number=' '
        self._toWhatsApp_Msg=' '
        # ex = connection.conection.mycursor.callproc('SelectCaseWhatApp_proc', [caseid, ])
        # connection.conection.mycursor.stored_results()
        # for result in connection.conection.mycursor.stored_results():
        #     w = result.fetchall()[0]
        #     print(w)
        #     self._FromWhatsApp_Msg_FirstName=str(w[1])
        #     self._FromWhatsApp_Msg_LastName=str(w[1])
        #     self._FromWhatsApp_Msg_Latitude=str(w[1])
        #     self._FromWhatsApp_Msg_Longtude=str(w[1])
        #     self._FromWhatsApp_Msg_IP=str(w[1])
        #     self._FromWhatsApp_Msg_DateandTime=str(w[1])
        #     self._FromWhatsApp_Msg_number=str(w[1])
        #     self._FromWhatsApp_Msg=str(w[1])

        #     self._toWhatsApp_Msg_FirstName=str(w[1])
        #     self._toWhatsApp_Msg_LastName=str(w[1])
        #     self._toWhatsApp_Msg_Latitude_=str(w[1])
        #     self._toWhatsApp_Msg_Longtude=str(w[1])
        #     self._toWhatsApp_Msg_IP=str(w[1])
        #     self._toWhatsApp_Msg_DateandTime=str(w[1])
        #     self._toWhatsApp_Msg_number=str(w[1])
        #     self._toWhatsApp_Msg=str(w[1])
            
        
#firstName
    @property
    def FromWhatsApp_Msg_FirstName(self):
            return self._FromWhatsApp_Msg_FirstName

    @FromWhatsApp_Msg_FirstName.setter
    def FromWhatsApp_Msg_FirstName (self, value):
            self._FromWhatsApp_Msg_FirstName = value
    
    @property
    def toWhatsApp_Msg_FirstName(self):
            return self._toWhatsApp_Msg_FirstName

    @toWhatsApp_Msg_FirstName.setter
    def toWhatsApp_Msg_FirstName (self, value):
            self._toWhatsApp_Msg_FirstName = value
    #lastname
    @property
    def FromWhatsApp_Msg_LastName(self):
            return self._FromWhatsApp_Msg_LastName

    @FromWhatsApp_Msg_LastName.setter
    def FromWhatsApp_Msg_LastName (self, value):
            self._FromWhatsApp_Msg_LastName = value
    
    @property
    def toWhatsApp_Msg_LastName(self):
            return self._toWhatsApp_Msg_LastName

    @toWhatsApp_Msg_LastName.setter
    def toWhatsApp_Msg_LastName (self, value):
            self._toWhatsApp_Msg_LastName = value
    #longtude
    @property
    def FromWhatsApp_Msg_Longtude(self):
            return self._FromWhatsApp_Msg_Longtude

    @FromWhatsApp_Msg_Longtude.setter
    def FromWhatsApp_Msg_Longtude (self, value):
            self._FromWhatsApp_Msg_Longtude = value
    
    @property
    def toWhatsApp_Msg_Longtude(self):
            return self._toWhatsApp_Msg_Longtude

    @toWhatsApp_Msg_Longtude.setter
    def toWhatsApp_Msg_Longtude (self, value):
            self._toWhatsApp_Msg_Longtude = value

    #Latitudeg
    @property
    def FromWhatsApp_Msg_Latitude(self):
            return self._FromWhatsApp_Msg_Latitude

    @FromWhatsApp_Msg_Latitude.setter
    def FromWhatsApp_Msg_Latitude (self, value):
            self._FromWhatsApp_Msg_Latitude = value
    
    @property
    def toWhatsApp_Msg_Latitude(self):
            return self._toWhatsApp_Msg_Latitude

    @toWhatsApp_Msg_Latitude.setter
    def toWhatsApp_Msg_Latitude (self, value):
            self._toWhatsApp_Msg_Latitude = value
    #IP
    @property
    def FromWhatsApp_Msg_IP(self):
            return self._FromWhatsApp_Msg_IP

    @FromWhatsApp_Msg_IP.setter
    def FromWhatsApp_Msg_IP (self, value):
            self._FromWhatsApp_Msg_IP = value
    
    @property
    def toWhatsApp_Msg_IP(self):
            return self._toWhatsApp_Msg_IP

    @toWhatsApp_Msg_IP.setter
    def toWhatsApp_Msg_IP (self, value):
            self._toWhatsApp_Msg_IP = value
    # msg
     
    @property
    def FromWhatsApp_Msg(self):
            return self._FromWhatsApp_Msg

    @FromWhatsApp_Msg.setter
    def FromWhatsApp_Msg (self, value):
            self._FromWhatsApp_Msg = value
    
    @property
    def toWhatsApp_Msg(self):
            return self._toWhatsApp_Msg

    @toWhatsApp_Msg.setter
    def toWhatsApp_Msg (self, value):
            self._toWhatsApp_Msg = value
    #DateandTime
    
    @property
    def FromWhatsApp_Msg_DateandTime(self):
            return self._FromWhatsApp_Msg_DateandTime

    @FromWhatsApp_Msg_DateandTime.setter
    def FromWhatsApp_Msg_DateandTime (self, value):
            self._FromWhatsApp_Msg_DateandTime = value
    
    @property
    def toWhatsApp_Msg_DateandTime(self):
            return self._toWhatsApp_Msg_DateandTime

    @toWhatsApp_Msg_DateandTime.setter
    def toWhatsApp_Msg_DateandTime (self, value):
            self._toWhatsApp_Msg_DateandTime = value
    
    #number
    
    @property
    def FromWhatsApp_Msg_number(self):
            return self._FromWhatsApp_Msg_number

    @FromWhatsApp_Msg_number.setter
    def FromWhatsApp_Msg_DateandTime (self, value):
            self._FromWhatsApp_Msg_number = value
    
    @property
    def toWhatsApp_Msg_number(self):
            return self._toWhatsApp_Msg_number

    @toWhatsApp_Msg_number.setter
    def toWhatsApp_Msg_number (self, value):
            self._toWhatsApp_Msg_number = value
    
    def FromData(cls, FromWhatsApp_Msg_FirstName,FromWhatsApp_Msg_LastName,FromWhatsApp_Msg_number,
    FromWhatsApp_Msg_Longtude, FromWhatsApp_Msg_Latitude,FromWhatsApp_Msg_IP,FromWhatsApp_Msg_DateandTime, FromWhatsApp_Msg,toWhatsApp_Msg_FirstName, toWhatsApp_Msg_LastName, toWhatsApp_Msg_number, toWhatsApp_Msg_IP, toWhatsApp_Msg_DateandTime ):
        
        cls.FromWhatsApp_Msg_FirstName = str(FromWhatsApp_Msg_FirstName)
        cls.FromWhatsApp_Msg_LastName= str(FromWhatsApp_Msg_LastName)
        cls.FromWhatsApp_Msg_number=str(FromWhatsApp_Msg_number)
        cls.FromWhatsApp_Msg_Longtude=str(FromWhatsApp_Msg_Longtude)
        cls.FromWhatsApp_Msg_Latitude=str(FromWhatsApp_Msg_Latitude)
        cls.FromWhatsApp_Msg_IP=str(FromWhatsApp_Msg_IP)
        cls.FromWhatsApp_Msg_DateandTime=str(FromWhatsApp_Msg_DateandTime)
        cls.FromWhatsApp_Msg=str(FromWhatsApp_Msg)
        cls.toWhatsApp_Msg_FirstName=str(toWhatsApp_Msg_FirstName)
        cls.toWhatsApp_Msg_LastName=str(toWhatsApp_Msg_LastName)
        cls.toWhatsApp_Msg_number=str(toWhatsApp_Msg_number)
        cls.toWhatsApp_Msg_IP=str(toWhatsApp_Msg_IP)
        cls.toWhatsApp_Msg_DateandTime=str(toWhatsApp_Msg_DateandTime)
      #  ex.peopleID=str(peopleID)
        return cls

    def getAllWhatsApp(self):
        WhatsAPP=[]
        ex = connection.conection.mycursor.callproc('selectallwhatsapp')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                WhatsAPP.append(allWhatsApp.FromData(self,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12]))
        print(WhatsAPP)
        return WhatsAPP