import types, libtoontown, libtoontownDowncasts, FFIExternalObject

class PosHpr(FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libtoontownDowncasts]

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def __overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(self, pos, hpr):
        self.this = libtoontown._inPet4yJ_mZ(pos.this, hpr.this)
        self.userManagesMemory = 1

    def __overloaded_constructor_ptrConstLPoint3f(self, pos):
        self.this = libtoontown._inPet4yC1B1(pos.this)
        self.userManagesMemory = 1

    def __overloaded_constructor(self):
        self.this = libtoontown._inPet4yw9z8()
        self.userManagesMemory = 1

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def destructor(self):
        if libtoontown and libtoontown._inPet4ykD4a:
            libtoontown._inPet4ykD4a(self.this)

    def getPos(self):
        returnValue = libtoontown._inPet4yKdTP(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        return returnObject
        return

    def getHpr(self):
        returnValue = libtoontown._inPet4yHm7x(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        return returnObject
        return

    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self.__overloaded_constructor()
        else:
            if numArgs == 1:
                import Point3
                if isinstance(_args[0], Point3.Point3):
                    return self.__overloaded_constructor_ptrConstLPoint3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            else:
                if numArgs == 2:
                    import Point3
                    if isinstance(_args[0], Point3.Point3):
                        import Point3
                        if isinstance(_args[1], Point3.Point3):
                            return self.__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(_args[0], _args[1])
                        else:
                            raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                    else:
                        raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '