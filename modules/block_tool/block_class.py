import maya.cmds as mc

SHAPE_LIST = ['FK', 'IK', 'Spline', 'Finger', 'Root', 'Main']
SEC_LIST = ['FKSec', 'IKSec', 'SplineSec']
SIDE_LIST = ['M', 'L', 'R']


class Block(object):
    def __init__(self, joint='', name='Default', function='Child', side='M', mirror=True, orientX='Common',
                 orientY='Common', worldX=[1, 0, 0], worldY=[1, 0, 0], fat=1, parent=None, children=[], subdivide=0):
        self.joint = joint
        self.name = name
        self.function = function
        self.side = side
        self.mirror = mirror
        self.orientX = orientX
        self.worldX = worldX
        self.orientY = orientY
        self.worldY = worldY
        self.fat = fat
        self.parent = parent
        self.children = children
        self.parentBlock = None
        self.childrenBlock = []

        self.ik_start_joint = None
        self.ik_middle_joint = None
        self.ik_end_joint = None
        self.ik_toe_joint = None
        self.ik_toeEnd_joint = None

        self.spline_start_joint = None
        self.spline_middle_joints = []
        self.spline_end_joint = None

        self.fk_start_joint = None
        self.fk_joints = []

        self.ik_solver = None

        self.ssc_instance = True

        if children:
            self.first_child = children[0]
            self.first_child_side = ['M', 'L', 'R'][mc.getAttr(self.first_child + '.side')]
        else:
            self.first_child = None
            self.first_child_side = None
        self.subdivide = subdivide
        self.instance = True

    def getChildrenBlock(self):
        return self.childrenBlock

    def setChildrenBlock(self, blocks):
        self.childrenBlock = blocks

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
        self.worldX = worldX
        mc.setAttr(self.joint + '.worldX', worldX[0], worldX[1], worldX[2])

    def getWorldY(self):
        return self.worldY

    def setWorldY(self, worldY):
        self.worldY = worldY
        mc.setAttr(self.joint + '.worldY', worldY[0], worldY[1], worldY[2])

    def getFat(self):
        return self.fat

    def setFat(self, fat):
        self.fat = fat
        mc.setAttr(self.joint + '.fat', fat)

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

    def setIKToeJoint(self, ik_toe_joint):
        self.ik_toe_joint = ik_toe_joint

    def getIKToeJoint(self):
        return self.ik_toe_joint

    def setIKToeEndJoint(self, ik_toeEnd_joint):
        self.ik_toeEnd_joint = ik_toeEnd_joint

    def getIKToeEndJoint(self):
        return self.ik_toeEnd_joint

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

    def getFirstChildSide(self):
        return self.first_child_side

    def setFirstChildSide(self, side):
        self.first_child_side = side

    def setSubdivide(self, subdivide):
        mc.setAttr(self.joint + '.subdivide', subdivide)
        self.subdivide = subdivide

    def getSubdivide(self):
        return self.subdivide

    def setSSCInstance(self, ssc):
        self.ssc_instance = ssc

    def getSSCInstance(self):
        return self.ssc_instance

    def setInstance(self, instance):
        self.instance = instance

    def getInstance(self):
        return self.instance



class FKBlock(Block):
    def __init__(self, segScaleComp=True, secondControl=True, fkShape='FK', secShape='FKSec', *args, **kwargs):
        super(FKBlock, self).__init__(*args, **kwargs)
        self.segScaleComp = segScaleComp
        self.secondControl = secondControl
        self.fkShape = fkShape
        self.secShape = secShape

    def getSegScaleComp(self):
        return self.segScaleComp

    def setSegScaleComp(self, ssc):
        mc.setAttr(self.joint + '.segScaleComp', ssc)
        self.segScaleComp = ssc

    def getSecondControl(self):
        return self.secondControl

    def setSecondControl(self, secondControl):
        # print secondControl
        mc.setAttr(self.joint + '.secondControl', secondControl)
        self.secondControl = secondControl

    def getFKShape(self):
        return self.fkShape

    def setFKShape(self, fkShape):
        mc.setAttr(self.joint + '.fkShape', fkShape)
        self.fkShape = SHAPE_LIST[fkShape]

    def getSecShape(self):
        return self.secShape

    def setSecShape(self, secShape):
        mc.setAttr(self.joint + '.secShape', secShape)
        self.secShape = SEC_LIST[secShape]


class IKBlock(Block):
    def __init__(self, segScaleComp=True, secondControl=True, ikShape='IK', fkShape='FK', secShape='IKSec', *args, **kwargs):
        super(IKBlock, self).__init__(*args, **kwargs)
        self.segScaleComp = segScaleComp
        self.secondControl = secondControl
        self.ikShape = ikShape
        self.fkShape = fkShape
        self.secShape = secShape

    def getSegScaleComp(self):
        return self.segScaleComp

    def setSegScaleComp(self, ssc):
        mc.setAttr(self.joint + '.segScaleComp', ssc)
        self.segScaleComp = ssc

    def getSecondControl(self):
        return self.secondControl

    def setSecondControl(self, secondControl):
        mc.setAttr(self.joint + '.secondControl', secondControl)
        self.secondControl = secondControl

    def getIKShape(self):
        return self.ikShape

    def setIKShape(self, ikShape):
        mc.setAttr(self.joint + '.ikShape', ikShape)
        self.ikShape = SHAPE_LIST[ikShape]

    def getFKShape(self):
        return self.fkShape

    def setFKShape(self, fkShape):
        mc.setAttr(self.joint + '.fkShape', fkShape)
        self.fkShape = SHAPE_LIST[fkShape]

    def getSecShape(self):
        return self.secShape

    def setSecShape(self, secShape):
        mc.setAttr(self.joint + '.secShape', secShape)
        self.secShape = SEC_LIST[secShape]


class SplineBlock(Block):
    def __init__(self, secondControl=True, splineShape='Spline', secShape='SplineSec', *args, **kwargs):
        super(SplineBlock, self).__init__(*args, **kwargs)
        self.secondControl = secondControl
        self.splineShape = splineShape
        self.secShape = secShape

    def getSecondControl(self):
        return self.secondControl

    def setSecondControl(self, secondControl):
        mc.setAttr(self.joint + '.secondControl', secondControl)
        self.secondControl = secondControl

    def getSplineShape(self):
        return self.splineShape

    def setSplineShape(self, splineShape):
        mc.setAttr(self.joint + '.splineShape', splineShape)
        self.splineShape = SHAPE_LIST[splineShape]

    def getSecShape(self):
        return self.secShape

    def setSecShape(self, secShape):
        mc.setAttr(self.joint + '.secShape', secShape)
        self.secShape = SEC_LIST[secShape]


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
    def __init__(self, segScaleComp=True, fingerShape='Finger', *args, **kwargs):
        super(HandBlock, self).__init__(*args, **kwargs)
        self.segScaleComp = segScaleComp
        self.fingerShape = fingerShape

    def getSegScaleComp(self):
        return self.segScaleComp

    def setSegScaleComp(self, ssc):
        mc.setAttr(self.joint + '.segScaleComp', ssc)
        self.segScaleComp = ssc

    def getFKShape(self):
        return self.fingerShape

    def setFKShape(self, fingerShape):
        mc.setAttr(self.joint + '.fingerShape', fingerShape)
        self.fingerShape = SHAPE_LIST[fingerShape]
        # self.fingerShape = fingerShape


class FootBlock(Block):
    def __init__(self, segScaleComp=True, *args, **kwargs):
        super(FootBlock, self).__init__(*args, **kwargs)
        self.segScaleComp = segScaleComp

    def getSegScaleComp(self):
        return self.segScaleComp

    def setSegScaleComp(self, ssc):
        mc.setAttr(self.joint + '.segScaleComp', ssc)
        self.segScaleComp = ssc

