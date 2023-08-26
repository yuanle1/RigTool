#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import maya.cmds as mc
import block_class
reload(block_class)
from modules import maya_utilities as maya_utilities

# 确认block属性
def ensureBlockAttrs(block):
    if not mc.objExists(block + '.name'):
        mc.addAttr(block, ln='name', sn='n', dataType='string')
        mc.setAttr(block + '.name', 'Default', type='string')

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

    block_type_list = [None, 'FK', 'IK', 'Spline', 'Child', 'End', 'Eye', 'Hand', 'Foot', ]
    joint_label = mc.getAttr(block + '.type')
    if joint_label == 18:
        joint_type = mc.getAttr(block + '.otherType')
        if joint_type == 'Chest' or joint_type == 'chest':
            mc.setAttr(block + '.otherType', 'FK')
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

    if block_type == 'FK':
        if not mc.objExists(block + '.secondControl'):
            mc.addAttr(block, ln='secondControl', sn='secControl', attributeType='bool', dv=True)
        if not mc.objExists(block + '.subdivide'):
            mc.addAttr(block, ln='subdivide', sn='subdivide', attributeType='long', dv=2)
        if not mc.objExists(block + '.fkShape'):
            mc.addAttr(block, ln='fkShape', sn='fkShape', attributeType='enum', enumName='FK:IK')
        if not mc.objExists(block + '.secShape'):
            mc.addAttr(block, ln='secShape', sn='secShape', attributeType='enum', enumName='FK:IK')
        mc.setAttr(block + '.overrideColorRGB', 116 / 255.0, 185 / 255.0, 255 / 255.0)

    elif block_type == 'IK':
        if not mc.objExists(block + '.secondControl'):
            mc.addAttr(block, ln='secondControl', sn='secControl', attributeType='bool', dv=True)
        if not mc.objExists(block + '.subdivide'):
            mc.addAttr(block, ln='subdivide', sn='subdivide', attributeType='long', dv=2)
        if not mc.objExists(block + '.ikShape'):
            mc.addAttr(block, ln='ikShape', sn='ikShape', attributeType='enum', enumName='FK:IK:Spline')
        if not mc.objExists(block + '.secShape'):
            mc.addAttr(block, ln='secShape', sn='secShape', attributeType='enum', enumName='FKSec:IKSec:SplineSec')
        mc.setAttr(block + '.overrideColorRGB', 255 / 255.0, 118 / 255.0, 117 / 255.0)

    elif block_type == 'Spline':
        if not mc.objExists(block + '.secondControl'):
            mc.addAttr(block, ln='secondControl', sn='secControl', attributeType='bool', dv=True)
        if not mc.objExists(block + '.subdivide'):
            mc.addAttr(block, ln='subdivide', sn='subdivide', attributeType='long', dv=2)
        if not mc.objExists(block + '.splineShape'):
            mc.addAttr(block, ln='splineShape', sn='splineShape', attributeType='enum', enumName='FK:IK:Spline')
        if not mc.objExists(block + '.secShape'):
            mc.addAttr(block, ln='secShape', sn='secShape', attributeType='enum', enumName='FKSec:IKSec:SplineSec')
        mc.setAttr(block + '.overrideColorRGB', 253 / 255.0, 203 / 255.0, 110 / 255.0)

    elif block_type == 'Hand':
        mc.setAttr(block + '.overrideColorRGB', 255 / 255.0, 118 / 255.0, 117 / 255.0)
    elif block_type == 'Foot':
        mc.setAttr(block + '.overrideColorRGB', 255 / 255.0, 118 / 255.0, 117 / 255.0)
    # elif block_type == 'Toe':
    #     mc.setAttr(block + '.overrideColorRGB', 255 / 255.0, 118 / 255.0, 117 / 255.0)
    elif block_type == 'End':
        mc.setAttr(block + '.overrideColorRGB', 255 / 255.0, 255 / 255.0, 255 / 255.0)
    elif block_type == 'Child':
        parent = mc.listRelatives(block, p=True)
        if not parent:
            mc.setAttr(block + '.overrideEnabled', False)
        elif mc.getAttr(parent[0] + '.otherType') in ['Hand', 'Foot']:
            mc.setAttr(block + '.overrideColorRGB', 116 / 255.0, 185 / 255.0, 255 / 255.0)
        else:
            parent = parent[0]
            color = mc.getAttr(parent + '.overrideColorRGB')[0]
            mc.setAttr(block + '.overrideColorRGB', color[0], color[1], color[2])


