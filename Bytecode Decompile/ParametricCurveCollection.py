import types, libpanda, libpandaDowncasts, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject, ReferenceCount

class ParametricCurveCollection(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libpandaDowncasts, libpandaexpressDowncasts]

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def constructor(self):
        self.this = libpanda._inPHc9WxrUC()
        self.userManagesMemory = 1

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def destructor(self):
        if libpanda and libpanda._inPHc9WdI4s:
            libpanda._inPHc9WdI4s(self.this)

    def __overloaded_addCurve_ptrParametricCurveCollection_ptrParametricCurve(self, curve):
        returnValue = libpanda._inPHc9WXyhA(self.this, curve.this)
        return returnValue

    def __overloaded_addCurve_ptrParametricCurveCollection_ptrParametricCurve_int(self, curve, index):
        returnValue = libpanda._inPHc9WtU26(self.this, curve.this, index)
        return returnValue

    def addCurves(self, node):
        returnValue = libpanda._inPHc9WO_D0(self.this, node.this)
        return returnValue

    def __overloaded_removeCurve_ptrParametricCurveCollection_ptrParametricCurve(self, curve):
        returnValue = libpanda._inPHc9WrSBL(self.this, curve.this)
        return returnValue

    def __overloaded_removeCurve_ptrParametricCurveCollection_int(self, index):
        returnValue = libpanda._inPHc9WPy0q(self.this, index)
        return returnValue

    def hasCurve(self, curve):
        returnValue = libpanda._inPHc9WafPA(self.this, curve.this)
        return returnValue

    def clear(self):
        returnValue = libpanda._inPHc9WJs_a(self.this)
        return returnValue

    def clearTimewarps(self):
        returnValue = libpanda._inPHc9WU3KR(self.this)
        return returnValue

    def getNumCurves(self):
        returnValue = libpanda._inPHc9WZbyN(self.this)
        return returnValue

    def getCurve(self, index):
        returnValue = libpanda._inPHc9Wpks_(self.this, index)
        import ParametricCurve
        returnObject = ParametricCurve.ParametricCurve(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def getXyzCurve(self):
        returnValue = libpanda._inPHc9WYo8i(self.this)
        import ParametricCurve
        returnObject = ParametricCurve.ParametricCurve(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def getHprCurve(self):
        returnValue = libpanda._inPHc9WV_TC(self.this)
        import ParametricCurve
        returnObject = ParametricCurve.ParametricCurve(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def getDefaultCurve(self):
        returnValue = libpanda._inPHc9W_FGT(self.this)
        import ParametricCurve
        returnObject = ParametricCurve.ParametricCurve(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def getNumTimewarps(self):
        returnValue = libpanda._inPHc9Wip1P(self.this)
        return returnValue

    def getTimewarpCurve(self, n):
        returnValue = libpanda._inPHc9W6SlK(self.this, n)
        import ParametricCurve
        returnObject = ParametricCurve.ParametricCurve(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def getMaxT(self):
        returnValue = libpanda._inPHc9Wjy26(self.this)
        return returnValue

    def makeEven(self, maxT, segmentsPerUnit):
        returnValue = libpanda._inPHc9WG4bH(self.this, maxT, segmentsPerUnit)
        return returnValue

    def faceForward(self, segmentsPerUnit):
        returnValue = libpanda._inPHc9WnOll(self.this, segmentsPerUnit)
        return returnValue

    def resetMaxT(self, maxT):
        returnValue = libpanda._inPHc9W62p2(self.this, maxT)
        return returnValue

    def __overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLMatrix4f___enum__CoordinateSystem(self, t, result, cs):
        returnValue = libpanda._inPHc9WDS8W(self.this, t, result.this, cs)
        return returnValue

    def __overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLMatrix4f(self, t, result):
        returnValue = libpanda._inPHc9Wf7Zb(self.this, t, result.this)
        return returnValue

    def __overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLVecBase3f_ptrLVecBase3f(self, t, xyz, hpr):
        returnValue = libpanda._inPHc9WvrTO(self.this, t, xyz.this, hpr.this)
        return returnValue

    def evaluateT(self, t):
        returnValue = libpanda._inPHc9WkozF(self.this, t)
        return returnValue

    def evaluateXyz(self, t, xyz):
        returnValue = libpanda._inPHc9WKi9F(self.this, t, xyz.this)
        return returnValue

    def evaluateHpr(self, t, hpr):
        returnValue = libpanda._inPHc9WRYqE(self.this, t, hpr.this)
        return returnValue

    def __overloaded_adjustXyz_ptrParametricCurveCollection_float_ptrConstLVecBase3f(self, t, xyz):
        returnValue = libpanda._inPHc9WHVjM(self.this, t, xyz.this)
        return returnValue

    def __overloaded_adjustXyz_ptrParametricCurveCollection_float_float_float_float(self, t, x, y, z):
        returnValue = libpanda._inPHc9Wn2SI(self.this, t, x, y, z)
        return returnValue

    def __overloaded_adjustHpr_ptrParametricCurveCollection_float_ptrConstLVecBase3f(self, t, xyz):
        returnValue = libpanda._inPHc9WNQfE(self.this, t, xyz.this)
        return returnValue

    def __overloaded_adjustHpr_ptrParametricCurveCollection_float_float_float_float(self, t, h, p, r):
        returnValue = libpanda._inPHc9WxtOA(self.this, t, h, p, r)
        return returnValue

    def recompute(self):
        returnValue = libpanda._inPHc9Wl2Rj(self.this)
        return returnValue

    def stitch(self, a, b):
        returnValue = libpanda._inPHc9WWz_C(self.this, a.this, b.this)
        return returnValue

    def output(self, out):
        returnValue = libpanda._inPHc9Wd_Jm(self.this, out.this)
        return returnValue

    def __overloaded_write_ptrConstParametricCurveCollection_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPHc9W57RA(self.this, out.this, indentLevel)
        return returnValue

    def __overloaded_write_ptrConstParametricCurveCollection_ptrOstream(self, out):
        returnValue = libpanda._inPHc9Wfrdh(self.this, out.this)
        return returnValue

    def __overloaded_writeEgg_ptrParametricCurveCollection_ptrFilename___enum__CoordinateSystem(self, filename, cs):
        returnValue = libpanda._inPHc9WOXGo(self.this, filename.this, cs)
        return returnValue

    def __overloaded_writeEgg_ptrParametricCurveCollection_ptrFilename(self, filename):
        returnValue = libpanda._inPHc9Wi0bC(self.this, filename.this)
        return returnValue

    def __overloaded_writeEgg_ptrParametricCurveCollection_ptrOstream_ptrConstFilename___enum__CoordinateSystem(self, out, filename, cs):
        returnValue = libpanda._inPHc9Wcx15(self.this, out.this, filename.this, cs)
        return returnValue

    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self.__overloaded_write_ptrConstParametricCurveCollection_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            if numArgs == 2:
                import Ostream
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.__overloaded_write_ptrConstParametricCurveCollection_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    def adjustHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self.__overloaded_adjustHpr_ptrParametricCurveCollection_float_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            if numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.__overloaded_adjustHpr_ptrParametricCurveCollection_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

    def evaluate(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import Mat4
                if isinstance(_args[1], Mat4.Mat4):
                    return self.__overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLMatrix4f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Mat4.Mat4> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            if numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    import VBase3, Mat4
                    if isinstance(_args[1], VBase3.VBase3):
                        import VBase3
                        if isinstance(_args[2], VBase3.VBase3):
                            return self.__overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLVecBase3f_ptrLVecBase3f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                    else:
                        if isinstance(_args[1], Mat4.Mat4):
                            if isinstance(_args[2], types.IntType):
                                return self.__overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLMatrix4f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                            else:
                                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> <Mat4.Mat4> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    def adjustXyz(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self.__overloaded_adjustXyz_ptrParametricCurveCollection_float_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            if numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.__overloaded_adjustXyz_ptrParametricCurveCollection_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

    def writeEgg(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self.__overloaded_writeEgg_ptrParametricCurveCollection_ptrFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        else:
            if numArgs == 2:
                import Filename
                if isinstance(_args[0], Filename.Filename):
                    if isinstance(_args[1], types.IntType):
                        return self.__overloaded_writeEgg_ptrParametricCurveCollection_ptrFilename___enum__CoordinateSystem(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
            else:
                if numArgs == 3:
                    import Ostream
                    if isinstance(_args[0], Ostream.Ostream):
                        import Filename
                        if isinstance(_args[1], Filename.Filename):
                            if isinstance(_args[2], types.IntType):
                                return self.__overloaded_writeEgg_ptrParametricCurveCollection_ptrOstream_ptrConstFilename___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                            else:
                                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
                    else:
                        raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
                else:
                    raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    def removeCurve(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import ParametricCurve
            if isinstance(_args[0], types.IntType):
                return self.__overloaded_removeCurve_ptrParametricCurveCollection_int(_args[0])
            else:
                if isinstance(_args[0], ParametricCurve.ParametricCurve):
                    return self.__overloaded_removeCurve_ptrParametricCurveCollection_ptrParametricCurve(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <ParametricCurve.ParametricCurve> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    def addCurve(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import ParametricCurve
            if isinstance(_args[0], ParametricCurve.ParametricCurve):
                return self.__overloaded_addCurve_ptrParametricCurveCollection_ptrParametricCurve(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <ParametricCurve.ParametricCurve> '
        else:
            if numArgs == 2:
                import ParametricCurve
                if isinstance(_args[0], ParametricCurve.ParametricCurve):
                    if isinstance(_args[1], types.IntType):
                        return self.__overloaded_addCurve_ptrParametricCurveCollection_ptrParametricCurve_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ParametricCurve.ParametricCurve> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '