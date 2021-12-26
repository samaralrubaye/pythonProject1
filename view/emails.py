import Model.connection


class emails:
    def __init__(self, emailid):
        self._emailtext = ' '
        self._timeDate = ' '
        self._Email = ' '
        self._email_longtude=' '
        self._email_latitude=' '
        self.emailid = emailid
        ex = Model.connection.conection.mycursor.callproc('email_proc', [emailid, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
            w = result.fetchall()[0]
            print(w)
            self.emailtext = str(w[1])
            self.timeDate=str(w[2])
            self.Email=str(w[3])
            self.email_longtude=str(w[4])
            self.email_latitude=str(w[5])

    @property
    def email_latitude(self):
        return self._email_latitude

    @email_latitude.setter
    def email_latitude(self, value):
        self._email_latitude = value

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
        ex = Model.connection.conection.mycursor.callproc('proc_deleteEmail', [self.emailid])
        Model.connection.conection.mycursor.stored_results()


z = emails(24)
#print(z.Email)
#print(z.timeDate)
