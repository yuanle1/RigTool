#!/usr/bin/env python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import block_class
import math

reload(block_class)
from modules import maya_utilities as maya_utilities

SHAPE_LIST = ['FK', 'IK', 'Spline', 'Finger', 'Root', 'Main', 'Head', 'Scapula', 'Sec', 'Aim', 'Bendy', 'Start',
              'Switch', 'Spline', 'SplineSec', 'Cv', 'Roll', 'Pivot', 'Pole', 'Gravity', 'Seed', 'Cross']
SEC_LIST = ['FKSec', 'IKSec', 'SplineSec']
SIDE_LIST = ['M', 'L', 'R']


# 确认block属性
def ensureBlockAttrs(block):
    side_list = ['M', 'L', 'R']
    side = getBlockSide(block)

    if mc.getAttr(block + '.side') == 3:
        mc.setAttr(block + '.side', side_list.index(side))

    side = side_list[mc.getAttr(block + '.side')]
    if not mc.objExists(block + '.mirror'):
        mc.addAttr(block, ln='mirror', attributeType='bool')
        if side == 'M':
            mc.setAttr(block + '.mirror', False)
        else:
            mc.setAttr(block + '.mirror', True)

    if not mc.objExists(block + '.orientX'):
        mc.addAttr(block, ln='orientX', sn='ox', attributeType='enum', enumName='Common:Parent:Free:World')
    if not mc.objExists(block + '.worldX'):
        mc.addAttr(block, ln='worldX', sn='wx', attributeType='double3')
        mc.addAttr(block, ln='worldXX', sn='wxx', attributeType='double', p='worldX')
        mc.addAttr(block, ln='worldXY', sn='wxy', attributeType='double', p='worldX')
        mc.addAttr(block, ln='worldXZ', sn='wxz', attributeType='double', p='worldX')
        mc.setAttr(block + '.worldXX', 1.00)
        mc.setAttr(block + '.worldXY', 0.00)
        mc.setAttr(block + '.worldXZ', 0.00)
    if not mc.objExists(block + '.orientY'):
        mc.addAttr(block, ln='orientY', sn='oy', attributeType='enum', enumName='Common:Parent:Free:World')
    if not mc.objExists(block + '.worldY'):
        mc.addAttr(block, ln='worldY', sn='wy', attributeType='double3')
        mc.addAttr(block, ln='worldYX', sn='wyx', attributeType='double', p='worldY')
        mc.addAttr(block, ln='worldYY', sn='wyy', attributeType='double', p='worldY')
        mc.addAttr(block, ln='worldYZ', sn='wyz', attributeType='double', p='worldY')
        mc.setAttr(block + '.worldYX', 0.00)
        mc.setAttr(block + '.worldYY', 1.00)
        mc.setAttr(block + '.worldYZ', 0.00)
    if not mc.objExists(block + '.fat'):
        mc.addAttr(block, ln='fat', attributeType='double', min=0, dv=1)

    block_type_list = [None, 'FK', 'IK', 'Spline', 'Aim', 'Child', 'End', 'Hand', 'Foot']
    joint_label = mc.getAttr(block + '.type')
    if joint_label == 18:
        joint_type = mc.getAttr(block + '.otherType')
        if joint_type == 'Chest' or joint_type == 'chest':
            mc.setAttr(block + '.otherType', 'FK', )
        elif not joint_type in block_type_list:
            if mc.listRelatives(block, type='joint'):
                mc.setAttr(block + '.otherType', 'Child', type='string')
            else:
                mc.setAttr(block + '.otherType', 'End', type='string')
    else:
        mc.setAttr(block + '.type', 18)
        if joint_label == 2 or joint_label == 10:
            mc.setAttr(block + '.otherType', 'IK', type='string')
        elif joint_label == 4:
            mc.setAttr(block + '.otherType', 'Foot', type='string')
        # elif joint_label == 5:
        #     mc.setAttr(block + '.otherType', 'Toe', type='string')
        elif joint_label == 6:
            mc.setAttr(block + '.otherType', 'Spline', type='string')
        elif joint_label == 12:
            mc.setAttr(block + '.otherType', 'Hand', type='string')
        else:
            if mc.listRelatives(block, type='joint'):
                mc.setAttr(block + '.otherType', 'Child', type='string')
            else:
                mc.setAttr(block + '.otherType', 'End', type='string')

    block_type = mc.getAttr(block + '.otherType')
    mc.setAttr(block + '.overrideEnabled', True)
    mc.setAttr(block + '.overrideRGBColors', 1)
    if not mc.objExists(block + '.subdivide'):
        mc.addAttr(block, ln='subdivide', sn='subdivide', attributeType='long', dv=0)
    if block_type == 'FK':
        if not mc.objExists(block + '.name'):
            mc.addAttr(block, ln='name', sn='n', dataType='string')
            mc.setAttr(block + '.name', '', type='string')
        if not mc.objExists(block + '.segScaleComp'):
            mc.addAttr(block, ln='segScaleComp', attributeType='bool', dv=True)
        if not mc.objExists(block + '.secondControl'):
            mc.addAttr(block, ln='secondControl', sn='secControl', attributeType='bool', dv=True)
        if not mc.objExists(block + '.fkShape'):
            mc.addAttr(block, ln='fkShape', sn='fkShape', attributeType='enum', enumName=':'.join(SHAPE_LIST))
            mc.setAttr(block + '.fkShape', 0)
        if not mc.objExists(block + '.secShape'):
            mc.addAttr(block, ln='secShape', sn='secShape', attributeType='enum', enumName=':'.join(SEC_LIST))
            mc.setAttr(block + '.secShape', 0)
        mc.setAttr(block + '.overrideColorRGB', 116 / 255.0, 185 / 255.0, 255 / 255.0)

    elif block_type == 'IK':
        if not mc.objExists(block + '.name'):
            mc.addAttr(block, ln='name', sn='n', dataType='string')
            mc.setAttr(block + '.name', '', type='string')
        if not mc.objExists(block + '.segScaleComp'):
            mc.addAttr(block, ln='segScaleComp', attributeType='bool', dv=True)
        if not mc.objExists(block + '.secondControl'):
            mc.addAttr(block, ln='secondControl', sn='secControl', attributeType='bool', dv=True)
        if not mc.objExists(block + '.ikShape'):
            mc.addAttr(block, ln='ikShape', sn='ikShape', attributeType='enum', enumName=':'.join(SHAPE_LIST))
            mc.setAttr(block + '.ikShape', 1)
        if not mc.objExists(block + '.fkShape'):
            mc.addAttr(block, ln='fkShape', sn='fkShape', attributeType='enum', enumName=':'.join(SHAPE_LIST))
            mc.setAttr(block + '.ikShape', 0)
        if not mc.objExists(block + '.secShape'):
            mc.addAttr(block, ln='secShape', sn='secShape', attributeType='enum', enumName=':'.join(SEC_LIST))
            mc.setAttr(block + '.secShape', 1)
        if not mc.objExists(block + '.switchPivot'):
            mc.addAttr(block, ln='switchPivot', dataType='string')
            mc.setAttr(block + '.switchPivot', '', type='string')
        mc.setAttr(block + '.overrideColorRGB', 255 / 255.0, 118 / 255.0, 117 / 255.0)

    elif block_type == 'Spline':
        if not mc.objExists(block + '.name'):
            mc.addAttr(block, ln='name', sn='n', dataType='string')
            mc.setAttr(block + '.name', '', type='string')
        if not mc.objExists(block + '.secondControl'):
            mc.addAttr(block, ln='secondControl', sn='secControl', attributeType='bool', dv=True)
        if not mc.objExists(block + '.splineShape'):
            mc.addAttr(block, ln='splineShape', sn='splineShape', attributeType='enum', enumName=':'.join(SHAPE_LIST))
            mc.setAttr(block + '.splineShape', 2)
        if not mc.objExists(block + '.secShape'):
            mc.addAttr(block, ln='secShape', sn='secShape', attributeType='enum', enumName=':'.join(SEC_LIST))
            mc.setAttr(block + '.secShape', 2)
        mc.setAttr(block + '.overrideColorRGB', 253 / 255.0, 203 / 255.0, 110 / 255.0)

    elif block_type == 'Aim':
        if not mc.objExists(block + '.segScaleComp'):
            mc.addAttr(block, ln='segScaleComp', attributeType='bool', dv=False)
        mc.setAttr(block + '.overrideColorRGB', 198 / 255.0, 160 / 255.0, 230 / 255.0)

    elif block_type == 'Hand':
        if not mc.objExists(block + '.name'):
            mc.addAttr(block, ln='name', sn='n', dataType='string')
            mc.setAttr(block + '.name', '', type='string')
        if not mc.objExists(block + '.segScaleComp'):
            mc.addAttr(block, ln='segScaleComp', attributeType='bool', dv=False)
        if not mc.objExists(block + '.fingerShape'):
            mc.addAttr(block, ln='fingerShape', sn='fingerShape', attributeType='enum', enumName=':'.join(SHAPE_LIST))
            mc.setAttr(block + '.fingerShape', 3)
        if not mc.objExists(block + '.fingerPivot'):
            mc.addAttr(block, ln='fingerPivot', dataType='string')
        if not mc.objExists(block + '.thumbList'):
            thumb_list = []
            mc.addAttr(block, ln='thumbList', dataType='string')
            mc.select(block, hi=True)
            for joint in mc.ls(sl=True, type='joint'):
                if 'thumb' in joint or 'Thumb' in joint:
                    thumb_list.append(joint)
            if len(thumb_list) > 2:
                mc.setAttr(block + '.thumbList', ';'.join(thumb_list), type='string')
            else:
                mc.setAttr(block + '.thumbList', '', type='string')
        if not mc.objExists(block + '.indexList'):
            index_list = []
            mc.addAttr(block, ln='indexList', dataType='string')
            mc.select(block, hi=True)
            for joint in mc.ls(sl=True, type='joint'):
                if 'index' in joint or 'Index' in joint:
                    index_list.append(joint)
            if len(index_list) > 2:
                mc.setAttr(block + '.indexList', ';'.join(index_list), type='string')
            else:
                mc.setAttr(block + '.indexList', '', type='string')
        if not mc.objExists(block + '.middleList'):
            middle_list = []
            mc.addAttr(block, ln='middleList', dataType='string')
            mc.select(block, hi=True)
            for joint in mc.ls(sl=True, type='joint'):
                if 'middle' in joint or 'Middle' in joint:
                    middle_list.append(joint)
            if len(middle_list) > 2:
                mc.setAttr(block + '.middleList', ';'.join(middle_list), type='string')
            else:
                mc.setAttr(block + '.middleList', '', type='string')
        if not mc.objExists(block + '.ringList'):
            ring_list = []
            mc.addAttr(block, ln='ringList', dataType='string')
            mc.select(block, hi=True)
            for joint in mc.ls(sl=True, type='joint'):
                if 'ring' in joint or 'Ring' in joint:
                    ring_list.append(joint)
            if len(ring_list) > 2:
                mc.setAttr(block + '.ringList', ';'.join(ring_list), type='string')
            else:
                mc.setAttr(block + '.ringList', '', type='string')
        if not mc.objExists(block + '.pinkyList'):
            pinky_list = []
            mc.addAttr(block, ln='pinkyList', dataType='string')
            mc.select(block, hi=True)
            for joint in mc.ls(sl=True, type='joint'):
                if 'pinky' in joint or 'Pinky' in joint:
                    pinky_list.append(joint)
            if len(pinky_list) > 2:
                mc.setAttr(block + '.pinkyList', ';'.join(pinky_list), type='string')
            else:
                mc.setAttr(block + '.pinkyList', '', type='string')
        mc.setAttr(block + '.overrideColorRGB', 255 / 255.0, 118 / 255.0, 117 / 255.0)


    elif block_type == 'Foot':
        if not mc.objExists(block + '.name'):
            mc.addAttr(block, ln='name', sn='n', dataType='string')
            mc.setAttr(block + '.name', '', type='string')
        if not mc.objExists(block + '.segScaleComp'):
            mc.addAttr(block, ln='segScaleComp', attributeType='bool', dv=False)
        if not mc.objExists(block + '.heelPivot'):
            mc.addAttr(block, ln='heelPivot', dataType='string')
            mc.setAttr(block + '.heelPivot', '', type='string')
        if not mc.objExists(block + '.footInnerPivot'):
            mc.addAttr(block, ln='footInnerPivot', dataType='string')
            mc.setAttr(block + '.footInnerPivot', '', type='string')
        if not mc.objExists(block + '.footOuterPivot'):
            mc.addAttr(block, ln='footOuterPivot', dataType='string')
            mc.setAttr(block + '.footOuterPivot', '', type='string')

        mc.setAttr(block + '.overrideColorRGB', 255 / 255.0, 118 / 255.0, 117 / 255.0)
    # elif block_type == 'Toe':
    #     mc.setAttr(block + '.overrideColorRGB', 255 / 255.0, 118 / 255.0, 117 / 255.0)
    elif block_type == 'End':
        mc.setAttr(block + '.overrideColorRGB', 255 / 255.0, 255 / 255.0, 255 / 255.0)
    elif block_type == 'Child':
        parent = mc.listRelatives(block, p=True)
        if not parent:
            mc.setAttr(block + '.overrideEnabled', False)
        elif mc.getAttr(parent[0] + '.otherType') in ['Hand', 'Aim']:
            mc.setAttr(block + '.overrideColorRGB', 116 / 255.0, 185 / 255.0, 255 / 255.0)
        else:
            parent = parent[0]
            color = mc.getAttr(parent + '.overrideColorRGB')[0]
            mc.setAttr(block + '.overrideColorRGB', color[0], color[1], color[2])

        if not mc.objExists(block + '.fkShape'):
            mc.addAttr(block, ln='fkShape', sn='fkShape', attributeType='enum', enumName=':'.join(SHAPE_LIST))
            mc.setAttr(block + '.fkShape', 0)


