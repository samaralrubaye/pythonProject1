#from _typeshed import Self
import connection
#import sys
#sys.path.append("PYTHONPROJECT1/Model.connection.py")


class cases:
    def __init__(self, caseid = None):
        super(cases,self).__init__()
        if caseid == None:
            return
        self._caseName = ''
        self.caseid = caseid
        ex = connection.conection.mycursor.callproc('case_proc', [caseid, ])
        connection.conection.mycursor.stored_results()
        for result in connection.conection.mycursor.stored_results():
            w = result.fetchall()[0]
            print(w)
            self.caseName = str(w[1])

    @classmethod
    def FromData(cls, caseName, ):
        cls.caseName = str(caseName)

        return cls

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
        ex = connection.conection.mycursor.callproc('proc_addCase', [self.caseName,])
        connection.conection.mycursor.stored_results()

    def update_Case(self,caseId,caseName):
        ex = connection.conection.mycursor.callproc('proc_updateCase', [self.caseId,self.caseName])
        connection.conection.mycursor.stored_results()

    def delete_Case(self,caseId,caseName):
        ex = connection.conection.mycursor.callproc('proc_deleteCase', [self.caseId,self.caseName])
        connection.conection.mycursor.stored_results()

    def getAllCases(self):
        AllCases=[]
        ex =connection.conection.mycursor.callproc('allCases_proc')

        for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                AllCases.append( cases.FromData(i[0],i[1]))

        return AllCases

    def fromData(self,id,name):
        ex= cases()
        ex.caseId  = id
        ex.caseName  = str(name)
        return ex
    

    def getAll(self,userID):
       tempCases = []
       w = connection.conection.mycursor.callproc('casesforinvestigators',[userID,])

       for result in connection.conection.mycursor.stored_results():
            for i in result.fetchall():
                tempCases.append(cases.fromData(self,i[0],i[1]))

       return tempCases
      

