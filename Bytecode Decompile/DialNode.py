import types, libpanda, libpandaDowncasts, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject, DataNode

class DialNode(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libpandaDowncasts, libpandaexpressDowncasts]

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def constructor(self, client, deviceName):
        self.this = libpanda._inPOfOPm9Tp(client.this, deviceName)
        self.userManagesMemory = 1

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def getClassType():
        returnValue = libpanda._inPOfOP1JS5()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    getClassType = staticmethod(getClassType)

    def isValid(self):
        returnValue = libpanda._inPOfOPonZa(self.this)
        return returnValue

    def getNumDials(self):
        returnValue = libpanda._inPOfOPpBgJ(self.this)
        return returnValue

    def readDial(self, index):
        returnValue = libpanda._inPOfOPQlFp(self.this, index)
        return returnValue

    def isDialKnown(self, index):
        returnValue = libpanda._inPOfOPcP5l(self.this, index)
        return returnValue