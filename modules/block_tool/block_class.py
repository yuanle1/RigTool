import maya.cmds as mc

SHAPE_LIST = ['FK', 'IK', 'Spline', 'Finger', 'Root', 'Main', 'Head', 'Scapula', 'Sec', 'Aim', 'Bendy', 'Start',
              'Switch', 'Spline', 'SplineSec', 'Cv', 'Roll', 'Pivot', 'Pole', 'Gravity', 'Seed', 'Cross']
SEC_LIST = ['FKSec', 'IKSec', 'SplineSec']
SIDE_LIST = ['M', 'L', 'R']


class Block(object):
    def __init__(self, joint='', function='Child', side='M', mirror=True, orientX='Common',
                 orientY='Common', worldX=[1, 0, 0], worldY=[1, 0, 0], fat=1, parent=None, children=[], subdivide=0):
        self.joint = joint
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

        self.ik_start_block = None
        self.ik_middle_block = None
        self.ik_end_block = None
        self.ik_toe_block = None
        self.ik_toeEnd_block = None

        self.spline_start_block = None
        self.spline_middle_blocks = []
        self.spline_end_block = None

        self.fk_start_block = None
        self.fk_blocks = []

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
        self.is_finger = False
        self.start_finger = ''
        self.thumb_blocks = []
        self.index_blocks = []
        self.middle_blocks = []
        self.ring_blocks = []
        self.pinky_blocks = []



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

    def getIKStartBlock(self):
        return self.ik_start_block

    def getIKStartJoint(self):
        if self.ik_start_block:
            return self.ik_start_block.getJoint()
        else:
            return None

    def getIKMiddleBlock(self):
        return self.ik_middle_block

    def getIKMiddleJoint(self):
        if self.ik_middle_block:
            return self.ik_middle_block.getJoint()
        else:
            return None

    def getIKEndBlock(self):
        return self.ik_end_block

    def getIKEndJoint(self):
        if self.ik_end_block:
            return self.ik_end_block.getJoint()
        else:
            return None

    def getSplineStartBlock(self):
        return self.spline_start_block

    def getSplineStartJoint(self):
        if self.spline_start_block:
            return self.spline_start_block.getJoint()
        else:
            return None

    def getSplineMiddleBlocks(self):
        return self.spline_middle_blocks

    def getSplineMiddleJoints(self):
        return [block.getJoint() for block in self.spline_middle_blocks]

    def getSplineEndBlock(self):
        return self.spline_end_block

    def getSplineEndJoint(self):
        if self.spline_end_block:
            return self.spline_end_block.getJoint()
        else:
            return None

    def setIKStartBlock(self, ik_start_block):
        self.ik_start_block = ik_start_block

    def setIKMiddleBlock(self, ik_middle_block):
        self.ik_middle_block = ik_middle_block

    def setIKEndBlock(self, ik_end_block):
        self.ik_end_block = ik_end_block

    def setIKToeBlock(self, ik_toe_block):
        self.ik_toe_block = ik_toe_block

    def getIKToeBlock(self):
        return self.ik_toe_block

    def getIKToeJoint(self):
        if self.ik_toe_block:
            return self.ik_toe_block.getJoint()
        else:
            return None

    def setIKToeEndBlock(self, ik_toeEnd_block):
        self.ik_toeEnd_block = ik_toeEnd_block

    def getIKToeEndBlock(self):
        return self.ik_toeEnd_block

    def getIKToeEndJoint(self):
        if self.ik_toeEnd_block:
            return self.ik_toeEnd_block.getJoint()
        else:
            return None

    def setSplineStartBlock(self, spline_start_block):
        self.spline_start_block = spline_start_block

    def setSplineMiddleBlocks(self, spline_middle_blocks):
        self.spline_middle_blocks = spline_middle_blocks

    def setSplineEndBlock(self, spline_end_block):
        self.spline_end_block = spline_end_block

    def getFKStartBlock(self):
        return self.fk_start_block

    def getFKStartJoint(self):
        if self.fk_start_block:
            return self.fk_start_block.getJoint()
        else:
            return None

    def setFKStartBlock(self, fk_start_block):
        self.fk_start_block = fk_start_block

    def getFKBlocks(self):
        return self.fk_blocks

    def getFKJoints(self):
        return [block.getJoint() for block in self.fk_blocks]

    def setFKBlocks(self, fk_blocks):
        self.fk_blocks = fk_blocks

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

    def setIsFinger(self, is_finger):
        self.is_finger = is_finger

    def getIsFinger(self):
        return self.is_finger

    def setStartFinger(self, start_finger):
        self.start_finger = start_finger

    def getStartFinger(self):
        return self.start_finger

    def setThumbBlocks(self, thumb_blocks):
        self.thumb_blocks = thumb_blocks

    def getThumbBlock(self):
        return self.thumb_blocks

    def setIndexBlocks(self, index_blocks):
        self.index_blocks = index_blocks

    def getIndexBlock(self):
        return self.index_blocks

    def setMiddleBlocks(self, middle_blocks):
        self.middle_blocks = middle_blocks

    def getMiddleBlock(self):
        return self.middle_blocks

    def setRingBlocks(self, ring_blocks):
        self.ring_blocks = ring_blocks

    def getRingBlock(self):
        return self.ring_blocks

    def setPinkyBlocks(self, pinky_blocks):
        self.pinky_blocks = pinky_blocks

    def getPinkyBlocks(self):
        return self.pinky_blocks