# 确认Block属性
def ensureAllBlockAttrs():
    if not mc.objExists('Block'):
        return
    mc.select('Block', hi=True)
    block_joints = mc.ls(sl=True, type='joint')
    for block_joint in block_joints:
        ensureBlockAttrs(block_joint)

def ensureBlockInfo(block):
    function = block.getFunction()
    if function == 'IK':
        for block_child in block.getChildrenBlock():
            if block_child.getFunction() == 'Child':
                for block_child_child in block_child.getChildrenBlock():
                    if block_child_child.getFunction() in ['Hand', 'Foot', 'FK', 'Spline', 'End']:
                        block.setIKStartJoint(block.getJoint())
                        block.setIKMiddleJoint(block_child.getJoint())
                        block.setIKEndJoint(block_child_child.getJoint())
                        block.setIKSolver('IKRPSolver')
                        block.setFirstChild(block_child.getJoint())

                        block_child.setIKStartJoint(block.getJoint())
                        block_child.setIKMiddleJoint(block_child.getJoint())
                        block_child.setIKEndJoint(block_child_child.getJoint())
                        block_child.setIKSolver('IKRPSolver')
                        block_child.setFirstChild(block_child_child.getJoint())

                        block_child_child.setIKStartJoint(block.getJoint())
                        block_child_child.setIKMiddleJoint(block_child.getJoint())
                        block_child_child.setIKEndJoint(block_child_child.getJoint())
                        block_child_child.setIKSolver('IKRPSolver')
                        break

    elif function == 'Spline':
        spline_child_blocks = []
        spline_end_block = iterateSpline(block, spline_child_blocks)
        spline_child_joints = [i.getJoint() for i in spline_child_blocks]



        if spline_child_joints and spline_end_block:
            block.setSplineStartJoint(block.getJoint())
            block.setSplineMiddleJoints(spline_child_joints)
            block.setSplineEndJoint(spline_end_block.getJoint())
            block.setIKSolver('SplineSolver')


            for spline_child_block in spline_child_blocks:
                spline_child_block.setSplineStartJoint(block.getJoint())
                spline_child_block.setSplineMiddleJoints(spline_child_joints)
                spline_child_block.setSplineEndJoint(spline_end_block.getJoint())
                spline_child_block.setIKSolver('SplineSolver')

            spline_end_block.setSplineStartJoint(block.getJoint())
            spline_end_block.setSplineMiddleJoints(spline_child_joints)
            spline_end_block.setSplineEndJoint(spline_end_block.getJoint())
            spline_end_block.setIKSolver('SplineSolver')


    elif function == 'FK':
        fk_child_blocks = []
        for block_child in block.getChildrenBlock():
            iterateFK(block_child, fk_child_blocks)
        fk_child_joints = [i.getJoint() for i in fk_child_blocks]

        block.setFKStartJoint(block.getJoint())
        block.setFKJoints(fk_child_joints)
        if block.getIKSolver() != 'IKRPSolver' and block.getIKSolver() != 'SplineSolver':
            block.setIKSolver('FK')
        for fk_child_block in fk_child_blocks:
            fk_child_block.setFKStartJoint(block.getJoint())
            fk_child_block.setFKJoints(fk_child_joints)
            fk_child_block.setIKSolver('FK')

