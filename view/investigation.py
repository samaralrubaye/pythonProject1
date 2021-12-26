import Model.connection

class investGation:
    def __init__(self,  investigationid):
        self._peopleID = ''
        self._comment=''
        self._examinerCasrid=' '
        self.investigationid = investigationid
        self.results= []
        ex = Model.connection.conection.mycursor.callproc('investigatin_proc', [investigationid, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
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




w=investGation(1)
print(w.examinerCasrid)