# 确认Block属性
def ensureAllBlockAttrs():
    if not mc.objExists('Block'):
        return
    if not mc.objExists('Block.name'):
        mc.addAttr('Block', ln='name', sn='n', dataType='string')
        mc.setAttr('Block.n', 'Main', type='string')
    if not mc.objExists('Block.mainCount'):
        mc.addAttr('Block', ln='mainCount', attributeType='long', dv=1)
    if not mc.objExists('Block.rootControl'):
        mc.addAttr('Block', ln='rootControl', attributeType='bool', dv=True)
    if not mc.objExists('Block.gravityControl'):
        mc.addAttr('Block', ln='gravityControl', attributeType='bool', dv=True)

    mc.select('Block', hi=True)
    block_joints = mc.ls(sl=True, type='joint')
    for block_joint in block_joints:
        ensureBlockAttrs(block_joint)


def clearBlockAttr(block):
    block_joint = block.getJoint()
    for attr in mc.listAttr(block_joint, ud=True):
        if mc.attributeQuery(attr, node=block_joint, exists=True):
            mc.deleteAttr(block_joint + '.' + attr)


def ensureBlockInfo(block):
    # mirror
    side = block.getSide()
    mirror = block.getMirror()
    # 父骨骼mirror子骨骼部mirror
    if not side == 'M':
        if not mirror:
            block.setInstance(False)
        else:
            if block.getParentBlock():
                if block.getParentBlock().getSide() != 'M' and not block.getParentBlock().getInstance():
                    block.setInstance(False)

    # function
    function = block.getFunction()
    if function == 'IK':
        for block_child in block.getChildrenBlock():
            if block_child.getFunction() == 'Child':
                for block_child_child in block_child.getChildrenBlock():
                    if block_child_child.getFunction() in ['Hand', 'Foot', 'FK', 'Spline', 'End', 'IK', 'Aim']:
                        block.setIKStartBlock(block)
                        block.setIKMiddleBlock(block_child)
                        block.setIKEndBlock(block_child_child)
                        block.setIKSolver('IKRPSolver')
                        block.setFirstChild(block_child.getJoint())
                        block.setFirstChildSide(['M', 'L', 'R'][mc.getAttr(block_child.getJoint() + '.side')])

                        block_child.setIKStartBlock(block)
                        block_child.setIKMiddleBlock(block_child)
                        block_child.setIKEndBlock(block_child_child)
                        block_child.setIKSolver('IKRPSolver')
                        block_child.setFirstChild(block_child_child.getJoint())
                        block_child.setFirstChildSide(['M', 'L', 'R'][mc.getAttr(block_child.getJoint() + '.side')])
                        # block_child.setSubdivide(block.getSubdivide())

                        block_child_child.setIKStartBlock(block)
                        block_child_child.setIKMiddleBlock(block_child)
                        block_child_child.setIKEndBlock(block_child_child)
                        block_child_child.setIKSolver('IKRPSolver')

                        segScaleComp = block.getSegScaleComp()
                        block_child.setSSCInstance(segScaleComp)
                        break

    elif function == 'Spline':
        spline_child_blocks = []
        spline_end_block = iterateSpline(block, spline_child_blocks)
        if spline_child_blocks and spline_end_block:
            block.setSplineStartBlock(block)
            block.setSplineMiddleBlocks(spline_child_blocks)
            block.setSplineEndBlock(spline_end_block)
            block.setIKSolver('SplineSolver')

            for spline_child_block in spline_child_blocks:
                spline_child_block.setSplineStartBlock(block)
                spline_child_block.setSplineMiddleBlocks(spline_child_block)
                spline_child_block.setSplineEndBlock(spline_end_block)
                spline_child_block.setIKSolver('SplineSolver')
                # spline_child_block.setSubdivide(block.getSubdivide())

            spline_end_block.setSplineStartBlock(block)
            spline_end_block.setSplineMiddleBlocks(spline_child_blocks)
            spline_end_block.setSplineEndBlock(spline_end_block)
            spline_end_block.setIKSolver('SplineSolver')


    elif function in ['FK', 'Hand', 'Foot', 'Aim']:
        fk_child_blocks = []
        for block_child in block.getChildrenBlock():
            iterateFK(block_child, fk_child_blocks)

        block.setFKStartBlock(block)
        block.setFKBlocks(fk_child_blocks)
        segScaleComp = block.getSegScaleComp()
        if block.getIKSolver() != 'IKRPSolver' and block.getIKSolver() != 'SplineSolver':
            block.setIKSolver('FK')
        for fk_child_block in fk_child_blocks:
            fk_child_block.setFKStartBlock(block)
            fk_child_block.setFKBlocks(fk_child_blocks)
            fk_child_block.setIKSolver('FK')
            fk_child_block.setSSCInstance(segScaleComp)

        if function == 'Foot':
            for child_block in block.getChildrenBlock():
                if child_block.getFunction() == 'Child':
                    for child_child_block in child_block.getChildrenBlock():
                        if child_child_block.getFunction() == 'End':
                            block.setIKToeBlock(child_block)
                            block.setIKToeEndBlock(child_child_block)
                            child_block.setIKToeBlock(child_block)
                            child_block.setIKToeEndBlock(child_child_block)
                            child_child_block.setIKToeBlock(child_block)
                            child_child_block.setIKToeEndBlock(child_child_block)
                            child_block.setSSCInstance(segScaleComp)

                            child_block.setIKStartBlock(block.getIKStartBlock())
                            child_child_block.setIKStartBlock(block.getIKStartBlock())
                            break

    if function == 'Hand':
        thumb_blocks = []
        thumb_ist = block.getThumbList()
        for block_child in block.getChildrenBlock():
            iterateFinger(block_child, thumb_blocks, thumb_ist)
        block.setThumbBlocks(thumb_blocks)
        for thumb_block in thumb_blocks:
            thumb_block.setStartFinger(thumb_blocks[0])

        index_blocks = []
        index_ist = block.getIndexList()
        for block_child in block.getChildrenBlock():
            iterateFinger(block_child, index_blocks, index_ist)
        block.setIndexBlocks(index_blocks)
        for index_block in index_blocks:
            index_block.setStartFinger(index_blocks[0])

        middle_blocks = []
        middle_list = block.getMiddleList()
        for block_child in block.getChildrenBlock():
            iterateFinger(block_child, middle_blocks, middle_list)
        block.setMiddleBlocks(middle_blocks)
        for middle_block in middle_blocks:
            middle_block.setStartFinger(middle_blocks[0])

        ring_blocks = []
        ring_list = block.getRingList()
        for block_child in block.getChildrenBlock():
            iterateFinger(block_child, ring_blocks, ring_list)
        block.setRingBlocks(ring_blocks)
        for ring_block in ring_blocks:
            ring_block.setStartFinger(ring_blocks[0])

        pinky_blocks = []
        pinky_list = block.getPinkyList()
        for block_child in block.getChildrenBlock():
            iterateFinger(block_child, pinky_blocks, pinky_list)
        block.setPinkyBlocks(pinky_blocks)
        for pinky_block in pinky_blocks:
            pinky_block.setStartFinger(pinky_blocks[0])

