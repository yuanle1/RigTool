#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import maya.cmds as mc

import modules.maya_utilities as maya_utilities
import block_utilities
import block_class

import maya_widgets.flatten_widget as flatten_widget
import maya_widgets.switch_button as switch_button

import copy

class BlockBuilder(QWidget):
    def __init__(self, parent=None):
        super(BlockBuilder, self).__init__(parent)
        self.setupUI()
        self.connect()

    def setupUI(self):
        font = maya_utilities.font

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 5, 0, 5)

        self.main_root_layout = QHBoxLayout()
        self.main_root_layout.setContentsMargins(5, 0, 0, 0)

        self.main_layout.addLayout(self.main_root_layout)

        self.main_control_grid = QGridLayout()
        self.main_control_grid.setHorizontalSpacing(10)
        # self.main_control_grid.setVerticalSpacing(0)
        self.main_root_layout.addStretch()
        self.main_root_layout.addLayout(self.main_control_grid)

        self.name_label = QLabel()
        self.name_label.setFont(font)
        self.name_label.setText('Name:')
        self.name_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.main_control_grid.addWidget(self.name_label, 0, 0)

        self.name_linEdit = flatten_widget.MLineEdit()
        self.name_linEdit.setFont(font)
        self.name_linEdit.setText('Main')
        self.name_linEdit.setMinimumWidth(80)
        self.name_linEdit.setStyleSheet('''
                                            border:none;
                                            background-color:transparent;
                                            border-bottom: 1px solid rgb(60, 60, 60);
                                            padding-bottom: 0px;
                                        ''')
        self.main_control_grid.addWidget(self.name_linEdit, 0, 1)

        self.main_count_label = QLabel()
        self.main_count_label.setFont(font)
        self.main_count_label.setText('Main Count:')
        self.main_count_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.main_control_grid.addWidget(self.main_count_label, 1, 0)

        self.main_count_spin = flatten_widget.MSpinBox()
        self.main_count_spin.setFont(font)
        self.main_count_spin.setMinimum(1)
        self.main_count_spin.setFixedWidth(50)
        self.main_count_spin.setFixedHeight(16)

        self.main_control_grid.addWidget(self.main_count_spin, 1, 1)

        self.main_root_layout.addStretch()

        self.line = QFrame()
        self.line.setFrameShape(QFrame.VLine)
        self.line.setStyleSheet('''
                                                    border-left:1px solid rgb(60, 60, 60);
                                                ''')
        self.line.setFixedWidth(2)
        self.line.setFixedHeight(36)
        self.main_root_layout.addWidget(self.line)

        self.main_root_layout.addStretch()

        self.root_control_grid = QGridLayout()
        self.root_control_grid.setHorizontalSpacing(10)
        # self.root_control_grid.setVerticalSpacing(0)
        self.main_root_layout.addLayout(self.root_control_grid)

        self.root_control_label = QLabel()
        self.root_control_label.setFont(font)
        self.root_control_label.setText('Root Control:')
        self.root_control_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.root_control_grid.addWidget(self.root_control_label, 0, 0)

        self.root_control_check = switch_button.MSwitch()
        self.root_control_check.setChecked(True)
        self.root_control_grid.addWidget(self.root_control_check, 0, 1)

        self.gravity_control_label = QLabel()
        self.gravity_control_label.setFont(font)
        self.gravity_control_label.setText('Gravity Control:')
        self.gravity_control_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.root_control_grid.addWidget(self.gravity_control_label, 1, 0)

        self.gravity_control_check = switch_button.MSwitch()
        self.gravity_control_check.setChecked(True)
        self.root_control_grid.addWidget(self.gravity_control_check, 1, 1)

        self.main_root_layout.addStretch()

        self.build_frame = QFrame()
        self.addShadow(self.build_frame)
        self.build_frame.setObjectName('build_frame')
        self.build_frame.setStyleSheet('''
                                        #build_frame
                                        {
                                            background-color:rgb(54, 54, 54);
                                            border-radius:5px;
                                        }
                                        ''')
        self.build_layout = QHBoxLayout()
        self.build_layout.setContentsMargins(0, 0, 0, 0)
        self.build_frame.setLayout(self.build_layout)
        self.main_layout.addWidget(self.build_frame)

        self.display_layout = QVBoxLayout()
        self.display_layout.setSpacing(3)
        self.display_layout.setContentsMargins(5, 5, 10, 5)
        self.build_layout.addLayout(self.display_layout)

        # block
        self.display_block_frame = QFrame()
        self.addShadow(self.display_block_frame)
        self.display_block_frame.setFixedHeight(20)
        self.display_block_frame.setObjectName('display_block_frame')
        self.display_block_frame.setStyleSheet('''
                                                #display_block_frame
                                                {
                                                    background-color:rgb(69, 69, 69);
                                                    border-radius:3px;
                                                }
                                                ''')
        self.display_block_layout = QHBoxLayout()
        self.display_block_layout.setContentsMargins(8, 0, 2, 0)
        self.display_block_layout.setSpacing(3)
        self.display_block_frame.setLayout(self.display_block_layout)
        self.display_layout.addWidget(self.display_block_frame)

        self.display_block_label = DisplayLabel('block_display')
        self.display_block_label.setFont(font)
        self.display_block_label.setText('Block')
        self.display_block_layout.addWidget(self.display_block_label)

        self.display_block_layout.addStretch()

        self.display_block_check = DisplayCheck()
        self.display_block_layout.addWidget(self.display_block_check)

        self.only_block_check = OnlyDisplayCheck()
        self.display_block_layout.addWidget(self.only_block_check)

        # mesh
        self.display_mesh_frame = QFrame()
        self.addShadow(self.display_mesh_frame)
        self.display_mesh_frame.setFixedHeight(20)
        self.display_mesh_frame.setObjectName('display_mesh_frame')
        self.display_mesh_frame.setStyleSheet('''
                                                        #display_mesh_frame
                                                        {
                                                            background-color:rgb(69, 69, 69);
                                                            border-radius:3px;
                                                        }
                                                        ''')
        self.display_mesh_layout = QHBoxLayout()
        self.display_mesh_layout.setContentsMargins(8, 0, 2, 0)
        self.display_mesh_layout.setSpacing(3)
        self.display_mesh_frame.setLayout(self.display_mesh_layout)
        self.display_layout.addWidget(self.display_mesh_frame)

        self.display_mesh_label = DisplayLabel('mesh_display')
        self.display_mesh_label.setFont(font)
        self.display_mesh_label.setText('Mesh')
        self.display_mesh_layout.addWidget(self.display_mesh_label)

        self.display_mesh_layout.addStretch()

        self.display_mesh_check = DisplayCheck()
        self.display_mesh_layout.addWidget(self.display_mesh_check)

        self.only_mesh_check = OnlyDisplayCheck()
        self.display_mesh_layout.addWidget(self.only_mesh_check)

        # skeleton
        self.display_skeleton_frame = QFrame()
        self.addShadow(self.display_skeleton_frame)
        self.display_skeleton_frame.setFixedHeight(20)
        self.display_skeleton_frame.setObjectName('display_skeleton_frame')
        self.display_skeleton_frame.setStyleSheet('''
                                                        #display_skeleton_frame
                                                        {
                                                            background-color:rgb(69, 69, 69);
                                                            border-radius:3px;
                                                        }
                                                        ''')
        self.display_skeleton_layout = QHBoxLayout()

        self.display_skeleton_layout.setContentsMargins(8, 0, 2, 0)
        self.display_skeleton_layout.setSpacing(3)
        self.display_skeleton_frame.setLayout(self.display_skeleton_layout)
        self.display_layout.addWidget(self.display_skeleton_frame)

        self.display_skeleton_label = DisplayLabel('skeleton_display')
        self.display_skeleton_label.setFont(font)
        self.display_skeleton_label.setText('Skeleton')
        self.display_skeleton_layout.addWidget(self.display_skeleton_label)

        self.display_skeleton_layout.addStretch()

        self.display_skeleton_check = DisplayCheck()
        self.display_skeleton_layout.addWidget(self.display_skeleton_check)

        self.only_skeleton_check = OnlyDisplayCheck()
        self.display_skeleton_layout.addWidget(self.only_skeleton_check)

        # control
        self.display_control_frame = QFrame()
        self.addShadow(self.display_control_frame)
        self.display_control_frame.setFixedHeight(20)
        self.display_control_frame.setObjectName('display_control_frame')
        self.display_control_frame.setStyleSheet('''
                                                        #display_control_frame
                                                        {
                                                            background-color:rgb(69, 69, 69);
                                                            border-radius:3px;
                                                        }
                                                        ''')
        self.display_control_layout = QHBoxLayout()
        self.display_control_layout.setContentsMargins(8, 0, 2, 0)
        self.display_control_layout.setSpacing(3)
        self.display_control_frame.setLayout(self.display_control_layout)
        self.display_layout.addWidget(self.display_control_frame)

        self.display_control_label = DisplayLabel('control_display')
        self.display_control_label.setFont(font)
        self.display_control_label.setText('Control')
        self.display_control_layout.addWidget(self.display_control_label)

        self.display_control_layout.addStretch()

        self.display_control_check = DisplayCheck()
        self.display_control_layout.addWidget(self.display_control_check)

        self.only_control_check = OnlyDisplayCheck()
        self.display_control_layout.addWidget(self.only_control_check)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 5, 4)
        self.build_layout.addLayout(self.layout)

        self.edit_layout = QHBoxLayout()
        self.edit_layout.setContentsMargins(5, 10, 5, 0)
        self.layout.addLayout(self.edit_layout)

        self.reorient_button = FlattenBuildButton('reorient')
        self.edit_layout.addWidget(self.reorient_button)

        self.delete_button = FlattenBuildButton('delete')
        self.edit_layout.addWidget(self.delete_button)

        self.restore_button = FlattenBuildButton('restore')
        self.edit_layout.addWidget(self.restore_button)

        self.setting_button = FlattenBuildButton('setting')
        self.edit_layout.addWidget(self.setting_button)

        self.build_button = QPushButton()
        font.setPointSize(10)
        self.build_button.setFont(font)
        self.build_button.setText('Build')
        self.build_button.setMinimumSize(QSize(160, 45))
        self.build_button.setObjectName('build_button')
        icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/build/build.png', 35, 35)
        self.build_button.setIcon(icon)
        self.build_button.setIconSize(QSize(35, 35))
        self.build_button.setStyleSheet('''
                                            #build_button
                                            {
                                                color:rgb(180, 180, 180);
                                                background-color:rgb(61, 61, 61);
                                                border-radius:5px;
                                                border:2px solid rgb(71, 71, 71);
                                            } 
                                            #build_button:hover
                                            {
                                                background-color:rgb(91, 93, 95)
                                            }
                                            #build_button:press
                                            {
                                                background-color:rgb(91, 93, 95)
                                            }
                                        ''')
        self.layout.addWidget(self.build_button)

        # self.layout.addStretch()

        self.updateWidget()

    def connect(self):
        self.name_linEdit.textChanged.connect(self.setName)
        self.main_count_spin.valueChanged.connect(self.setMainCount)
        self.root_control_check.toggled.connect(self.setRootControl)
        self.gravity_control_check.toggled.connect(self.setGravityControl)

    def setName(self, name):
        if not mc.objExists('Block'):
            return
        mc.setAttr('Block.name', name, type='string')

    def setMainCount(self, main_count):
        if not mc.objExists('Block'):
            return
        mc.setAttr('Block.mainCount', main_count)

    def setRootControl(self, checked):
        if not mc.objExists('Block'):
            return
        mc.setAttr('Block.rootControl', checked)

    def setGravityControl(self, checked):
        if not mc.objExists('Block'):
            return
        mc.setAttr('Block.gravityControl', checked)

    def addShadow(self, widget):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 0)
        shadow.setBlurRadius(5)
        shadow.setColor(QColor(40, 40, 40))
        widget.setGraphicsEffect(shadow)

    def updateWidget(self):
        if not mc.objExists('Block'):
            return
        self.name_linEdit.setText(mc.getAttr('Block.name'))
        self.main_count_spin.setValue(mc.getAttr('Block.mainCount'))
        self.root_control_check.setChecked(mc.getAttr('Block.rootControl'))
        self.gravity_control_check.setChecked(mc.getAttr('Block.gravityControl'))

    def build(self, blocks):
        if not mc.objExists('Block'):
            return

        block_utilities.ensureAllBlockInfo(blocks)
        scale = block_utilities.getBlockScale()

        # 检查
        if not mc.file(maya_utilities.CURVE_FILE, q=True, ex=True):
            mc.error("File not found:" + maya_utilities.CURVE_FILE)
        # 确认属性
        block_utilities.ensureAllBlockAttrs()
        # 轴向
        block_utilities.updateBlockOrient(blocks)

        mc.file(maya_utilities.CURVE_FILE, i=True, ignoreVersion=True)
        mc.setAttr('curveGroup.v', 0)

        # Sets
        mc.select(cl=True)
        mc.sets(n='ControlSet')
        mc.sets(n='DeformSet')
        mc.sets(n='AllSet')
        mc.sets(n='Sets')
        mc.sets('AllSet', 'ControlSet', 'DeformSet', add='Sets')
        mc.sets(mc.listRelatives('curveGroup', c=True), add='ControlSet')
        # 2nd
        group_rig = mc.createNode('transform', n=mc.getAttr('Block.name') + '_Rig')
        mc.parent('Block', group_rig)
        block_utilities.lockAttrs(group_rig, 1, 1, 1, 0)
        # 3rd
        mc.createNode('transform', n='Motion_System', p=group_rig)
        mc.createNode('transform', n='Deformation_System', p=group_rig)
        mc.createNode('transform', n='Geometry', p=group_rig)
        # mc.setAttr('Block.v', l=False)
        # mc.setAttr('Block.v', 0, l=True)
        mc.setAttr('Geometry.inheritsTransform', 0, l=True)

        # 4th
        mc.createNode('transform', n='Main_System', p='Motion_System')

        # 创建main控制器
        main_count = mc.getAttr('Block.mainCount')
        main_name = mc.getAttr('Block.name')
        main_ctrl = main_name + '_Ctrl'
        for i in range(main_count):
            if i == 0:
                self.createController('Main', 'MainShape', main_ctrl, None, scale, block_joint=None)
                mc.parent(main_ctrl, 'Main_System')
            else:
                self.createController('Main', 'MainShape', '{0}{1}_Ctrl'.format(main_name, i), None,
                                      scale * 1 + 0.2 * i, block_joint=None)
                mc.parent('{0}{1}_Ctrl'.format(main_name, i), 'Main_System')

        for i in range(1, main_count - 1, 1):
            mc.parent('{0}{1}_Ctrl'.format(main_name, i + 1), '{0}{1}_Ctrl'.format(main_name, i))
        if main_count > 1:
            mc.parent('{0}1_Ctrl'.format(main_name), main_ctrl)

        mc.addAttr(main_ctrl, ln='jointVis', k=1, at='bool', dv=1)
        mc.setAttr(main_ctrl + '.jointVis', k=False, cb=True)






        # 生成Deform
        for b in [1, -1]:
            for block in blocks:
                block_joint = block.getJoint()
                side = block.getSide()
                mirror = block.getMirror()
                if b == -1 and side == 'M': continue
                if b == -1 and not mirror: continue
                if b == -1:
                    side = 'R' if side == 'L' else 'L'

                pos = mc.xform(block_joint, q=True, ws=True, t=True)
                rot = mc.xform(block_joint, q=True, ws=True, ro=True)
                deform_joint = side + '_' + block_joint + '_Jnt'
                mc.select(clear=True)
                mc.joint(n=deform_joint)
                mc.sets(deform_joint, add='DeformSet')
                # Root
                if block == blocks[0]:
                    mc.connectAttr(main_ctrl + '.jointVis', deform_joint + '.v')
                    mc.setAttr(deform_joint + '.segmentScaleCompensate', 0)

                mc.setAttr(deform_joint + '.rotateOrder', mc.getAttr(block_joint + '.rotateOrder'))
                mc.xform(deform_joint, ws=True, t=[pos[0] * b, pos[1], pos[2]])
                mc.xform(deform_joint, ws=True, ro=rot)

                if b == -1:
                    mirror_joint = mc.mirrorJoint(deform_joint, mirrorYZ=True, mirrorBehavior=True)
                    rot = mc.xform(mirror_joint, q=True, ws=True, ro=True)
                    mc.xform(deform_joint, ws=True, ro=rot)
                    mc.delete(mirror_joint)


        # deepcopy block
        mirror_blocks = []
        mirror_dic = {}
        for block in blocks:
            if not block.getSide() == 'M':
                if block.getInstance():
                    mirror_block = copy.deepcopy(block)
                    mirror_dic[mirror_block.getJoint()] = mirror_block
                    mirror_blocks.append(mirror_block)
                    side = block.getSide()
                    side = 'R' if side == 'L' else 'L'
                    mirror_block.setSide(side)
                    child_side = block.getFirstChildSide()
                    if child_side != 'M':
                        child_side = 'R' if child_side == 'L' else 'L'
                        mirror_block.setFirstChildSide(child_side)

        for mirror_block in mirror_blocks:
            parent = mc.listRelatives(mirror_block.getJoint(), parent=True, type='joint') or [None]
            parent = parent[0]

            if parent in mirror_dic.keys():
                mirror_block.setParentBlock(mirror_dic[parent])

        blocks.extend(mirror_blocks)
        deforms = []
        for block in blocks:
            deform = block_class.Deform(block)
            deforms.append(deform)

        # create part joints
        for deform in deforms:
            deform_joint = deform.getDeformJoint()
            mc.select(deform_joint)
            for part_joint in deform.getPartJoints():
                mc.joint(n=part_joint)
                mc.sets(part_joint, add='DeformSet')
                mc.setAttr(part_joint + '.rotateOrder', mc.getAttr(deform_joint + '.rotateOrder'))

        # parent deform_joint
        for deform in deforms:
            deform_joint = deform.getDeformJoint()
            deform_parent_joint = deform.getDeformParentJoint()
            if deform_parent_joint:
                mc.parent(deform_joint, deform_parent_joint)

        # parent part
        for deform in deforms:
            deform_child_joint = deform.getDeformChildJoint()
            if deform_child_joint:
                deform_joint = deform.getDeformJoint()
                part_joints = deform.getPartJoints()
                subdivide = deform.getSubdivide()
                part_dist = mc.getAttr(deform_child_joint + '.tx') / (subdivide + 1.0)
                for i in range(subdivide):
                    mc.setAttr(part_joints[i] + '.tx', part_dist)
                    mc.connectAttr(deform_joint + '.sx', part_joints[i] + '.sx')
                    mc.connectAttr(deform_joint + '.sy', part_joints[i] + '.sy')
                    mc.connectAttr(deform_joint + '.sz', part_joints[i] + '.sz')

                if part_joints:
                    mc.parent(deform_child_joint, w=True)
                    mc.parent(deform_child_joint, part_joints[-1])




    def createController(self, type, shape, name, side, scale, block_joint=None):
        mc.select(cl=True)
        if type == 'Main':
            mc.duplicate(shape, n=name)

        mc.scale(scale * 3, scale * 3, scale * 3, name, r=True)
        mc.makeIdentity(name, apply=True)
        mc.xform(name, ws=True, t=[0, 0, 0])