class Deform:
    def __init__(self, block):
        self.block = block
        self.parent_block = self.block.getParentBlock()
        self.side = self.block.getSide()
        self.block_joint = self.block.getJoint()
        self.deform_joint = self.side + '_' + self.block_joint + '_Jnt'
        self.fk_ctrl = self.side + '_' + self.block_joint + '_FK_Ctrl'
        if self.parent_block:
            self.parent_side = self.parent_block.getSide()
            self.parent_function = self.parent_block.getFunction()
            self.block_parent_joint = self.parent_block.getJoint()
            self.deform_parent_joint = self.block.getParentBlock().getSide() + '_' + self.block.getParentBlock().getJoint() + '_Jnt'
            self.fk_parent_ctrl = self.parent_side + '_' + self.block_parent_joint + '_FK_Ctrl'
            self.fk_parent_joint = self.parent_side + '_' + self.block_parent_joint + '_FK_Jnt'
            self.ik_parent_joint = self.parent_side + '_' + self.block_parent_joint + '_IK_Jnt'
        else:
            self.parent_side = None
            self.parent_function = None
            self.deform_parent_joint = None
            self.block_parent_joint = None
            self.fk_parent_ctrl = None
            self.fk_parent_joint = None
            self.ik_parent_joint = None

        self.subdivide = self.block.getSubdivide()
        self.part_joints = [self.side + '_' + self.block_joint + '_Part{}'.format(i) + '_Jnt' for i in
                            range(1, self.subdivide + 1, 1)]
        self.fk_joint = self.side + '_' + self.block_joint + '_FK_Jnt'
        self.ik_joint = self.side + '_' + self.block_joint + '_IK_Jnt'
        if not self.block.getFirstChild():
            self.deform_child_joint = None
        else:
            self.deform_child_joint = self.block.getFirstChildSide() + '_' + self.block.getFirstChild() + '_Jnt'



        self.function = block.getFunction()
        self.ik_solver = block.getIKSolver()

        self.fk_grp = None
        self.ik_grp = self.side + '_' + self.block_joint + '_IK_Grp'
    def getSide(self):
        return self.side

    def getJoint(self):
        return self.block_joint

    def getDeformJoint(self):
        return self.deform_joint

    def getDeformParentJoint(self):
        return self.deform_parent_joint

    def getDeformChildJoint(self):
        return self.deform_child_joint

    def getSubdivide(self):
        return self.subdivide

    def getPartJoints(self):
        return self.part_joints

    def getFunction(self):
        return self.function

    def getIKSolver(self):
        return self.block.getIKSolver()

    def getFat(self):
        return self.block.getFat()

    def getFKShape(self):
        if hasattr(self.block, 'getFKShape'):
            return self.block.getFKShape()
        else:
            return 'FK'

    def getFKJoint(self):
        return self.fk_joint

    def getIKJoint(self):
        return self.ik_joint

    def getFKCtrl(self):
        return self.fk_ctrl

    def getFKParentCtrl(self):
        return self.fk_parent_ctrl
    def getFKParentJoint(self):
        return self.fk_parent_joint

    def getIKParentJoint(self):
        return self.ik_parent_joint
    def getParent(self):
        return self.block_parent_joint

    def getParentSide(self):
        return self.parent_side

    def getParentFunction(self):
        return self.parent_function

    def getIKToeJoint(self):
        return self.block.getIKToeJoint()

    def getSSC(self):
        return self.block.getSSCInstance()

    def getIKEndJoint(self):
        return self.block.getIKEndJoint()

    def getFKGrp(self):
        return self.fk_grp

    def setFKGrp(self, fk_grp):
        self.fk_grp = fk_grp

    def getIKGrp(self):
        return self.ik_grp

    def setIKGrp(self, ik_grp):
        self.ik_grp = ik_grp