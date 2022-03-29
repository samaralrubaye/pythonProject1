import connection
class allWhatsApp:
    def __init__(self):
        self._fromWhatsApp_Msg_FirstName=' '
        self._fromWhatsApp_Msg_LastName=' '
        self._fromWhatsApp_Msg_Latitude=' '
        self._fromWhatsApp_Msg_Longtude=' '
        self._fromWhatsApp_Msg_IP=' '
        self._fromWhatsApp_Msg_DateandTime=' '
        self._fromWhatsApp_Msg_number=' '
        self._fromWhatsApp_Msg=' '

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
            return self._fromWhatsApp_Msg_FirstName

    @FromWhatsApp_Msg_FirstName.setter
    def FromWhatsApp_Msg_FirstName (self, value):
            self._fromWhatsApp_Msg_FirstName = value
    
    @property
    def ToWhatsApp_Msg_FirstName(self):
            return self._toWhatsApp_Msg_FirstName

    @ToWhatsApp_Msg_FirstName.setter
    def ToWhatsApp_Msg_FirstName (self, value):
            self._toWhatsApp_Msg_FirstName = value
    #lastname
    @property
    def FromWhatsApp_Msg_LastName(self):
            return self._fromWhatsApp_Msg_LastName

    @FromWhatsApp_Msg_LastName.setter
    def FromWhatsApp_Msg_LastName (self, value):
            self._fromWhatsApp_Msg_LastName = value
    
    @property
    def ToWhatsApp_Msg_LastName(self):
            return self._toWhatsApp_Msg_LastName

    @ToWhatsApp_Msg_LastName.setter
    def ToWhatsApp_Msg_LastName (self, value):
            self._toWhatsApp_Msg_LastName = value
    #longtude
    @property
    def FromWhatsApp_Msg_Longtude(self):
            return self._fromWhatsApp_Msg_Longtude

    @FromWhatsApp_Msg_Longtude.setter
    def FromWhatsApp_Msg_Longtude (self, value):
            self._fromWhatsApp_Msg_Longtude = value
    
    @property
    def ToWhatsApp_Msg_Longtude(self):
            return self._toWhatsApp_Msg_Longtude

    @ToWhatsApp_Msg_Longtude.setter
    def ToWhatsApp_Msg_Longtude (self, value):
            self._toWhatsApp_Msg_Longtude = value

    #Latitudeg
    @property
    def FromWhatsApp_Msg_Latitude(self):
            return self._fromWhatsApp_Msg_Latitude

    @FromWhatsApp_Msg_Latitude.setter
    def FromWhatsApp_Msg_Latitude (self, value):
            self._fromWhatsApp_Msg_Latitude = value
    
    @property
    def ToWhatsApp_Msg_Latitude(self):
            return self._toWhatsApp_Msg_Latitude

    @ToWhatsApp_Msg_Latitude.setter
    def ToWhatsApp_Msg_Latitude (self, value):
            self._toWhatsApp_Msg_Latitude = value
    #IP
    @property
    def FromWhatsApp_Msg_IP(self):
            return self._fromWhatsApp_Msg_IP

    @FromWhatsApp_Msg_IP.setter
    def FromWhatsApp_Msg_IP (self, value):
            self._fromWhatsApp_Msg_IP = value
    
    @property
    def ToWhatsApp_Msg_IP(self):
            return self._toWhatsApp_Msg_IP

    @ToWhatsApp_Msg_IP.setter
    def ToWhatsApp_Msg_IP (self, value):
            self._toWhatsApp_Msg_IP = value
    # msg
     
    @property
    def FromWhatsApp_Msg(self):
            return self._fromWhatsApp_Msg

    @FromWhatsApp_Msg.setter
    def FromWhatsApp_Msg (self, value):
            self._fromWhatsApp_Msg = value
    
    @property
    def ToWhatsApp_Msg(self):
            return self._toWhatsApp_Msg

    @ToWhatsApp_Msg.setter
    def ToWhatsApp_Msg (self, value):
            self._toWhatsApp_Msg = value
    #DateandTime
    
    @property
    def FromWhatsApp_Msg_DateandTime(self):
            return self._fromWhatsApp_Msg_DateandTime

    @FromWhatsApp_Msg_DateandTime.setter
    def FromWhatsApp_Msg_DateandTime (self, value):
            self._fromWhatsApp_Msg_DateandTime = value
    
    @property
    def ToWhatsApp_Msg_DateandTime(self):
            return self._toWhatsApp_Msg_DateandTime

    @ToWhatsApp_Msg_DateandTime.setter
    def ToWhatsApp_Msg_DateandTime (self, value):
            self._toWhatsApp_Msg_DateandTime = value
    
    #number
    
    @property
    def FromWhatsApp_Msg_number(self):
            return self._fromWhatsApp_Msg_number

    @FromWhatsApp_Msg_number.setter
    def FromWhatsApp_Msg_number (self, value):
            self._fromWhatsApp_Msg_number = value
    
    @property
    def ToWhatsApp_Msg_number(self):
            return self._toWhatsApp_Msg_number

    @ToWhatsApp_Msg_number.setter
    def ToWhatsApp_Msg_number (self, value):
            self._toWhatsApp_Msg_number = value
    
    def FromData(self, fromWhatsApp_Msg_FirstName,fromWhatsApp_Msg_LastName,fromWhatsApp_Msg_number,
    fromWhatsApp_Msg_Longtude, fromWhatsApp_Msg_Latitude,fromWhatsApp_Msg_IP,toWhatsApp_Msg_FirstName, toWhatsApp_Msg_LastName, toWhatsApp_Msg_number,toWhatsApp_Msg_Latitude,toWhatsApp_Msg_Longtude, toWhatsApp_Msg_IP, fromWhatsApp_Msg, toWhatsApp_Msg_DateandTime ):
        W=allWhatsApp()
        W.FromWhatsApp_Msg_FirstName = str(fromWhatsApp_Msg_FirstName)
        W.FromWhatsApp_Msg_LastName= str(fromWhatsApp_Msg_LastName)
        W.FromWhatsApp_Msg_number=str(fromWhatsApp_Msg_number)
        W.FromWhatsApp_Msg_Longtude=str(fromWhatsApp_Msg_Longtude)
        W.FromWhatsApp_Msg_Latitude=str(fromWhatsApp_Msg_Latitude)
        W.FromWhatsApp_Msg_IP=str(fromWhatsApp_Msg_IP)
        W.FromWhatsApp_Msg_DateandTime=str(toWhatsApp_Msg_number)
        W.FromWhatsApp_Msg=str(fromWhatsApp_Msg)
        W.ToWhatsApp_Msg_FirstName=str(toWhatsApp_Msg_FirstName)
        W.ToWhatsApp_Msg_LastName=str(toWhatsApp_Msg_LastName)
        W.ToWhatsApp_Msg_number=str( toWhatsApp_Msg_DateandTime)
        W.ToWhatsApp_Msg_Longtude=str(toWhatsApp_Msg_Longtude)
        W.ToWhatsApp_Msg_Latitude=str(toWhatsApp_Msg_Latitude)
        W.ToWhatsApp_Msg_IP=str(toWhatsApp_Msg_IP)
        W.ToWhatsApp_Msg_DateandTime=str( toWhatsApp_Msg_DateandTime)
      #  ex.peopleID=str(peopleID)
        return W

    def getAllWhatsApp(self,caseid, datefrom,dateto, textcontent,txtsender,txtresipain):
        WhatsAPP=[]
        ex = connection.conection.mycursor.callproc('selectallwhatsapp',[textcontent,datefrom,dateto,caseid,txtsender,txtresipain])

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                WhatsAPP.append(allWhatsApp.FromData(self,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))
        print(WhatsAPP)
        return WhatsAPP