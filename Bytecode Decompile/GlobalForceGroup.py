import ForceGroup

class GlobalForceGroup(ForceGroup.ForceGroup):
    __module__ = __name__

    def __init__(self, name=None):
        ForceGroup.ForceGroup.__init__(self, name)

    def addForce(self, force):
        ForceGroup.ForceGroup.addForce(force)
        if force.isLinear() == 0:
            base.addAngularIntegrator()
        if force.isLinear() == 1:
            physicsMgr.addLinearForce(force)
        else:
            physicsMgr.addAngularForce(force)

    def removeForce(self, force):
        ForceGroup.ForceGroup.removeForce(force)
        if force.isLinear() == 1:
            physicsMgr.removeLinearForce(force)
        else:
            physicsMgr.removeAngularForce(force)