def iterateSpline(block, spline_child_blocks):
    if block.getFunction() == 'Child':
        spline_child_blocks.append(block)
    elif block.getFunction() in ['End', 'FK', 'IK', 'Spline', 'Hand', 'Foot']:
        if len(spline_child_blocks) >= 1:
            # spline_child_joints.append(block.getJoint())
            return block
        else:
            spline_child_blocks[:] = []  # 必须这样写，不能保持直接spline_child_joints = [], 不然和传入的spline_child_joints不是一个地址
    for block_child in block.getChildrenBlock():
        return iterateSpline(block_child, spline_child_blocks)


def iterateFK(block, fk_child_blocks):
    if block.getFunction() == 'Child':
        fk_child_blocks.append(block)
    elif block.getFunction() in ['End', 'FK', 'IK', 'Spline', 'Hand', 'Foot']:
        return
    for block_child in block.getChildrenBlock():
        iterateFK(block_child, fk_child_blocks)
def iterateFinger(block, finger_blocks, finger_list):
    if block.getJoint() in finger_list:
        finger_blocks.append(block)
        block.setIsFinger(True)
    else:
        return
    for block_child in block.getChildrenBlock():
        iterateFinger(block_child, finger_blocks, finger_list)


def ensureAllBlockInfo(blocks):
    if not mc.objExists('Block'):
        return
    for block in blocks:
        ensureBlockInfo(block)



