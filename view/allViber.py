import connection
class allViber:
    def __init__(self):
        self._FromViber_Msg_FirstName=' '
        self._FromViber_Msg_LastName=' '
        self._FromViber_Msg_Latitude=' '
        self._FromViber_Msg_Longtude=' '
        self._FromViber_Msg_IP=' '
        self._FromViber_Msg_DateandTime=' '
        self._FromViber_Msg_number=' '
        self._FromViber_Msg=' '

        self._toViber_Msg_FirstName=' '
        self._toViber_Msg_LastName=' '
        self._toViber_Msg_Latitude_=' '
        self._toViber_Msg_Longtude=' '
        self._toViber_Msg_IP=' '
        self._toViber_Msg_DateandTime=' '
        self._toViber_Msg_number=' '
        self._toViber_Msg=' '
        # ex = connection.conection.mycursor.callproc('SelectCaseVibe_proc', [caseid, ])
        # connection.conection.mycursor.stored_results()
        # for result in connection.conection.mycursor.stored_results():
        #     w = result.fetchall()[0]
        #     print(w)
        #     self._FromViber_Msg_FirstName=str(w[1])
        #     self._FromViber_Msg_LastName=str(w[1])
        #     self._FromViber_Msg_Latitude=str(w[1])
        #     self._FromViber_Msg_Longtude=str(w[1])
        #     self._FromViber_Msg_IP=str(w[1])
        #     self._FromViber_Msg_DateandTime=str(w[1])
        #     self._FromViber_Msg_number=str(w[1])
        #     self._FromViber_Msg=str(w[1])

        #     self._toViber_Msg_FirstName=str(w[1])
        #     self._toViber_Msg_LastName=str(w[1])
        #     self._toViber_Msg_Latitude_=str(w[1])
        #     self._toViber_Msg_Longtude=str(w[1])
        #     self._toViber_Msg_IP=str(w[1])
        #     self._toViber_Msg_DateandTime=str(w[1])
        #     self._toViber_Msg_number=str(w[1])
        #     self._toViber_Msg=str(w[1])
            

        
#firstName
    @property
    def FromViber_Msg_FirstName(self):
            return self._FromViber_Msg_FirstName

    @FromViber_Msg_FirstName.setter
    def FromViber_Msg_FirstName (self, value):
            self._FromViber_Msg_FirstName = value
    
    @property
    def toViber_Msg_FirstName(self):
            return self._toViber_Msg_FirstName

    @toViber_Msg_FirstName.setter
    def toViber_Msg_FirstName (self, value):
            self._toViber_Msg_FirstName = value
    #lastname
    @property
    def FromViber_Msg_LastName(self):
            return self._FromViber_Msg_LastName

    @FromViber_Msg_LastName.setter
    def FromViber_Msg_LastName (self, value):
            self._FromViber_Msg_LastName = value
    
    @property
    def toViber_Msg_LastName(self):
            return self._toViber_Msg_LastName

    @toViber_Msg_LastName.setter
    def toViber_Msg_LastName (self, value):
            self._toViber_Msg_LastName = value
    #longtude
    @property
    def FromViber_Msg_Longtude(self):
            return self._FromViber_Msg_Longtude

    @FromViber_Msg_Longtude.setter
    def FromViber_Msg_Longtude (self, value):
            self._FromViber_Msg_Longtude = value
    
    @property
    def toViber_Msg_Longtude(self):
            return self._toViber_Msg_Longtude

    @toViber_Msg_Longtude.setter
    def toViber_Msg_Longtude (self, value):
            self._toViber_Msg_Longtude = value

    #Latitudeg
    @property
    def FromViber_Msg_Latitude(self):
            return self._FromViber_Msg_Latitude

    @FromViber_Msg_Latitude.setter
    def FromViber_Msg_Latitude (self, value):
            self._FromViber_Msg_Latitude = value
    
    @property
    def toViber_Msg_Latitude(self):
            return self._toViber_Msg_Latitude

    @toViber_Msg_Latitude.setter
    def toViber_Msg_Latitude (self, value):
            self._toViber_Msg_Latitude = value
    #IP
    @property
    def FromViber_Msg_IP(self):
            return self._FromViber_Msg_IP

    @FromViber_Msg_IP.setter
    def FromViber_Msg_IP (self, value):
            self._FromViber_Msg_IP = value
    
    @property
    def toViber_Msg_IP(self):
            return self._toViber_Msg_IP

    @toViber_Msg_IP.setter
    def toViber_Msg_IP (self, value):
            self._toViber_Msg_IP = value
    # msg
     
    @property
    def FromViber_Msg(self):
            return self._FromViber_Msg

    @FromViber_Msg.setter
    def FromViber_Msg (self, value):
            self._FromViber_Msg = value
    
    @property
    def toViber_Msg(self):
            return self._toViber_Msg

    @toViber_Msg.setter
    def toViber_Msg (self, value):
            self._toViber_Msg = value
    #DateandTime
    
    @property
    def FromViber_Msg_DateandTime(self):
            return self._FromViber_Msg_DateandTime

    @FromViber_Msg_DateandTime.setter
    def FromViber_Msg_DateandTime (self, value):
            self._FromViber_Msg_DateandTime = value
    
    @property
    def toViber_Msg_DateandTime(self):
            return self._toViber_Msg_DateandTime

    @toViber_Msg_DateandTime.setter
    def toViber_Msg_DateandTime (self, value):
            self._toViber_Msg_DateandTime = value
    
    #number
    
    @property
    def FromViber_Msg_number(self):
            return self._FromViber_Msg_number

    @FromViber_Msg_number.setter
    def FromViber_Msg_DateandTime (self, value):
            self._FromViber_Msg_number = value
    
    @property
    def toViber_Msg_number(self):
            return self._toViber_Msg_number

    @toViber_Msg_number.setter
    def toViber_Msg_number (self, value):
            self._toViber_Msg_number = value
    
    def FromData(cls, FromViber_Msg_FirstName,FromViber_Msg_LastName,FromViber_Msg_number,FromViber_Msg_Latitude, FromViber_Msg_Longtude,FromViber_Msg, FromViber_Msg_DateandTime, toViber_Msg_FirstName, toViber_Msg_LastName, toViber_Msg_number, toViber_Msg_Latitude, toViber_Msg_Longtude, toViber_Msg, toViber_Msg_DateandTime ):
       
        cls.FromViber_Msg_FirstName = str(FromViber_Msg_FirstName)
        cls.FromViber_Msg_LastName= str(FromViber_Msg_LastName)
        cls.FromViber_Msg_number=str(FromViber_Msg_number)
        cls.FromViber_Msg_Latitude=str(FromViber_Msg_Latitude)
        cls.FromViber_Msg_Longtude=str(FromViber_Msg_Longtude)
        cls.FromViber_Msg=str(FromViber_Msg)
        cls.FromViber_Msg_DateandTime=str(FromViber_Msg_DateandTime)

        cls.toViber_Msg_FirstName = str(toViber_Msg_FirstName)
        cls.toViber_Msg_LastName= str(toViber_Msg_LastName)
        cls.toViber_Msg_number=str(toViber_Msg_number)
        cls.toViber_Msg_Latitude=str(toViber_Msg_Latitude)
        cls.toViber_Msg_Longtude=str(toViber_Msg_Longtude)
        cls.toViber_Msg=str(toViber_Msg)
        cls.toViber_Msg_DateandTime=str(toViber_Msg_DateandTime)

      #  ex.peopleID=str(peopleID)
        return cls

    def getAllVibers(self):
        Viberarray=[]
        ex = connection.conection.mycursor.callproc('selectALLViber')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                Viberarray.append(allViber.FromData(self,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))

        return Viberarray

