#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import maya.cmds as mc

import modules.maya_utilities as maya_utilities
from block_utilities import *
from modules.maya_utilities import *
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
        self.display_block_check.setChecked(True)
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

        self.updateWidget()

    def connect(self):
        self.name_linEdit.textChanged.connect(self.setName)
        self.main_count_spin.valueChanged.connect(self.setMainCount)
        self.root_control_check.toggled.connect(self.setRootControl)
        self.gravity_control_check.toggled.connect(self.setGravityControl)

        self.display_block_check.clicked.connect(lambda: self.displayBlock(self.display_block_check.isChecked()))
        self.display_skeleton_check.clicked.connect(
            lambda: self.displaySkeleton(self.display_skeleton_check.isChecked()))
        self.display_mesh_check.clicked.connect(lambda: self.displayMesh(self.display_mesh_check.isChecked()))
        self.display_control_check.clicked.connect(lambda: self.displayControl(self.display_control_check.isChecked()))

        self.only_block_check.clicked.connect(self.onlyDisplayBlock)
        self.only_skeleton_check.clicked.connect(self.onlyDisplaySkeleton)
        self.only_mesh_check.clicked.connect(self.onlyDisplayMesh)
        self.only_control_check.clicked.connect(self.onlyDisplayControl)

        self.restore_button.clicked.connect(self.restoreBuildPose)
        self.delete_button.clicked.connect(self.deleteRig)

    def displayBlock(self, checked):
        if mc.objExists('Block'):
            mc.setAttr('Block.v', checked)
        mc.refresh()

    def displayControl(self, checked):
        if mc.objExists('Motion_System'):
            mc.setAttr('Motion_System.v', checked)
        mc.refresh()

    def displaySkeleton(self, checked):
        if mc.objExists('Deformation_System'):
            mc.setAttr('Deformation_System.v', checked)
        mc.refresh()

    def displayMesh(self, checked):
        return
        mc.refresh()

    def onlyDisplayBlock(self):
        checked = self.only_block_check.isChecked()
        if checked:
            self.only_control_check.setChecked(False)
            self.only_skeleton_check.setChecked(False)
            self.only_mesh_check.setChecked(False)

            self.displayBlock(True)
            self.displayControl(False)
            self.displaySkeleton(False)
            self.displayMesh(False)
        else:
            self.displayBlock(self.display_block_check.isChecked())
            self.displayControl(self.display_control_check.isChecked())
            self.displaySkeleton(self.display_skeleton_check.isChecked())
            self.displayMesh(self.display_mesh_check.isChecked())

    def onlyDisplayControl(self):
        checked = self.only_control_check.isChecked()
        if checked:
            self.only_block_check.setChecked(False)
            self.only_skeleton_check.setChecked(False)
            self.only_mesh_check.setChecked(False)

            self.displayBlock(False)
            self.displayControl(True)
            self.displaySkeleton(False)
            self.displayMesh(False)
        else:
            self.displayBlock(self.display_block_check.isChecked())
            self.displayControl(self.display_control_check.isChecked())
            self.displaySkeleton(self.display_skeleton_check.isChecked())
            self.displayMesh(self.display_mesh_check.isChecked())

    def onlyDisplaySkeleton(self):
        checked = self.only_skeleton_check.isChecked()
        if checked:
            self.only_block_check.setChecked(False)
            self.only_control_check.setChecked(False)
            self.only_mesh_check.setChecked(False)

            self.displayBlock(False)
            self.displayControl(False)
            self.displaySkeleton(True)
            self.displayMesh(False)
        else:
            self.displayBlock(self.display_block_check.isChecked())
            self.displayControl(self.display_control_check.isChecked())
            self.displaySkeleton(self.display_skeleton_check.isChecked())
            self.displayMesh(self.display_mesh_check.isChecked())

    def onlyDisplayMesh(self):
        checked = self.only_mesh_check.isChecked()
        if checked:
            self.only_block_check.setChecked(False)
            self.only_control_check.setChecked(False)
            self.only_skeleton_check.setChecked(False)

            self.displayBlock(False)
            self.displayControl(False)
            self.displaySkeleton(False)
            self.displayMesh(True)
        else:
            self.displayBlock(self.display_block_check.isChecked())
            self.displayControl(self.display_control_check.isChecked())
            self.displaySkeleton(self.display_skeleton_check.isChecked())
            self.displayMesh(self.display_mesh_check.isChecked())

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
        self.deleteRig()
        ensureAllBlockInfo(blocks)
        scale = getBlockScale()

        # 检查
        if not mc.file(maya_utilities.CURVE_FILE, q=True, ex=True):
            mc.error("File not found:" + maya_utilities.CURVE_FILE)
        # 确认属性
        ensureAllBlockAttrs()
        # 轴向
        updateBlockOrient(blocks)

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
        lockAttrs(group_rig, 1, 1, 1, 0)
        # 3rd
        mc.createNode('transform', n='Motion_System', p=group_rig)
        mc.createNode('transform', n='Deformation_System', p=group_rig)
        mc.createNode('transform', n='Constraint_System', p=group_rig)
        mc.createNode('transform', n='Geometry', p=group_rig)
        mc.setAttr('Block.v', l=False)
        # mc.setAttr('Block.v', 0, l=True)
        mc.setAttr('Geometry.inheritsTransform', 0, l=True)

        # 4th
        mc.createNode('transform', n='Main_System', p='Motion_System')
        mc.createNode('transform', n='Root_System', p='Motion_System')
        mc.createNode('transform', n='FK_System', p='Motion_System')
        mc.createNode('transform', n='IK_System', p='Motion_System')
        mc.createNode('transform', n='Spline_System', p='Motion_System')
        mc.createNode('transform', n='Switch_System', p='Motion_System')
        mc.createNode('transform', n='Twist_System', p='Motion_System')
        mc.createNode('transform', n='Bendy_System', p='Motion_System')
        mc.createNode('transform', n='Part_System', p='Motion_System')
        mc.createNode('transform', n='Aim_System', p='Motion_System')
        mc.createNode('transform', n='Gravity_System', p='Motion_System')
        mc.createNode('transform', n='Finger_System', p='Motion_System')

        # 创建main控制器
        main_ctrls = []
        main_count = mc.getAttr('Block.mainCount')
        main_name = mc.getAttr('Block.name')
        for i in range(main_count):
            if i == 0:
                main_ctrl = self.createController('Main', 'MainShape', main_name, None, scale, loc=None)
                main_ctrls.append(main_ctrl)
                mc.parent(main_ctrl, 'Main_System')
            else:
                main_part_ctrl = self.createController('Main', 'MainShape', '{0}{1}'.format(main_name, i), None,
                                                       scale * 1 + 0.2 * i, loc=None)
                main_ctrls.append(main_part_ctrl)
                mc.parent(main_part_ctrl, 'Main_System')

        for i in range(len(main_ctrls) - 1):
            mc.parent(main_ctrls[i], main_ctrls[i + 1])

        main_allScale_mult = 'Main_AllScale_Mult'
        mc.createNode('multiplyDivide', n=main_allScale_mult)

        main_scale_mults = []
        for i in range(0, len(main_ctrls) - 1, 1):
            if i == 0:
                main_scale_mult = 'Main_Scale_Mult'
            else:
                main_scale_mult = 'Main_Scale{}_Mult'.format(i)
            main_scale_mults.append(main_scale_mult)
            mc.createNode('multiplyDivide', n=main_scale_mult)

        for i, main_scale_mult in enumerate(main_scale_mults):
            if i == 0:
                mc.connectAttr(main_ctrls[i] + '.s', main_scale_mults[i] + '.input1')
                mc.connectAttr(main_ctrls[i + 1] + '.s', main_scale_mults[i] + '.input2')
            else:
                mc.connectAttr(main_scale_mults[i - 1] + '.output', main_scale_mults[i] + '.input1')
                mc.connectAttr(main_ctrls[i + 1] + '.s', main_scale_mults[i] + '.input2')

        if main_scale_mults:
            mc.connectAttr(main_scale_mults[-1] + '.output', main_allScale_mult + '.input1')
        else:
            mc.connectAttr(main_ctrls[0] + '.s', main_allScale_mult + '.input1')
        main_ctrl = main_ctrls[0]

        mc.addAttr(main_ctrl, ln='jointVis', k=1, at='bool', dv=1)
        mc.setAttr(main_ctrl + '.jointVis', k=False, cb=True)
        mc.addAttr(main_ctrl, ln='fkVis', k=1, at='bool', dv=1)
        mc.setAttr(main_ctrl + '.fkVis', k=False, cb=True)
        mc.addAttr(main_ctrl, ln='ikVis', k=1, at='bool', dv=1)
        mc.setAttr(main_ctrl + '.ikVis', k=False, cb=True)
        mc.addAttr(main_ctrl, ln='splineVis', k=1, at='bool', dv=1)
        mc.setAttr(main_ctrl + '.splineVis', k=False, cb=True)
        mc.addAttr(main_ctrl, ln='partVis', k=1, at='bool', dv=0)
        mc.setAttr(main_ctrl + '.partVis', k=False, cb=True)
        mc.addAttr(main_ctrl, ln='bendyVis', k=1, at='bool', dv=1)
        mc.setAttr(main_ctrl + '.bendyVis', k=False, cb=True)
        mc.addAttr(main_ctrl, ln='aimVis', k=1, at='bool', dv=1)
        mc.setAttr(main_ctrl + '.aimVis', k=False, cb=True)
        mc.addAttr(main_ctrl, ln='fingerVis', k=1, at='bool', dv=1)
        mc.setAttr(main_ctrl + '.fingerVis', k=False, cb=True)
        mc.addAttr(main_ctrl, ln='gravityVis', k=1, at='bool', dv=1)
        mc.setAttr(main_ctrl + '.gravityVis', k=False, cb=True)

        mc.connectAttr(main_ctrl + '.fkVis', 'FK_System.v')
        mc.connectAttr(main_ctrl + '.ikVis', 'IK_System.v')
        mc.connectAttr(main_ctrl + '.splineVis', 'Spline_System.v')
        mc.connectAttr(main_ctrl + '.bendyVis', 'Bendy_System.v')
        mc.connectAttr(main_ctrl + '.partVis', 'Part_System.v')
        mc.connectAttr(main_ctrl + '.aimVis', 'Aim_System.v')
        mc.connectAttr(main_ctrl + '.gravityVis', 'Gravity_System.v')
        mc.connectAttr(main_ctrl + '.fingerVis', 'Finger_System.v')

        # mc.connectAttr(main_allScale_mult + '.output', 'FK_System.s')
        # mc.connectAttr(main_allScale_mult + '.output', 'IK_System.s')
        # mc.connectAttr(main_allScale_mult + '.output', 'Deformation_System.s')
        # mc.connectAttr(main_allScale_mult + '.output', 'Spline_System.s')

        # 5th
        mc.createNode('transform', n='IK_Joints', p='IK_System')
        mc.createNode('transform', n='IK_Control', p='IK_System')
        mc.createNode('transform', n='IK_Follow', p='IK_System')
        mc.createNode('transform', n='IK_Static', p='IK_System')
        mc.createNode('transform', n='IK_Message', p='IK_System')

        mc.createNode('transform', n='Spline_Control', p='Spline_System')
        mc.createNode('transform', n='Spline_Curve', p='Spline_System')
        mc.createNode('transform', n='Spline_Joint', p='Spline_System')

        mc.createNode('transform', n='Twist_Joint', p='Twist_System')
        mc.createNode('transform', n='Twist_Handle', p='Twist_System')

        mc.createNode('transform', n='Bendy_Curve', p='Bendy_System')
        mc.createNode('transform', n='Bendy_Control', p='Bendy_System')
        mc.createNode('transform', n='Bendy_Xform', p='Bendy_System')

        mc.createNode('transform', n='Part_Control', p='Part_System')

        # fk follow root
        mc.createNode('transform', n='FK_Follow_Root_Grp', p='FK_System')

        for i in ['FK_System', 'IK_System', 'Spline_Control', 'Root_System', 'Switch_System',
                  'Aim_System', 'Deformation_System', 'Part_System', 'Bendy_Control', 'Gravity_System',
                  'Finger_System']:
            mc.parentConstraint(main_ctrl, i)
            mc.connectAttr(main_allScale_mult + '.output', i + '.s')
            # mc.scaleConstraint(main_ctrl, i)

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
                mc.makeIdentity(deform_joint, apply=True)

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
                    mirror_block.side = side
                    child_side = block.getFirstChildSide()
                    if child_side != 'M':
                        child_side = 'R' if child_side == 'L' else 'L'
                        mirror_block.setFirstChildSide(child_side)

        for mirror_block in mirror_blocks:
            parent = mc.listRelatives(mirror_block.getJoint(), parent=True, type='joint') or [None]
            parent = parent[0]
            if parent in mirror_dic.keys():
                mirror_block.setParentBlock(mirror_dic[parent])
        all_blocks = [block for block in blocks]
        all_blocks.extend(mirror_blocks)
        deforms = []
        for block in all_blocks:
            deform = block_class.Deform(block)
            deforms.append(deform)
            if block in mirror_blocks:
                deform.setIsMirror(True)

        mc.parent(deforms[0].getDeformJoint(), 'Deformation_System')

        # create part joints
        for deform in deforms:
            fat = deform.getFat()
            deform_joint = deform.getDeformJoint()
            mc.addAttr(deform_joint, ln='fat', at='double', min=0, dv=fat)
            mc.select(deform_joint)
            for part_joint in deform.getPartJoints():
                mc.joint(n=part_joint)
                mc.addAttr(part_joint, ln='fat', at='double', min=0, dv=fat)
                mc.sets(part_joint, add='DeformSet')
                mc.setAttr(part_joint + '.rotateOrder', mc.getAttr(deform_joint + '.rotateOrder'))
                mc.makeIdentity(part_joint, apply=True)

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

        # create root
        root_joint = deforms[0].getDeformJoint()
        root_ctrl = self.createController('Root', 'RootShape', 'Root', 'M', scale * 1.5, loc=root_joint)
        root_pos = root_ctrl.replace('_Ctrl', '_Pos')
        mc.parent(root_pos, 'Root_System')

        mc.parentConstraint(root_ctrl, 'FK_Follow_Root_Grp')

        # create FK
        for deform in deforms:
            if not deform.getIKSolver() in ['FK', 'IKRPSolver']:
                continue
            deform_joint = deform.getDeformJoint()
            name = deform.getJoint()
            side = deform.getSide()
            fat = deform.getFat()
            fk_shape = deform.getFKShape()
            fk_joint = deform.getFKJoint()
            fk_ctrl = self.createController('FK', fk_shape + 'Shape', name + '_FK', side, scale * fat, deform_joint)
            mc.select(fk_ctrl)
            mc.joint(n=fk_joint)
            mc.setAttr(fk_joint + '.drawStyle', 2)
            # fk_joint的scale保持不变
            mc.connectAttr(fk_ctrl + '.scale', fk_joint + '.inverseScale')
            mc.setAttr(fk_joint + '.rotateOrder', mc.getAttr(deform_joint + '.rotateOrder'))

        # parent FK
        for deform in deforms:
            fk_ctrl = deform.getFKCtrl()
            if not mc.objExists(fk_ctrl):
                continue

            fk_pos = fk_ctrl.replace('_Ctrl', '_Pos')
            parent_side = deform.getParentSide()
            block_parent_joint = deform.getParent()
            fk_parent_ctrl = deform.getFKParentCtrl()
            fk_parent_joint = fk_parent_ctrl.replace('_Ctrl', '_Jnt')
            if not deform.getParent():
                mc.parent(fk_pos, 'FK_Follow_Root_Grp')
            elif deform.getIKSolver() != deform.block.getParentBlock().getIKSolver():
                # Toes应该算在虽然不是IKRPSolver，当也应该放进腿部IK中
                if deform.getIKToeJoint() != deform.getJoint():
                    fk_grp = parent_side + '_' + block_parent_joint + '_FK_Grp'
                    if not mc.objExists(fk_grp):
                        mc.createNode('transform', n=fk_grp, p='FK_System')
                        deform.setFKGrp(fk_grp)
                        align(fk_grp, deform.getDeformParentJoint(), 1, 0, 0, 0)
                        mc.pointConstraint(deform.getDeformParentJoint(), fk_grp)
                        mc.orientConstraint(deform.getDeformParentJoint(), fk_grp)
                    mc.parent(fk_pos, fk_grp)
                    if deform.getParentFunction() == 'Wrist':
                        mc.connectAttr('Main..fingerVis', fk_grp + '.v')
                else:
                    mc.parent(fk_pos, fk_parent_joint)

            else:
                if mc.objExists(fk_parent_joint):
                    mc.parent(fk_pos, fk_parent_joint)

        # segmentScaleCompensate FK
        # 使FK控制器连达到骨骼segmentScaleCompensate的效果
        # 常规情况下一个FK的层级链，FK1进行缩放，FK2、FK3由于是子物体也会缩放，
        # 在当前骨骼位置上放一个PS2，父骨骼位置放一个PS1，PS2是PS1子物体，
        # 用父骨骼scale约束PS1，并且开启ssc，此时缩放父控制器来缩放父骨骼，从而实现PS1的缩放，PS2因缩放产生位移
        # 用PS2point约束当前骨骼的组，实现ssc效果
        for deform in deforms:
            fk_ctrl = deform.getFKCtrl()
            if not mc.objExists(fk_ctrl):
                continue
            ssc = deform.getSSC()
            side = deform.getSide()
            block_joint = deform.getJoint()
            deform_joint = deform.getDeformJoint()
            deform_parent_joint = deform.getDeformParentJoint()
            fk_ctrl = deform.getFKCtrl()
            fk_parent_joint = deform.getFKParentJoint()
            fk_joint = deform.getFKJoint()
            fk_pos = fk_ctrl.replace('_Ctrl', '_Pos')
            if ssc:
                if deform.getParent() and deform.getIKSolver() == deform.block.getParentBlock().getIKSolver() and deform.getFunction() != 'End':
                    fk_ps1 = mc.createNode('transform', n=side + '_' + block_joint + '_PS1_Grp', p=fk_parent_joint)
                    fk_ps2 = mc.createNode('transform', n=side + '_' + block_joint + '_PS2_Grp', p=fk_joint)
                    mc.parent(fk_ps2, fk_ps1)
                    mc.scaleConstraint(fk_parent_joint, fk_ps1)
                    mc.pointConstraint(fk_ps2, fk_pos, mo=True)
            else:

                if mc.objExists(fk_joint):
                    mc.setAttr(fk_parent_joint + '.segmentScaleCompensate', 0)
                fk_grp = deform.getFKGrp()
                if fk_grp:
                    if not mc.isConnected(deform_parent_joint + '.s', fk_grp + '.s'):
                        mc.connectAttr(deform_parent_joint + '.s', fk_grp + '.s')

        # Create IK
        for deform in deforms:
            if deform.getIKSolver() == 'IKRPSolver' or deform.getIsToe() or deform.getIsToeEnd():
                function = deform.getFunction()
                block_joint = deform.getJoint()
                deform_joint = deform.getDeformJoint()
                deform_parent_joint = deform.getDeformParentJoint()
                ik_joint = deform.getIKJoint()
                ik_grp = deform.getIKGrp()
                mc.select(clear=True)
                mc.joint(n=ik_joint)
                mc.setAttr(ik_joint + '.drawStyle', 2)
                mc.setAttr(ik_joint + '.rotateOrder', mc.getAttr(block_joint + '.rotateOrder'))
                if function == 'IK':
                    # IKStart
                    mc.createNode('transform', n=ik_grp)
                    mc.setAttr(ik_grp + '.rotateOrder', mc.getAttr(block_joint + '.rotateOrder'))
                    mc.parent(ik_joint, ik_grp)
                    if mc.objExists(deform_parent_joint):
                        mc.parentConstraint(deform_parent_joint, ik_grp)
                    else:
                        align(ik_grp, deform_parent_joint)
                align(ik_joint, deform_joint, 1, 1, 0, 0)
                mc.makeIdentity(ik_joint, apply=True, r=True)

        # Parent IK
        for deform in deforms:
            if deform.getIKSolver() == 'IKRPSolver' or deform.getIsToe() or deform.getIsToeEnd():
                function = deform.getFunction()
                ik_joint = deform.getIKJoint()
                ik_parent_joint = deform.getIKParentJoint()
                ik_grp = deform.getIKGrp()
                if function == 'IK':
                    mc.parent(ik_grp, 'IK_Control')
                else:
                    mc.parent(ik_joint, ik_parent_joint)

        # Constraint to FK
        for deform in deforms:
            fk_joint = deform.getFKJoint()
            ik_joint = deform.getIKJoint()
            deform_joint = deform.getDeformJoint()
            if mc.objExists(fk_joint) and mc.objExists(ik_joint):
                mc.pointConstraint(fk_joint, deform_joint)
                mc.orientConstraint(fk_joint, deform_joint)
                mc.pointConstraint(ik_joint, deform_joint, weight=0)
                mc.orientConstraint(ik_joint, deform_joint, weight=0)
            elif mc.objExists(fk_joint):
                mc.pointConstraint(fk_joint, deform_joint)
                mc.orientConstraint(fk_joint, deform_joint)

        # # Root_Ctrl控制器Root
        # if not mc.objExists(deforms[0].getFKJoint()):
        #     mc.parentConstraint(root_ctrl, deforms[0].getDeformJoint(), mo=True)
        # Advanced IK
        for deform in deforms:
            function = deform.getFunction()
            if not function == 'IK':
                continue
            ik_start = deform.getIKStartJoint()
            ik_middle = deform.getIKMiddleJoint()
            ik_end = deform.getIKEndJoint()
            if not ik_start or not ik_middle or not ik_end:
                continue
            fat = deform.getFat()
            side = deform.getSide()
            ik_name = deform.getName()
            ik_start_joint = side + '_' + ik_start + '_IK_Jnt'
            ik_middle_joint = side + '_' + ik_middle + '_IK_Jnt'
            ik_end_joint = side + '_' + ik_end + '_IK_Jnt'
            ik_handle = side + '_' + ik_name + '_IK_Handle'
            ik_effector = side + '_' + ik_name + '_IK_Effector1'
            ik_ctrl = deform.getIKCtrl()
            pole_ctrl = deform.getPoleCtrl()
            poleAim_grp = deform.getPoleAimGrp()
            ik_pos = ik_ctrl.replace('_Ctrl', '_Pos')
            pole_pos = pole_ctrl.replace('_Ctrl', '_Pos')
            temp = mc.ikHandle(n=ik_handle, solver='ikRPsolver', sj=ik_start_joint, ee=ik_end_joint)[1]
            mc.rename(temp, ik_effector)
            mc.setAttr(ik_handle + '.v', 0, lock=True)
            mc.setAttr(ik_effector + '.v', 0, lock=True)
            mc.setAttr(ik_effector + '.rotateOrder', mc.getAttr(ik_end + '.rotateOrder'))
            self.createController('IK', 'IKShape', ik_name, side, scale * deform.getIKEndBlock().getFat(),
                                  loc=ik_end_joint)
            mc.parent(ik_pos, 'IK_Control')
            mc.parent(ik_handle, ik_ctrl)
            # 防止IK_start_ctrl缩放带动手脚
            # mc.connectAttr(ik_ctrl + '.s', ik_end_joint + '.s')
            mc.scaleConstraint(ik_ctrl, ik_end_joint)
            mc.setAttr(ik_end_joint + '.ssc', False)

            ik_grp = deform.getIKGrp()
            ikStart_Ctrl = ik_ctrl.replace('_IK_Ctrl', '_IKStart_Ctrl')
            ikStart_Pos = ikStart_Ctrl.replace('_Ctrl', '_Pos')
            self.createController('FK', 'StartShape', ik_name + '_IKStart', side, scale * fat * 1.5, loc=ik_start_joint)
            mc.setAttr(ikStart_Ctrl + '.sx', lock=True)
            mc.setAttr(ikStart_Ctrl + '.sy', lock=True)
            mc.setAttr(ikStart_Ctrl + '.sz', lock=True)
            mc.parent(ikStart_Pos, ik_grp)
            mc.parent(ik_start_joint, ikStart_Ctrl)
            # pole
            self.createController('Pole', 'PoleShape', ik_name, side, scale, loc=None)
            # mc.parent(pole_pos, 'IK_Follow_Main_Grp')
            mc.parent(pole_pos, ikStart_Ctrl)
            lockAttrs(pole_ctrl, 0, 1, 1, 1)
            # 点约束加目标约束
            temp1 = mc.createNode('transform', n='temp_pole_placer1')
            temp2 = mc.createNode('transform', n='temp_pole_placer2', p='temp_pole_placer1')
            temp3 = mc.createNode('transform', n='temp_pole_placer3', p='temp_pole_placer2')
            con = mc.pointConstraint(ik_start_joint, ik_end_joint, temp1)[0]
            pos1 = mc.xform(ik_middle_joint, q=True, ws=True, t=True)
            pos2 = mc.xform(ik_end_joint, q=True, ws=True, t=True)
            dist1 = getDistance(pos1, pos2)
            mc.setAttr(con + '.{}W0'.format(ik_start_joint), dist1)
            pos3 = mc.xform(ik_start_joint, q=True, ws=True, t=True)
            dist2 = getDistance(pos1, pos3)
            mc.setAttr(con + '.{}W1'.format(ik_end_joint), dist2)
            mc.aimConstraint(ik_middle_joint, temp2, aimVector=(1, 0, 0), upVector=(0, 1, 0), worldUpType='object',
                             worldUpObject=ik_start_joint)
            ik_length = dist1 + dist2
            mc.setAttr(temp3 + '.tx', ik_length)
            mc.matchTransform(pole_pos, temp3, position=True)
            mc.delete(temp1)
            mc.poleVectorConstraint(pole_ctrl, ik_handle)
            # 创建指向pole的线
            ann_shape = side + '_' + ik_name + '_Pole_AnnotationShape'
            ann = side + '_' + ik_name + '_Pole_Annotation'
            mc.createNode('annotationShape', n=ann_shape)
            mc.setAttr(ann_shape + '.overrideEnabled', True)
            mc.setAttr(ann_shape + '.overrideDisplayType', 1)
            mc.setAttr(ann_shape + '.overrideRGBColors', 1)
            mc.setAttr(ann_shape + '.overrideColorRGB', 255 / 255.0, 118 / 255.0, 117 / 255.0)
            mc.parent(ann, ik_middle_joint)
            mc.setAttr(ann + '.t', 0, 0, 0)
            mc.connectAttr(pole_ctrl + 'Shape.worldMatrix[0]', ann + 'Shape.dagObjectMatrix[0]')

            # 创建ikfk_aligned
            ikfk_aligned = side + '_' + ik_name + 'ikfkAligned'
            ikfk_aligned_offset = side + '_' + ik_name + 'ikfkAligned_Offset'
            mc.createNode('transform', n=ikfk_aligned_offset, p=ik_ctrl)
            mc.createNode('transform', n=ikfk_aligned, p=ikfk_aligned_offset)
            mc.orientConstraint(ikfk_aligned, ik_end_joint)

            # 创建poleAim
            mc.createNode('transform', n=poleAim_grp)
            align(poleAim_grp, ik_start_joint, 1, 0, 0, 0)
            con = mc.aimConstraint(ik_ctrl, poleAim_grp, aimVector=(1, 0, 0), upVector=(0, 1, 0),
                                   worldUpVector=(0, 1, 0), worldUpType='objectrotation',
                                   worldUpObject=ikfk_aligned_offset)[0]
            mc.parent(poleAim_grp, 'IK_Control')
            ik_parent = mc.listRelatives(ik_start_joint, p=True)
            mc.pointConstraint(ik_parent, poleAim_grp)

            mc.addAttr(ik_ctrl, k=True, ln='swivel', at='double', dv=0)
            mc.connectAttr(ik_ctrl + '.swivel', con + '.offset.offsetX')

        # Advanced Spline
        for deform in deforms:
            function = deform.getFunction()
            if not function == 'Spline':
                continue
            spline_blocks = [deform.getSplineStartBlock()]
            spline_blocks.extend(deform.getSplineMiddleBlocks())
            spline_blocks.append(deform.getSplineEndBlock())
            deform_joints = []
            block_joints = []
            spline_joints = []  # 不拉伸时驱动
            fat = deform.getFat()
            side = deform.getSide()
            spline_name = deform.getName()
            spline_curve = side + '_' + spline_name + '_Spline_Curve'

            spline_grp = side + '_' + spline_name + '_Spline_Grp'
            deform_parent_joint = deform.getDeformParentJoint()
            mc.createNode('transform', n=spline_grp)
            if deform_parent_joint:
                align(spline_grp, deform_parent_joint, 1, 1, 0, 0)
                mc.parentConstraint(deform_parent_joint, spline_grp)
            else:
                align(spline_grp, deforms[0].getDeformJoint(), 1, 1, 0, 0)
                mc.parentConstraint(root_ctrl, spline_grp)
            mc.parent(spline_grp, 'Spline_Control')

            for spline_block in spline_blocks:
                deform_joints.append(spline_block.getSide() + '_' + spline_block.getJoint() + '_Jnt')
                block_joints.append(spline_block.getJoint())
                if spline_block != spline_blocks[-1]:
                    deform_joints.extend(
                        [spline_block.getSide() + '_' + spline_block.getJoint() + 'Part{}_Jnt'.format(i) for i in
                         range(1, spline_block.getSubdivide() + 1, 1)])
                    block_joints.extend([spline_block.getJoint() + 'Part{}'.format(i) for i in
                                         range(1, spline_block.getSubdivide() + 1, 1)])

            spline_joint_grp = side + '_' + spline_name + '_SplineJoint_Grp'
            mc.createNode('transform', n=spline_joint_grp)
            align(spline_joint_grp, deform_joints[0], 1, 1, 0, 0)
            mc.parent(spline_joint_grp, 'Spline_Joint')
            # 创建Spline骨骼
            mc.select(clear=True)
            for i, deform_joint in enumerate(deform_joints):
                spline_joint = deform_joint.replace('_Jnt', '_Spline_Jnt')
                spline_joints.append(spline_joint)
                mc.joint(n=spline_joint)
                mc.setAttr(spline_joint + '.drawStyle', 2)
                align(spline_joint, deform_joint, 1, 1, 0, 0)
                mc.makeIdentity(spline_joint, apply=True, r=True)

            # 用于处理拉伸
            spline_start_joint = side + '_' + spline_name + '_Start_Jnt'
            spline_end_joint = side + '_' + spline_name + '_End_Jnt'
            spline_start_orient = side + '_' + spline_name + '_Start_Orient'
            spline_end_orient = side + '_' + spline_name + '_End_Orient'
            spline_startTwist_orient = side + '_' + spline_name + '_StartTwist_Orient'
            spline_endTwist_orient = side + '_' + spline_name + '_EndTwist_Orient'

            mc.select(clear=True)
            mc.joint(n=spline_start_joint)
            mc.setAttr(spline_start_joint + '.drawStyle', 2)
            align(spline_start_joint, spline_joints[0], 1, 1, 0, 0)
            mc.makeIdentity(spline_start_joint, apply=True, r=True)
            mc.parent(spline_joints[1], spline_start_joint)
            mc.select(spline_joints[-2])
            mc.joint(n=spline_end_joint)
            mc.setAttr(spline_end_joint + '.drawStyle', 2)
            align(spline_end_joint, spline_joints[-1], 1, 1, 0, 0)
            mc.setAttr(spline_end_joint + '.jo', 0, 0, 0)
            mc.makeIdentity(spline_end_joint, apply=True, r=True)
            mc.createNode('transform', n=spline_start_orient)
            align(spline_start_orient, spline_start_joint, 1, 1, 0, 0)
            mc.createNode('transform', n=spline_end_orient)
            align(spline_end_orient, spline_end_joint, 1, 1, 0, 0)
            mc.createNode('transform', n=spline_startTwist_orient)
            align(spline_startTwist_orient, spline_start_joint, 1, 1, 0, 0)
            mc.createNode('transform', n=spline_endTwist_orient)
            align(spline_endTwist_orient, deform_joints[-1], 1, 1, 0, 0)


            points = [mc.xform(spline_deform_joint, q=True, ws=True, t=True) for spline_deform_joint in
                      spline_joints]
            if len(points) < 4:
                mc.curve(n=spline_curve, d=1, point=points)
            else:
                mc.curve(n=spline_curve, d=3, point=points)
            spline_curve_shape = spline_curve + 'Shape'
            temp = mc.listRelatives(spline_curve, s=True)

            mc.rename(temp, spline_curve_shape)
            mc.setAttr(spline_curve_shape + '.overrideEnabled', 1)
            mc.setAttr(spline_curve_shape + '.overrideDisplayType', 1)
            mc.parent(spline_curve, 'Spline_Curve')
            mc.parent(spline_start_joint, spline_joint_grp)

            spline_handle = side + '_' + spline_name + '_Spline_Handle'
            spline_effector = side + '_' + spline_name + '_Spline_Effector'
            temp = mc.ikHandle(n=spline_handle, solver='ikSplineSolver', sj=spline_start_joint,
                               ee=spline_end_joint, createCurve=False)[1]
            mc.rename(temp, spline_effector)
            mc.setAttr(spline_handle + '.v', 0)
            mc.setAttr(spline_effector + '.v', 0)
            mc.setAttr(spline_effector + '.rotateOrder', mc.getAttr(spline_joints[0] + '.rotateOrder'))
            mc.parent(spline_handle, spline_grp)

            mc.createNode('motionPath', n='temp_MotionPath')
            mc.createNode('transform', n='temp_pos')
            mc.connectAttr(spline_curve_shape + '.worldSpace', 'temp_MotionPath.geometryPath')
            mc.connectAttr('temp_MotionPath.allCoordinates', 'temp_pos.t')
            mc.connectAttr('temp_MotionPath.rotate', 'temp_pos.rotate')
            mc.setAttr('temp_MotionPath.fractionMode', True)
            mc.setAttr('temp_MotionPath.worldUpType', 2)
            mc.setAttr('temp_MotionPath.frontAxis', 0)
            mc.setAttr('temp_MotionPath.upAxis', 1)
            mc.setAttr('temp_MotionPath.worldUpVector', 0, 1, 0)
            mc.connectAttr(spline_joints[0] + '.worldMatrix[0]', 'temp_MotionPath.worldUpMatrix')
            if deform.getIsMirror():
                mc.setAttr('tempMotionPath.inverseFront', 1)

            # 创建cv控制器, cv控制器直接控制曲线
            spline_cv_grp = side + '_' + spline_name + '_SplineCV_Grp'
            mc.createNode('transform', n=spline_cv_grp)
            mc.parent(spline_cv_grp, spline_grp)
            align(spline_cv_grp, deform_joints[0], 1, 1, 0, 0)
            cv_ctrls = []
            for i, spline_deform_joint in enumerate(spline_joints):
                cv_ctrl = self.createController('Cv', 'CvShape', spline_name + '_CV{}'.format(i), side, scale * fat,
                                                loc=None)
                mc.setAttr(cv_ctrl + '.v', False, l=True)
                cv_ctrls.append(cv_ctrl)
                cv_pos = cv_ctrl.replace('_Ctrl', '_Pos')
                mc.parent(cv_pos, spline_cv_grp)
                mc.matchTransform(cv_pos, spline_deform_joint, position=True)
                mc.connectAttr(cv_ctrl + 'Shape.worldPosition[0]',
                               spline_curve_shape + '.controlPoints[{}]'.format(i))

                if i == 0 or i == len(spline_joints) - 1:
                    mc.parent(cv_ctrl, w=True)
                    mc.delete(cv_pos)

            for i in range(len(spline_joints)):
                mc.setAttr('temp_MotionPath.uValue', i / (len(spline_joints) - 1.0))
                align(cv_ctrls[i], 'temp_pos', 0, 1, 0, 0)

            spline_ctrl_grp = side + '_' + spline_name + '_SplineCtrl_Grp'
            mc.createNode('transform', n=spline_ctrl_grp)
            mc.parent(spline_ctrl_grp, spline_grp)
            align(spline_ctrl_grp, deform_joints[0], 1, 1, 0, 0)

            # 创建Spline控制器
            spline_ctrls = []
            splineSec_ctrls = []
            spline_poss = []
            for i in range(1, len(spline_blocks) + 1, 1):
                if i == 1:
                    # align(spline_pos, deform_joints[0], 1, 1, 0, 0)
                    # align(splineSec_pos, deform_joints[0], 1, 1, 0, 0)
                    spline_ctrl = self.createController('Spline', 'SplineShape', spline_name + '{}_Spline'.format(i),
                                                        side,
                                                        scale * fat * 3, loc=deform_joints[0])
                    splineSec_ctrl = self.createController('Spline', 'SplineSecShape',
                                                           spline_name + '{}_SplineSec'.format(i),
                                                           side, scale * fat * 2, loc=deform_joints[0])
                elif i == len(spline_blocks):
                    mc.createNode('transform', n='temp')
                    align('temp', deform_joints[-1], 1, 0, 0, 0)
                    align('temp', deform_joints[-1], 1, 0, 0, 0)
                    align('temp', deform_joints[-2], 0, 1, 0, 0)
                    align('temp', deform_joints[-2], 0, 1, 0, 0)
                    spline_ctrl = self.createController('Spline', 'SplineShape', spline_name + '{}_Spline'.format(i),
                                                        side,
                                                        scale * fat * 3, loc='temp')
                    splineSec_ctrl = self.createController('Spline', 'SplineSecShape',
                                                           spline_name + '{}_SplineSec'.format(i),
                                                           side, scale * fat * 2, loc='temp')
                    mc.delete('temp')
                else:
                    mc.setAttr('temp_MotionPath.uValue', (i - 1.0) / (3.0 - 1.0))
                    # align(spline_pos, 'temp_pos', 1, 1, 0, 0)
                    # align(splineSec_pos, 'temp_pos', 1, 1, 0, 0)
                    spline_ctrl = self.createController('Spline', 'SplineShape', spline_name + '{}_Spline'.format(i),
                                                        side,
                                                        scale * fat * 3, loc='temp_pos')
                    splineSec_ctrl = self.createController('Spline', 'SplineSecShape',
                                                           spline_name + '{}_SplineSec'.format(i),
                                                           side, scale * fat * 2, loc='temp_pos')

                spline_ctrls.append(spline_ctrl)
                splineSec_ctrls.append(splineSec_ctrl)
                spline_pos = spline_ctrl.replace('_Ctrl', '_Pos')
                spline_poss.append(spline_pos)
                mc.parent(spline_pos, spline_ctrl_grp)
                if i == 1:
                    mc.parent(cv_ctrls[0], spline_ctrl)
                if i == 3:
                    mc.parent(cv_ctrls[-1], spline_ctrl)

            mc.parent(spline_start_orient, spline_ctrls[0])
            mc.parent(spline_end_orient, spline_ctrls[-1])
            mc.parent(spline_startTwist_orient, spline_ctrls[0])
            mc.parent(spline_endTwist_orient, spline_ctrls[-1])

            for i in range(1, len(spline_blocks) - 1, 1):
                con = mc.parentConstraint(spline_ctrls[0], spline_ctrls[-1], spline_poss[i], mo=True)[0]
                w0 = 1.0 - i / (len(spline_blocks) - 1.0)
                w1 = 1.0 - w0
                mc.setAttr('{0}.{1}W0'.format(con, spline_ctrls[0]), w0)
                mc.setAttr('{0}.{1}W1'.format(con, spline_ctrls[-1]), w1)
                mc.setAttr(con + '.interpType', 2)

            spline_sec_grp = side + '_' + spline_name + '_SplineSec_Grp'
            mc.createNode('transform', n=spline_sec_grp)
            mc.parent(spline_sec_grp, spline_grp)
            align(spline_sec_grp, deform_joints[0], 1, 1, 0, 0)

            splineSec_poss = [splineSec_ctrl.replace('_Ctrl', '_Pos') for splineSec_ctrl in splineSec_ctrls]
            cv_poss = [cv_ctrl.replace('_Ctrl', '_Pos') for cv_ctrl in cv_ctrls]
            for i in range(len(splineSec_ctrls)):
                if i == 0:
                    mc.parent(splineSec_poss[i], spline_sec_grp)
                if i != len(splineSec_ctrls) - 1:
                    mc.parent(splineSec_poss[i + 1], splineSec_ctrls[i])

            # cv控制器收到spline控制器控制每个cv控制器收到两个spline控制器控制，以距离为权重，更近的spline控制更强
            # 除了第二个和和倒数第二个，为了让胯和胸腔更硬，首位控制更强， stiff最大时，它俩只受首尾控制
            # Spline控制器 stiff
            for i in range(1, len(cv_ctrls) - 1, 1):
                cv_ctrl = cv_ctrls[i]
                pos1 = mc.xform(cv_ctrl, q=True, ws=True, t=True)
                dist_list = [getDistance(pos1, mc.xform(spline_ctrl, q=True, ws=True, t=True)) for spline_ctrl in
                             spline_ctrls]
                temp = sorted(dist_list)
                min_dist1 = temp[0]
                min_dist2 = temp[1]
                index1 = dist_list.index(min_dist1)
                index2 = dist_list.index(min_dist2)

                con = mc.parentConstraint(spline_ctrls[index1], spline_ctrls[index2], cv_poss[i], mo=True)[0]
                mc.setAttr('{0}.{1}W0'.format(con, spline_ctrls[index1]), min_dist2 / (min_dist1 + min_dist2))
                mc.setAttr('{0}.{1}W1'.format(con, spline_ctrls[index2]), min_dist1 / (min_dist1 + min_dist2))
                # 处理胸腔，胸腔很硬,stiff控制曲线首尾，让曲线首尾直一点
                if i == 1 or i == len(cv_ctrls) - 2:
                    mc.addAttr(spline_ctrls[index1], ln='stiff', at='double', min=0, max=10, dv=0, k=True)
                    spline_stiff_range = side + '_' + spline_name + '_Stiff{}_Range'.format(index1)
                    mc.createNode('setRange', n=spline_stiff_range)

                    mc.connectAttr(spline_ctrls[index1] + '.stiff', spline_stiff_range + '.valueX')
                    mc.connectAttr(spline_ctrls[index1] + '.stiff', spline_stiff_range + '.valueY')
                    mc.setAttr(spline_stiff_range + '.minX', min_dist2 / (min_dist1 + min_dist2))
                    mc.setAttr(spline_stiff_range + '.minY', min_dist1 / (min_dist1 + min_dist2))
                    mc.setAttr(spline_stiff_range + '.maxX', 1)
                    mc.setAttr(spline_stiff_range + '.oldMax', 10, 10, 0, type='float3')
                    mc.connectAttr(spline_stiff_range + '.outValueX', '{0}.{1}W0'.format(con, spline_ctrls[index1]))
                    mc.connectAttr(spline_stiff_range + '.outValueY', '{0}.{1}W1'.format(con, spline_ctrls[index2]))

            mc.delete('temp_pos')

            mc.connectAttr(spline_curve + '.worldSpace[0]', spline_handle + '.inCurve')

            mc.parent(spline_ctrls[-1].replace('_Ctrl', '_Pos'), splineSec_ctrls[-1])

            # spline stretchy
            spline_curveInfo = side + '_' + spline_name + '_Spline_CurveInfo'
            mc.createNode('curveInfo', n=spline_curveInfo)
            mc.connectAttr(spline_curve + '.worldSpace[0]', spline_curveInfo + '.inputCurve')

            mc.addAttr(spline_ctrls[-1], k=True, ln='stretchy', at='double', min=0, max=10, dv=10)
            spline_ratio_mult = side + '_' + spline_name + '_Ratio_Mult'
            mc.createNode('multiplyDivide', n=spline_ratio_mult)
            mc.setAttr(spline_ratio_mult + '.operation', 2)
            # 当前长度除以原始长度
            mc.connectAttr(spline_curveInfo + '.arcLength', spline_ratio_mult + '.input1X')
            mc.setAttr(spline_ratio_mult + '.input2X', mc.getAttr(spline_curveInfo + '.arcLength'))
            # 添加Main缩放的影响
            spline_allScale_mult = side + '_' + spline_name + '_AllScale_Mult'
            mc.createNode('multiplyDivide', n=spline_allScale_mult)
            mc.setAttr(spline_allScale_mult + '.operation', 2)
            mc.connectAttr(spline_ratio_mult + '.outputX', spline_allScale_mult + '.input1X')
            mc.connectAttr(main_allScale_mult + '.outputX', spline_allScale_mult + '.input2X')

            # stretch 10 -> 1
            spline_stretch_unit = side + '_' + spline_name + '_Stretchy_Unit'
            mc.createNode('unitConversion', n=spline_stretch_unit)
            mc.setAttr(spline_stretch_unit + '.conversionFactor', 0.1)
            mc.connectAttr(spline_ctrls[-1] + '.stretchy', spline_stretch_unit + '.input')
            # 1 - stretch
            spline_stretch_reverse = side + '_' + spline_name + '_Stretchy_Reverse'
            mc.createNode('reverse', n=spline_stretch_reverse)
            mc.connectAttr(spline_stretch_unit + '.output', spline_stretch_reverse + '.inputX')

            # （（当前曲线长度 / 初始曲线长度） * mainScale） * 原始tx
            for i in range(1, len(spline_joints), 1):
                spline_joint = spline_joints[i]
                if i == len(spline_joints) - 1:
                    spline_joint = spline_end_joint
                # 记录spline骨骼的初始tx
                spline_stretch_mult = side + '_' + block_joints[i] + '_Stretchy_Mult'
                mc.createNode('multiplyDivide', n=spline_stretch_mult)
                mc.setAttr(spline_stretch_mult + '.input1X', mc.getAttr(spline_joint + '.tx'))
                mc.connectAttr(spline_allScale_mult + '.outputX', spline_stretch_mult + '.input2X')
                # 添加stretchy属性影响
                spline_stretchy_blend = side + '_' + block_joints[i] + '_Stretchy_Blend'
                mc.createNode('blendTwoAttr', n=spline_stretchy_blend)
                mc.setAttr(spline_stretchy_blend + '.input[0]', mc.getAttr(spline_joint + '.tx'))
                mc.connectAttr(spline_stretch_mult + '.outputX', spline_stretchy_blend + '.input[1]')
                mc.connectAttr(spline_stretchy_blend + '.output', spline_joint + '.tx')
                mc.connectAttr(spline_stretch_unit + '.output', spline_stretchy_blend + '.attributesBlender')

            # IKAc 拉伸
            # 不拉伸时使用SplineIK
            # 拉伸时使用IKAc，ikac直接使用曲线，根据原始位置确定AC骨骼在曲线上的比例位置
            attach_grp = side + '_' + spline_name + '_Attach_Grp'
            mc.createNode('transform', n=attach_grp)
            mc.parent(attach_grp, spline_joint_grp)
            attach_joints = []
            for spline_joint in spline_joints:
                mc.select(attach_grp)
                attach_joint = spline_joint.replace('_Spline_Jnt', '_Attach_Jnt')
                mc.joint(n=attach_joint)
                mc.setAttr(attach_joint + '.drawStyle', 2)
                attach_joints.append(attach_joint)

            if mc.objExists('temp_nearestPointOnCurve'):
                mc.delete('temp_nearestPointOnCurve')
            mc.createNode('nearestPointOnCurve', n='temp_nearestPointOnCurve')
            mc.connectAttr(spline_curve + '.worldSpace[0]', 'temp_nearestPointOnCurve.inputCurve')
            for i, attach_joint in enumerate(attach_joints):
                attach_pointOnCurveInfo = side + '_' + block_joints[i] + '_SplineAc_PointOnCurveInfo'
                mc.createNode('pointOnCurveInfo', n=attach_pointOnCurveInfo)
                mc.connectAttr(spline_curve + '.worldSpace[0]', attach_pointOnCurveInfo + '.inputCurve')
                mc.setAttr(attach_pointOnCurveInfo + '.turnOnPercentage', 0)

                pos = mc.xform(spline_joints[i], q=True, ws=True, t=True)
                mc.setAttr('temp_nearestPointOnCurve.inPosition', pos[0], pos[1], pos[2])
                mc.setAttr(attach_pointOnCurveInfo + '.parameter',
                           mc.getAttr('temp_nearestPointOnCurve.result.parameter'))
                mc.connectAttr(attach_pointOnCurveInfo + '.position', attach_joint + '.t')

                if i == 0:
                    world_up_object = spline_start_joint
                else:
                    world_up_object = attach_joints[i - 1]
                if i < len(attach_joints) - 1:
                    if not deform.getIsMirror():
                        aim_vector = (1, 0, 0)
                    else:
                        aim_vector = (-1, 0, 0)
                    con = mc.aimConstraint(attach_joints[i + 1], attach_joints[i], aimVector=aim_vector,
                                     upVector=(0, 1, 0), worldUpType='objectrotation', worldUpObject=world_up_object,
                                     worldUpVector=(0, 1, 0))[0]
                    mc.connectAttr(spline_joints[i] + '.rx', con + '.offset.offsetX')
            mc.delete('temp_nearestPointOnCurve')

            # lock start orient
            mc.addAttr(spline_ctrls[0], k=True, ln='lockStartOrient', at='double', min=0, max=10, dv=10)
            mc.parent(spline_joints[0], spline_ctrls[0])
            con = mc.orientConstraint(spline_start_joint, spline_start_orient, spline_joints[0])[0]
            spline_lockStartOrient_unit = side + '_' + spline_name + '_lockStartOrient_unit'
            mc.createNode('unitConversion', n=spline_lockStartOrient_unit)
            mc.connectAttr(spline_ctrls[0] + '.lockStartOrient', spline_lockStartOrient_unit + '.input')
            mc.setAttr(spline_lockStartOrient_unit + '.conversionFactor', 0.1)
            spline_lockStartOrient_reverse = side + '_' + spline_name + '_lockStartOrient_reverse'
            mc.createNode('reverse', n=spline_lockStartOrient_reverse)
            mc.connectAttr(spline_lockStartOrient_unit + '.output', spline_lockStartOrient_reverse + '.inputX')
            mc.connectAttr(spline_lockStartOrient_reverse + '.outputX', '{0}.{1}W0'.format(con, spline_start_joint))
            mc.connectAttr(spline_lockStartOrient_unit + '.output', '{0}.{1}W1'.format(con, spline_start_orient))

            # lock end orient
            mc.addAttr(spline_ctrls[-1], k=True, ln='lockEndOrient', at='double', min=0, max=10, dv=10)
            mc.parent(spline_joints[-1], spline_ctrls[-1])
            con = mc.orientConstraint(spline_end_joint, spline_end_orient, spline_joints[-1])[0]
            spline_lockEndOrient_unit = side + '_' + spline_name + '_lockEndOrient_unit'
            mc.createNode('unitConversion', n=spline_lockEndOrient_unit)
            mc.connectAttr(spline_ctrls[-1] + '.lockEndOrient', spline_lockEndOrient_unit + '.input')
            mc.setAttr(spline_lockEndOrient_unit + '.conversionFactor', 0.1)
            spline_lockEndOrient_reverse = side + '_' + spline_name + '_lockEndOrient_reverse'
            mc.createNode('reverse', n=spline_lockEndOrient_reverse)
            mc.connectAttr(spline_lockEndOrient_unit + '.output', spline_lockEndOrient_reverse + '.inputX')
            mc.connectAttr(spline_lockEndOrient_reverse + '.outputX', '{0}.{1}W0'.format(con, spline_end_joint))
            mc.connectAttr(spline_lockEndOrient_unit + '.output', '{0}.{1}W1'.format(con, spline_end_orient))

            for i in range(len(attach_joints)):
                if i == 0:
                    mc.pointConstraint(spline_joints[0], deform_joints[0])
                    mc.orientConstraint(spline_joints[0], deform_joints[0])
                else:

                    if i == len(attach_joints) - 1:
                        con = mc.pointConstraint(attach_joints[i], spline_end_joint, deform_joints[i])[0]
                        mc.connectAttr(spline_stretch_unit + '.output', '{0}.{1}W0'.format(con, attach_joints[i]))
                        mc.connectAttr(spline_stretch_reverse + '.outputX', '{0}.{1}W1'.format(con, spline_end_joint))
                        mc.orientConstraint(spline_joints[-1], deform_joints[-1])
                    else:
                        con = mc.pointConstraint(attach_joints[i], spline_joints[i], deform_joints[i])[0]
                        mc.connectAttr(spline_stretch_unit + '.output', '{0}.{1}W0'.format(con, attach_joints[i]))
                        mc.connectAttr(spline_stretch_reverse + '.outputX', '{0}.{1}W1'.format(con, spline_joints[i]))
                        con = mc.orientConstraint(attach_joints[i], spline_joints[i], deform_joints[i])[0]
                        mc.connectAttr(spline_stretch_unit + '.output', '{0}.{1}W0'.format(con, attach_joints[i]))
                        mc.connectAttr(spline_stretch_reverse + '.outputX', '{0}.{1}W1'.format(con, spline_joints[i]))

                    # mc.connectAttr(spline_ratio_mult + '.output.outputX', attach_joints[i] + '.sx')
                    # mc.connectAttr(spline_ratio_mult + '.output.outputX', attach_joints[i] + '.sy')
                    # mc.connectAttr(spline_ratio_mult + '.output.outputX', attach_joints[i] + '.sz')
            # Twist
            mc.setAttr(spline_handle + '.dTwistControlEnable', 1)
            mc.setAttr(spline_handle + '.dWorldUpType', 4)
            mc.connectAttr(spline_startTwist_orient + '.worldMatrix', spline_handle + '.dWorldUpMatrix')
            mc.connectAttr(spline_endTwist_orient + '.worldMatrix', spline_handle + '.dWorldUpMatrixEnd')

            for i, spline_joint in enumerate(spline_joints):
                spline_scaler = side + '_' + block_joints[i] + '_Scaler'
                mc.createNode('transform', n=spline_scaler)
                mc.parent(spline_scaler, spline_grp)
                pos1 = mc.xform(q=True, ws=True, t=True)
                dist_list = [getDistance(pos1, mc.xform(spline_ctrl, q=True, ws=True, t=True)) for spline_ctrl in spline_ctrls]
                temp = sorted(dist_list)
                min_dist1 = temp[0]
                min_dist2 = temp[1]
                index1 = dist_list.index(min_dist1)
                index2 = dist_list.index(min_dist2)

                con = mc.scaleConstraint(spline_ctrls[index1], spline_ctrls[index2], spline_scaler)[0]
                mc.setAttr('{0}.{1}W0'.format(con, spline_ctrls[index1]), min_dist2 / (min_dist1 + min_dist2))
                mc.setAttr('{0}.{1}W1'.format(con, spline_ctrls[index2]), min_dist2 / (min_dist1 + min_dist2))
                mc.connectAttr(spline_scaler + '.s', deform_joints[i] + '.s')

        # Advanced Switch
        for deform in deforms:
            function = deform.getFunction()
            ik_ctrl = deform.getIKCtrl()
            if not function == 'IK':
                continue
            if not mc.objExists(ik_ctrl):
                continue
            side = deform.getSide()
            ik_name = deform.getName()
            deform_joint = deform.getDeformJoint()
            ik_start_joint = side + '_' + deform.getIKStartJoint() + '_IK_Jnt'
            ik_middle_joint = side + '_' + deform.getIKMiddleJoint() + '_IK_Jnt'
            switch_ctrl = deform.getSwitchCtrl()
            switch_pivot = deform.getSwitchPivot()
            self.createController('Switch', 'SwitchShape', ik_name + '_Switch', side, scale, loc=None)

            block_joint = deform.getJoint()
            switch_grp = side + '_' + block_joint + '_Switch_Grp'
            mc.createNode('transform', n=switch_grp)
            mc.parent(switch_grp, 'Switch_System')

            deform_parent_joint = deform.getDeformParentJoint()
            if mc.objExists(deform_parent_joint):
                mc.parentConstraint(deform_parent_joint, switch_grp)
            else:
                mc.parentConstraint(deform_joint, switch_grp)
            mc.parent(switch_ctrl, deform_joint)
            mc.setAttr(switch_ctrl + '.t', 0, 0, 0)
            mc.setAttr(switch_ctrl + '.r', 0, 0, 0)

            if mc.objExists(switch_pivot):
                if mc.objExists('temp_switch_pivot'):
                    mc.delete('temp_switch_pivot')
                mc.createNode('transform', n='temp_switch_pivot')
                mc.matchTransform('temp_switch_pivot', switch_pivot)
                if deform.getIsMirror():
                    mc.setAttr('temp_switch_pivot.tx', -mc.getAttr('temp_switch_pivot.tx'))
                mc.matchTransform(switch_ctrl, 'temp_switch_pivot', position=True)
                mc.delete('temp_switch_pivot')
                rot = mc.xform(switch_ctrl, q=True, ws=True, ro=True)
                rot = [90, 0, rot[2]]
                mc.xform(switch_ctrl, ws=True, ro=rot)
            else:
                length = mc.getAttr(ik_middle_joint + '.tx')
                mc.setAttr(switch_ctrl + '.tx', length / 2.0)

                rot = mc.xform(switch_ctrl, q=True, ws=True, ro=True)
                rot = [90, 0, rot[2]]
                mc.xform(switch_ctrl, ws=True, ro=rot)
                if deform.getIsMirror():
                    mc.move(0, 0, length / 2.0, switch_ctrl, os=True, r=True)
                else:
                    mc.move(0, 0, -length / 2.0, switch_ctrl, os=True, r=True)
            mc.parent(switch_ctrl, w=True)
            mc.makeIdentity(switch_ctrl, apply=True, r=True)
            mc.parent(switch_ctrl, switch_grp)

            lockAttrs(switch_ctrl, 1, 1, 1, 1)
            mc.addAttr(switch_ctrl, k=True, ln='blend', at='double', min=0, max=10, dv=0)
            mc.addAttr(switch_ctrl, ln='startJoint', dt='string')
            mc.setAttr(switch_ctrl + '.startJoint', deform.getIKStartJoint(), l=True, type='string')
            mc.addAttr(switch_ctrl, ln='middleJoint', dt='string')
            mc.setAttr(switch_ctrl + '.middleJoint', deform.getIKMiddleJoint(), l=True, type='string')
            mc.addAttr(switch_ctrl, ln='endJoint', dt='string')
            mc.setAttr(switch_ctrl + '.endJoint', deform.getIKEndJoint(), l=True, type='string')

            switchBlend_unit = side + '_' + ik_name + '_SwitchBlend_Unit'
            mc.createNode('unitConversion', n=switchBlend_unit)
            mc.setAttr(switchBlend_unit + '.conversionFactor', 0.1)
            mc.connectAttr(switch_ctrl + '.blend', switchBlend_unit + '.input', f=True)
            switchBlend_reverse = side + '_' + ik_name + '_SwitchBlend_Reverse'
            mc.createNode('reverse', n=switchBlend_reverse)
            mc.connectAttr(switchBlend_unit + '.output', switchBlend_reverse + '.inputX')

            ik_grp = ik_ctrl.replace('_Ctrl', '_Grp')
            ik_pos = ik_ctrl.replace('_Ctrl', '_Pos')
            fk_ctrl = deform.getFKCtrl()
            fk_pos = fk_ctrl.replace('_Ctrl', '_Pos')
            pole_ann = ik_ctrl.replace('_IK_Ctrl', '_Pole_Annotation')

            # vis
            fkVis_cond = side + '_' + ik_name + '_FKVis_cond'
            mc.createNode('condition', n=fkVis_cond)
            mc.connectAttr(switchBlend_unit + '.output', fkVis_cond + '.firstTerm')
            mc.setAttr(fkVis_cond + '.secondTerm', 1)
            mc.setAttr(fkVis_cond + '.colorIfTrueR', 1)
            mc.setAttr(fkVis_cond + '.colorIfFalseR', 0)
            mc.setAttr(fkVis_cond + '.operation', 4)
            mc.connectAttr(fkVis_cond + '.outColorR', fk_pos + '.v', f=True)

            ikVis_cond = side + '_' + ik_name + '_IKVis_cond'
            mc.createNode('condition', n=ikVis_cond)
            mc.connectAttr(switchBlend_unit + '.output', ikVis_cond + '.firstTerm')
            mc.setAttr(ikVis_cond + '.secondTerm', 0)
            mc.setAttr(ikVis_cond + '.colorIfTrueR', 1)
            mc.setAttr(ikVis_cond + '.colorIfFalseR', 0)
            mc.setAttr(ikVis_cond + '.operation', 2)
            mc.connectAttr(ikVis_cond + '.outColorR', ik_pos + '.v', f=True)
            mc.connectAttr(ikVis_cond + '.outColorR', ik_grp + '.v', f=True)
            mc.connectAttr(ikVis_cond + '.outColorR', pole_ann + '.v', f=True)

        for deform in deforms:
            deform_joint = deform.getDeformJoint()
            point_con = deform_joint + '_pointConstraint1'
            orient_con = deform_joint + '_orientConstraint1'
            fk_joint = deform.getFKJoint()
            ik_joint = deform.getIKJoint()
            side = deform.getSide()
            block_joint = deform.getJoint()
            if not mc.objExists(fk_joint) or not mc.objExists(ik_joint):
                continue
            switch_ctrl = deform.getSwitchCtrl()
            switchBlend_unit = switch_ctrl.replace('_Switch_Ctrl', '_SwitchBlend_Unit')
            switchBlend_reverse = switch_ctrl.replace('_Switch_Ctrl', '_SwitchBlend_Reverse')
            mc.connectAttr(switchBlend_reverse + '.outputX', '{0}.{1}W0'.format(point_con, fk_joint))
            mc.connectAttr(switchBlend_reverse + '.outputX', '{0}.{1}W0'.format(orient_con, fk_joint))
            mc.connectAttr(switchBlend_unit + '.output', '{0}.{1}W1'.format(point_con, ik_joint))
            mc.connectAttr(switchBlend_unit + '.output', '{0}.{1}W1'.format(orient_con, ik_joint))

            # 需要创建FKIKGrp， 和deform_child_joint一致，直接使用deform_child_joint会出现循环
            fkik_loc = fk_joint.replace('_FK_Jnt', '_FKIK_Loc')
            mc.createNode('transform', n=fkik_loc)
            mc.parent(fkik_loc, 'Switch_System')
            align(fkik_loc, deform_joint, 1, 1, 0, 1)
            self.constraintFKIK(mc.parentConstraint, switch_ctrl, fk_joint, ik_joint, fkik_loc)

        # Advance Foot
        for deform in deforms:
            function = deform.getFunction()
            if not function == 'Foot':
                continue
            toe_block = deform.getIKToeBlock()
            toeEnd_block = deform.getIKToeEndBlock()
            if not toe_block or not toeEnd_block:
                continue
            heel_pivot = deform.getHeelPivot()
            footInner_pivot = deform.getFootInnerPivot()
            footOuter_pivot = deform.getFootOuterPivot()
            if not heel_pivot:
                continue
            side = deform.getSide()
            ik_name = deform.getIKStartBlock().getName()
            ik_ctrl = side + '_' + ik_name + '_IK_Ctrl'

            ik_handle = ik_ctrl.replace('_Ctrl', '_Handle')
            fat = deform.getIKToeBlock().getFat()
            heel_ctrl = side + '_' + ik_name + '_Heel_Ctrl'
            ik_start_joint = side + '_' + deform.getIKStartJoint() + '_IK_Jnt'
            ik_middle_joint = side + '_' + deform.getIKMiddleJoint() + '_IK_Jnt'
            ik_end_joint = side + '_' + deform.getIKEndJoint() + '_IK_Jnt'
            ik_toe_joint = side + '_' + deform.getIKToeJoint() + '_IK_Jnt'
            ik_toeEnd_joint = side + '_' + deform.getIKToeEndJoint() + '_IK_Jnt'
            toe_handle = side + '_' + ik_name + '_Toe_Handle'
            toeEnd_handle = side + '_' + ik_name + '_ToeEnd_Handle'
            toe_effector = side + '_' + ik_name + '_Toe_Effector'
            toeEnd_effector = side + '_' + ik_name + '_ToeEnd_Effector'
            temp = mc.ikHandle(n=toeEnd_handle, solver='ikSCsolver', sj=ik_toe_joint, ee=ik_toeEnd_joint)[1]
            mc.rename(temp, toeEnd_effector)
            mc.setAttr(toeEnd_handle + '.v', 0, lock=True)
            mc.setAttr(toeEnd_effector + '.v', 0, lock=True)
            temp = mc.ikHandle(n=toe_handle, solver='ikSCsolver', sj=ik_end_joint, ee=ik_toe_joint)[1]
            mc.rename(temp, toe_effector)
            mc.setAttr(toe_handle + '.v', 0, lock=True)
            mc.setAttr(toe_effector + '.v', 0, lock=True)

            if mc.objExists(heel_pivot):
                if mc.objExists('temp_heel_pivot'):
                    mc.delete('temp_heel_pivot')
                mc.createNode('transform', n='temp_heel_pivot')
                mc.matchTransform('temp_heel_pivot', heel_pivot)
                if deform.getIsMirror():
                    mc.setAttr('temp_heel_pivot.tx', -mc.getAttr('temp_heel_pivot.tx'))
            if objsExists([footInner_pivot, footOuter_pivot]):
                if mc.objExists('temp_footInner_pivot'):
                    mc.delete('temp_footInner_pivot')
                mc.createNode('transform', n='temp_footInner_pivot')
                mc.matchTransform('temp_footInner_pivot', footInner_pivot)
                if deform.getIsMirror():
                    mc.setAttr('temp_footInner_pivot.tx', -mc.getAttr('temp_footInner_pivot.tx'))
                if mc.objExists('temp_footOuter_pivot'):
                    mc.delete('temp_footOuter_pivot')
                mc.createNode('transform', n='temp_footOuter_pivot')
                mc.matchTransform('temp_footOuter_pivot', footOuter_pivot)
                if deform.getIsMirror():
                    mc.setAttr('temp_footOuter_pivot.tx', -mc.getAttr('temp_footOuter_pivot.tx'))

            pos1 = mc.xform(ik_end_joint, q=True, ws=True, t=True)
            pos2 = mc.xform(ik_toe_joint, q=True, ws=True, t=True)
            if mc.objExists('temp_pivot'):
                mc.delete('temp_pivot')
            mc.createNode('transform', n='temp_pivot')
            mc.xform('temp_pivot', t=[pos1[0], pos2[1], pos1[2]], ws=True)
            mc.aimConstraint(ik_toe_joint, 'temp_pivot', aimVector=(0, 0, 1), upVector=(0, 1, 0), worldUpType='scene')
            ikToe_ctrl = self.createController('Toe', 'ToeShape', ik_name + '_IKToe', side, scale * fat,
                                               loc=ik_toe_joint)
            rollToe_ctrl = self.createController('Roll', 'RollShape1', ik_name + '_RollToe', side, scale * fat,
                                                 loc='temp_pivot')
            rollToeEnd_ctrl = self.createController('Roll', 'PivotShape', ik_name + '_RollToeEnd', side, scale * fat,
                                                    loc='temp_pivot')
            heel_ctrl = self.createController('Roll', 'PivotShape', ik_name + '_Heel', side, scale * fat,
                                              loc='temp_pivot')

            ikToe_pos = ikToe_ctrl.replace('_Ctrl', '_Pos')
            rollToe_pos = rollToe_ctrl.replace('_Ctrl', '_Pos')
            rollToeEnd_pos = rollToeEnd_ctrl.replace('_Ctrl', '_Pos')
            heel_pos = heel_ctrl.replace('_Ctrl', '_Pos')
            rollToe_connect = rollToe_ctrl.replace('_Ctrl', '_Connect')
            rollToeEnd_connect = rollToeEnd_ctrl.replace('_Ctrl', '_Connect')
            heel_connect = heel_ctrl.replace('_Ctrl', '_Connect')
            mc.setAttr(rollToeEnd_pos + '.ry', mc.getAttr('temp_pivot.ry'))
            mc.setAttr(rollToe_pos + '.ry', mc.getAttr('temp_pivot.ry'))
            mc.setAttr(heel_pos + '.ry', mc.getAttr('temp_pivot.ry'))
            mc.matchTransform(rollToe_pos, ik_toe_joint, position=True)
            mc.matchTransform(rollToeEnd_pos, ik_toeEnd_joint, position=True)
            mc.matchTransform(heel_pos, 'temp_heel_pivot', position=True)
            mc.delete('temp_heel_pivot')

            mc.parent(toe_handle, rollToe_ctrl)
            mc.parent(toeEnd_handle, ikToe_ctrl)
            mc.parent(ik_handle, rollToe_ctrl)
            mc.addAttr(ik_ctrl, ln='heelSlide', k=True, at='double', dv=0)
            mc.connectAttr(ik_ctrl + '.heelSlide', heel_connect + '.ry', f=True)
            mc.addAttr(ik_ctrl, ln='toeEndSlide', k=True, at='double', dv=0)
            mc.connectAttr(ik_ctrl + '.toeEndSlide', rollToeEnd_connect + '.ry', f=True)

            mc.addAttr(ik_ctrl, ln='roll', at='double', k=True)
            mc.addAttr(ik_ctrl, ln='rollStartAngle', at='double', dv=30, k=True)
            mc.addAttr(ik_ctrl, ln='rollEndAngle', at='double', dv=60, k=True)
            # 脚跟上挑
            roll_clamp = side + '_' + ik_name + '_ToeRoll_clamp'
            mc.createNode('clamp', n=roll_clamp)
            mc.connectAttr(ik_ctrl + '.roll', roll_clamp + '.input.inputR', f=True)
            mc.connectAttr(ik_ctrl + '.roll', roll_clamp + '.min.minR', f=True)
            mc.connectAttr(roll_clamp + '.outputR', heel_connect + '.rx', f=True)

            # 垫脚掌
            range1 = side + '_' + ik_name + '_RollToe_setRange1'
            mc.createNode('setRange', n=range1)
            mc.connectAttr(ik_ctrl + '.roll', range1 + '.valueX')
            mc.setAttr(range1 + '.maxX', 1)
            mc.connectAttr(ik_ctrl + '.rollStartAngle', range1 + '.oldMaxX')

            minus = side + '_' + ik_name + '_RollToe_Minus'
            mc.createNode('plusMinusAverage', n=minus)
            mc.setAttr(minus + '.operation', 2)
            mc.setAttr(minus + '.input1D[0]', 1)

            range2 = side + '_' + ik_name + '_RollToe_setRange2'
            mc.createNode('setRange', n=range2)
            mc.connectAttr(ik_ctrl + '.roll', range2 + '.valueX')
            mc.setAttr(range2 + '.maxX', 1)
            mc.connectAttr(ik_ctrl + '.rollStartAngle', range2 + '.oldMinX')
            mc.connectAttr(ik_ctrl + '.rollEndAngle', range2 + '.oldMaxX')
            mc.connectAttr(range2 + '.outValueX', minus + '.input1D[1]')

            rollToe_cond_mult = side + '_' + ik_name + '_RollToeCond_mult'
            mc.createNode('multiplyDivide', n=rollToe_cond_mult)
            mc.connectAttr(minus + '.output1D', rollToe_cond_mult + '.input1X')
            mc.connectAttr(range1 + '.outValueX', rollToe_cond_mult + '.input2X')

            rollToe_output_mult = side + '_' + ik_name + '_RollToeOutput_mult'
            mc.createNode('multiplyDivide', n=rollToe_output_mult)
            mc.connectAttr(rollToe_cond_mult + '.outputX', rollToe_output_mult + '.input1X')
            mc.connectAttr(ik_ctrl + '.roll', rollToe_output_mult + '.input2X')

            mc.connectAttr(rollToe_output_mult + '.outputX', rollToe_connect + '.rx')

            # 踮脚尖
            rollToeEnd_range = side + '_' + ik_name + '_RollToeEnd_setRange'
            mc.createNode('setRange', n=rollToeEnd_range)
            mc.connectAttr(ik_ctrl + '.roll', rollToeEnd_range + '.valueX')
            mc.setAttr(rollToeEnd_range + '.maxX', 1)
            mc.connectAttr(ik_ctrl + '.rollStartAngle', rollToeEnd_range + '.oldMinX')
            mc.connectAttr(ik_ctrl + '.rollEndAngle', rollToeEnd_range + '.oldMaxX')
            rollToeEnd_output_mult = side + '_' + ik_name + '_RollToeEndOutput_mult'
            mc.createNode('multiplyDivide', n=rollToeEnd_output_mult)
            mc.connectAttr(rollToeEnd_range + '.outValueX', rollToeEnd_output_mult + '.input1X')
            mc.connectAttr(ik_ctrl + '.roll', rollToeEnd_output_mult + '.input2X')
            mc.connectAttr(rollToeEnd_output_mult + '.outputX', rollToeEnd_connect + '.rx')

            if deform.getIsMirror():
                unit = mc.listConnections(heel_connect + '.ry')[0]
                mc.setAttr(unit + '.conversionFactor', -mc.getAttr(unit + '.conversionFactor'))
                unit = mc.listConnections(rollToeEnd_connect + '.ry')[0]
                mc.setAttr(unit + '.conversionFactor', -mc.getAttr(unit + '.conversionFactor'))

            if footOuter_pivot and footInner_pivot:
                mc.addAttr(ik_ctrl, ln='rock', k=True, at='double', dv=0)
                footInner_ctrl = self.createController('Roll', 'PivotShape', ik_name + '_RollFootInner', side,
                                                       scale * fat, loc=ik_toe_joint)
                footOuter_ctrl = self.createController('Roll', 'PivotShape', ik_name + '_RollFootOuter', side,
                                                       scale * fat, loc=ik_toe_joint)
                footInner_pos = footInner_ctrl.replace('_Ctrl', '_Pos')
                footOuter_pos = footOuter_ctrl.replace('_Ctrl', '_Pos')
                mc.setAttr(footInner_pos + '.ry', mc.getAttr('temp_pivot.ry'))
                mc.setAttr(footOuter_pos + '.ry', mc.getAttr('temp_pivot.ry'))
                mc.matchTransform(footInner_pos, 'temp_footInner_pivot', position=True)
                mc.matchTransform(footOuter_pos, 'temp_footOuter_pivot', position=True)

                mc.parent(rollToe_pos, rollToeEnd_ctrl)
                mc.parent(ikToe_pos, rollToeEnd_ctrl)
                mc.parent(rollToeEnd_pos, footInner_ctrl)
                mc.parent(footInner_pos, footOuter_ctrl)
                mc.parent(footOuter_pos, heel_ctrl)
                mc.parent(heel_pos, ik_ctrl)

                footInner_connect = footInner_ctrl.replace('_Ctrl', '_Connect')
                footOuter_connect = footOuter_ctrl.replace('_Ctrl', '_Connect')

                mc.connectAttr(ik_ctrl + '.rock', footInner_connect + '.rz', f=True)
                mc.connectAttr(ik_ctrl + '.rock', footOuter_connect + '.rz', f=True)
                if deform.getIsMirror():
                    mc.transformLimits(footOuter_connect, rotationZ=[0, 45], enableRotationZ=[True, False])
                    mc.transformLimits(footInner_connect, rotationZ=[-45, 0], enableRotationZ=[False, True])
                    unit = mc.listConnections(footInner_connect + '.rz')[0]
                    mc.setAttr(unit + '.conversionFactor', -mc.getAttr(unit + '.conversionFactor'))
                    unit = mc.listConnections(footOuter_connect + '.rz')[0]
                    mc.setAttr(unit + '.conversionFactor', -mc.getAttr(unit + '.conversionFactor'))
                else:
                    mc.transformLimits(footInner_connect, rotationZ=[0, 45], enableRotationZ=[True, False])
                    mc.transformLimits(footOuter_connect, rotationZ=[-45, 0], enableRotationZ=[False, True])
            else:
                mc.parent(rollToe_pos, rollToeEnd_ctrl)
                mc.parent(ikToe_pos, rollToeEnd_ctrl)
                mc.parent(rollToeEnd_pos, heel_ctrl)
                mc.parent(heel_pos, ik_ctrl)

            mc.delete('temp_pivot')
            mc.delete('temp_footInner_pivot')
            mc.delete('temp_footOuter_pivot')

        # Advanced Scale
        for deform in deforms:
            side = deform.getSide()
            block_joint = deform.getJoint()
            deform_joint = deform.getDeformJoint()
            ik_joint = deform.getIKJoint()
            fk_joint = deform.getFKJoint()
            fk_ctrl = deform.getFKCtrl()
            switch_ctrl = deform.getSwitchCtrl()
            ik_ctrl = deform.getIKCtrl()
            if objsExists([switch_ctrl, fk_ctrl, ik_ctrl]):
                scale_blend = side + '_' + block_joint + '_Scale_Blend'
                mc.createNode('blendColors', n=scale_blend)
                mc.setAttr(scale_blend + '.color1G', 1)
                mc.setAttr(scale_blend + '.color1B', 1)
                switchBlend_unit = switch_ctrl.replace('_Switch_Ctrl', '_SwitchBlend_Unit')
                mc.connectAttr(switchBlend_unit + '.output', scale_blend + '.blender')
                mc.connectAttr(fk_ctrl + '.s', scale_blend + '.color2')
                mc.connectAttr(scale_blend + '.output', deform_joint + '.s')
                if block_joint == deform.getIKEndJoint():
                    mc.connectAttr(ik_ctrl + '.s', scale_blend + '.color1')

            elif mc.objExists(fk_ctrl):
                mc.connectAttr(fk_ctrl + '.s', deform_joint + '.s')

        # Advanced Stretchy
        for deform in deforms:
            function = deform.getFunction()
            if not function == 'IK':
                continue
            side = deform.getSide()
            ik_name = deform.getName()
            ik_ctrl = deform.getIKCtrl()
            pole_ctrl = deform.getPoleCtrl()
            ik_start_ctrl = ik_ctrl.replace('_IK_Ctrl', '_IKStart_Ctrl')
            ik_start_joint = side + '_' + deform.getIKStartJoint() + '_IK_Jnt'
            ik_middle_joint = side + '_' + deform.getIKMiddleJoint() + '_IK_Jnt'
            ik_end_joint = side + '_' + deform.getIKEndJoint() + '_IK_Jnt'
            start_joint = deform.getIKStartBlock().getJoint()
            middle_joint = deform.getIKMiddleBlock().getJoint()
            end_joint = deform.getIKEndBlock().getJoint()

            pos1 = mc.xform(ik_middle_joint, q=True, ws=True, t=True)
            pos2 = mc.xform(ik_end_joint, q=True, ws=True, t=True)
            dist1 = getDistance(pos1, pos2)
            pos3 = mc.xform(ik_start_joint, q=True, ws=True, t=True)
            dist2 = getDistance(pos1, pos3)
            ik_length = dist1 + dist2

            mc.addAttr(ik_ctrl, ln='stretchy', at='double', min=0, max=10, dv=0, k=True)

            ik_stretchy_range = side + '_' + ik_name + '_Stretchy_Range'
            mc.createNode('setRange', n=ik_stretchy_range)
            mc.setAttr(ik_stretchy_range + '.maxX', 1)
            mc.setAttr(ik_stretchy_range + '.oldMaxX', 1)
            mc.connectAttr(ik_ctrl + '.stretchy', ik_stretchy_range + '.valueX')

            ik_start_to_end_dist = side + '_' + start_joint + '_To_' + end_joint + '_Distance'
            ik_start_to_end_distShape = side + '_' + start_joint + '_To_' + end_joint + '_DistanceShape'
            mc.createNode('distanceDimShape', n=ik_start_to_end_distShape)
            temp = mc.listRelatives(ik_start_to_end_distShape, p=True)[0]
            mc.rename(temp, ik_start_to_end_dist)
            mc.setAttr(ik_start_to_end_dist + '.v', 0)
            mc.parent(ik_start_to_end_dist, 'IK_Message')
            ik_start_loc = side + '_' + ik_name + '_Start_Loc'
            ik_end_loc = side + '_' + ik_name + '_End_Loc'
            mc.spaceLocator(n=ik_start_loc)
            mc.spaceLocator(n=ik_end_loc)
            mc.parent(ik_start_loc, 'IK_Message')
            mc.parent(ik_end_loc, 'IK_Message')
            mc.setAttr(ik_start_loc + '.v', False)
            mc.setAttr(ik_end_loc + '.v', False)
            mc.pointConstraint(ik_start_ctrl, ik_start_loc)
            mc.pointConstraint(ik_ctrl, ik_end_loc)
            mc.connectAttr(ik_start_loc + '.t', ik_start_to_end_distShape + '.startPoint')
            mc.connectAttr(ik_end_loc + '.t', ik_start_to_end_distShape + '.endPoint')
            # stretchy 10 -> 1
            ik_stretchy_unit = side + '_' + ik_name + '_Stretchy_Unit'
            mc.createNode('unitConversion', n=ik_stretchy_unit)
            mc.setAttr(ik_stretchy_unit + '.conversionFactor', 0.1)
            mc.connectAttr(ik_ctrl + '.stretchy', ik_stretchy_unit + '.input')
            # 将最小长度设置为ik_length
            ik_stretchy_cond = side + '_' + ik_name + '_Stretchy_Cond'
            mc.createNode('condition', n=ik_stretchy_cond)
            mc.setAttr(ik_stretchy_cond + '.operation', 3)
            mc.connectAttr(ik_start_to_end_distShape + '.distance', ik_stretchy_cond + '.firstTerm')
            mc.connectAttr(ik_start_to_end_distShape + '.distance', ik_stretchy_cond + '.colorIfTrue.colorIfTrueR')
            mc.setAttr(ik_stretchy_cond + '.colorIfFalse.colorIfFalseR', ik_length)
            mc.setAttr(ik_stretchy_cond + '.secondTerm', ik_length)
            # 混合原始长度
            ik_stretchy_blend = side + '_' + ik_name + '_Stretchy_Blend'
            mc.createNode('blendTwoAttr', n=ik_stretchy_blend)
            mc.setAttr(ik_stretchy_blend + '.input[0]', ik_length)
            mc.connectAttr(ik_stretchy_cond + '.outColor.outColorR', ik_stretchy_blend + '.input[1]')
            mc.connectAttr(ik_stretchy_unit + '.output', ik_stretchy_blend + '.attributesBlender')
            # 获取拉伸比例
            ik_strechy_ratio_div = side + '_' + ik_name + '_Stretchy_Ratio_Div'
            mc.createNode('multiplyDivide', n=ik_strechy_ratio_div)
            mc.setAttr(ik_strechy_ratio_div + '.operation', 2)
            mc.setAttr(ik_strechy_ratio_div + '.input2X', ik_length)
            mc.connectAttr(ik_stretchy_blend + '.output', ik_strechy_ratio_div + '.input1X')

            # length1 * 原始长度 * 拉伸比例
            mc.addAttr(ik_ctrl, ln='length1', at='double', dv=1, min=0, k=True)
            ik_start_to_middle_stretchy_mult = side + '_' + start_joint + '_to_' + middle_joint + '_Stretchy_Mult'
            mc.createNode('multiplyDivide', n=ik_start_to_middle_stretchy_mult)
            mc.setAttr(ik_start_to_middle_stretchy_mult + '.operation', 1)
            mc.connectAttr(ik_ctrl + '.length1', ik_start_to_middle_stretchy_mult + '.input1X')
            mc.setAttr(ik_start_to_middle_stretchy_mult + '.input2X', mc.getAttr(ik_middle_joint + '.tx'))

            ik_start_to_middle_length_mult = side + '_' + start_joint + '_To_' + middle_joint + '_Length_Mult'
            mc.createNode('multiplyDivide', n=ik_start_to_middle_length_mult)
            mc.connectAttr(ik_strechy_ratio_div + '.outputX', ik_start_to_middle_length_mult + '.input1X')
            mc.connectAttr(ik_start_to_middle_stretchy_mult + '.outputX', ik_start_to_middle_length_mult + '.input2X')
            # length2 * 原始长度 * 拉伸比例
            mc.addAttr(ik_ctrl, ln='length2', at='double', dv=1, min=0, k=True)
            ik_middle_to_end_stretchy_mult = side + '_' + middle_joint + '_to_' + end_joint + '_Stretchy_Mult'
            mc.createNode('multiplyDivide', n=ik_middle_to_end_stretchy_mult)
            mc.setAttr(ik_middle_to_end_stretchy_mult + '.operation', 1)
            mc.connectAttr(ik_ctrl + '.length2', ik_middle_to_end_stretchy_mult + '.input1X')
            mc.setAttr(ik_middle_to_end_stretchy_mult + '.input2X', mc.getAttr(ik_end_joint + '.tx'))

            ik_middle_to_end_length_mult = side + '_' + middle_joint + '_To_' + end_joint + '_Length_Mult'
            mc.createNode('multiplyDivide', n=ik_middle_to_end_length_mult)
            mc.connectAttr(ik_strechy_ratio_div + '.outputX', ik_middle_to_end_length_mult + '.input1X')
            mc.connectAttr(ik_middle_to_end_stretchy_mult + '.outputX', ik_middle_to_end_length_mult + '.input2X')
            # fatness1
            mc.addAttr(ik_ctrl, ln='fatness1', at='double', dv=1, min=0, k=True)
            ik_start_to_middle_fatness_mult = side + '_' + start_joint + '_To_' + middle_joint + '_Fatness_Mult'
            mc.createNode('multiplyDivide', n=ik_start_to_middle_fatness_mult)
            mc.connectAttr(ik_ctrl + '.fatness1', ik_start_to_middle_fatness_mult + '.input1X')
            # fatness2
            mc.addAttr(ik_ctrl, ln='fatness2', at='double', dv=1, min=0, k=True)
            ik_middle_to_end_fatness_mult = side + '_' + middle_joint + '_To_' + end_joint + '_Fatness_Mult'
            mc.createNode('multiplyDivide', n=ik_middle_to_end_fatness_mult)
            mc.connectAttr(ik_ctrl + '.fatness2', ik_middle_to_end_fatness_mult + '.input1X')

            # pole lock 10 -> 1
            mc.addAttr(pole_ctrl, ln='lock', at='double', min=0, max=10, k=True)
            pole_lock_unit = side + '_' + ik_name + '_PoleLock_unit'
            mc.createNode('unitConversion', n=pole_lock_unit)
            mc.setAttr(pole_lock_unit + '.conversionFactor', 0.1)
            mc.connectAttr(pole_ctrl + '.lock', pole_lock_unit + '.input')

            # 用lock属性混合length1 * 原始长度 * 拉伸比例和start到pole_ctrl的距离
            pole_loc = side + '_' + ik_name + '_Pole_loc'
            mc.spaceLocator(n=pole_loc)
            mc.parent(pole_loc, 'IK_Message')
            mc.setAttr(pole_loc + '.v', False)
            mc.pointConstraint(pole_ctrl, pole_loc)

            pole_start_to_middle_lock_blend = side + '_' + start_joint + '_To_' + middle_joint + '_Lock_Blend'
            mc.createNode('blendTwoAttr', n=pole_start_to_middle_lock_blend)
            mc.connectAttr(pole_lock_unit + '.output', pole_start_to_middle_lock_blend + '.attributesBlender')
            # start到pole_ctrl的距离
            ik_start_to_pole_dist = side + '_' + start_joint + '_To_Pole_Distance'
            ik_start_to_pole_distShape = side + '_' + start_joint + '_To_Pole_DistanceShape'
            mc.createNode('distanceDimShape', n=ik_start_to_pole_distShape)
            temp = mc.listRelatives(ik_start_to_pole_distShape, p=True)[0]
            mc.rename(temp, ik_start_to_pole_dist)
            mc.setAttr(ik_start_to_pole_dist + '.v', False)
            mc.parent(ik_start_to_pole_dist, 'IK_Message')
            mc.connectAttr(ik_start_loc + '.t', ik_start_to_pole_distShape + '.startPoint')
            mc.connectAttr(pole_loc + '.t', ik_start_to_pole_distShape + '.endPoint')
            # mainscale
            pole_start_to_middle_allScale_mult = side + '_' + start_joint + '_To_' + middle_joint + '_AllScale_Mult'
            mc.createNode('multiplyDivide', n=pole_start_to_middle_allScale_mult)
            mc.setAttr(pole_start_to_middle_allScale_mult + '.operation', 2)
            # mc.connectAttr(ik_start_to_pole_distShape + '.distance', pole_start_to_middle_allScale_mult + '.input1X')
            # start到pole_ctrl的距离是正数，L为正，R为负
            ik_start_to_pole_dist_unit = side + '_' + start_joint + '_To_Pole_Distance_Unit'
            mc.createNode('unitConversion', n=ik_start_to_pole_dist_unit)
            if side == 'R':
                mc.setAttr(ik_start_to_pole_dist_unit + '.conversionFactor', -1.0)
            else:
                mc.setAttr(ik_start_to_pole_dist_unit + '.conversionFactor', 1.0)
            # mc.connectAttr(pole_start_to_middle_allScale_mult + '.outputX', ik_start_to_pole_dist_unit + '.input')
            mc.connectAttr(ik_start_to_pole_distShape + '.distance', ik_start_to_pole_dist_unit + '.input')
            mc.connectAttr(ik_start_to_middle_length_mult + '.outputX', pole_start_to_middle_lock_blend + '.input[0]')
            mc.connectAttr(ik_start_to_pole_dist_unit + '.output', pole_start_to_middle_lock_blend + '.input[1]')
            # 连到IK骨骼
            mc.connectAttr(pole_start_to_middle_lock_blend + '.output', ik_middle_joint + '.tx')

            # 用lock属性混合length1 * 原始长度 * 拉伸比例和start到pole_ctrl的距离
            pole_middle_to_end_lock_blend = side + '_' + middle_joint + '_To_' + end_joint + '_Lock_Blend'
            mc.createNode('blendTwoAttr', n=pole_middle_to_end_lock_blend)
            mc.connectAttr(pole_lock_unit + '.output', pole_middle_to_end_lock_blend + '.attributesBlender')
            # pole_ctrl到end的距离
            ik_pole_to_end_dist = side + '_Pole_To_' + end_joint + '_Distance'
            ik_pole_to_end_distShape = side + '_Pole_To_' + end_joint + '_DistanceShape'
            mc.createNode('distanceDimShape', n=ik_pole_to_end_distShape)
            temp = mc.listRelatives(ik_pole_to_end_distShape, p=True)[0]
            mc.rename(temp, ik_pole_to_end_dist)
            mc.setAttr(ik_pole_to_end_dist + '.v', False)
            mc.parent(ik_pole_to_end_dist, 'IK_Message')
            mc.connectAttr(pole_loc + '.t', ik_pole_to_end_distShape + '.startPoint')
            mc.connectAttr(ik_end_loc + '.t', ik_pole_to_end_distShape + '.endPoint')
            # mainscale
            pole_middle_to_end_allScale_mult = side + '_' + middle_joint + '_To_' + end_joint + '_AllScale_Mult'
            mc.createNode('multiplyDivide', n=pole_middle_to_end_allScale_mult)
            mc.setAttr(pole_middle_to_end_allScale_mult + '.operation', 2)
            mc.connectAttr(ik_pole_to_end_distShape + '.distance', pole_middle_to_end_allScale_mult + '.input1X')
            # mc.connectAttr(main_allScale_mult + '.outputX', pole_middle_to_end_allScale_mult + '.input2X')
            # start到pole_ctrl的距离是正数，L为正，R为负
            ik_pole_to_end_dist_unit = side + '_Pole_To_' + end_joint + '_Distance_Unit'
            mc.createNode('unitConversion', n=ik_pole_to_end_dist_unit)
            if side == 'R':
                mc.setAttr(ik_pole_to_end_dist_unit + '.conversionFactor', -1.0)
            else:
                mc.setAttr(ik_pole_to_end_dist_unit + '.conversionFactor', 1.0)
            # mc.connectAttr(pole_middle_to_end_allScale_mult + '.outputX', ik_pole_to_end_dist_unit + '.input')
            mc.connectAttr(ik_pole_to_end_distShape + '.distance', ik_pole_to_end_dist_unit + '.input')
            mc.connectAttr(ik_middle_to_end_length_mult + '.outputX', pole_middle_to_end_lock_blend + '.input[0]')
            mc.connectAttr(ik_pole_to_end_dist_unit + '.output', pole_middle_to_end_lock_blend + '.input[1]')
            # 连到IK骨骼
            mc.connectAttr(pole_middle_to_end_lock_blend + '.output', ik_end_joint + '.tx')

        # Advanced Twist(IK)
        for deform in deforms:
            solver = deform.getIKSolver()
            subdivide = deform.getSubdivide()
            if not subdivide:
                continue
            block_joint = deform.getJoint()
            deform_joint = deform.getDeformJoint()
            deform_parent_joint = deform.getDeformParentJoint()
            deform_child_joint = deform.getDeformChildJoint()
            side = deform.getSide()
            if solver != 'IKRPSolver':
                continue

            switch_ctrl = deform.getSwitchCtrl()
            fk_joint = deform.getFKJoint()
            ik_joint = deform.getIKJoint()
            fkik_loc = deform.getFKIKLoc()
            fkik_child_loc = deform.getFKIKChildLoc()

            fat = deform.getFat()
            twist_grp = side + '_' + block_joint + '_Twist_Grp'
            mc.createNode('transform', n=twist_grp)
            mc.parent(twist_grp, 'Twist_Joint')
            align(twist_grp, deform_joint, 1, 1, 0, 1)
            mc.parentConstraint(fkik_loc, twist_grp)
            # self.constraintFKIK(mc.parentConstraint, switch_ctrl, fk_joint, ik_joint, twist_grp)

            mc.select(clear=True)
            twist_start_joint = side + '_' + block_joint + '_TwistStart_Jnt'
            mc.joint(n=twist_start_joint)
            mc.setAttr(twist_start_joint + '.drawStyle', 2)
            twist_end_joint = side + '_' + block_joint + '_TwistEnd_Jnt'
            mc.joint(n=twist_end_joint)
            mc.setAttr(twist_end_joint + '.drawStyle', 2)
            mc.parent(twist_start_joint, twist_grp)
            align(twist_start_joint, deform_joint, 1, 1, 0, 1)
            mc.makeIdentity(twist_start_joint, apply=True, r=True)
            align(twist_end_joint, deform_child_joint, 1, 0, 0, 1)
            twist_joints = []
            for i in range(subdivide + 1):
                mc.select(clear=True)
                mc.select(twist_start_joint)
                twist_joint = side + '_' + block_joint + '_Twist{}_Jnt'.format(i)
                mc.joint(n=twist_joint)
                mc.parent(twist_joint, twist_grp)
                twist_joints.append(twist_joint)
                mc.makeIdentity(twist_joint, apply=True, r=True)
                mc.setAttr(twist_joint + '.drawStyle', 2)
            twist_handle = side + '_' + block_joint + '_Twist_Handle'
            twist_effector = side + '_' + block_joint + '_Twist_Effector'
            temp = mc.ikHandle(n=twist_handle, solver='ikRPsolver', sj=twist_start_joint, ee=twist_end_joint)[1]
            mc.rename(temp, twist_effector)
            mc.pointConstraint(fkik_child_loc, twist_handle)
            # self.constraintFKIK(mc.pointConstraint, switch_ctrl, deform.getFKChildJoint(), deform.getIKChildJoint(),
            #                     twist_handle)

            mc.setAttr(twist_handle + '.r', 0, 0, 0)
            mc.setAttr(twist_handle + '.v', False)
            twist_handle_grp = side + '_' + block_joint + '_TwistHandle_Grp'
            mc.createNode('transform', n=twist_handle_grp)
            mc.parent(twist_handle_grp, 'Twist_Handle')
            deform_parent_joint.replace('_Jnt', '_Twist_Grp')
            if mc.objExists(deform_parent_joint.replace('_Jnt', '_Twist_Grp')):
                mc.parentConstraint(deform_parent_joint.replace('_Jnt', '_Twist_Grp'), twist_handle_grp)
            else:
                mc.parentConstraint(deform_parent_joint, twist_handle_grp)
            mc.parent(twist_handle, twist_handle_grp)

            part_joints = [deform_joint]
            part_joints.extend(deform.getPartJoints())
            for i in range(subdivide + 1):
                twist_radio_mult = side + '_' + block_joint + '_TwistRatio{}_Mult'.format(i)
                mc.createNode('multiplyDivide', n=twist_radio_mult)
                mc.setAttr(twist_radio_mult + '.input2X', 1.0 - (i / (subdivide + 1.0)))
                mc.connectAttr(twist_start_joint + '.rx', twist_radio_mult + '.input1X')
                mc.connectAttr(twist_radio_mult + '.outputX', twist_joints[i] + '.rx')

            if mc.objExists(deform_joint + '_orientConstraint1'):
                mc.delete(deform_joint + '_orientConstraint1')
            # for i in range(subdivide + 1):
            #     mc.orientConstraint(twist_joints[i], part_joints[i])
            mc.orientConstraint(twist_joints[0], part_joints[0])

        # Advanced Reverse Twist(IKEnd)
        for deform in deforms:
            solver = deform.getIKSolver()
            subdivide = deform.getSubdivide()
            function = deform.getFunction()
            block_parent_joint = deform.getParent()
            if subdivide:
                continue
            if function not in ['Hand', 'Foot', 'End']:
                continue
            if solver != 'IKRPSolver':
                continue
            side = deform.getSide()
            parent_subdivide = deform.getParentDivide()
            block_joint = deform.getJoint()
            deform_joint = deform.getDeformJoint()
            deform_parent_joint = deform.getDeformParentJoint()
            switch_ctrl = deform.getSwitchCtrl()
            fk_joint = deform.getFKJoint()
            ik_joint = deform.getIKJoint()
            fk_parent_joint = deform.getFKParentJoint()
            ik_parent_joint = deform.getIKParentJoint()
            fkik_parent_loc = deform.getFKIKParentLoc()
            fkik_loc = deform.getFKIKLoc()

            twist_grp = side + '_' + block_joint + '_Twist_Grp'
            mc.createNode('transform', n=twist_grp)
            mc.parent(twist_grp, 'Twist_Joint')
            align(twist_grp, deform_joint, 1, 1, 0, 1)
            # self.constraintFKIK(mc.parentConstraint, switch_ctrl, fk_parent_joint, ik_parent_joint, twist_grp)
            mc.parentConstraint(fkik_parent_loc, twist_grp)

            mc.select(clear=True)
            twist_start_joint = side + '_' + block_joint + '_TwistStart_Jnt'
            mc.joint(n=twist_start_joint)
            mc.setAttr(twist_start_joint + '.drawStyle', 2)
            twist_end_joint = side + '_' + block_joint + '_TwistEnd_Jnt'
            mc.joint(n=twist_end_joint)
            mc.setAttr(twist_end_joint + '.drawStyle', 2)
            mc.parent(twist_start_joint, twist_grp)
            align(twist_start_joint, deform_parent_joint, 1, 1, 0, 1)
            mc.makeIdentity(twist_start_joint, apply=True, r=True)
            align(twist_end_joint, deform_joint, 1, 0, 0, 1)
            twist_joints = []
            for i in range(parent_subdivide + 1):
                mc.select(clear=True)
                mc.select(twist_start_joint)
                twist_joint = side + '_' + block_joint + '_Twist{}_Jnt'.format(i)
                mc.joint(n=twist_joint)
                mc.parent(twist_joint, twist_grp)
                twist_joints.append(twist_joint)
                mc.makeIdentity(twist_joint, apply=True, r=True)
                mc.setAttr(twist_joint + '.drawStyle', 2)
            twist_handle = side + '_' + block_joint + '_Twist_Handle'
            twist_effector = side + '_' + block_joint + '_Twist_Effector'
            temp = mc.ikHandle(n=twist_handle, solver='ikRPsolver', sj=twist_start_joint, ee=twist_end_joint)[1]

            mc.rename(temp, twist_effector)
            mc.setAttr(twist_handle + '.r', 0, 0, 0)
            mc.setAttr(twist_handle + '.v', False)
            twist_handle_grp = side + '_' + block_joint + '_TwistHandle_Grp'
            mc.createNode('transform', n=twist_handle_grp)
            mc.parent(twist_handle_grp, 'Twist_Handle')
            deform_parent_joint.replace('_Jnt', '_Twist_Grp')
            # self.constraintFKIK(mc.parentConstraint, switch_ctrl, fk_joint, ik_joint, twist_handle_grp)
            mc.parentConstraint(fkik_loc, twist_handle_grp)
            mc.parent(twist_handle, twist_handle_grp)

            twist_parent_joints = [side + '_' + block_parent_joint + '_Twist{}_Jnt'.format(i) for i in
                                   range(parent_subdivide + 1)]
            for i in range(parent_subdivide + 1):
                twist_parent_radio_mult = side + '_' + block_parent_joint + '_TwistRatio{}_Mult'.format(i)
                mc.disconnectAttr(twist_parent_radio_mult + '.outputX', twist_parent_joints[i] + '.rx')

            for i in range(parent_subdivide + 1):
                twist_radio_mult = side + '_' + block_joint + '_TwistRatio{}_Mult'.format(i)
                mc.createNode('multiplyDivide', n=twist_radio_mult)
                mc.setAttr(twist_radio_mult + '.input2X', i / (parent_subdivide + 1.0))
                mc.connectAttr(twist_start_joint + '.rx', twist_radio_mult + '.input1X')
                mc.connectAttr(twist_radio_mult + '.outputX', twist_joints[i] + '.rx')

                twist_parent_radio_mult = side + '_' + block_parent_joint + '_TwistRatio{}_Mult'.format(i)
                twist_radio_add = side + '_' + block_parent_joint + '_TwistRatio{}_Add'.format(i)
                mc.createNode('addDoubleLinear', n=twist_radio_add)
                mc.connectAttr(twist_parent_radio_mult + '.outputX', twist_radio_add + '.input1')
                mc.connectAttr(twist_radio_mult + '.outputX', twist_radio_add + '.input2')
                mc.connectAttr(twist_radio_add + '.output', twist_parent_joints[i] + '.rx')

        for deform in deforms:
            solver = deform.getIKSolver()
            subdivide = deform.getSubdivide()
            if not subdivide:
                continue
            if solver != 'IKRPSolver':
                continue
            side = deform.getSide()
            fat = deform.getFat()
            block_joint = deform.getJoint()
            deform_joint = deform.getDeformJoint()
            fk_ctrl = deform.getFKCtrl()
            part_joints = [deform_joint]
            part_joints.extend(deform.getPartJoints())
            fkik_loc = deform.getFKIKLoc()
            fkik_child_Loc = deform.getFKIKChildLoc()
            scale_blend = side + '_' + block_joint + '_Scale_Blend'
            # IK Part Translate
            part_ctrls = []
            part_poss = []
            part_grp = side + '_' + block_joint + '_Part_Grp'
            mc.createNode('transform', n=part_grp)

            align(part_grp, deform_joint, 1, 1, 0, 1)
            # 只影响控制器大小，不影响世纪骨骼大小
            mc.connectAttr(scale_blend + '.output', part_grp + '.s')
            mc.parentConstraint(fkik_loc, part_grp)
            mc.parent(part_grp, 'Part_Control')

            for i in range(subdivide + 1):
                part_ctrl = self.createController('Part', 'SecShape', block_joint + '_Part{}'.format(i), side,
                                                  scale * fat, part_joints[i])
                part_pos = part_ctrl.replace('_Ctrl', '_Pos')
                mc.parent(part_pos, part_grp)
                part_ctrls.append(part_ctrl)
                part_poss.append(part_pos)

                con = mc.pointConstraint(fkik_loc, fkik_child_Loc, part_pos)[0]

                w0 = 1.0 - ((i) / (subdivide + 1.0))
                w1 = ((i) / (subdivide + 1.0))

                mc.setAttr('{}.{}W0'.format(con, fkik_loc), w0)
                mc.setAttr('{}.{}W1'.format(con, fkik_child_Loc), w1)
                # 删除FK和IK对蒙皮骨骼的约束，改为使用part
                if i == 0:
                    mc.delete(part_joints[i] + '_orientConstraint1')
                    mc.delete(part_joints[i] + '_pointConstraint1')

                # scale
                if i == 0:
                    mc.disconnectAttr(scale_blend + '.output', deform_joint + '.s')

                else:
                    mc.disconnectAttr(deform_joint + '.sx', part_joints[i] + '.sx')
                    mc.disconnectAttr(deform_joint + '.sy', part_joints[i] + '.sy')
                    mc.disconnectAttr(deform_joint + '.sz', part_joints[i] + '.sz')

                # FK的scale属性和Part的scale属性相乘
                part_scale_mult = side + '_' + block_joint + '_Part{}Scale_Mult'.format(i)
                mc.createNode('multiplyDivide', n=part_scale_mult)
                mc.connectAttr(scale_blend + '.output', part_scale_mult + '.input1')
                mc.connectAttr(part_ctrl + '.s', part_scale_mult + '.input2')
                mc.connectAttr(part_scale_mult + '.output', part_joints[i] + '.s')

            twist_joints = [side + '_' + block_joint + '_Twist{}_Jnt'.format(i) for i in range(subdivide + 1)]
            # part_ctrl通过offset混合进FKIK的控制
            for i, part_joint in enumerate(part_joints):
                mc.orientConstraint(twist_joints[i], part_poss[i])
                mc.parentConstraint(part_ctrls[i], part_joint)

        # Advanced Bendy
        for deform in deforms:
            solver = deform.getIKSolver()
            subdivide = deform.getSubdivide()
            if not subdivide:
                continue
            if solver != 'IKRPSolver':
                continue
            block_joint = deform.getJoint()
            deform_joint = deform.getDeformJoint()
            deform_child_joint = deform.getDeformChildJoint()
            fk_joint = deform.getFKJoint()
            ik_joint = deform.getIKJoint()
            switch_ctrl = deform.getSwitchCtrl()
            side = deform.getSide()
            fat = deform.getFat()

            bendy_curve = side + '_' + block_joint + '_Bendy_Curve'
            bendy_curve_shape = side + '_' + block_joint + '_Bendy_CurveShape'
            points = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
            mc.curve(n=bendy_curve, d=3, p=points)
            mc.setAttr(bendy_curve + '.v', False)
            temp = mc.listRelatives(bendy_curve, s=True)[0]
            mc.rename(temp, bendy_curve_shape)
            mc.parent(bendy_curve, 'Bendy_Curve')
            bendy_grp = side + '_' + block_joint + '_Bendy_Grp'
            scale_blend = side + '_' + block_joint + '_Scale_Blend'
            mc.createNode('transform', n=bendy_grp)
            mc.parent(bendy_grp, 'Bendy_Control')
            self.constraintFKIK(mc.parentConstraint, switch_ctrl, fk_joint, ik_joint, bendy_grp)
            # 只影响控制器大小，不影响世纪骨骼大小
            mc.connectAttr(scale_blend + '.output', bendy_grp + '.s')
            bendy_locs = []
            bendy_ctrls = []
            bendy_poss = []
            for i in range(5):
                bendy_loc = side + '_' + block_joint + '_Bendy{}_Locator'.format(i)
                bendy_locs.append(bendy_loc)
                mc.spaceLocator(n=bendy_loc)
                mc.parent(bendy_loc, bendy_grp)
                mc.setAttr(bendy_loc + '.v', False, lock=True)
                mc.connectAttr(bendy_loc + 'Shape.worldPosition[0]'.format(i),
                               bendy_curve + 'Shape.controlPoints[{}]'.format(i))
                factor = (1.0 / 4.0) * i
                con = mc.pointConstraint(deform_joint, deform_child_joint, bendy_loc)[0]
                mc.setAttr('{}.{}W0'.format(con, deform_joint), 1 - factor)
                mc.setAttr('{}.{}W1'.format(con, deform_child_joint), factor)
                mc.delete(con)
                # controller
                if i != 4:
                    bendy_ctrl = ''
                    if i == 0 or i == 2:
                        bendy_ctrl = self.createController('FK', 'BendyShape',
                                                           deform_joint.replace('_Jnt', '_Bendy{}').format(i)[2:],
                                                           side,
                                                           scale * fat / 1.42, bendy_loc)
                    elif i == 1 or i == 3:
                        bendy_ctrl = self.createController('FK', 'SecShape',
                                                           deform_joint.replace('_Jnt', '_Bendy{}').format(i)[2:],
                                                           side,
                                                           scale * fat / 1.414, bendy_loc)
                        mc.setAttr(bendy_ctrl + 'Shape.overrideColorRGB', 253 / 255.0, 203 / 255.0, 110 / 255.0)
                    bendy_pos = bendy_ctrl.replace('_Ctrl', '_Pos')
                    bendy_poss.append(bendy_pos)
                    bendy_ctrls.append(bendy_ctrl)
                    align(bendy_pos, deform_joint, 0, 1, 0, 0)
                    mc.parent(bendy_pos, bendy_grp)
                    mc.parent(bendy_locs[i], bendy_ctrl)

            for i in range(subdivide + 1):
                bendy_curveInfo = side + '_' + block_joint + 'bendy{}_curveInfo'.format(i)
                mc.createNode('pointOnCurveInfo', n=bendy_curveInfo)
                mc.connectAttr(bendy_curve + '.worldSpace[0]', bendy_curveInfo + '.inputCurve')
                bendy_xform = side + '_' + block_joint + 'bendy{}_xform'.format(i)
                mc.createNode('transform', n=bendy_xform)
                mc.parent(bendy_xform, 'Bendy_Xform')
                mc.connectAttr(bendy_curveInfo + '.position', bendy_xform + '.t')
                mc.extrude(bendy_curve, n='temp_Surface', ch=True, rn=False, po=0, et=0, upn=1, length=1,
                           rotation=0, scale=1, dl=3)
                mc.createNode('closestPointOnSurface', n='temp_ClosestPointOnSurface')
                mc.spaceLocator(n='temp_ClosestPointOnSurfaceLoc')
                mc.connectAttr('temp_Surface.worldSpace[0]', "temp_ClosestPointOnSurface.inputSurface")
                mc.connectAttr('temp_ClosestPointOnSurfaceLoc.worldPosition[0]',
                               'temp_ClosestPointOnSurface.inPosition')
                con = mc.pointConstraint(deform_joint, deform_child_joint, 'temp_ClosestPointOnSurfaceLoc')[0]
                factor = i / (subdivide + 1.0)
                mc.setAttr('{}.{}W0'.format(con, deform_joint), 1 - factor)
                mc.setAttr('{}.{}W1'.format(con, deform_child_joint), factor)
                mc.setAttr(bendy_curveInfo + '.parameter', mc.getAttr('temp_ClosestPointOnSurface.parameterU'))
                mc.delete(['temp_ClosestPointOnSurface', 'temp_ClosestPointOnSurfaceLoc', 'temp_Surface'])
                part_ctrl = side + '_' + block_joint + '_Part{}'.format(i) + '_Ctrl'
                part_pos = side + '_' + block_joint + '_Part{}'.format(i) + '_Pos'
                twist_joint = side + '_' + block_joint + '_Twist{}'.format(i) + '_Jnt'
                mc.delete(part_pos + '_orientConstraint1')
                mc.delete(part_pos + '_pointConstraint1')
                mc.pointConstraint(bendy_xform, part_pos)

                if side == 'R':
                    mc.tangentConstraint(bendy_curve, part_pos, aimVector=(-1, 0, 0), upVector=(0, 1, 0),
                                         worldUpType='objectrotation', worldUpVector=(0, 1, 0),
                                         worldUpObject=twist_joint)
                else:
                    mc.tangentConstraint(bendy_curve, part_pos, aimVector=(1, 0, 0), upVector=(0, 1, 0),
                                         worldUpType='objectrotation', worldUpVector=(0, 1, 0),
                                         worldUpObject=twist_joint)

        # Advanced Bendy
        for deform in deforms:
            solver = deform.getIKSolver()
            subdivide = deform.getSubdivide()
            if not subdivide:
                continue
            if solver != 'IKRPSolver':
                continue
            block_joint = deform.getJoint()
            deform_joint = deform.getDeformJoint()
            deform_child_joint = deform.getDeformChildJoint()
            side = deform.getSide()
            fkik_loc = deform.getFKIKLoc()
            fkik_child_loc = deform.getFKIKChildLoc()
            bendy0_ctrl = deform_joint.replace('_Jnt', '_Bendy0_Ctrl')
            bendy1_ctrl = deform_joint.replace('_Jnt', '_Bendy1_Ctrl')
            bendy2_ctrl = deform_joint.replace('_Jnt', '_Bendy2_Ctrl')
            bendy3_ctrl = deform_joint.replace('_Jnt', '_Bendy3_Ctrl')
            bendy0_pos = deform_joint.replace('_Jnt', '_Bendy0_Pos')
            bendy1_pos = deform_joint.replace('_Jnt', '_Bendy1_Pos')
            bendy2_pos = deform_joint.replace('_Jnt', '_Bendy2_Pos')
            bendy3_pos = deform_joint.replace('_Jnt', '_Bendy3_Pos')
            bendy0_child_ctrl = deform_child_joint.replace('_Jnt', '_Bendy0_Ctrl')

            loc4 = side + '_' + block_joint + '_Bendy4_Locator'
            bendy_poss = [side + '_' + block_joint + '_Bendy{}'.format(i) + '_Pos' for i in range(4)]
            bendy_ctrls = [side + '_' + block_joint + '_Bendy{}'.format(i) + '_Ctrl' for i in range(4)]
            mc.pointConstraint(fkik_loc, bendy_poss[0])
            if mc.objExists(bendy0_child_ctrl):
                mc.parent(loc4, bendy0_child_ctrl)
                for i in range(1, 4, 1):
                    factor = i / 4.0
                    con = mc.pointConstraint(bendy0_ctrl, bendy0_child_ctrl, bendy_poss[i])[0]
                    mc.setAttr('{}.{}W0'.format(con, bendy0_ctrl), 1 - factor)
                    mc.setAttr('{}.{}W1'.format(con, bendy0_child_ctrl), factor)
                mc.aimConstraint(bendy0_child_ctrl, bendy2_pos, aimVector=(1, 0, 0), upVector=(0, 1, 0),
                                 worldUpType='objectrotation', worldUpVector=(0, 1, 0), worldUpObject=bendy0_ctrl)
            else:
                mc.parentConstraint(fkik_child_loc, loc4)
                for i in range(1, 4, 1):
                    factor = i / 4.0
                    con = mc.pointConstraint(bendy0_ctrl, fkik_child_loc, bendy_poss[i])[0]
                    mc.setAttr('{}.{}W0'.format(con, bendy0_ctrl), 1 - factor)
                    mc.setAttr('{}.{}W1'.format(con, fkik_child_loc), factor)
                    bendy_pos = deform_joint.replace('_Jnt', '_Bendy{}_Pos').format(i)
                mc.aimConstraint(fkik_child_loc, bendy2_pos, aimVector=(1, 0, 0), upVector=(0, 1, 0),
                                 worldUpType='objectrotation', worldUpVector=(0, 1, 0), worldUpObject=bendy0_ctrl)

            for bendy_pos in [bendy_poss[1], bendy_poss[3]]:
                mc.connectAttr(bendy_ctrls[2] + '.t', bendy_pos + '_pointConstraint1.offset')

            mc.parent(bendy1_pos, bendy2_ctrl)
            mc.parent(bendy3_pos, bendy2_ctrl)
            # # middle控制1和3
            # bendy1_rotate_loc = side + '_' + block_joint + '_Bendy1Rotate_Loc'
            # bendy3_rotate_loc = side + '_' + block_joint + '_Bendy3Rotate_Loc'
            # mc.createNode('transform', n=bendy1_rotate_loc)
            # align(bendy1_rotate_loc, bendy1_ctrl, 1, 1, 0, 0)
            # mc.createNode('transform', n=bendy3_rotate_loc)
            # align(bendy3_rotate_loc, bendy3_ctrl, 1, 1, 0, 0)
            #
            # mc.parent(bendy1_rotate_loc, bendy2_ctrl)
            # mc.parent(bendy3_rotate_loc, bendy2_ctrl)
            # mc.delete([bendy1_pos + '_pointConstraint1', bendy3_pos + '_pointConstraint1'])
            # mc.orientConstraint(bendy1_rotate_loc, bendy1_pos)
            # mc.orientConstraint(bendy3_rotate_loc, bendy3_pos)
            # con1 = mc.pointConstraint(bendy1_rotate_loc, bendy1_pos)[0]
            # con3 = mc.pointConstraint(bendy3_rotate_loc, bendy3_pos)[0]
            #
            #
            # loc1 = side + '_' + block_joint + '_Loc1'
            # mc.createNode('transform', n=loc1)
            # align(loc1, fkik_loc, 1, 1, 0, 0)
            # loc2 = side + '_' + block_joint + '_Loc2'
            # mc.createNode('transform', n=loc2)
            # align(loc2, fkik_child_loc, 1, 1, 0, 0)
            # mc.parent(loc2, loc1)
            # if mc.objExists(bendy0_child_ctrl):
            #     mc.parentConstraint(fkik_loc, loc1)
            #     mc.parentConstraint(bendy0_child_ctrl, loc2)
            # else:
            #     mc.parentConstraint(fkik_loc, loc1)
            #     mc.parentConstraint(fkik_child_loc, loc2)
            # bendy_minus = side + '_' + block_joint + '_Bendy_minus'
            # mc.createNode('plusMinusAverage', n=bendy_minus)
            # mc.setAttr(bendy_minus + '.operation', 2)
            # mc.connectAttr(loc2 + '.t', bendy_minus + '.input3D[0]')
            # mc.connectAttr(loc2 + '.t', bendy_minus + '.input3D[1]')
            # mc.disconnectAttr(loc2 + '.t', bendy_minus + '.input3D[1]')
            # bendy1_mul = side + '_' + block_joint + '_Bendy1_Mul'
            # mc.createNode('multiplyDivide', n=bendy1_mul)
            # mc.connectAttr(bendy_minus + '.output3D', bendy1_mul + '.input1')
            # mc.setAttr(bendy1_mul + '.input2X', -0.25)
            # mc.setAttr(bendy1_mul + '.input2Y', -0.25)
            # mc.setAttr(bendy1_mul + '.input2Z', -0.25)
            # mc.connectAttr(bendy1_mul + '.output', con1 + '.offset')
            #
            # bendy3_mul = side + '_' + block_joint + '_Bendy3_Mul'
            # mc.createNode('multiplyDivide', n=bendy3_mul)
            # mc.connectAttr(bendy_minus + '.output3D', bendy3_mul + '.input1')
            # mc.setAttr(bendy3_mul + '.input2X', 0.25)
            # mc.setAttr(bendy3_mul + '.input2Y', 0.25)
            # mc.setAttr(bendy3_mul + '.input2Z', 0.25)
            # mc.connectAttr(bendy3_mul + '.output', con3 + '.offset')

        # scale = getBlockScale()
        # mc.select(deforms[0].getDeformJoint(), hi=True)
        # for i, deform_joint in enumerate(mc.ls(sl=True)):
        #     deform_child_joint = mc.listRelatives(deform_joint, type='transform') or [None]
        #     deform_child_joint = deform_child_joint[0]
        #     if not deform_child_joint:
        #         continue
        #     poly = 'Poly{}'.format(i)
        #     mc.polyCube(n=poly)
        #     mc.rotate(0, -90, 0, relative=True)
        #     mc.delete(poly, constructionHistory=True)
        #     mc.makeIdentity(poly, apply=True, r=True)
        #     mc.move(0.5, 0, 0, poly + '.vtx[0:3]', relative=True)
        #     mc.move(-0.5, 0, 0, poly + '.vtx[4:7]', relative=True)
        #     mc.matchTransform(poly, deform_joint)
        #     # t = mc.getAttr(deform_child_joint + '.t')[0]
        #     fat = mc.getAttr(deform_joint + '.fat')
        #     if deform_joint.startswith('L_'):
        #         mc.move(scale * 0.2, 0, 0, poly + '.vtx[4:7]', relative=True, os=True)
        #     elif deform_joint.startswith('M_'):
        #         mc.move(scale * 0.2, 0, 0, poly + '.vtx[4:7]', relative=True, os=True)
        #     else:
        #         mc.move(-scale * 0.2, 0, 0, poly + '.vtx[0:3]', relative=True, os=True)
        #     print fat
        #     mc.scale(1, fat * 3, fat * 3, poly, r=True)

        # IK fatness
        for deform in deforms:
            function = deform.getFunction()
            if function != 'IK':
                continue
            side = deform.getSide()
            ik_grp = deform.getIKGrp()
            ik_ctrl = deform.getIKCtrl()
            start_joint = deform.getIKStartJoint()
            scale_start_blend = side + '_' + start_joint + '_Scale_Blend'
            mc.connectAttr(ik_ctrl + '.fatness1', scale_start_blend + '.color1R')
            mc.connectAttr(ik_ctrl + '.fatness1', scale_start_blend + '.color1G')
            mc.connectAttr(ik_ctrl + '.fatness1', scale_start_blend + '.color1B')

            middle_joint = deform.getIKMiddleJoint()
            scale_middle_blend = side + '_' + middle_joint + '_Scale_Blend'
            mc.connectAttr(ik_ctrl + '.fatness2', scale_middle_blend + '.color1R')
            mc.connectAttr(ik_ctrl + '.fatness2', scale_middle_blend + '.color1G')
            mc.connectAttr(ik_ctrl + '.fatness2', scale_middle_blend + '.color1B')

        # Advanced Aim
        for deform in deforms:
            function = deform.getFunction()
            if function != 'Aim':
                continue
            side = deform.getSide()
            fat = deform.getFat()
            block_joint = deform.getJoint()
            deform_joint = deform.getDeformJoint()
            deform_parent_joint = deform.getDeformParentJoint()
            aim_grp = side + '_' + block_joint + '_Aim_Grp'
            aim_ctrl = deform.getAimCtrl()
            aim_pos = aim_ctrl.replace('_Ctrl', '_Pos')
            fk_ctrl = deform.getFKCtrl()
            self.createController('Aim', 'AimShape', block_joint, side, scale * fat, None)
            lockAttrs(aim_ctrl, 0, 1, 1, 1)
            aim_followOn_grp = side + '_' + block_joint + '_AimFollowOn_Grp'
            aim_followOff_grp = side + '_' + block_joint + '_AimFollowOff_Grp'
            mc.createNode('transform', n=aim_followOn_grp)
            mc.createNode('transform', n=aim_followOff_grp)
            pos = mc.xform(deform_joint, q=True, ws=True, t=True)
            mc.xform(aim_followOn_grp, t=[pos[0], pos[1], pos[2] + scale * 2], ws=True)
            mc.xform(aim_followOff_grp, t=[pos[0], pos[1], pos[2] + scale * 2], ws=True)
            align(aim_pos, aim_followOn_grp, 1, 0, 0, 0)

            mc.addAttr(aim_ctrl, ln='follow', k=True, at='double', min=0, max=10, dv=10)
            aim_follow_unit = side + '_' + block_joint + '_AimFollow_Unit'
            mc.createNode('unitConversion', n=aim_follow_unit)
            mc.setAttr(aim_follow_unit + '.conversionFactor', 0.1)
            mc.connectAttr(aim_ctrl + '.follow', aim_follow_unit + '.input')

            aim_follow_reverse = side + '_' + block_joint + '_AimFollow_Reverse'
            mc.createNode('reverse', n=aim_follow_reverse)
            mc.connectAttr(aim_follow_unit + '.output', aim_follow_reverse + '.inputX')

            con = mc.parentConstraint(aim_followOn_grp, aim_followOff_grp, aim_pos)[0]
            mc.parentConstraint(deform_parent_joint, aim_followOn_grp, mo=True)

            mc.connectAttr(aim_follow_unit + '.output', '{0}.{1}W0'.format(con, aim_followOn_grp))
            mc.connectAttr(aim_follow_reverse + '.outputX', '{0}.{1}W1'.format(con, aim_followOff_grp))

            if side == 'R':
                mc.aimConstraint(aim_ctrl, fk_ctrl, aimVector=(-1, 0, 0), upVector=(0, 0, 1), worldUpVector=(0, 0, 1),
                                 worldUpType='objectrotation', worldUpObject=deform_parent_joint)
            else:
                mc.aimConstraint(aim_ctrl, fk_ctrl, aimVector=(1, 0, 0), upVector=(0, 0, 1), worldUpVector=(0, 0, 1),
                                 worldUpType='objectrotation', worldUpObject=deform_parent_joint)

            mc.createNode('transform', n=aim_grp)
            mc.parent(aim_grp, 'Aim_System')
            mc.parent(aim_pos, aim_grp)
            mc.parent(aim_followOn_grp, aim_grp)
            mc.parent(aim_followOff_grp, aim_grp)

        # # Advanced Finger
        for deform in deforms:
            function = deform.getFunction()
            side = deform.getSide()
            fat = deform.getFat()
            if function != 'Hand':
                continue
            block_joint = deform.getJoint()
            deform_joint = deform.getDeformJoint()
            finger_blocks_list = [deform.getThumbBlock(), deform.getIndexBlocks(), deform.getMiddleBlocks(),
                                  deform.getRingBlocks(), deform.getPinkyBlocks()]
            finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']

            switch_ctrl = side + '_' + block_joint + '_Switch_Ctrl'
            switch_pivot = deform.getFingerPivot()
            self.createController('Switch', 'CrossShape', block_joint + '_Switch', side, scale * fat, loc=None)
            switch_grp = side + '_' + block_joint + '_Switch_Grp'
            mc.createNode('transform', n=switch_grp)
            mc.matchTransform(switch_grp, deform_joint)
            mc.parentConstraint(deform_joint, switch_grp)
            mc.parent(switch_ctrl, switch_grp)
            mc.parent(switch_grp, 'Finger_System')

            if mc.objExists(switch_pivot):
                if mc.objExists('tempr_switch_pivot'):
                    mc.delete('temp_switch_pivot')
                mc.createNode('transform', n='temp_switch_pivot')
                mc.matchTransform('temp_switch_pivot', switch_pivot)
                if deform.getIsMirror():
                    mc.setAttr('temp_switch_pivot.tx', -mc.getAttr('temp_switch_pivot.tx'))
                mc.matchTransform(switch_ctrl, 'temp_switch_pivot', position=True)
                mc.delete('temp_switch_pivot')
            lockAttrs(switch_ctrl, 1, 1, 1, 1)

            for finger_blocks in finger_blocks_list:
                deform_joints = [side + '_' + finger_block.getJoint() + '_Jnt' for finger_block in finger_blocks]
                ik_joints = [side + '_' + finger_block.getJoint() + '_IK_Jnt' for finger_block in finger_blocks]
                fk_joints = [side + '_' + finger_block.getJoint() + '_FK_Jnt' for finger_block in finger_blocks]
                bend_joints = [side + '_' + finger_block.getJoint() + '_IKBend_Jnt' for finger_block in finger_blocks]
                squeeze_joints = [side + '_' + finger_block.getJoint() + '_IKSqueeze_Jnt' for finger_block in
                                  finger_blocks]
                finger_name = finger_names[finger_blocks_list.index(finger_blocks)]
                mc.select(clear=True)
                for i in range(len(bend_joints)):
                    mc.joint(n=bend_joints[i])
                    # mc.setAttr(bend_joints[i] + '.v', False)
                    align(bend_joints[i], deform_joints[i], 1, 1, 0, 0)
                    preferredAngle = mc.getAttr(finger_blocks[i].getJoint() + '.preferredAngle')[0]
                    mc.setAttr(bend_joints[i] + '.preferredAngleX', preferredAngle[0])
                    mc.setAttr(bend_joints[i] + '.preferredAngleY', preferredAngle[1])
                    mc.setAttr(bend_joints[i] + '.preferredAngleZ', preferredAngle[2])

                mc.select(clear=True)
                for i in range(len(squeeze_joints)):
                    mc.joint(n=squeeze_joints[i])
                    align(squeeze_joints[i], deform_joints[i], 1, 1, 0, 0)
                    preferredAngle = mc.getAttr(finger_blocks[i].getJoint() + '.preferredAngle')[0]
                    mc.setAttr(squeeze_joints[i] + '.preferredAngleX', preferredAngle[0])
                    mc.setAttr(squeeze_joints[i] + '.preferredAngleY', preferredAngle[1])
                    mc.setAttr(squeeze_joints[i] + '.preferredAngleZ', preferredAngle[2])

                mc.addAttr(switch_ctrl, ln='{}_blend'.format(finger_name), min=0, max=10, dv=0, at='double', k=True)
                switch_unit = side + '_' + finger_name + '_SwitchBlend_Unit'
                mc.createNode('unitConversion', n=switch_unit)
                mc.setAttr(switch_unit + '.conversionFactor', 0.1)
                mc.connectAttr(switch_ctrl + '.{}_blend'.format(finger_name), switch_unit + '.input')
                switch_reverse = side + '_' + finger_name + 'SwitchBlend_Reverse'
                mc.createNode('reverse', n=switch_reverse)
                mc.connectAttr(switch_unit + '.output', switch_reverse + '.inputX')

                mc.select(clear=True)
                for i in range(len(ik_joints)):
                    mc.joint(n=ik_joints[i])
                    align(ik_joints[i], deform_joints[i], 1, 1, 0, 0)
                    preferredAngle = mc.getAttr(finger_blocks[i].getJoint() + '.preferredAngle')[0]
                    mc.setAttr(ik_joints[i] + '.preferredAngleX', preferredAngle[0])
                    mc.setAttr(ik_joints[i] + '.preferredAngleY', preferredAngle[1])
                    mc.setAttr(ik_joints[i] + '.preferredAngleZ', preferredAngle[2])
                    if i != len(ik_joints) - 1:
                        point_con = mc.pointConstraint(ik_joints[i], deform_joints[i])[0]
                        orient_con = mc.orientConstraint(ik_joints[i], deform_joints[i])[0]
                        mc.connectAttr(switch_reverse + '.outputX', '{0}.{1}W0'.format(point_con, fk_joints[i]))
                        mc.connectAttr(switch_reverse + '.outputX', '{0}.{1}W0'.format(orient_con, fk_joints[i]))
                        mc.connectAttr(switch_unit + '.output', '{0}.{1}W1'.format(point_con, ik_joints[i]))
                        mc.connectAttr(switch_unit + '.output', '{0}.{1}W1'.format(orient_con, ik_joints[i]))

                ik_bend_handle = side + '_' + finger_name + '_IKBend_Handle'
                ik_squeeze1_handle = side + '_' + finger_name + '_IKSqueeze1_Handle'
                ik_squeeze2_handle = side + '_' + finger_name + '_IKSqueeze2_Handle'
                mc.ikHandle(n=ik_bend_handle, solver='ikSCsolver', sj=bend_joints[0], ee=bend_joints[-1])
                mc.ikHandle(n=ik_squeeze1_handle, solver='ikSCsolver', sj=squeeze_joints[0], ee=squeeze_joints[-2])
                mc.ikHandle(n=ik_squeeze2_handle, solver='ikSCsolver', sj=squeeze_joints[-2], ee=squeeze_joints[-1])
                mc.setAttr(ik_bend_handle + '.v', False)
                mc.setAttr(ik_squeeze1_handle + '.v', False)
                mc.setAttr(ik_squeeze2_handle + '.v', False)

                finger_grp = side + '_' + finger_name + '_Finger_Grp'
                mc.createNode('transform', n=finger_grp)
                align(finger_grp, deform_joint, 1, 1, 0, 0)
                mc.parentConstraint(deform_joint, finger_grp)


                mc.parent(finger_grp, 'Finger_System')

                finger_start_ctrl = self.createController('FK', 'SeedShape', finger_name + '_IKStart', side,
                                                          scale * fat * 0.3, deform_joints[0])
                mc.select(finger_start_ctrl + '.cv[*]')
                mc.move(0, 0, scale * fat * 0.5, r=True, os=True)
                finger_ctrl = self.createController('FK', 'CubeShape', finger_name + '_IK', side,
                                                    scale * fat * 0.3, deform_joints[-1])
                finger_squeeze_ctrl = self.createController('FK', 'FingerShape', finger_name + '_IKSqueeze', side,
                                                            scale * fat * 0.2, deform_joints[-1])
                finger_pos = finger_ctrl.replace('_Ctrl', '_Pos')
                finger_start_pos = finger_start_ctrl.replace('_Ctrl', '_Pos')
                finger_squeeze_pos = finger_squeeze_ctrl.replace('_Ctrl', '_Pos')
                mc.parent(ik_bend_handle, finger_ctrl)
                mc.parent(ik_squeeze1_handle, finger_squeeze_ctrl)
                mc.parent(ik_squeeze2_handle, finger_squeeze_ctrl)
                mc.parent(bend_joints[0], finger_start_ctrl)
                mc.parent(squeeze_joints[0], finger_start_ctrl)
                mc.parent(ik_joints[0], finger_start_ctrl)
                mc.parent(finger_squeeze_pos, finger_ctrl)
                mc.setAttr(ik_joints[0] + '.v', False)
                mc.setAttr(bend_joints[0] + '.v', False)
                mc.setAttr(squeeze_joints[0] + '.v', False)
                mc.setAttr(finger_squeeze_ctrl + '.v', False)

                mc.parent(finger_pos, finger_grp)
                mc.parent(finger_start_pos, finger_grp)


                mc.addAttr(finger_ctrl, ln='squeeze', k=True, at='double', min=0, max=10, dv=0)
                squeeze_unit = side + '_' + finger_name + '_Squeeze_Unit'
                mc.createNode('unitConversion', n=squeeze_unit)
                mc.setAttr(squeeze_unit + '.conversionFactor', 0.1)
                mc.connectAttr(finger_ctrl + '.squeeze', squeeze_unit + '.input')

                squeeze_reverse = side + '_' + finger_name + '_Squeeze_Reverse'
                mc.createNode('reverse', n=squeeze_reverse)
                mc.connectAttr(squeeze_unit + '.output', squeeze_reverse + '.inputX')

                for i in range(len(ik_joints)):
                    con = mc.parentConstraint(bend_joints[i], squeeze_joints[i], ik_joints[i])[0]
                    mc.connectAttr(squeeze_reverse + '.outputX', '{}.{}W0'.format(con, bend_joints[i]))
                    mc.connectAttr(squeeze_unit + '.output', '{}.{}W1'.format(con, squeeze_joints[i]))

                fk_pos = deform_joints[0].replace('_Jnt', '_FK_Pos')

                fkVis_cond = side + '_' + finger_name + '_FKVis_Cond'
                mc.createNode('condition', n=fkVis_cond)
                mc.connectAttr(switch_unit + '.output', fkVis_cond + '.firstTerm')
                mc.setAttr(fkVis_cond + '.secondTerm', 1)
                mc.setAttr(fkVis_cond + '.colorIfTrueR', 1)
                mc.setAttr(fkVis_cond + '.colorIfFalseR', 0)
                mc.setAttr(fkVis_cond + '.operation', 4)
                mc.connectAttr(fkVis_cond + '.outColorR', fk_pos + '.v', f=True)

                ikVis_cond = side + '_' + finger_name + '_IKVis_Cond'
                mc.createNode('condition', n=ikVis_cond)
                mc.connectAttr(switch_unit + '.output', ikVis_cond + '.firstTerm')
                mc.setAttr(ikVis_cond + '.secondTerm', 0)
                mc.setAttr(ikVis_cond + '.colorIfTrueR', 1)
                mc.setAttr(ikVis_cond + '.colorIfFalseR', 0)
                mc.setAttr(ikVis_cond + '.operation', 2)
                mc.connectAttr(ikVis_cond + '.outColorR', finger_grp + '.v', f=True)

                # squeeze_loc = side + '_' + finger_name + '_IKSqueeze_Loc'
                # mc.spaceLocator(n=squeeze_loc)
                # mc.setAttr(squeeze_loc + '.v', False)
                # align(squeeze_loc, bend_joints[-2], 1, 1, 0, 0)
                # mc.parent(squeeze_loc, bend_joints[-2])
                # if side == 'R':
                #     mc.aimConstraint(squeeze_loc, finger_squeeze_pos, aimVector=(1, 0, 0), upVector=(0, 1, 0),
                #                      worldUpType='objectrotation', worldUpVector=(0, 1, 0), worldUpObject=squeeze_loc)
                # else:
                #     mc.aimConstraint(squeeze_loc, finger_squeeze_pos, aimVector=(-1, 0, 0), upVector=(0, 1, 0),
                #                      worldUpType='objectrotation', worldUpVector=(0, 1, 0), worldUpObject=squeeze_loc)

        # Advanced Gravity
        if mc.getAttr('Block.gravityControl'):
            mc.parentConstraint('Main_Ctrl', 'Gravity_System')
            root_pos = 'Root_Pos'
            gravity_rot = 'Gravity_Rot'
            gravity_pos = 'Gravity_Pos'
            gravity_ctrl = 'Gravity_Ctrl'
            mc.createNode('transform', n=gravity_rot)
            align(gravity_rot, root_pos, 1, 1, 0, 0)
            mc.parent(gravity_rot, 'Root_System')
            self.createController('Gravity', 'GravityShape', 'Gravity', 'M', scale, loc=root_joint)
            mc.parent(gravity_pos, 'Gravity_System')
            mc.parent(root_pos, gravity_rot)
            mc.parentConstraint(gravity_ctrl, gravity_rot)
            gravity_minus = 'Gravity_Minus'
            mc.createNode('plusMinusAverage', n=gravity_minus)
            mc.setAttr(gravity_minus + '.operation', 2)
            mc.connectAttr(gravity_ctrl + '.t', gravity_minus + '.input3D[0]')
            mc.disconnectAttr(gravity_ctrl + '.t', gravity_minus + '.input3D[0]')
            mc.connectAttr(gravity_ctrl + '.t', gravity_minus + '.input3D[1]')
            mc.connectAttr(gravity_minus + '.output3D', root_pos + '.t')

        self.display_block_check.setChecked(False)
        self.displayBlock(False)
        self.display_control_check.setChecked(True)
        self.display_skeleton_check.setChecked(True)
        self.display_mesh_check.setChecked(True)
        self.only_block_check.setChecked(False)
        self.only_mesh_check.setChecked(False)
        self.only_skeleton_check.setChecked(False)
        self.only_control_check.setChecked(False)


        mc.delete('curveGroup')

        mc.select('Deformation_System', hi=True)
        con_list = mc.ls(sl=True, type='constraint')
        mc.parent(con_list, 'Constraint_System')

        if mc.objExists('Build_Pose'):
            mc.delete('Build_Pose')
        mc.createNode('dagPose', n='Build_Pose')
        mc.addAttr('Build_Pose', ln='code', dt='string')
        code = ''
        controls = mc.sets('ControlSet', q=True)
        for control in controls:
            attrs = mc.listAttr(control, k=True, unlocked=True)
            for attr in attrs:
                value = mc.getAttr(control + '.' + attr)
                code += '''mc.setAttr('{0}.{1}', {2});'''.format(control, attr, value)
        mc.setAttr('Build_Pose.code', code, type='string')

        mc.select(clear=True)

    def constraintFKIK(self, constraint, switch_ctrl, fk_joint, ik_joint, target):
        if mc.objExists(ik_joint):
            con = constraint(fk_joint, ik_joint, target)[0]
        else:
            con = constraint(fk_joint, target)[0]
        if mc.objExists(switch_ctrl):
            switch_blend_unit = switch_ctrl.replace('_Switch_Ctrl', '_SwitchBlend_Unit')
            switch_blend_reverse = switch_ctrl.replace('_Switch_Ctrl', '_SwitchBlend_Reverse')
            mc.connectAttr(switch_blend_reverse + '.outputX', '{}.{}W0'.format(con, fk_joint))
            mc.connectAttr(switch_blend_unit + '.output', '{}.{}W1'.format(con, ik_joint))

    def deleteRig(self):
        main_rig = mc.listRelatives('Block', p=True)
        if main_rig:
            mc.parent('Block', w=True)
            mc.setAttr('Block.v', True)
            mc.delete(main_rig)
            mc.select(clear=True)
            self.display_block_check.setChecked(True)
            self.display_mesh_check.setChecked(False)
            self.display_skeleton_check.setChecked(False)
            self.display_control_check.setChecked(False)

            self.only_block_check.setChecked(False)
            self.only_mesh_check.setChecked(False)
            self.only_skeleton_check.setChecked(False)
            self.only_control_check.setChecked(False)
        if mc.objExists('Sets'):
            mc.delete('Sets')
        if mc.objExists('ControlSet'):
            mc.delete('Sets')
        if mc.objExists('DeformSet'):
            mc.delete('Sets')
        if mc.objExists('AllSet'):
            mc.delete('Sets')



    def restoreBuildPose(self):
        if mc.objExists('Build_Pose'):
            code = mc.getAttr('Build_Pose.code')
            exec(code)

    def createController(self, function, shape, name, side, scale, loc=None):
        mc.select(cl=True)
        if function == 'Main':
            ctrl = name + '_Ctrl'
            mc.duplicate(shape, n=ctrl)
            mc.scale(scale * 6, scale * 6, scale * 6, ctrl, r=True)
            mc.xform(ctrl, ws=True, t=[0, 0, 0])
            mc.makeIdentity(ctrl, apply=True)
        elif function == 'Switch':
            ctrl = side + '_' + name + '_Ctrl'
            mc.duplicate(shape, n=ctrl)
            mc.scale(scale * 0.5, scale * 0.5, scale * 0.5, ctrl, r=True)
            mc.xform(ctrl, ws=True, t=[0, 0, 0])
            mc.makeIdentity(ctrl, apply=True)
        else:
            if function == 'Root':
                ctrl = name + '_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale * 2.5, scale * 2.5, scale * 2.5, ctrl, r=True)
                mc.matchTransform(ctrl, loc, position=True)
                mc.makeIdentity(ctrl, apply=True, scale=True)
            if function == 'Gravity':
                ctrl = name + '_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale * 1, scale * 1, scale * 1, ctrl, r=True)
                mc.matchTransform(ctrl, loc, position=True)
                mc.makeIdentity(ctrl, apply=True, scale=True)

            elif function == 'FK':
                ctrl = side + '_' + name + '_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale, scale, scale, ctrl, r=True)
                mc.matchTransform(ctrl, loc, position=True, rotation=True)
                mc.makeIdentity(ctrl, apply=True, scale=True)
            elif function == 'IK':
                ctrl = side + '_' + name + '_IK_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale, scale, scale, ctrl, r=True)
                mc.matchTransform(ctrl, loc, position=True, rotation=True)
                mc.makeIdentity(ctrl, apply=True, scale=True)
            elif function == 'Spline':
                ctrl = side + '_' + name + '_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale, scale, scale, ctrl, r=True)
                mc.matchTransform(ctrl, loc, position=True, rotation=True)
                mc.makeIdentity(ctrl, apply=True, scale=True, r=True)
            elif function == 'Cv':
                ctrl = side + '_' + name + '_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale, scale, scale, ctrl, r=True)
                mc.makeIdentity(ctrl, apply=True, scale=True)
            elif function == 'Pole':
                ctrl = side + '_' + name + '_Pole_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale * 0.2, scale * 0.2, scale * 0.2, ctrl, r=True)
                mc.makeIdentity(ctrl, apply=True, scale=True)
            elif function == 'Roll':
                ctrl = side + '_' + name + '_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale, scale, scale, ctrl, r=True)
                mc.matchTransform(ctrl, loc, position=True)
                mc.makeIdentity(ctrl, apply=True, scale=True)
            elif function == 'Toe':
                ctrl = side + '_' + name + '_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale, scale, scale, ctrl, r=True)
                mc.matchTransform(ctrl, loc, position=True, rotation=True)
                mc.makeIdentity(ctrl, apply=True, scale=True)
            elif function == 'Part':
                ctrl = side + '_' + name + '_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale, scale, scale, ctrl, r=True)
                mc.matchTransform(ctrl, loc, position=True, rotation=True)
                mc.makeIdentity(ctrl, apply=True, scale=True)
            elif function == 'Aim':
                ctrl = side + '_' + name + '_Aim_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale, scale, scale, ctrl, r=True)
                mc.makeIdentity(ctrl, apply=True, scale=True)
            elif function == 'Finger':
                ctrl = side + '_' + name + '_Finger_Ctrl'
                mc.duplicate(shape, n=ctrl)
                mc.scale(scale, scale, scale, ctrl, r=True)
                mc.matchTransform(ctrl, loc, position=True, rotation=True)
                mc.makeIdentity(ctrl, apply=True, scale=True)
            pos = mc.createNode('transform', n=ctrl.replace('_Ctrl', '_Pos'))
            driven = mc.createNode('transform', n=ctrl.replace('_Ctrl', '_Driven'), p=pos)
            connect = mc.createNode('transform', n=ctrl.replace('_Ctrl', '_Connect'), p=driven)
            offset = mc.createNode('transform', n=ctrl.replace('_Ctrl', '_Offset'), p=connect)
            mc.matchTransform(pos, ctrl, position=True, rotation=True)
            mc.parent(ctrl, offset)
            # output = mc.createNode('transform', n=ctrl.replace('_Ctrl', '_Output'))
            # mc.matchTransform(output, ctrl, position=True, rotation=True)
            # mc.parent(output, ctrl)
        return ctrl


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