def blockInstance(block_joint):
    joint = block_joint
    orient = ['Common', 'Parent', 'Free', 'World']
    fat = mc.getAttr(block_joint + '.fat')
    function = mc.getAttr(block_joint + '.otherType')
    side = SIDE_LIST[mc.getAttr(block_joint + '.side')]
    mirror = mc.getAttr(block_joint + '.mirror')
    orientX = orient[mc.getAttr(block_joint + '.orientX')]
    worldX = mc.getAttr(block_joint + '.worldX')[0]
    orientY = orient[mc.getAttr(block_joint + '.orientY')]
    worldY = mc.getAttr(block_joint + '.worldY')[0]
    parent = mc.listRelatives(block_joint, parent=True, type='joint') or [None]
    parent = parent[0]
    children = mc.listRelatives(block_joint, type='joint') or []
    subdivide = mc.getAttr(block_joint + '.subdivide')
    if function == 'FK':
        name = mc.getAttr(block_joint + '.n')
        segScaleComp = mc.getAttr(block_joint + '.segScaleComp')
        secondControl = mc.getAttr(block_joint + '.secondControl')
        fkShape = SHAPE_LIST[mc.getAttr(block_joint + '.fkShape')]
        secShape = SEC_LIST[mc.getAttr(block_joint + '.secShape')]
        block = block_class.FKBlock(joint=joint, name=name, function=function, side=side, mirror=mirror,
                                    orientX=orientX,
                                    orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children,
                                    secondControl=secondControl, fkShape=fkShape, secShape=secShape,
                                    subdivide=subdivide, fat=fat, segScaleComp=segScaleComp)

    elif function == 'IK':
        name = mc.getAttr(block_joint + '.n')
        segScaleComp = mc.getAttr(block_joint + '.segScaleComp')
        secondControl = mc.getAttr(block_joint + '.secondControl')
        ikShape = SHAPE_LIST[mc.getAttr(block_joint + '.ikShape')]
        fkShape = SHAPE_LIST[mc.getAttr(block_joint + '.fkShape')]
        secShape = SEC_LIST[mc.getAttr(block_joint + '.secShape')]
        switch_pivot = mc.getAttr(block_joint + '.switchPivot')
        block = block_class.IKBlock(joint=joint, name=name, function=function, side=side, mirror=mirror,
                                    orientX=orientX,
                                    orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children,
                                    secondControl=secondControl, ikShape=ikShape, fkShape=fkShape, secShape=secShape,
                                    subdivide=subdivide, fat=fat, segScaleComp=segScaleComp, switch_pivot=switch_pivot)

    elif function == 'Spline':
        name = mc.getAttr(block_joint + '.n')
        secondControl = mc.getAttr(block_joint + '.secondControl')
        splineShape = SHAPE_LIST[mc.getAttr(block_joint + '.splineShape')]
        secShape = SEC_LIST[mc.getAttr(block_joint + '.secShape')]
        block = block_class.SplineBlock(joint=joint, name=name, function=function, side=side, mirror=mirror,
                                        orientX=orientX,
                                        orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children,
                                        secondControl=secondControl, splineShape=splineShape, secShape=secShape,
                                        subdivide=subdivide, fat=fat)

    elif function == 'End':
        block = block_class.EndBlock(joint=joint, function=function, side=side, mirror=mirror,
                                     orientX=orientX,
                                     orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children,
                                     subdivide=subdivide, fat=fat)

    elif function == 'Child':
        fkShape = SHAPE_LIST[mc.getAttr(block_joint + '.fkShape')]
        block = block_class.ChildBlock(joint=joint, function=function, side=side, mirror=mirror,
                                       orientX=orientX,
                                       orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children,
                                       subdivide=subdivide, fat=fat, fkShape=fkShape)

    elif function == 'Hand':
        name = mc.getAttr(block_joint + '.n')
        segScaleComp = mc.getAttr(block_joint + '.segScaleComp')
        fingerShape = SHAPE_LIST[mc.getAttr(block_joint + '.fingerShape')]
        fingerPivot = mc.getAttr(block_joint + '.fingerPivot')
        thumbList = mc.getAttr(block_joint + '.thumbList').split(';')
        indexList = mc.getAttr(block_joint + '.indexList').split(';')
        middleList = mc.getAttr(block_joint + '.middleList').split(';')
        ringList = mc.getAttr(block_joint + '.ringList').split(';')
        pinkyList = mc.getAttr(block_joint + '.pinkyList').split(';')
        block = block_class.HandBlock(joint=joint, name=name, function=function, side=side, mirror=mirror,
                                      orientX=orientX,
                                      orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children,
                                      fingerShape=fingerShape, subdivide=subdivide, fat=fat, segScaleComp=segScaleComp,
                                      fingerPivot=fingerPivot, thumbList=thumbList, indexList=indexList,
                                      middleList=middleList, ringList=ringList, pinkyList=pinkyList)

    elif function == 'Foot':
        name = mc.getAttr(block_joint + '.n')
        segScaleComp = mc.getAttr(block_joint + '.segScaleComp')
        heel_pivot = mc.getAttr(block_joint + '.heelPivot')
        footOuter_pivot = mc.getAttr(block_joint + '.footOuterPivot')
        footInner_pivot = mc.getAttr(block_joint + '.footInnerPivot')
        block = block_class.FootBlock(joint=joint, name=name, function=function, side=side, mirror=mirror,
                                      orientX=orientX,
                                      orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children,
                                      subdivide=subdivide, fat=fat, segScaleComp=segScaleComp, heel_pivot=heel_pivot,
                                      footOuter_pivot=footOuter_pivot, footInner_pivot=footInner_pivot)
    elif function == 'Aim':
        segScaleComp = mc.getAttr(block_joint + '.segScaleComp')
        block = block_class.AimBlock(joint=joint, function=function, side=side, mirror=mirror, fat=fat,
                                     segScaleComp=segScaleComp, orientX=orientX, orientY=orientY, worldX=worldX,
                                     worldY=worldY, parent=parent, children=children)

    return block


