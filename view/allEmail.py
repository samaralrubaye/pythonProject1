
import connection
class allEmail:
    def __init__(self):
        self._fromEmail_firstName=' '
        self._fromEmail_lastname=' '
        self._fromEmail_longtude=' '
        self._fromEmail_latitude=' '
        self._fromEmail_content_text=' '
        self._fromEmail_timeDate=' '
        self._fromEmail_Email=' '
       

        self._toEmail_firstName=' '
        self._toEmail_lastname=' '
        self._toEmail_longtude=' '
        self._toEmail_latitude=' '
        self._toEmail_content_text=' '
        self._toEmail_timeDate=' '
        self._toEmail_Email=' '
       

        self._ccEmail_firstName=' '
        self._ccEmail_lastname=' '
        self._ccEmail_longtude=' '
        self._ccEmail_latitude=' '
        self._ccEmail_content_text=' '
        self._ccEmail_timeDate=' '
        self._ccEmail_Email=' '
        

        self._bccEmail_firstName=' '
        self._bccEmail_lastname=' '
        self._bccEmail_longtude=' '
        self._bccEmail_latitude=' '
        self._bccEmail_content_text=' '
        self._bccEmail_timeDate=' '
        self._bccEmail_Email=' '
      #  ex = connection.conection.mycursor.callproc('SelectedCasesEmail_proc', [caseid, ])
      #  connection.conection.mycursor.stored_results()
      #  for result in connection.conection.mycursor.stored_results():
          #  w = result.fetchall()[0]
        #     print(w)
        #     self.fromEmail_firstName=str(w[1])
        #     self.fromEmail_lastname=str(w[1])
        #     self.fromEmail_longtude=str(w[1])
        #     self.fromEmail_latitude=str(w[1])
        #     self.fromEmail_content_text=str(w[1])
        #     self.fromEmail_timeDate=str(w[1])
       

        #     self.toEmail_firstName=str(w[1])
        #     self.toEmail_lastname=str(w[1])
        #     self.toEmail_longtude=str(w[1])
        #     self.toEmail_latitude=str(w[1])
        #     self.toEmail_content_text=str(w[1])
        #     self.toEmail_timeDate=str(w[1])
       

        #     self.ccEmail_firstName=str(w[1])
        #     self.ccEmail_lastname=str(w[1])
        #     self.ccEmail_longtude=str(w[1])
        #     self.ccEmail_latitude=str(w[1])
        #     self.ccEmail_content_text=str(w[1])
        #     self.ccEmail_timeDate=str(w[1])
        

        #     self._bccEmail_firstName=str(w[1])
        #     self._bccEmail_lastname=str(w[1])
        #     self._bccEmail_longtude=str(w[1])
        #     self._bccEmail_latitude=str(w[1])
        #     self._bccEmail_content_text=str(w[1])
        #    self._bccEmail_timeDate=str(w[1])
            
       
    #firstName
    @property
    def fromEmail_firstName(self):
            return self._fromEmail_firstName

    @fromEmail_firstName.setter
    def fromEmail_firstName(self, value):
            self._fromEmail_firstName = value
    
    @property
    def toEmail_firstName(self):
            return self._toEmail_firstName

    @toEmail_firstName.setter
    def toEmail_firstName(self, value):
            self._toEmail_firstName = value
    
    @property
    def ccEmail_firstName(self):
            return self._ccEmail_firstName

    @ccEmail_firstName.setter
    def ccEmail_firstName(self, value):
            self._ccEmail_firstName = value
    
    
    @property
    def bccEmail_firstName(self):
            return self._bccEmail_firstName

    @bccEmail_firstName.setter
    def bccEmail_firstName(self, value):
            self._bccEmail_firstName = value
    
    @property
    def fromEmail_firstName(self):
            return self._fromEmail_firstName

    @fromEmail_firstName.setter
    def email_latitude(self, value):
            self._fromEmail_firstName = value
    # last name
    @property
    def toEmail_lastName(self):
            return self._toEmail_lastname

    @toEmail_lastName.setter
    def toEmail_lastname(self, value):
            self._toEmail_lastname = value
    
    @property
    def ccEmail_lastname(self):
            return self._ccEmail_lastname

    @ccEmail_lastname.setter
    def ccEmail_lastname(self, value):
            self._ccEmail_lastname = value
    
    
   
    @property
    def bccEmail_lastname(self):
            return self._bccEmail_lastname

    @bccEmail_lastname.setter
    def bccEmail_lastname(self, value):
            self._bccEmail_lastname = value
    @property
    def fromEmail_lastname(self):
            return self._fromEmail_lastname

    @fromEmail_lastname.setter
    def fromEmail_lastname(self, value):
            self._fromEmail_lastname = value
    #longtude
    @property
    def toEmail_longtude(self):
            return self._toEmail_longtude

    @toEmail_longtude.setter
    def toEmail_longtude(self, value):
            self._toEmail_longtude = value
    
    @property
    def ccEmail_longtude(self):
            return self._ccEmail_longtude

    @ccEmail_longtude.setter
    def ccEmail_longtude(self, value):
            self._ccEmail_longtude = value
    
    
    @property
    def bccEmail_longtude(self):
            return self._bccEmail_longtude

    @bccEmail_longtude.setter
    def bccEmail_longtude(self, value):
            self._bccEmail_longtude = value
    
   
     #latitude
    @property
    def toEmail_latitude(self):
            return self._toEmail_latitude

    @toEmail_latitude.setter
    def toEmail_latitude(self, value):
            self._toEmail_latitude = value
    
    @property
    def ccEmail_latitude(self):
            return self._ccEmail_latitude

    @ccEmail_latitude.setter
    def ccEmail_latitude(self, value):
            self._ccEmail_latitude = value
    
    
    @property
    def bccEmail_latitude(self):
            return self._bccEmail_latitude

    @bccEmail_latitude.setter
    def bccEmail_latitude(self, value):
            self._bccEmail_latitude = value
    
    
    
       #text
    @property
    def toEmail_content_text(self):
            return self._toEmail_content_text

    @toEmail_content_text.setter
    def toEmail_content_text(self, value):
            self._toEmail_content_text = value
    
    @property
    def ccEmail_content_text(self):
            return self._ccEmail_content_text

    @ccEmail_content_text.setter
    def ccEmail_content_text(self, value):
            self._ccEmail_content_text = value
    
    
    @property
    def bccEmail_content_text(self):
            return self._bccEmail_content_text

    @bccEmail_content_text.setter
    def bccEmail_content_text(self, value):
            self._bccEmail_content_text = value
    @property
    def fromEmail_content_text(self):
            return self._fromEmail_content_text

    @fromEmail_content_text.setter
    def fromEmail_content_text(self, value):
            self._fromEmail_content_text = value
    #date
    @property
    def toEmail_timeDate(self):
            return self._toEmail_timeDate

    @toEmail_timeDate.setter
    def toEmail_timeDate(self, value):
            self._toEmail_timeDate = value
    
    @property
    def ccEmail_timeDate(self):
            return self._ccEmail_timeDate

    @ccEmail_timeDate.setter
    def ccEmail_timeDate(self, value):
            self._ccEmail_timeDate = value
    
    @property
    def fromEmail_timeDate(self):
            return self._fromEmail_timeDate

    @fromEmail_timeDate.setter
    def fromEmail_timeDate(self, value):
            self._fromEmail_timeDate = value
    
    
    @property
    def bccEmail_timeDate(self):
            return self._bccEmail_timeDate

    @bccEmail_timeDate.setter
    def bccEmail_timeDate(self, value):
            self._bccEmail_timeDate = value
    #date
    @property
    def toEmail_Email(self):
            return self._toEmail_Email

    @toEmail_timeDate.setter
    def toEmail_timeDate(self, value):
            self._toEmail_Email = value
    
    @property
    def ccEmail_Email(self):
            return self._ccEmail_Email

    @ccEmail_Email.setter
    def ccEmail_Email(self, value):
            self._ccEmail_Email = value
    
    @property
    def fromEmail_Email(self):
            return self._fromEmail_Email

    @fromEmail_Email.setter
    def fromEmail_Email(self, value):
            self._fromEmail_Email = value
    
    
    @property
    def bccEmail_Email(self):
            return self._bccEmail_Email

    @bccEmail_Email.setter
    def bccEmail_Email(self, value):
            self._bccEmail_Email = value


    @property
    def fromEmail_latitude(self):
            return self._fromEmail_latitude

    @fromEmail_latitude.setter
    def fromEmail_latitude(self, value):
            self._fromEmail_latitude = value    

    @property
    def fromEmail_longtude(self):
            return self._fromEmail_longtude

    @fromEmail_longtude.setter
    def fromEmail_longtude(self, value):
            self._fromEmail_longtude = value

    def FromData(self,fromEmail_firstName,fromEmail_lastname,fromEmail_content_text,fromEmail_timeDate,fromEmail_Email
    ,fromEmail_latitude,fromEmail_longtude, toEmail_firstName,toEmail_lastname,toEmail_content_text,toEmail_timeDate,toEmail_Email, toEmail_latitude,toEmail_longtude, ccEmail_firstName,ccEmail_lastname,ccEmail_content_text,ccEmail_timeDate,ccEmail_Email,ccEmail_latitude,ccEmail_longtude, bccEmail_firstName,bccEmail_lastname,bccEmail_content_text ,bccEmail_timeDate,bccEmail_Email,bccEmail_latitude,bccEmail_longtude):
        
        e = allEmail()
        
        e.fromEmail_lastname = str(fromEmail_lastname)
        e.fromEmail_content_text=str(fromEmail_content_text)
        e.fromEmail_latitude=str(fromEmail_latitude)
        e.fromEmail_longtude=str(fromEmail_longtude)
        e.fromEmail_timeDate=(fromEmail_timeDate)
        e.fromEmail_Email=str(fromEmail_Email)

        e.toEmail_firstName = str(toEmail_firstName)
        e.toEmail_lastname = str(toEmail_lastname)
        e.toEmail_content_text=str(toEmail_content_text)
        e.toEmail_latitude=(toEmail_latitude)
        e.toEmail_longtude=(toEmail_longtude)
        e.toEmail_timeDate=(toEmail_timeDate)

        e.ccEmail_firstName = str(ccEmail_firstName)
        e.ccEmail_lastname = str(ccEmail_lastname)
        e.ccEmail_content_text=str(ccEmail_content_text)
        e.ccEmail_latitude=(ccEmail_latitude)
        e.ccEmail_longtude=(ccEmail_longtude)
        e.ccEmail_timeDate=(ccEmail_timeDate)
        e._ccEmail_Email=str(ccEmail_Email)
        
        e.bccEmail_firstName = str(bccEmail_firstName)
        e.bccEmail_lastname = str(bccEmail_lastname)
        e.bccEmail_content_text=str(bccEmail_content_text)
        e.bccEmail_latitude=(bccEmail_latitude)
        e.bccEmail_longtude=(bccEmail_longtude)
        e.bccEmail_timeDate=(bccEmail_timeDate)
        e.bccEmail_timeDate=str(bccEmail_Email)
        return e

    def getAllEmails(self):
        Emails=[]
        ex = connection.conection.mycursor.callproc('selectallemails')
        j =1
        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                Emails.append(allEmail.FromData(self,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],i[23],i[24],i[25],i[26],i[27]))
                j = j + 1
        print(j)
        return Emails

   