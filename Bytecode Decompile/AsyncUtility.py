import types, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject

class AsyncUtility(FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libpandaexpressDowncasts]

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdrGbb:
            libpandaexpress._inP2KOdrGbb(self.this)

    def setFrequency(self, frequency):
        returnValue = libpandaexpress._inP2KOdZi1H(self.this, frequency)
        return returnValue

    def getFrequency(self):
        returnValue = libpandaexpress._inP2KOdBEcb(self.this)
        return returnValue

    def createThread(self):
        returnValue = libpandaexpress._inP2KOd0BFM(self.this)
        return returnValue