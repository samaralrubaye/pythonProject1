import connection

class emailAttached:
    def __init__(self,  emailattachedid=None):
        super(emailAttached,self).__init__()
        if self._EmailID == None:
            return
        self._type=''
        self._file=' '
        self.emailattachedid = emailattachedid
        self.results= []
        ex = connection.conection.mycursor.callproc('email_attachment_proc', [emailattachedid, ])
        connection.conection.mycursor.stored_results()
        for result in connection.conection.mycursor.stored_results():
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
        self._emailattachedid= value


    def delete_vibermsg(self, ID):
        ex = connection.conection.mycursor.callproc('proc_deleteEmail', [self.proc_delet_email_attachment, ])
        connection.conection.mycursor.stored_results()
    def FromData(self, EmailID,type, file ):
        self.EmailID = str( EmailID)
        self.type = str(type)
        self.file= str(file)
        return self

    def getAllEmailAttached(self):
        attachment=[]
        ex = connection.conection.mycursor.callproc('alltheAttachedemails_proc')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                attachment.append(emailAttached.FromData(self,i[0],i[1],i[2],i[3]))

        return attachment


#w=emailAttached(1)

