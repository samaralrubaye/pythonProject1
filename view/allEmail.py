
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
    def FromEmail_firstName(self):
            return self._fromEmail_firstName

    @FromEmail_firstName.setter
    def FromEmail_firstName(self, value):
            self._fromEmail_firstName = value
    
    @property
    def ToEmail_firstName(self):
            return self._toEmail_firstName

    @ToEmail_firstName.setter
    def ToEmail_firstName(self, value):
            self._toEmail_firstName = value
    
    @property
    def CcEmail_firstName(self):
            return self._ccEmail_firstName

    @CcEmail_firstName.setter
    def CcEmail_firstName(self, value):
            self._ccEmail_firstName = value
    
    
    @property
    def BccEmail_firstName(self):
            return self._bccEmail_firstName

    @BccEmail_firstName.setter
    def BccEmail_firstName(self, value):
            self._bccEmail_firstName = value
    
    @property
    def FromEmail_firstName(self):
            return self._fromEmail_firstName

    @FromEmail_firstName.setter
    def FromEmail_firstName(self, value):
            self._fromEmail_firstName = value
    # last name
    @property
    def ToEmail_lastName(self):
            return self._toEmail_lastname

    @ToEmail_lastName.setter
    def ToEmail_lastname(self, value):
            self._toEmail_lastname = value
    
    @property
    def CcEmail_lastname(self):
            return self._ccEmail_lastname

    @CcEmail_lastname.setter
    def CcEmail_lastname(self, value):
            self._ccEmail_lastname = value
    
    
   
    @property
    def BccEmail_lastname(self):
            return self._bccEmail_lastname

    @BccEmail_lastname.setter
    def BccEmail_lastname(self, value):
            self._bccEmail_lastname = value
    @property
    def FromEmail_lastname(self):
            return self._fromEmail_lastname

    @FromEmail_lastname.setter
    def FromEmail_lastname(self, value):
            self._fromEmail_lastname = value
    #longtude
    @property
    def ToEmail_longtude(self):
            return self._toEmail_longtude

    @ToEmail_longtude.setter
    def ToEmail_longtude(self, value):
            self._toEmail_longtude = value
    
    @property
    def CcEmail_longtude(self):
            return self._ccEmail_longtude

    @CcEmail_longtude.setter
    def CcEmail_longtude(self, value):
            self._ccEmail_longtude = value
    
    
    @property
    def BccEmail_longtude(self):
            return self._bccEmail_longtude

    @BccEmail_longtude.setter
    def BccEmail_longtude(self, value):
            self._bccEmail_longtude = value
    
   
     #latitude
    @property
    def ToEmail_latitude(self):
            return self._toEmail_latitude

    @ToEmail_latitude.setter
    def ToEmail_latitude(self, value):
            self._toEmail_latitude = value
    
    @property
    def CcEmail_latitude(self):
            return self._ccEmail_latitude

    @CcEmail_latitude.setter
    def CcEmail_latitude(self, value):
            self._ccEmail_latitude = value
    
    
    @property
    def BccEmail_latitude(self):
            return self._bccEmail_latitude

    @BccEmail_latitude.setter
    def BccEmail_latitude(self, value):
            self._bccEmail_latitude = value
    
    
    
       #text
    @property
    def ToEmail_content_text(self):
            return self._toEmail_content_text

    @ToEmail_content_text.setter
    def ToEmail_content_text(self, value):
            self._toEmail_content_text = value
    
    @property
    def CcEmail_content_text(self):
            return self._ccEmail_content_text

    @CcEmail_content_text.setter
    def CcEmail_content_text(self, value):
            self._ccEmail_content_text = value
    
    
    @property
    def BccEmail_content_text(self):
            return self._bccEmail_content_text

    @BccEmail_content_text.setter
    def BccEmail_content_text(self, value):
            self._bccEmail_content_text = value
    @property
    def FromEmail_content_text(self):
            return self._fromEmail_content_text

    @FromEmail_content_text.setter
    def FromEmail_content_text(self, value):
            self._fromEmail_content_text = value
    #date
    @property
    def ToEmail_timeDate(self):
            return self._toEmail_timeDate

    @ToEmail_timeDate.setter
    def ToEmail_timeDate(self, value):
            self._toEmail_timeDate = value
    
    @property
    def CcEmail_timeDate(self):
            return self._ccEmail_timeDate

    @CcEmail_timeDate.setter
    def CcEmail_timeDate(self, value):
            self._ccEmail_timeDate = value
    
    @property
    def FromEmail_timeDate(self):
            return self._fromEmail_timeDate

    @FromEmail_timeDate.setter
    def FromEmail_timeDate(self, value):
            self._fromEmail_timeDate = value
    
    
    @property
    def BccEmail_timeDate(self):
            return self._bccEmail_timeDate

    @BccEmail_timeDate.setter
    def BccEmail_timeDate(self, value):
            self._bccEmail_timeDate = value
    #date
    @property
    def ToEmail_Email(self):
            return self._toEmail_Email

    @ToEmail_Email.setter
    def ToEmail_Email(self, value):
            self._toEmail_Email = value
    
    @property
    def CcEmail_Email(self):
            return self._ccEmail_Email

    @CcEmail_Email.setter
    def CcEmail_Email(self, value):
            self._ccEmail_Email = value
    
    @property
    def FromEmail_Email(self):
            return self._fromEmail_Email

    @FromEmail_Email.setter
    def FromEmail_Email(self, value):
            self._fromEmail_Email = value
    
    
    @property
    def BccEmail_Email(self):
            return self._bccEmail_Email

    @BccEmail_Email.setter
    def BccEmail_Email(self, value):
            self._bccEmail_Email = value


    @property
    def FromEmail_latitude(self):
            return self._fromEmail_latitude

    @FromEmail_latitude.setter
    def FromEmail_latitude(self, value):
            self._fromEmail_latitude = value    

    @property
    def FromEmail_longtude(self):
            return self._fromEmail_longtude

    @FromEmail_longtude.setter
    def FromEmail_longtude(self, value):
            self._fromEmail_longtude = value

    def FromData(self,fromEmail_firstName,fromEmail_lastname,fromEmail_content_text,fromEmail_timeDate,fromEmail_Email
    ,fromEmail_latitude,fromEmail_longtude, toEmail_firstName,toEmail_lastname,toEmail_content_text,toEmail_timeDate,
    toEmail_Email, toEmail_latitude,toEmail_longtude, ccEmail_firstName,ccEmail_lastname,ccEmail_content_text,ccEmail_timeDate,ccEmail_Email,ccEmail_latitude,ccEmail_longtude, bccEmail_firstName,bccEmail_lastname,bccEmail_content_text ,bccEmail_timeDate,bccEmail_Email,bccEmail_latitude,bccEmail_longtude):
        
        e = allEmail()
        e.FromEmail_firstName=str(fromEmail_firstName)
        e.FromEmail_lastname = str(fromEmail_lastname)
        e.FromEmail_content_text=str(fromEmail_content_text)
        e.FromEmail_latitude=(fromEmail_latitude)
        e.FromEmail_longtude=(fromEmail_longtude)
        e.FromEmail_timeDate=str(fromEmail_timeDate)
        e.FromEmail_Email=str(fromEmail_Email)

        e.ToEmail_firstName = str(toEmail_firstName)
        e.ToEmail_lastname = str(toEmail_lastname)
        e.ToEmail_content_text=str(toEmail_content_text)
        e.ToEmail_latitude=(toEmail_latitude)
        e.ToEmail_longtude=str(toEmail_longtude)
        e.ToEmail_timeDate=str(toEmail_timeDate)
        e.ToEmail_Email=str(toEmail_Email)

        e.CcEmail_firstName = str(ccEmail_firstName)
        e.CcEmail_lastname = str(ccEmail_lastname)
        e.CcEmail_content_text=str(ccEmail_content_text)
        e.CcEmail_latitude=(ccEmail_latitude)
        e.CcEmail_longtude=(ccEmail_longtude)
        e.CcEmail_timeDate=(ccEmail_timeDate)
        e.CcEmail_Email=str(ccEmail_Email)
        
        e.BccEmail_firstName = str(bccEmail_firstName)
        e.BccEmail_lastname = str(bccEmail_lastname)
        e.BccEmail_content_text=str(bccEmail_content_text)
        e.BccEmail_latitude=(bccEmail_latitude)
        e.BccEmail_longtude=(bccEmail_longtude)
        e.BccEmail_timeDate=(bccEmail_timeDate)
        e.BccEmail_timeDate=str(bccEmail_Email)
        return e

    def getAllEmails(self,caseid, datefrom,dateto, textcontent,txtsender,txtresipain):
        Emails=[]
        ex = connection.conection.mycursor.callproc('selectallemails',[textcontent,datefrom,dateto,caseid,txtsender,txtresipain])
        j =1
        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                Emails.append(allEmail.FromData(self,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],i[23],i[24],i[25],i[26],i[27]))
                j = j + 1
        print(j)
        return Emails

   