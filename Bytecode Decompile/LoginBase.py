

class LoginBase:
    __module__ = __name__
    freeTimeExpires = -1

    def __init__(self, tcr):
        self.tcr = tcr

    def sendLoginMsg(self, loginName, password, createFlag):
        pass

    def getErrorCode(self):
        return 0

    def needToSetParentPassword(self):
        return 0