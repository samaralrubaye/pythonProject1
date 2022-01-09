import connection

class investGation:
    def __init__(self,  investigationid=None):
        super(investGation,self).__init__()
        if investigationid == None:
            return
        
        self._peopleID = ''
        self._comment=''
        self._examinerCasrid=' '
        self.investigationid = investigationid
        self.results= []
        ex = connection.conection.mycursor.callproc('investigatin_proc', [investigationid, ])
        connection.conection.mycursor.stored_results()
        for result in connection.conection.mycursor.stored_results():
           w= result.fetchall()[0]
           #self.investigationid=str(w[0])
           self.commentnt=str(w[2])
           self.examinerCasrid =str(w[3])



    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self,value):
        self._comment=value


    @property
    def examinerCasrid(self):
        return self._examinerCasrid
    @examinerCasrid.setter
    def examinerCasrid(self,value):
        self._examinerCasrid=value
    @property
    def investigationid(self):
        return self.investigationid
    @investigationid.setter
    def investigationid(self,value):
        self.userid=value



    def delete_Investigation(self,ID):
        ex = connection.conection.mycursor.callproc('proc_investigatin', [self.investigationid])
        connection.conection.mycursor.stored_results()

    def fromData(self,peopleID,commant,examinercaseID):
        ex= investGation()
        ex.peopleID = str(peopleID)
        ex.commant = str(commant)
        ex.examinercaseID = examinercaseID
        return ex


    def getAllinvestGation(self):
        investTemp=[]
        ex = connection.conection.mycursor.callproc('Examiners')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                investTemp.append(investGation.fromData(self,i[1],i[2],i[3]))

        return investTemp