# scale为y轴距离
def getBlockScale():
    scale = 1
    if not mc.objExists('Block'):
        return scale
    blocks = mc.listRelatives('Block', f=True, ad=True, type='joint')
    blocks_pos_y = [mc.xform(block, q=True, ws=True, t=True)[1] for block in blocks]
    max_y = max(blocks_pos_y)
    min_y = min(blocks_pos_y)
    return (max_y - min_y) / 17.176163


def getBlockSide(block):
    side_treshold = 0.0001 * getBlockScale()
    pos = mc.xform(block, q=True, ws=True, t=True)
    if side_treshold > pos[0] > (-1 * side_treshold):
        return 'M'
    elif pos[0] > side_treshold:
        return 'L'
    elif pos[0] < side_treshold:
        return 'R'


def updateBlockOrient(blocks):
    with maya_utilities.Undoable():
        mc.select(clear=True)
        if not mc.objExists('Block'):
            return
        # 用于定位orientX为world时来作为约束物体
        temp_aim = mc.createNode('transform', n='tempAim')
        for block in blocks:
            block_joint = block.getJoint()
            block_parent = block.getParent()
            if block_parent:
                 mc.parent(block_joint, 'Block')
        dic = {}

        for block in blocks:
            block_joint = block.getJoint()
            loc_list = mc.listRelatives(block_joint, type='transform') or []
            dic[block_joint] = loc_list
            for loc in loc_list:
                mc.parent(loc, 'Block')
        print len(blocks)
        for block in blocks:
            function = block.getFunction()
            block_joint = block.getJoint()
            block_parent = block.getParent()
            block_children = block.getChildren()
            block_orient_x = block.getOrientX()
            block_world_x = block.getWorldX()
            block_orient_y = block.getOrientY()
            block_world_y = block.getWorldY()
            block_child = block.getFirstChild()
            aim_obj = ''
            aim_vector = ''

            if block_orient_x == 'Common':
                # x轴指向次级骨骼
                aim_obj = block_child
                if block.getSide() == 'R':
                    aim_vector = (-1, 0, 0)
                else:
                    aim_vector = (1, 0, 0)

            elif block_orient_x == 'World':
                # x轴指向world_x
                aim_obj = temp_aim
                mc.matchTransform(temp_aim, block_joint, position=True)
                mc.select(temp_aim)
                mc.move(block_world_x[0], block_world_x[1], block_world_x[2], temp_aim, r=True, ws=True)
                aim_vector = (1, 0, 0)

            elif block_orient_x == 'Free':
                pass
            elif block_orient_x == 'Parent':
                # -x轴指向world_x
                if block_parent:
                    aim_obj = block_parent

                if block.getSide() == 'R':
                    aim_vector = (1, 0, 0)
                else:
                    aim_vector = (-1, 0, 0)

            if block_orient_y == 'Common':
                if function == 'End':
                    # 和parent一致
                    if block_parent:
                        mc.parent(block_joint, block_parent)
                    mc.setAttr(block_joint + '.jo', 0, 0, 0, type='float3')
                    mc.setAttr(block_joint + '.r', 0, 0, 0, type='float3')

                    mc.parent(block_joint, 'Block')
                elif function == 'IK':
                    # IK起始骨骼的x轴指向子骨骼， y轴与IK结束骨骼一直， IK链的三根关节的y轴应该一致
                    if block.getIKSolver() == 'IKRPSolver':
                        if block.getSide() == 'R':
                            up_vec_obj = block.getIKEndJoint()
                            con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                                   worldUpType='object', worldUpObject=up_vec_obj)[0]
                            mc.delete(con)
                        else:
                            if mc.objExists('tempTransform'):
                                mc.delete('tempTransform')
                            if block.getIKMiddleJoint() and block.getIKStartJoint():
                                mc.parent(block.getIKMiddleJoint(), block_joint)
                                pos = mc.xform(block_joint, q=True, ws=True, t=True)
                                mc.createNode('transform', n='tempTransform', p=block.getIKMiddleJoint())
                                mc.parent('tempTransform', block_joint)
                                rot = mc.getAttr('tempTransform.r')[0]
                                if -0.001 < rot[2] < 0.001:
                                    mc.move(0, pos[1] / 100.0, 0, block.getIKMiddleJoint() + '.rotatePivot', os=True,
                                            r=True)
                                mc.parent(block.getIKMiddleJoint(), 'Block')
                                mc.delete('tempTransform')

                            up_vec_obj = block.getIKEndJoint()
                            con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, -1, 0),
                                                   worldUpType='object', worldUpObject=up_vec_obj)[0]
                            mc.delete(con)

                elif function == 'FK':
                    # if block.getSide() == 'M':
                    #     # 中间 FK关节y指向z
                    #     con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0), worldUpType='vector', worldUpVector=(0, 0, 1))[0]
                    #     mc.delete(con)
                    # elif block.getSide() == 'L':
                    #     print 11111, block_joint
                    #     # side FK关节y与原先尽量一致
                    #     up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                    #     mc.move(0, 1, 0, up_obj, r=True, os=True)
                    #     mc.parent(up_obj, w=True)
                    #     con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0), worldUpType='object', worldUpObject=up_obj)[0]
                    #     mc.delete(con)
                    #     mc.delete(up_obj)
                    up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                    mc.move(0, 1, 0, up_obj, r=True, os=True)
                    mc.parent(up_obj, w=True)
                    con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                           worldUpType='object', worldUpObject=up_obj)[0]
                    mc.delete(con)
                    mc.delete(up_obj)


                elif function == 'Spline':
                    if block.getSide() == 'M':
                        # con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0), worldUpType='vector', worldUpVector=(0, 0, 1))[0]
                        # mc.delete(con)
                        up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                        mc.move(0, 1, 0, up_obj, r=True, os=True)
                        mc.parent(up_obj, w=True)
                        con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                               worldUpType='object', worldUpObject=up_obj)[0]
                        mc.delete(con)
                        mc.delete(up_obj)
                    elif block.getSide() == 'L':
                        up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                        mc.move(0, 1, 0, up_obj, r=True, os=True)
                        mc.parent(up_obj, w=True)
                        con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                               worldUpType='object', worldUpObject=up_obj)[0]
                        mc.delete(con)
                        mc.delete(up_obj)
                    elif block.getSide() == 'R':
                        up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                        mc.move(0, -1, 0, up_obj, r=True, os=True)
                        mc.parent(up_obj, w=True)
                        con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, -1, 0),
                                               worldUpType='object', worldUpObject=up_obj)[0]
                        mc.delete(con)
                        mc.delete(up_obj)

                elif function == 'Hand':
                    if block_children:
                        up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                        mc.move(0, 1, 0, up_obj, r=True, os=True)
                        mc.parent(up_obj, w=True)
                        con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                               worldUpType='object', worldUpObject=up_obj)[0]
                        mc.delete(con)
                        mc.delete(up_obj)
                    else:
                        mc.setAttr(block_joint + '.jo', 0, 0, 0, type='float3')
                        mc.setAttr(block_joint + '.r', 0, 0, 0, type='float3')
                elif function == 'Foot':
                    if block_children:
                        up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                        mc.move(0, 1, 0, up_obj, r=True, os=True)
                        mc.parent(up_obj, w=True)
                        con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                               worldUpType='object', worldUpObject=up_obj)[0]
                        mc.delete(con)
                        mc.delete(up_obj)
                    else:
                        mc.setAttr(block_joint + '.jo', 0, 0, 0, type='float3')
                        mc.setAttr(block_joint + '.r', 0, 0, 0, type='float3')
                elif function == 'Child' or function == 'Aim':
                    if block.getIKSolver() == 'IKRPSolver':
                        up_vec_obj = block.getIKStartJoint()
                        con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                               worldUpType='objectrotation', worldUpObject=up_vec_obj,
                                               worldUpVector=(0, 1, 0))[0]
                        mc.delete(con)
                        mc.joint(block_joint, spa=True, e=True, ch=True)
                    elif block.getIKSolver() == 'SplineSolver':
                        if block.getSide() == 'M':
                            # con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0), worldUpType='vector', worldUpVector=(0, 0, 1))[0]
                            # mc.delete(con)
                            up_vec_obj = block.getSplineStartJoint()
                            con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                                   worldUpType='objectrotation', worldUpObject=up_vec_obj,
                                                   worldUpVector=(0, 1, 0))[0]
                            mc.delete(con)

                        elif block.getSide() == 'L':
                            up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                            mc.move(0, 1, 0, up_obj, r=True, os=True)
                            mc.parent(up_obj, w=True)
                            con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                                   worldUpType='object', worldUpObject=up_obj)[0]
                            mc.delete(con)
                            mc.delete(up_obj)

                    elif block.getIKSolver() == 'FK':
                        if block.getIsFinger():
                            if block == block.getStartFinger():
                                up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                                mc.move(0, 1, 0, up_obj, r=True, os=True)
                                mc.parent(up_obj, w=True)
                                con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                                       worldUpType='object', worldUpObject=up_obj)[0]
                                mc.delete(con)
                                mc.delete(up_obj)
                            else:
                                up_vec_obj = block.getStartFinger().getJoint()
                                con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                                       worldUpType='objectrotation', worldUpObject=up_vec_obj,
                                                       worldUpVector=(0, 1, 0))[0]
                                mc.delete(con)
                        else:
                            up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                            mc.move(0, 1, 0, up_obj, r=True, os=True)
                            mc.parent(up_obj, w=True)
                            con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                                   worldUpType='object', worldUpObject=up_obj)[0]
                            mc.delete(con)
                            mc.delete(up_obj)
                    else:
                        if block.getSide() == 'M':
                            con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                                   worldUpType='vector', worldUpVector=(0, 0, 1))[0]
                            mc.delete(con)
                        else:
                            up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                            mc.move(0, 1, 0, up_obj, r=True, os=True)
                            mc.parent(up_obj, w=True)
                            con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                                   worldUpType='object', worldUpObject=up_obj)[0]
                            mc.delete(con)
                            mc.delete(up_obj)


            elif block_orient_y == 'World':
                world_up_vector = block_world_y
                con = mc.aimConstraint(aim_obj, block_joint, worldUpType='Vector', aimVector=aim_vector,
                                       upVector=(0, 1, 0), worldUpVector=world_up_vector)
                mc.delete(con)

            elif block_orient_y == 'Free':
                pass
            elif block_orient_y == 'Parent':
                if block_parent:
                    up_vec_obj = block_parent
                    con = mc.aimConstraint(aim_obj, block_joint, worldUpType='objectrotation', worldUpObject=up_vec_obj,
                                           worldUpVector=(0, 1, 0))[0]
                    mc.delete(con)
            mc.makeIdentity(block_joint, apply=True, t=False, r=True, s=True)
        for block in blocks:
            if block.getParent():
                mc.parent(block.getJoint(), block.getParent())

        for block_joint, loc_list in dic.items():
            for loc in loc_list:
                mc.parent(loc, block_joint)
        mc.delete(temp_aim)
        mc.select(clear=True)


