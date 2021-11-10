from view.investigator import investigator


class investigatorSinglilton(investigator):
    __instance = None
    @staticmethod
    def getinstance():
        if investigatorSinglilton.__instance== None:
            raise Exception("there is no such  a investigator!")
        else:
            return investigatorSinglilton.__instance


    def __init__(self, __investigatorName ,__investigatorNumber):
        if investigatorSinglilton.__instance != None:
            raise Exception("singilton can not be instantieated")
        else:
            self.investigatorName= __investigatorName
            self.investigatorNumber=__investigatorNumber
            investigatorSinglilton.__instance=self