def iterateSpline(block, spline_child_blocks):
    if block.getFunction() == 'Child':
        spline_child_blocks.append(block)
    elif block.getFunction() in ['End', 'FK', 'IK', 'Spline', 'Hand', 'Foot']:
        if len(spline_child_blocks) >= 1:
            # spline_child_joints.append(block.getJoint())
            return block
        else:
            spline_child_blocks[:] = [] # 必须这样写，不能保持直接spline_child_joints = [], 不然和传入的spline_child_joints不是一个地址
    for block_child in block.getChildrenBlock():
        return iterateSpline(block_child, spline_child_blocks)

def iterateFK(block, fk_child_blocks):
    if block.getFunction() == 'Child':
        fk_child_blocks.append(block)
    elif block.getFunction() in ['End', 'FK', 'IK', 'Spline', 'Hand', 'Foot']:
        return
    for block_child in block.getChildrenBlock():
        iterateFK(block_child, fk_child_blocks)




def ensureAllBlockInfo(blocks):
    if not mc.objExists('Block'):
        return
    for block in blocks:
        ensureBlockInfo(block)


def blockInstance(block_joint):
    joint = block_joint
    orient = ['Common', 'Parent', 'Free', 'World']
    control = ['FK', 'IK', 'Spline']
    side_list = ['M', 'L', 'R']
    function = mc.getAttr(block_joint + '.otherType')
    name = mc.getAttr(block_joint + '.n')
    side = side_list[mc.getAttr(block_joint + '.side')]
    mirror = mc.getAttr(block_joint + '.mirror')
    orientX = orient[mc.getAttr(block_joint + '.orientX')]
    worldX = mc.getAttr(block_joint + '.worldX')[0]
    orientY = orient[mc.getAttr(block_joint + '.orientY')]
    worldY = mc.getAttr(block_joint + '.worldY')[0]
    parent = mc.listRelatives(block_joint, parent=True, type='joint') or [None]
    parent = parent[0]
    children = mc.listRelatives(block_joint, type='joint') or []

    if function == 'FK':
        secondControl = mc.getAttr(block_joint + '.secondControl')
        subdivide = mc.getAttr(block_joint + '.subdivide')
        fkShape = mc.getAttr(block_joint + '.fkShape')
        secShape = mc.getAttr(block_joint + '.secShape')
        block = block_class.FKBlock(joint=joint, name=name, function=function, side=side, mirror=mirror, orientX=orientX,
                                    orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children,
                                    secondControl=secondControl, subdivide=subdivide, fkShape=fkShape,
                                    secShape=secShape)
    elif function == 'IK':
        secondControl = mc.getAttr(block_joint + '.secondControl')
        subdivide = mc.getAttr(block_joint + '.subdivide')
        ikShape = mc.getAttr(block_joint + '.ikShape')
        secShape = mc.getAttr(block_joint + '.secShape')
        block = block_class.IKBlock(joint=joint, name=name, function=function, side=side, mirror=mirror, orientX=orientX,
                                    orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children,
                                    secondControl=secondControl, subdivide=subdivide, ikShape=ikShape,
                                    secShape=secShape)

    elif function == 'Spline':
        secondControl = mc.getAttr(block_joint + '.secondControl')
        subdivide = mc.getAttr(block_joint + '.subdivide')
        splineShape = mc.getAttr(block_joint + '.splineShape')
        secShape = mc.getAttr(block_joint + '.secShape')
        block = block_class.SplineBlock(joint=joint, name=name, function=function, side=side, mirror=mirror, orientX=orientX,
                                    orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children,
                                    secondControl=secondControl, subdivide=subdivide, splineShape=splineShape,
                                    secShape=secShape, )

    elif function == 'End':
        block = block_class.EndBlock(joint=joint, name=name, function=function, side=side, mirror=mirror, orientX=orientX,
                                    orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children)

    elif function == 'Child':
        block = block_class.ChildBlock(joint=joint, name=name, function=function, side=side, mirror=mirror, orientX=orientX,
                                    orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children)

    elif function == 'Hand':
        block = block_class.ChildBlock(joint=joint, name=name, function=function, side=side, mirror=mirror, orientX=orientX,
                                    orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children)

    elif function == 'Foot':
        block = block_class.ChildBlock(joint=joint, name=name, function=function, side=side, mirror=mirror, orientX=orientX,
                                    orientY=orientY, worldX=worldX, worldY=worldY, parent=parent, children=children)

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
                mc.move(1, 0, 0, temp_aim, r=True, ws=True)
                aim_vector = block_world_x

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
                            con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0), worldUpType='object', worldUpObject=up_vec_obj)[0]
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
                                    mc.move(0, pos[1] / 100.0, 0, block.getIKMiddleJoint() + '.rotatePivot', os=True, r=True)
                                mc.parent(block.getIKMiddleJoint(), 'Block')
                                mc.delete('tempTransform')

                            up_vec_obj = block.getIKEndJoint()
                            con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, -1, 0), worldUpType='object', worldUpObject=up_vec_obj)[0]
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
                        con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0), worldUpType='object', worldUpObject=up_obj)[0]
                        mc.delete(con)
                        mc.delete(up_obj)
                    elif block.getSide() == 'R':
                        up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                        mc.move(0, -1, 0, up_obj, r=True, os=True)
                        mc.parent(up_obj, w=True)
                        con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, -1, 0), worldUpType='object', worldUpObject=up_obj)[0]
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
                elif function == 'Child':
                    if block.getIKSolver() == 'IKRPSolver':
                        up_vec_obj = block.getIKStartJoint()
                        con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0), worldUpType='objectrotation', worldUpObject=up_vec_obj, worldUpVector=(0, 1, 0))[0]
                        mc.delete(con)
                        mc.joint(block_joint, spa=True, e=True, ch=True)
                    elif block.getIKSolver() == 'SplineSolver':
                        if block.getSide() == 'M':
                            # con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0), worldUpType='vector', worldUpVector=(0, 0, 1))[0]
                            # mc.delete(con)
                            up_vec_obj = block.getSplineStartJoint()
                            con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0), worldUpType='objectrotation', worldUpObject=up_vec_obj, worldUpVector=(0, 1, 0))[0]
                            mc.delete(con)

                        elif block.getSide() == 'L':
                            up_obj = mc.createNode('transform', p=block_joint, n='up_obj')
                            mc.move(0, 1, 0, up_obj, r=True, os=True)
                            mc.parent(up_obj, w=True)
                            con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0), worldUpType='object', worldUpObject=up_obj)[0]
                            mc.delete(con)
                            mc.delete(up_obj)

                    elif block.getIKSolver() == 'FK':
                        up_vec_obj = block.getFKStartJoint()
                        con = mc.aimConstraint(aim_obj, block_joint, aimVector=aim_vector, upVector=(0, 1, 0),
                                               worldUpType='objectrotation', worldUpObject=up_vec_obj,
                                               worldUpVector=(0, 1, 0))[0]
                        mc.delete(con)

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
                con = mc.aimConstraint(aim_obj, block_joint, worldUpType='Vector', aimVector=aim_vector, upVector=(0, 1, 0), worldUpVector=world_up_vector)
                mc.delete(con)

            elif block_orient_y == 'Free':
                pass
            elif block_orient_y == 'Parent':
                if block_parent:
                    up_vec_obj = block_parent
                    con = mc.aimConstraint(aim_obj, block_joint, worldUpType='objectrotation', worldUpObject=up_vec_obj, worldUpVector=(0, 1, 0))[0]
                    mc.delete(con)
            mc.makeIdentity(block_joint, apply=True, t=False, r=True, s=True)
        for block in blocks:
            if block.getParent():
                mc.parent(block.getJoint(), block.getParent())



        mc.delete(temp_aim)
        mc.select(clear=True)

























