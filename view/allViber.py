import connection
class allViber:
    def __init__(self):
        self._fromViber_Msg_FirstName=' '
        self._fromViber_Msg_LastName=' '
        self._fromViber_Msg_Latitude=' '
        self._fromViber_Msg_Longtude=' '
        self._fromViber_Msg_IP=' '
        self._fromViber_Msg_DateandTime=' '
        self._fromViber_Msg_number=' '
        self._fromViber_Msg=' '

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
            return self._fromViber_Msg_FirstName

    @FromViber_Msg_FirstName.setter
    def FromViber_Msg_FirstName (self, value):
            self._fromViber_Msg_FirstName = value
    
    @property
    def ToViber_Msg_FirstName(self):
            return self._toViber_Msg_FirstName

    @ToViber_Msg_FirstName.setter
    def ToViber_Msg_FirstName (self, value):
            self._toViber_Msg_FirstName = value
    #lastname
    @property
    def FromViber_Msg_LastName(self):
            return self._fromViber_Msg_LastName

    @FromViber_Msg_LastName.setter
    def FromViber_Msg_LastName (self, value):
            self._fromViber_Msg_LastName = value
    
    @property
    def ToViber_Msg_LastName(self):
            return self._toViber_Msg_LastName

    @ToViber_Msg_LastName.setter
    def ToViber_Msg_LastName(self, value):
            self._toViber_Msg_LastName = value
    #longtude
    @property
    def FromViber_Msg_Longtude(self):
            return self._fromViber_Msg_Longtude

    @FromViber_Msg_Longtude.setter
    def FromViber_Msg_Longtude(self, value):
            self._fromViber_Msg_Longtude = value
    
    @property
    def ToViber_Msg_Longtude(self):
            return self._toViber_Msg_Longtude

    @ToViber_Msg_Longtude.setter
    def ToViber_Msg_Longtude(self, value):
            self._toViber_Msg_Longtude = value

    #Latitudeg
    @property
    def FromViber_Msg_Latitude(self):
            return self._fromViber_Msg_Latitude

    @FromViber_Msg_Latitude.setter
    def FromViber_Msg_Latitude(self, value):
            self._fromViber_Msg_Latitude = value
    
    @property
    def ToViber_Msg_Latitude(self):
            return self._toViber_Msg_Latitude

    @ToViber_Msg_Latitude.setter
    def ToViber_Msg_Latitude(self, value):
            self._toViber_Msg_Latitude = value
    #IP
    @property
    def FromViber_Msg_IP(self):
            return self._fromViber_Msg_IP

    @FromViber_Msg_IP.setter
    def FromViber_Msg_IP(self, value):
            self._fromViber_Msg_IP = value
    
    @property
    def ToViber_Msg_IP(self):
            return self._toViber_Msg_IP

    @ToViber_Msg_IP.setter
    def ToViber_Msg_IP(self, value):
            self._toViber_Msg_IP = value
    # msg
     
    @property
    def FromViber_Msg(self):
            return self._fromViber_Msg

    @FromViber_Msg.setter
    def FromViber_Msg(self, value):
            self._fromViber_Msg = value
    
    @property
    def ToViber_Msg(self):
            return self._toViber_Msg

    @ToViber_Msg.setter
    def ToViber_Msg(self, value):
            self._toViber_Msg = value
    #DateandTime
    
    @property
    def FromViber_Msg_DateandTime(self):
            return self._fromViber_Msg_DateandTime

    @FromViber_Msg_DateandTime.setter
    def FromViber_Msg_DateandTime(self, value):
            self._fromViber_Msg_DateandTime = value
    
    @property
    def ToViber_Msg_DateandTime(self):
            return self._toViber_Msg_DateandTime

    @ToViber_Msg_DateandTime.setter
    def ToViber_Msg_DateandTime(self, value):
            self._toViber_Msg_DateandTime = value
    
    #number
    
    @property
    def FromViber_Msg_number(self):
            return self._fromViber_Msg_number

    @FromViber_Msg_number.setter
    def FromViber_Msg_number(self, value):
            self._fromViber_Msg_number = value
    
    @property
    def ToViber_Msg_number(self):
            return self._toViber_Msg_number

    @ToViber_Msg_number.setter
    def ToViber_Msg_number(self, value):
            self._toViber_Msg_number = value
    
    def FromData(self, fromViber_Msg_FirstName,fromViber_Msg_LastName,fromViber_Msg_number, fromViber_Msg_Longtude,fromViber_Msg_Latitude,fromViber_Msg,
     toViber_Msg_FirstName, 
     toViber_Msg_LastName, toViber_Msg_number, toViber_Msg_Longtude, toViber_Msg_Latitude, toViber_Msg_IP,
     toViber_Msg, toViber_Msg_DateandTime ):
        v=allViber()
        v.FromViber_Msg_FirstName = str(fromViber_Msg_FirstName)
        v.FromViber_Msg_LastName= str(fromViber_Msg_LastName)
        v.FromViber_Msg_number=str(fromViber_Msg_number)
        v.FromViber_Msg_Latitude=str(fromViber_Msg_Latitude)
        v.FromViber_Msg_Longtude=str(fromViber_Msg_Longtude)
        v.FromViber_Msg=str(fromViber_Msg)
        

        v.ToViber_Msg_FirstName = str(toViber_Msg_FirstName)
        v.ToViber_Msg_LastName= str(toViber_Msg_LastName)
        v.ToViber_Msg_number=str(toViber_Msg_number)
        v.ToViber_Msg_Latitude=str(toViber_Msg_Latitude)
        v.ToViber_Msg_Longtude=str(toViber_Msg_Longtude)
        v.ToViber_Msg_IP=str(toViber_Msg_IP)
        v.ToViber_Msg=str(toViber_Msg)
        v.ToViber_Msg_DateandTime=str(toViber_Msg_DateandTime)

      #  ex.peopleID=str(peopleID)
        return v

    def getAllVibers(self):
        Viberarray=[]
        ex = connection.conection.mycursor.callproc('selectALLViber')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                Viberarray.append(allViber.FromData(self,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))
               
        return Viberarray

