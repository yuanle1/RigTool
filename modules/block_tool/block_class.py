import maya.cmds as mc
class Block(object):
    def __init__(self, joint='', name='Default', function='Child', side='M', mirror=True, orientX='Common', orientY='Common',
                 worldX=[1, 0, 0], worldY=[1, 0, 0], parent=None, children=[]):
        self.joint = joint
        self.name = name
        self.function = function
        self.side = side
        self.mirror = mirror
        self.orientX = orientX
        self.worldX = worldX
        self.orientY = orientY
        self.worldY = worldY
        self.parent = parent
        self.children = children
        self.parentBlock = None
        self.childrenBlock = []

        self.ik_start_joint = None
        self.ik_middle_joint = None
        self.ik_end_joint = None

        self.spline_start_joint = None
        self.spline_middle_joints = []
        self.spline_end_joint = None

        self.fk_start_joint = None
        self.fk_joints = []

        self.ik_solver = None
        if children:
            self.first_child = children[0]
        else:
            self.first_child = None

    def getChildrenBlock(self):
        return self.childrenBlock

    def addChildrenBlock(self, childBlock):
        self.childrenBlock.append(childBlock)

    def getParentBlock(self):
        return self.parentBlock

    def setParentBlock(self, parentBlock):
        self.parentBlock = parentBlock

    def getJoint(self):
        return self.joint

    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children

    def getFunction(self):
        return self.function

    def setFunction(self, function):
        self.function = function
        mc.setAttr(self.joint + '.otherType', function, type='string')

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side
        side_list = ['M', 'L', 'R']
        mc.setAttr(self.joint + '.side', side_list.index(side))

    def getMirror(self):
        return self.mirror

    def setMirror(self, mirror):
        self.mirror = mirror
        mc.setAttr(self.joint + '.mirror', mirror)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        mc.setAttr(self.joint + '.name', name)

    def getOrientX(self):
        return self.orientX

    def setOrientX(self, orientX):
        self.orientX = orientX
        orient_list = ['Common', 'Parent', 'Free', 'World']
        mc.setAttr(self.joint + '.orientX', orient_list.index(orientX))

    def getOrientY(self):
        return self.orientY

    def setOrientY(self, orientY):
        self.orientY = orientY
        orient_list = ['Common', 'Parent', 'Free', 'World']
        mc.setAttr(self.joint + '.orientY', orient_list.index(orientY))

    def getWorldX(self):
        return self.worldX

    def setWorldX(self, worldX):
        print worldX
        self.worldX = worldX
        mc.setAttr(self.joint + '.worldX', worldX[0], worldX[1], worldX[2])

    def getWorldY(self):
        return self.worldY

    def setWorldY(self, worldY):
        self.worldY = worldY
        mc.setAttr(self.joint + '.worldY', worldY[0], worldY[1], worldY[2])

    def getIKStartJoint(self):
        return self.ik_start_joint

    def getIKMiddleJoint(self):
        return self.ik_middle_joint

    def getIKEndJoint(self):
        return self.ik_end_joint

    def getSplineStartJoint(self):
        return self.spline_start_joint

    def getSplineMiddleJoints(self):
        return self.spline_middle_joints

    def getSplineEndJoint(self):
        return self.spline_end_joint

    def setIKStartJoint(self, ik_start_joint):
        self.ik_start_joint = ik_start_joint

    def setIKMiddleJoint(self, ik_middle_joint):
        self.ik_middle_joint = ik_middle_joint

    def setIKEndJoint(self, ik_end_joint):
        self.ik_end_joint = ik_end_joint

    def setSplineStartJoint(self, spline_start_joint):
        self.spline_start_joint = spline_start_joint

    def setSplineMiddleJoints(self, spline_middle_joints):
        self.spline_middle_joints = spline_middle_joints

    def addSplineMiddleJoints(self, spline_middle_joint):
        self.spline_middle_joints.append(spline_middle_joint)

    def setSplineEndJoint(self, spline_end_joint):
        self.spline_end_joint = spline_end_joint

    def getFKStartJoint(self):
        return self.fk_start_joint

    def setFKStartJoint(self, fk_start_joint):
        self.fk_start_joint = fk_start_joint

    def getFKJoints(self):
        return self.fk_joints

    def setFKJoints(self, fk_joints):
        self.fk_joints = fk_joints

    def getIKSolver(self):
        return self.ik_solver

    def setIKSolver(self, ik_solver):
        self.ik_solver = ik_solver

    def getFirstChild(self):
        return self.first_child

    def setFirstChild(self, first_child):
        return self.first_child

