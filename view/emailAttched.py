import Model.connection

class emailAttached:
    def __init__(self,  emailattachedid):
        self._EmailID = ''
        self._type=''
        self._file=' '
        self.emailattachedid = emailattachedid
        self.results= []
        ex = Model.connection.conection.mycursor.callproc('email_attachment_proc', [emailattachedid, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           #self.investigationid=str(w[0])
           self.EmailID=str(w[1])
           self.type=str(w[2])
           self.file =str(w[3])



    @property
    def EmailID(self):
        return self._EmailID

    @EmailID.setter
    def EmailID(self,value):
        self._EmailID=value


    @property
    def type(self):
        return self._type
    @type.setter
    def type(self,value):
        self._type=value

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value


    @property
    def emailattachedid(self):
        return self._emailattachedid
    @emailattachedid.setter
    def emailattachedid(self,value):
        self._emailattachedid=value


    def delete_vibermsg(self, ID):
        ex = Model.connection.conection.mycursor.callproc('proc_deleteEmail', [self._proc_delet_email_attachment, ])
        Model.connection.conection.mycursor.stored_results()

w=emailAttached(1)


