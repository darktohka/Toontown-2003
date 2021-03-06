import types, libpanda, libpandaDowncasts, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject, SelectiveChildNode

class SequenceNode(SelectiveChildNode.SelectiveChildNode, FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libpandaDowncasts, libpandaexpressDowncasts]

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def constructor(self, cycleRate, name):
        self.this = libpanda._inPkJyoygAs(cycleRate, name)
        self.userManagesMemory = 1

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def destructor(self):
        if libpanda and libpanda._inPkJyo_77X:
            libpanda._inPkJyo_77X(self.this)

    def getClassType():
        returnValue = libpanda._inPkJyoNJ9E()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    getClassType = staticmethod(getClassType)

    def setCycleRate(self, cycleRate):
        returnValue = libpanda._inPkJyoYDCt(self.this, cycleRate)
        return returnValue

    def getCycleRate(self):
        returnValue = libpanda._inPkJyomfhi(self.this)
        return returnValue

    def setVisibleChild(self, index):
        returnValue = libpanda._inPkJyowb0Q(self.this, index)
        return returnValue