
from sys import implementation
from examiners import ExaMiners
import connection

class emails:
    def __init__(self, emailid=None):
        super(ExaMiners,self).__init__()
        if emailid == None:
            return
        self._emailtext = ' '
        self._timeDate = ' '
        self._Email = ' '
        self._email_longtude=' '
        self._email_latitude=' '
        self.emailid = emailid
        self._peopleID=' '
        ex = connection.conection.mycursor.callproc('email_proc', [emailid, ])
        connection.conection.mycursor.stored_results()
        for result in connection.conection.mycursor.stored_results():
            w = result.fetchall()[0]
            print(w)
            self.emailtext = str(w[1])
            self.timeDate=str(w[2])
            self.Email=str(w[3])
            self.email_longtude=str(w[4])
            self.email_latitude=str(w[5])
            self.peopleID=str(w[6])

    
    @property
    def email_latitude(self):
        return self._email_latitude

    @email_latitude.setter
    def email_latitude(self, value):
        self._email_latitude = value

    @property
    def peopleID(self):
        return self._peopleID

    @peopleID.setter
    def peopleID(self, value):
        self._peopleID = value

    @property
    def email_longtude(self):
        return self._Email

    @email_longtude.setter
    def email_longtude(self, value):
        self._email_longtude = value

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, value):
        self._Email = value
    @property
    def timeDate(self):
        return self._timeDate

    @timeDate.setter
    def timeDate(self, value):
        self._timeDate = value
    @property
    def emailid(self):
        return self.emailid

    @emailid.setter
    def emailid(self, value):
        self.emailid = value

    @property
    def emailtext(self):
        return self._emailtext

    @emailtext.setter
    def emailtext(self, value):
        self._emailtext = value



    def delete_email(self,ID):
        ex = connection.conection.mycursor.callproc('proc_deleteEmail', [self.emailid])
        connection.conection.mycursor.stored_results()
    
    def FromData(self, emailtext,timeDate,Email,email_longtude, email_latitude,peopleID):
        self.emailtext = str(emailtext)
        self.timeDate = str(timeDate)
        self.Email=str(Email)
        self.email_longtude=str(email_longtude)
        self.email_latitude=str(email_latitude)
        self.peopleID=str(peopleID)
        return self

    def getAllEmails(self):
        Emails=[]
        ex = connection.conection.mycursor.callproc('allemails_proc')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                Emails.append(emails.FromData(self,i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

        return Emails


#z = emails(24)
#print(z.Email)
#print(z.timeDate)
