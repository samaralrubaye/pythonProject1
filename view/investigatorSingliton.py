from investigator import investigator


class investigatorSinglilton(investigator):
    __instance = None
    @staticmethod
    def getinstance():
        if investigatorSinglilton.__instance== None:
            raise Exception("there is no such  a investigator!")
        else:
            return investigatorSinglilton.__instance


    def __init__(self, investigatorName ,investigatorNumber):
        if investigatorSinglilton.__instance != None:
            raise Exception("singilton can not be instantieated")
        else:
            self.investigatorName= investigatorName
            self.investigatorNumber=investigatorNumber
            investigatorSinglilton.__instance=self
    @staticmethod
    def get_data():
        print(f"Name: {investigatorSinglilton.__instance.investigatorName}, Number:{investigatorSinglilton.__instance.investigatorNumber}")
I=investigatorSinglilton("mm", 30)
print(I)
I.get_data()