def lockAttrs(obj, trans, rot, scale, vis):
    mc.setAttr(obj + '.tx', l=trans, k=not trans)
    mc.setAttr(obj + '.ty', l=trans, k=not trans)
    mc.setAttr(obj + '.tz', l=trans, k=not trans)
    mc.setAttr(obj + '.rx', l=trans, k=not rot)
    mc.setAttr(obj + '.ry', l=trans, k=not rot)
    mc.setAttr(obj + '.rz', l=trans, k=not rot)
    mc.setAttr(obj + '.sx', l=trans, k=not scale)
    mc.setAttr(obj + '.sy', l=trans, k=not scale)
    mc.setAttr(obj + '.sz', l=trans, k=not scale)
    mc.setAttr(obj + '.visibility', l=vis, k=not vis)


def objsExists(objs):
    for obj in objs:
        if not mc.objExists(obj):
            return False
    return True


def align(obj, target, translate, rotate, jointOrient, rotateOrder):
    mc.matchTransform(obj, target, position=translate, rotation=rotate)
    if rotateOrder:
        mc.setAttr(obj + '.rotateOrder', mc.getAttr(target + '.rotateOrder'))
    if jointOrient:
        mc.setAttr(obj + '.jointOrient', mc.getAttr(target + '.jointOrient'))


def getDistance(pos1, pos2):
    posX = pos2[0] - pos1[0]
    posY = pos2[1] - pos1[1]
    posZ = pos2[2] - pos1[2]
    return math.sqrt(pow(posX, 2) + pow(posY, 2) + pow(posZ, 2))