class DisplayCheck(QPushButton):
    def __init__(self, parent=None):
        super(DisplayCheck, self).__init__(parent)
        self.setCheckable(True)
        icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/build/display.svg', 14, 14)
        self.setIcon(icon)
        self.setIconSize(QSize(16, 18))
        self.setObjectName('DisplayCheck')
        self.setStyleSheet('''
                              #DisplayCheck
                              {
                                  border:none;
                                  border-radius:3px;
                                  background-color:transparent;
                              }
                              #DisplayCheck:checked
                              {
                                  background-color:rgb(98,150,141);
                              }
                          ''')


class OnlyDisplayCheck(QPushButton):
    def __init__(self, parent=None):
        super(OnlyDisplayCheck, self).__init__(parent)
        self.setCheckable(True)
        icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/build/only.svg', 14, 14)
        self.setIcon(icon)
        self.setIconSize(QSize(16, 18))
        self.setObjectName('DisplayCheck')
        self.setStyleSheet('''
                              #DisplayCheck
                              {
                                  border:none;
                                  border-radius:3px;
                                  background-color:transparent;
                              }
                              #DisplayCheck:checked
                              {
                                  background-color:rgb(176,120,108);
                              }
                          ''')


class DisplayLabel(QLabel):
    def __init__(self, icon, parent=None):
        super(DisplayLabel, self).__init__(parent)
        self.setStyleSheet('''  
                                background-color:transparent;
                                background-image:url(D:/Project/RigTools/Resources/icons/build/%s.svg);
                                background-repeat: no-repeat; 
                                background-position: left center ;
                                padding-left:18px;
                            ''' % (icon))


class FlattenBuildButton(QPushButton):
    def __init__(self, icon, parent=None):
        super(FlattenBuildButton, self).__init__(parent)
        self.icon = icon
        self.setObjectName('BuildFlattenButton')
        self.setStyleSheet('''
                            #BuildFlattenButton
                            {
                                background-color:transparent;
                                border:none;
                            }
                            ''')
        self.setIcon(
            maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/build/{}.svg'.format(self.icon), 22, 22))
        self.setIconSize(QSize(22, 22))
        self.setFixedSize(QSize(30, 30))

    def enterEvent(self, event):
        self.setIcon(
            maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/build/{}.svg'.format(self.icon), 24, 24))
        self.setIconSize(QSize(24, 24))

    def leaveEvent(self, event):
        self.setIcon(
            maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/build/{}.svg'.format(self.icon), 22, 22))
        self.setIconSize(QSize(22, 22))