class FKBlock(Block):
    def __init__(self, name='', segScaleComp=True, secondControl=True, fkShape='FK', secShape='FKSec', *args, **kwargs):
        super(FKBlock, self).__init__(*args, **kwargs)
        self.name = name
        self.segScaleComp = segScaleComp
        self.secondControl = secondControl
        self.fkShape = fkShape
        self.secShape = secShape

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        mc.setAttr(self.joint + '.name', name, type='string')

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
    def __init__(self, name='', segScaleComp=True, secondControl=True, ikShape='IK', fkShape='FK', secShape='IKSec',
                 switch_pivot='', *args, **kwargs):
        super(IKBlock, self).__init__(*args, **kwargs)
        self.name = name
        self.segScaleComp = segScaleComp
        self.secondControl = secondControl
        self.ikShape = ikShape
        self.fkShape = fkShape
        self.secShape = secShape
        self.switch_pivot = switch_pivot

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        mc.setAttr(self.joint + '.name', name, type='string')

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

    def getSwitchPivot(self):
        return self.switch_pivot

    def setSwitchPivot(self, switch_pivot):
        mc.setAttr(self.joint + '.switchPivot', switch_pivot, type='string')
        self.switch_pviot = switch_pivot


class SplineBlock(Block):
    def __init__(self, name='', secondControl=True, splineShape='Spline', secShape='SplineSec', *args, **kwargs):
        super(SplineBlock, self).__init__(*args, **kwargs)
        self.name = name
        self.secondControl = secondControl
        self.splineShape = splineShape
        self.secShape = secShape

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        mc.setAttr(self.joint + '.name', name, type='string')

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


class EndBlock(Block):
    def __init__(self, *args, **kwargs):
        super(EndBlock, self).__init__(*args, **kwargs)


class ChildBlock(Block):
    def __init__(self, fkShape, *args, **kwargs):
        super(ChildBlock, self).__init__(*args, **kwargs)
        self.fkShape = fkShape

    def getFKShape(self):
        return self.fkShape

    def setFKShape(self, fkShape):
        mc.setAttr(self.joint + '.fkShape', fkShape)
        self.fkShape = SHAPE_LIST[fkShape]


class AimBlock(Block):
    def __init__(self, segScaleComp=True, *args, **kwargs):
        super(AimBlock, self).__init__(*args, **kwargs)
        self.segScaleComp = segScaleComp

    def getSegScaleComp(self):
        return self.segScaleComp

    def setSegScaleComp(self, ssc):
        mc.setAttr(self.joint + '.segScaleComp', ssc)
        self.segScaleComp = ssc


class HandBlock(Block):
    def __init__(self, name='', segScaleComp=False, fingerShape='Finger', fingerPivot='', thumbList=[], indexList=[],
                 middleList=[], ringList=[], pinkyList=[], *args, **kwargs):
        super(HandBlock, self).__init__(*args, **kwargs)
        self.name = name
        self.segScaleComp = segScaleComp
        self.fingerShape = fingerShape
        self.fingerPivot = fingerPivot
        self.thumbList = thumbList
        self.indexList = indexList
        self.middleList = middleList
        self.ringList = ringList
        self.pinkyList = pinkyList

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        mc.setAttr(self.joint + '.name', name, type='string')

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

    def setThumbList(self, thumbList):
        self.thumbList = thumbList
        mc.setAttr(self.joint + '.thumbList', ';'.join(thumbList), type='string')

    def getThumbList(self):
        return self.thumbList

    def setIndexList(self, indexList):
        self.indexList = indexList
        mc.setAttr(self.joint + '.indexList', ';'.join(indexList), type='string')

    def getIndexList(self):
        return self.indexList

    def setMiddleList(self, middleList):
        self.middleList = middleList
        mc.setAttr(self.joint + '.middleList', ';'.join(middleList), type='string')

    def getMiddleList(self):
        return self.middleList

    def setRingList(self, ringList):
        self.ringList = ringList
        mc.setAttr(self.joint + '.ringList', ';'.join(ringList), type='string')

    def getRingList(self):
        return self.ringList

    def setPinkyList(self, pinkyList):
        self.pinkyList = pinkyList
        mc.setAttr(self.joint + '.pinkyList', ';'.join(pinkyList), type='string')

    def getPinkyList(self):
        return self.pinkyList

    def setFingerPivot(self, fingerPivot):
        self.fingerPivot = fingerPivot
        mc.setAttr(self.joint + '.fingerPivot', fingerPivot, type='string')

    def getFingerPivot(self):
        return self.fingerPivot