class FKBlock(Block):
    def __init__(self, secondControl=True, subdivide=2, fkShape='FK', secShape='FKSec', *args, **kwargs):
        super(FKBlock, self).__init__(*args, **kwargs)
        self.secondControl = secondControl
        self.subdivide = subdivide
        self.fkShape = fkShape
        self.secShape = secShape

    def getSecondControl(self):
        return self.secondControl

    def setSecondControl(self, secondControl):
        self.secondControl = secondControl

    def getSubdivide(self):
        return self.subdivide

    def setSubdivide(self, subdivide):
        self.subdivide = subdivide

    def getFKShape(self):
        return self.fkShape

    def setFKShape(self, fkShape):
        self.fkShape = fkShape

    def getSecShape(self):
        return self.secShape

    def setSecShape(self, secShape):
        self.secShape = secShape

class IKBlock(Block):
    def __init__(self, secondControl=True, subdivide=2, ikShape='IK', secShape='IKSec', *args, **kwargs):
        super(IKBlock, self).__init__(*args, **kwargs)
        self.secondControl = secondControl
        self.subdivide = subdivide
        self.splineShape = ikShape
        self.secShape = secShape

        self.ik_start_joint = self.joint
        self.ik_middle_joint = None
        self.ik_end_joint = None



    def firstChild(self):
        pass

    def getSecondControl(self):
        return self.secondControl

    def setSecondControl(self, secondControl):
        self.secondControl = secondControl

    def getSubdivide(self):
        return self.subdivide

    def setSubdivide(self, subdivide):
        self.subdivide = subdivide

    def getIKShape(self):
        return self.ikShape

    def setIKShape(self, ikShape):
        self.ikShape = ikShape

    def getSecShape(self):
        return self.secShape

    def setSecShape(self, secShape):
        self.secShape = secShape

class SplineBlock(Block):
    def __init__(self, secondControl=True, subdivide=2, splineShape='Spline', secShape='SplineSec', *args, **kwargs):
        super(SplineBlock, self).__init__(*args, **kwargs)
        self.secondControl = secondControl
        self.subdivide = subdivide
        self.splineShape = splineShape
        self.secShape = secShape

        self.spline_start = self.joint
        self.spline_middle = []
        self.spline_end = None

    def getSecondControl(self):
        return self.secondControl

    def setSecondControl(self, secondControl):
        self.secondControl = secondControl

    def getSubdivide(self):
        return self.subdivide

    def setSubdivide(self, subdivide):
        self.subdivide = subdivide

    def getSplineShape(self):
        return self.splineShape

    def setSplineShape(self, splineShape):
        self.splineShape = splineShape

    def getSecShape(self):
        return self.secShape

    def setSecShape(self, secShape):
        self.secShape = secShape

class AimBlock(Block):
    pass

class EndBlock(Block):
    def __init__(self, *args, **kwargs):
        super(EndBlock, self).__init__(*args, **kwargs)

class ChildBlock(Block):
    def __init__(self, *args, **kwargs):
        super(ChildBlock, self).__init__(*args, **kwargs)











class EyeBlock(Block):
    pass

class HandBlock(Block):
    pass

class FootBlock(Block):
    pass