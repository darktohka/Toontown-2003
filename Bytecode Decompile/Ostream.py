import types, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject

class Ostream(FFIExternalObject.FFIExternalObject):
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
        if libpandaexpress and libpandaexpress._inPJoxtqCB5:
            libpandaexpress._inPJoxtqCB5(self.this)

    def put(self, c):
        returnValue = libpandaexpress._inPJoxtdovs(self.this, c)
        return returnValue

    def flush(self):
        returnValue = libpandaexpress._inPJoxtztz3(self.this)
        return returnValue