class FootBlock(Block):
    def __init__(self, name='', segScaleComp=False, heel_pivot='', footOuter_pivot='', footInner_pivot='', *args,
                 **kwargs):
        super(FootBlock, self).__init__(*args, **kwargs)
        self.name = name
        self.segScaleComp = segScaleComp
        self.heel_pivot = heel_pivot
        self.footOuter_pivot = footOuter_pivot
        self.footInner_pivot = footInner_pivot

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        mc.setAttr(self.joint + '.name', name, type='string')

    def getSegScaleComp(self):
        return self.segScaleComp

    def setSegScaleComp(self, ssc):
        mc.setAttr(self.joint + '.segScaleComp', ssc)
        self.segScaleComp = ssc

    def getHeelPivot(self):
        return self.heel_pivot

    def setHeelPivot(self, heel_pivot):
        mc.setAttr(self.joint + '.heelPivot', heel_pivot, type='string')
        self.heel_pivot = heel_pivot

    def getFootInnerPivot(self):
        return self.footInner_pivot

    def setFootInnerPivot(self, footInner_pivot):
        mc.setAttr(self.joint + '.footInnerPivot', footInner_pivot, type='string')
        self.footInner_pivot = footInner_pivot

    def getFootOuterPivot(self):
        return self.footOuter_pivot

    def setFootOuterPivot(self, footOuter_pivot):
        mc.setAttr(self.joint + '.footOuterPivot', footOuter_pivot, type='string')
        self.footOuter_pivot = footOuter_pivot


