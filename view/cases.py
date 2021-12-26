import Model.connection


class cases:
    def __init__(self, caseid):
        self._caseName = ''
        self.caseid = caseid
        ex = Model.connection.conection.mycursor.callproc('case_proc', [caseid, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
            w = result.fetchall()[0]
            print(w)
            self.caseName = str(w[1])

    @property
    def caseId(self):
        return self.caseid

    @caseId.setter
    def caseId(self, value):
        self.caseid = value

    @property
    def caseName(self):
        return self._caseName

    @caseName.setter
    def caseName(self, value):
        self._caseName = value

    def createCase(self,caseName):
        ex = Model.connection.conection.mycursor.callproc('proc_addCase', [self.caseName,])
        Model.connection.conection.mycursor.stored_results()

    def update_Case(self,caseId,caseName):
        ex = Model.connection.conection.mycursor.callproc('proc_updateCase', [self.caseId,self.caseName])
        Model.connection.conection.mycursor.stored_results()

    def delete_Case(self,caseId,caseName):
        ex = Model.connection.conection.mycursor.callproc('proc_deleteCase', [self.caseId,self.caseName])
        Model.connection.conection.mycursor.stored_results()

z = cases(1)
print(z.caseId)
print(z.caseName)
