import Model.connection


class eXaminerCases:
    def __init__(self, examinerCaseid):
        self._examinerID = ' '
        self._caseId=' '
        self.examinerCaseid= examinerCaseid
        ex = Model.connection.conection.mycursor.callproc('xaminercase_proc', [examinerCaseid, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
            w = result.fetchall()[0]
            print(w)
            self.examinerID = w[1]
            self.caseId= w[2]

    @property
    def examinerCaseid(self):
        return self.examinerCaseid

    @examinerCaseid.setter
    def examinerCaseid(self, value):
        self.examinerCaseid = value

    @property
    def caseId(self):
        return self.caseId

    @caseId.setter
    def caseId(self, value):
        self.caseId = value

    @property
    def examinerID(self):
        return self._examinerID

    @examinerID.setter
    def examinerID(self, value):
        self._examinerID = value

    def createExaminerCase(self,examinerID,caseId):
        ex = Model.connection.conection.mycursor.callproc('proc_addexaminercase', [self.examinerID,self.caseId,])
        Model.connection.conection.mycursor.stored_results()

    def update_ExaminerCase(self,ID,examinerID,caseId):
        ex = Model.connection.conection.mycursor.callproc('proc_updateExaminer', [self.examinerCaseid,self._examinerID,self.caseId,])
        Model.connection.conection.mycursor.stored_results()

    def delete_ExaminerCase(self,ID,examinerID,caseId):
        ex = Model.connection.conection.mycursor.callproc('proc_deletexaminercase', [self.examinerCaseid,self._examinerID,self.caseId,])
        Model.connection.conection.mycursor.stored_results()


z = eXaminerCases(2222222)


