import types, libtoontown, libtoontownDowncasts, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject, DNANode

class DNAProp(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libtoontownDowncasts, libpandaexpressDowncasts]

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def __overloaded_constructor_ptrConstDNAProp(self, prop):
        self.this = libtoontown._inPet4yoaqd(prop.this)
        self.userManagesMemory = 1

    def __overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPet4yaXqa(initialName)
        self.userManagesMemory = 1

    def __overloaded_constructor(self):
        self.this = libtoontown._inPet4yzpQW()
        self.userManagesMemory = 1

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def destructor(self):
        if libtoontown and libtoontown._inPet4yoE3M:
            libtoontown._inPet4yoE3M(self.this)

    def getClassType():
        returnValue = libtoontown._inPet4yXJUZ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    getClassType = staticmethod(getClassType)

    def setCode(self, code):
        returnValue = libtoontown._inPet4ycY51(self.this, code)
        return returnValue

    def getCode(self):
        returnValue = libtoontown._inPet4ybDIt(self.this)
        return returnValue

    def setColor(self, color):
        returnValue = libtoontown._inPet4yZUox(self.this, color.this)
        return returnValue

    def getColor(self):
        returnValue = libtoontown._inPet4yFxCQ(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self.__overloaded_constructor()
        else:
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.__overloaded_constructor_atomicstring(_args[0])
                else:
                    if isinstance(_args[0], DNAProp):
                        return self.__overloaded_constructor_ptrConstDNAProp(_args[0])
                    else:
                        raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAProp> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '