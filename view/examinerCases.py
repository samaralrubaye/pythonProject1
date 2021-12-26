import Model.connection


class eXaminerCases:
    def __init__(self, examinerCaseid):
        self._examinerID = ' '
        self.examinerCaseid= examinerCaseid
        ex = Model.connection.conection.mycursor.callproc('xaminercase_proc', [examinerCaseid, ])
        Model.connection.conection.mycursor.stored_results()
        for result in Model.connection.conection.mycursor.stored_results():
            w = result.fetchall()[0]
            print(w)
            self.examinerID = w[1]

    @property
    def examinerCaseid(self):
        return self.examinerCaseid

    @examinerCaseid.setter
    def examinerCaseid(self, value):
        self.examinerCaseid = value

    @property
    def examinerID(self):
        return self._examinerID

    @examinerID.setter
    def examinerID(self, value):
        self._examinerID = value


z = eXaminerCases(2222222)