class Deform:
    def __init__(self, block):
        self.is_mirror = False
        self.block = block
        self.parent_block = self.block.getParentBlock()
        self.side = self.block.getSide()
        self.block_joint = self.block.getJoint()
        self.deform_joint = self.side + '_' + self.block_joint + '_Jnt'
        self.blend_joint = self.side + '_' + self.block_joint + '_Blend_Jnt'
        self.fk_ctrl = self.side + '_' + self.block_joint + '_FK_Ctrl'
        self.aim_ctrl = self.side + '_' + self.block_joint + '_Aim_Ctrl'
        self.fkik_loc = self.side + '_' + self.block_joint + '_FKIK_Loc'
        if self.block.getIKStartBlock():
            self.ik_ctrl = self.side + '_' + self.block.getIKStartBlock().getName() + '_IK_Ctrl'
        else:
            self.ik_ctrl = ''
        if self.block.getIKStartBlock():
            self.switch_ctrl = self.side + '_' + self.block.getIKStartBlock().getName() + '_Switch_Ctrl'
        else:
            self.switch_ctrl = ''
        self.pole_ctrl = self.side + '_' + self.getName() + '_Pole_Ctrl'
        self.poleAim_grp = self.side + '_' + self.getName() + '_PoleAim_Grp'
        if self.parent_block:
            self.parent_side = self.parent_block.getSide()
            self.parent_function = self.parent_block.getFunction()
            self.block_parent_joint = self.parent_block.getJoint()
            self.deform_parent_joint = self.block.getParentBlock().getSide() + '_' + self.block.getParentBlock().getJoint() + '_Jnt'
            self.fk_parent_ctrl = self.parent_side + '_' + self.block_parent_joint + '_FK_Ctrl'
            self.fk_parent_joint = self.parent_side + '_' + self.block_parent_joint + '_FK_Jnt'
            self.ik_parent_joint = self.parent_side + '_' + self.block_parent_joint + '_IK_Jnt'

            if self.parent_block.getIKStartBlock():
                self.switch_parent_ctrl = self.side + '_' + self.parent_block.getIKStartBlock().getName() + '_Switch_Ctrl'
                self.fkik_parent_loc = self.side + '_' + self.block_parent_joint + '_FKIK_Loc'
            else:
                self.switch_parent_ctrl = ''
                self.fkik_parent_loc = ''
        else:
            self.parent_side = None
            self.parent_function = None
            self.deform_parent_joint = ''
            self.block_parent_joint = ''
            self.fk_parent_ctrl = ''
            self.fk_parent_joint = ''
            self.ik_parent_joint = ''
            self.switch_parent_ctrl = ''
            self.fkik_parent_loc = ''

        self.subdivide = self.block.getSubdivide()
        if self.parent_block:
            self.parent_subdivide = self.parent_block.getSubdivide()
        else:
            self.parent_subdivide = 0
        self.part_joints = [self.side + '_' + self.block_joint + 'Part{}'.format(i) + '_Jnt' for i in
                            range(1, self.subdivide + 1, 1)]
        self.part_parent_joints = [self.side + '_' + self.block_parent_joint + 'Part{}'.format(i) + '_Jnt' for i in
                                   range(1, self.parent_subdivide + 1, 1)]
        self.fk_joint = self.side + '_' + self.block_joint + '_FK_Jnt'
        self.ik_joint = self.side + '_' + self.block_joint + '_IK_Jnt'
        if not self.block.getFirstChild():
            self.block_child_joint = ''
            self.deform_child_joint = ''
            self.fk_child_joint = ''
            self.ik_child_joint = ''
            self.fkik_child_loc = ''
        else:
            self.block_child_joint = self.block.getFirstChild()
            self.deform_child_joint = self.block.getFirstChildSide() + '_' + self.block.getFirstChild() + '_Jnt'
            self.fk_child_joint = self.block.getFirstChildSide() + '_' + self.block.getFirstChild() + '_FK_Jnt'
            self.ik_child_joint = self.block.getFirstChildSide() + '_' + self.block.getFirstChild() + '_IK_Jnt'
            self.fkik_child_loc = self.block.getFirstChildSide() + '_' + self.block_child_joint + '_FKIK_Loc'

        self.function = block.getFunction()
        self.ik_solver = block.getIKSolver()

        self.fk_grp = None
        self.ik_grp = self.side + '_' + self.getName() + '_IK_Grp'
        self.spline_grp = self.side + '_' + self.getName() + '_Spline_Grp'

        self.thumb_blocks = block.getThumbBlock()
        self.index_blocks = block.getIndexBlock()
        self.middle_blocks = block.getMiddleBlock()
        self.ring_blocks = block.getRingBlock()
        self.pinky_blocks = block.getPinkyBlocks()

    def setIsMirror(self, is_mirror):
        self.is_mirror = is_mirror

    def getIsMirror(self):
        return self.is_mirror

    def getSide(self):
        return self.side

    def getName(self):
        if hasattr(self.block, 'getName'):
            return self.block.getName()
        else:
            return ''

    def getJoint(self):
        return self.block_joint

    def getBlendJoint(self):
        return self.blend_joint

    def getDeformJoint(self):
        return self.deform_joint

    def getDeformParentJoint(self):
        return self.deform_parent_joint

    def getDeformChildJoint(self):
        return self.deform_child_joint

    def getFKChildJoint(self):
        return self.fk_child_joint

    def getIKChildJoint(self):
        return self.ik_child_joint

    def getFKIKChildLoc(self):
        return self.fkik_child_loc

    def getFKIKParentLoc(self):
        return self.fkik_parent_loc

    def getSubdivide(self):
        return self.subdivide

    def getParentDivide(self):
        return self.parent_subdivide

    def getPartJoints(self):
        return self.part_joints

    def getPartParentJoints(self):
        return self.part_parent_joints

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

    def getAimCtrl(self):
        return self.aim_ctrl

    def getFKIKLoc(self):
        return self.fkik_loc

    def getPoleCtrl(self):
        return self.pole_ctrl

    def getPoleAimGrp(self):
        return self.poleAim_grp

    def getFKParentCtrl(self):
        return self.fk_parent_ctrl

    def getSwitchParentCtrl(self):
        return self.switch_parent_ctrl

    def getIKCtrl(self):
        return self.ik_ctrl

    def getSwitchCtrl(self):
        return self.switch_ctrl

    def getFKParentJoint(self):
        return self.fk_parent_joint

    def getIKParentJoint(self):
        return self.ik_parent_joint

    def getChildJoint(self):
        return self.block_child_joint

    def getParent(self):
        return self.block_parent_joint

    def getParentSide(self):
        return self.parent_side

    def getParentFunction(self):
        return self.parent_function

    def getIKToeJoint(self):
        if hasattr(self.block, 'getIKToeJoint'):
            return self.block.getIKToeJoint()
        else:
            return ''

    def getIKToeEndJoint(self):
        if hasattr(self.block, 'getIKToeEndJoint'):
            return self.block.getIKToeEndJoint()
        else:
            return ''

    def getSSC(self):
        return self.block.getSSCInstance()

    def getIKStartBlock(self):
        if hasattr(self.block, 'getIKStartBlock'):
            return self.block.getIKStartBlock()
        else:
            return ''

    def getIKStartJoint(self):
        if hasattr(self.block, 'getIKStartJoint'):
            return self.block.getIKStartJoint()
        else:
            return ''

    def getIKMiddleBlock(self):
        if hasattr(self.block, 'getIKMiddleBlock'):
            return self.block.getIKMiddleBlock()
        else:
            return ''

    def getIKMiddleJoint(self):
        if hasattr(self.block, 'getIKMiddleJoint'):
            return self.block.getIKMiddleJoint()
        else:
            return ''

    def getIKEndJoint(self):
        if hasattr(self.block, 'getIKEndJoint'):
            return self.block.getIKEndJoint()
        else:
            return ''

    def getIKEndBlock(self):
        return self.block.getIKEndBlock()

    def getFKGrp(self):
        return self.fk_grp

    def setFKGrp(self, fk_grp):
        self.fk_grp = fk_grp

    def getIKGrp(self):
        return self.ik_grp

    def setIKGrp(self, ik_grp):
        self.ik_grp = ik_grp

    def getSplineGrp(self):
        return self.spline_grp

    def setSplineGrp(self, spline_grp):
        self.spline_grp = spline_grp

    def getIKToeBlock(self):
        if hasattr(self.block, 'getIKToeBlock'):
            return self.block.getIKToeBlock()
        else:
            return None

    def getIKToeEndBlock(self):
        if hasattr(self.block, 'getIKToeEndBlock'):
            return self.block.getIKToeEndBlock()
        else:
            return None

    def getFootOuterPivot(self):
        if hasattr(self.block, 'getFootOuterPivot'):
            return self.block.getFootOuterPivot()
        else:
            return ''

    def getFootInnerPivot(self):
        if hasattr(self.block, 'getFootInnerPivot'):
            return self.block.getFootInnerPivot()
        else:
            return ''

    def getHeelPivot(self):
        if hasattr(self.block, 'getHeelPivot'):
            return self.block.getHeelPivot()
        else:
            return ''

    def getIsToe(self):
        if self.getIKToeBlock():
            if self.getIKToeBlock().getJoint() == self.block_joint:
                return True
        return False

    def getIsToeEnd(self):
        if self.getIKToeEndBlock():
            if self.getIKToeEndBlock().getJoint() == self.block_joint:
                return True
        return False

    def getSwitchPivot(self):
        if hasattr(self.block, 'getSwitchPivot'):
            return self.block.getSwitchPivot()
        else:
            return ''

    def getSplineStartBlock(self):
        if hasattr(self.block, 'getSplineStartBlock'):
            return self.block.getSplineStartBlock()
        else:
            return None

    def getSplineStartJoint(self):
        if hasattr(self.block, 'getSplineStartJoint'):
            return self.block.getSplineStartJoint()
        else:
            return ''

    def getSplineMiddleBlocks(self):
        if hasattr(self.block, 'getSplineMiddleBlocks'):
            return self.block.getSplineMiddleBlocks()
        else:
            return None

    def getSplineMiddleJoints(self):
        if hasattr(self.block, 'getSplineMiddleJoints'):
            return self.block.getSplineMiddleJoints()
        else:
            return []

    def getSplineEndBlock(self):
        if hasattr(self.block, 'getSplineEndBlock'):
            return self.block.getSplineEndBlock()
        else:
            return None

    def getSplineEndJoint(self):
        if hasattr(self.block, 'getSplineEndJoint'):
            return self.block.getSplineEndJoint()
        else:
            return ''

    def getThumbBlock(self):
        return self.thumb_blocks

    def getIndexBlocks(self):
        return self.index_blocks

    def getMiddleBlocks(self):
        return self.middle_blocks

    def getRingBlocks(self):
        return self.ring_blocks

    def getPinkyBlocks(self):
        return self.pinky_blocks

    def getFingerPivot(self):
        return self.block.getFingerPivot()