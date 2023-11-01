#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import maya.cmds as mc

import modules.maya_utilities as maya_utilities
import maya_widgets.switch_button as switch_button
import maya_widgets.flatten_widget as flatten_widget
reload(flatten_widget)
from modules.maya_utilities import ICONS_DIR








class HandBlock(QWidget):
    def __init__(self, parent=None, block=None):
        super(HandBlock, self).__init__(parent)
        self.block = block
        self.setupUI()
        self.connect()

    def setupUI(self):
        font = maya_utilities.font
        font.setPointSize(8)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(5)
        self.main_layout.setContentsMargins(0, 2, 6, 0)

        ## OrientX
        self.orient_x_layout = QHBoxLayout()
        self.orient_x_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.orient_x_layout)

        self.orient_x_label = flatten_widget.MPointLabel(self)
        self.orient_x_label.setFont(font)
        self.orient_x_label.setText('OrientX')
        self.orient_x_label.setFixedWidth(140)
        self.orient_x_layout.addWidget(self.orient_x_label)

        self.orient_x_combo = flatten_widget.MComboBox(color=[59, 59, 59], border=1)
        self.orient_x_combo.setFont(font)
        self.orient_x_combo.addItems(['Common', 'Parent', 'Free', 'World'])
        self.orient_x_layout.addWidget(self.orient_x_combo)
        self.addLine()

        ## WorldX
        self.world_x_layout = QHBoxLayout()
        self.world_x_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.world_x_layout)

        self.world_x_label = flatten_widget.MPointLabel(self)
        self.world_x_label.setFont(font)
        self.world_x_label.setText('WorldX')
        self.world_x_label.setFixedWidth(140)
        self.world_x_layout.addWidget(self.world_x_label)

        self.world_x_x_spin = flatten_widget.MDoubleSpinBox()
        self.world_x_layout.addWidget(self.world_x_x_spin)
        self.world_x_y_spin = flatten_widget.MDoubleSpinBox()
        self.world_x_layout.addWidget(self.world_x_y_spin)
        self.world_x_z_spin = flatten_widget.MDoubleSpinBox()
        self.world_x_layout.addWidget(self.world_x_z_spin)
        self.addLine()


        ## OrientY
        self.orient_y_layout = QHBoxLayout()
        self.orient_y_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.orient_y_layout)

        self.orient_y_label = flatten_widget.MPointLabel(self)
        self.orient_y_label.setFont(font)
        self.orient_y_label.setText('OrientY')
        self.orient_y_label.setFixedWidth(140)
        self.orient_y_layout.addWidget(self.orient_y_label)

        self.orient_y_combo = flatten_widget.MComboBox(color=[59, 59, 59], border=1)
        self.orient_y_combo.setFont(font)
        self.orient_y_combo.addItems(['Common', 'Parent', 'Free', 'World'])
        self.orient_y_layout.addWidget(self.orient_y_combo)
        self.addLine()

        ## WorldY
        self.world_y_layout = QHBoxLayout()
        self.world_y_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.world_y_layout)

        self.world_y_label = flatten_widget.MPointLabel(self)
        self.world_y_label.setFont(font)
        self.world_y_label.setText('WorldX')
        self.world_y_label.setFixedWidth(140)
        self.world_y_layout.addWidget(self.world_y_label)

        self.world_y_x_spin = flatten_widget.MDoubleSpinBox()
        self.world_y_layout.addWidget(self.world_y_x_spin)
        self.world_y_y_spin = flatten_widget.MDoubleSpinBox()
        self.world_y_layout.addWidget(self.world_y_y_spin)
        self.world_y_z_spin = flatten_widget.MDoubleSpinBox()
        self.world_y_layout.addWidget(self.world_y_z_spin)
        self.addLine()

        ## Name
        self.name_layout = QHBoxLayout()
        self.name_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.name_layout)

        self.name_label = flatten_widget.MPointLabel(self)
        self.name_label.setFont(font)
        self.name_label.setText('Name')
        self.name_label.setFixedWidth(140)
        self.name_layout.addWidget(self.name_label)

        self.name_lineEdit = flatten_widget.MLineEdit()
        self.name_lineEdit.setPlaceholderText('Default')
        self.name_lineEdit.setFont(font)
        self.name_lineEdit.setStyleSheet('''
                                                                            border:none;
                                                                            background-color:transparent;
                                                                            border-bottom: 1px solid rgb(120, 120, 120);
                                                                            padding-bottom: 0px;
                                                                        ''')
        self.name_layout.addWidget(self.name_lineEdit)
        self.addLine()

        ## fat
        self.fat_layout = QHBoxLayout()
        self.fat_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.fat_layout)

        self.fat_label = flatten_widget.MPointLabel(self)
        self.fat_label.setFont(font)
        self.fat_label.setText('Fat')
        self.fat_label.setFixedWidth(140)
        self.fat_layout.addWidget(self.fat_label)

        self.fat_spin = flatten_widget.MDoubleSpinBox()
        self.fat_spin.setSingleStep(0.1)
        self.fat_layout.addWidget(self.fat_spin)
        self.addLine()

        ## SegScaleComp
        self.segScaleComp_layout = QHBoxLayout()
        self.segScaleComp_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.segScaleComp_layout)

        self.segScaleComp_label = flatten_widget.MPointLabel(self)
        self.segScaleComp_label.setFont(font)
        self.segScaleComp_label.setText('Seg Scale Comp')
        self.segScaleComp_label.setFixedWidth(140)
        self.segScaleComp_layout.addWidget(self.segScaleComp_label)

        self.segScaleComp_check = switch_button.MSwitch()
        self.segScaleComp_check.setChecked(False)
        self.segScaleComp_layout.addWidget(self.segScaleComp_check)
        self.segScaleComp_layout.addStretch()
        self.addLine()

        ## FingerShape
        self.fingerShape_layout = QHBoxLayout()
        self.fingerShape_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.fingerShape_layout)

        self.fingerShape_label = flatten_widget.MPointLabel(self)
        self.fingerShape_label.setFont(font)
        self.fingerShape_label.setText('Finger Shape')
        self.fingerShape_label.setFixedWidth(140)
        self.fingerShape_layout.addWidget(self.fingerShape_label)

        self.fingerShape_combo = flatten_widget.MComboBox(color=[59, 59, 59], border=1)
        self.fingerShape_combo.setFont(font)
        self.fingerShape_combo.addItems(['FK', 'IK', 'Spline', 'Finger', 'Main'])
        self.fingerShape_layout.addWidget(self.fingerShape_combo)
        self.addLine()

        ## Finger IK
        self.fingerIK_layout = QHBoxLayout()
        self.fingerIK_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.fingerIK_layout)

        self.fingerIK_label = flatten_widget.MPointLabel(self)
        self.fingerIK_label.setFont(font)
        self.fingerIK_label.setText('Finger IK')
        self.fingerIK_label.setFixedWidth(140)
        self.fingerIK_layout.addWidget(self.fingerIK_label)

        self.finger_check = switch_button.MSwitch()
        self.finger_check.setChecked(True)
        self.fingerIK_layout.addWidget(self.finger_check)
        self.fingerIK_layout.addStretch()
        self.addLine()

        # Finger Pivot
        self.finger_layout = QHBoxLayout()
        self.finger_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.finger_layout)

        self.finger_label = flatten_widget.MPointLabel(self)
        self.finger_label.setFont(font)
        self.finger_label.setText('Finger Pivot')
        self.finger_label.setFixedWidth(140)
        self.finger_layout.addWidget(self.finger_label)

        self.finger_lineEdit = flatten_widget.MLineEdit()
        self.finger_lineEdit.setPlaceholderText('None')
        self.finger_lineEdit.setFont(font)
        self.finger_lineEdit.setObjectName('lineEdit')
        self.finger_layout.addWidget(self.finger_lineEdit)
        self.finger_lineEdit.setStyleSheet('''
                                     #lineEdit_button
                                     {
                                         background-color:transparent;
                                         color:none;
                                         border: none;
                                     }
                                     #lineEdit
                                     {
                                         border:none;
                                         background-color:transparent;
                                         border-bottom: 1px solid rgb(120, 120, 120);
                                         padding-bottom: 0px;
                                     }
                                     ''')

        self.finger_pick_button = flatten_widget.MFlattentButton(size=18)
        self.finger_pick_button.setObjectName('lineEdit_button')
        self.finger_pick_button.setIcon(maya_utilities.getIcon(ICONS_DIR + 'pick.svg', 18, 18))
        self.finger_pick_button.setIconSize(QSize(18, 18))

        layout = QHBoxLayout()
        self.finger_lineEdit.setLayout(layout)
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.finger_pick_button)
        self.addLine()



        # Thumb
        self.thumb_layout = QHBoxLayout()
        self.thumb_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.thumb_layout)

        self.thumb_label = flatten_widget.MPointLabel(self)
        self.thumb_label.setFont(font)
        self.thumb_label.setText('Thumb List')
        self.thumb_label.setFixedWidth(140)
        self.thumb_layout.addWidget(self.thumb_label)

        self.thumb_lineEdit = flatten_widget.MLineEdit()
        self.thumb_lineEdit.setPlaceholderText('None')
        self.thumb_lineEdit.setFont(font)
        self.thumb_lineEdit.setObjectName('lineEdit')
        self.thumb_layout.addWidget(self.thumb_lineEdit)
        self.thumb_lineEdit.setStyleSheet('''
                                     #lineEdit_button
                                     {
                                         background-color:transparent;
                                         color:none;
                                         border: none;
                                     }
                                     #lineEdit
                                     {
                                         border:none;
                                         background-color:transparent;
                                         border-bottom: 1px solid rgb(120, 120, 120);
                                         padding-bottom: 0px;
                                     }
                                     ''')

        self.thumb_pick_button = flatten_widget.MFlattentButton(size=18)
        self.thumb_pick_button.setObjectName('lineEdit_button')
        self.thumb_pick_button.setIcon(maya_utilities.getIcon(ICONS_DIR + 'pick.svg', 18, 18))
        self.thumb_pick_button.setIconSize(QSize(18, 18))

        layout = QHBoxLayout()
        self.thumb_lineEdit.setLayout(layout)
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.thumb_pick_button)
        self.addLine()

        # Index
        self.index_layout = QHBoxLayout()
        self.index_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.index_layout)

        self.index_label = flatten_widget.MPointLabel(self)
        self.index_label.setFont(font)
        self.index_label.setText('Index List')
        self.index_label.setFixedWidth(140)
        self.index_layout.addWidget(self.index_label)

        self.index_lineEdit = flatten_widget.MLineEdit()
        self.index_lineEdit.setPlaceholderText('None')
        self.index_lineEdit.setFont(font)
        self.index_lineEdit.setObjectName('lineEdit')
        self.index_layout.addWidget(self.index_lineEdit)
        self.index_lineEdit.setStyleSheet('''
                                      #lineEdit_button
                                      {
                                          background-color:transparent;
                                          color:none;
                                          border: none;
                                      }
                                      #lineEdit
                                      {
                                          border:none;
                                          background-color:transparent;
                                          border-bottom: 1px solid rgb(120, 120, 120);
                                          padding-bottom: 0px;
                                      }
                                      ''')

        self.index_pick_button = flatten_widget.MFlattentButton(size=18)
        self.index_pick_button.setObjectName('lineEdit_button')
        self.index_pick_button.setIcon(maya_utilities.getIcon(ICONS_DIR + 'pick.svg', 18, 18))
        self.index_pick_button.setIconSize(QSize(18, 18))

        layout = QHBoxLayout()
        self.index_lineEdit.setLayout(layout)
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.index_pick_button)
        self.addLine()


        # Middle
        self.middle_layout = QHBoxLayout()
        self.middle_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.middle_layout)

        self.middle_label = flatten_widget.MPointLabel(self)
        self.middle_label.setFont(font)
        self.middle_label.setText('Middle List')
        self.middle_label.setFixedWidth(140)
        self.middle_layout.addWidget(self.middle_label)

        self.middle_lineEdit = flatten_widget.MLineEdit()
        self.middle_lineEdit.setPlaceholderText('None')
        self.middle_lineEdit.setFont(font)
        self.middle_lineEdit.setObjectName('lineEdit')
        self.middle_layout.addWidget(self.middle_lineEdit)
        self.middle_lineEdit.setStyleSheet('''
                                      #lineEdit_button
                                      {
                                          background-color:transparent;
                                          color:none;
                                          border: none;
                                      }
                                      #lineEdit
                                      {
                                          border:none;
                                          background-color:transparent;
                                          border-bottom: 1px solid rgb(120, 120, 120);
                                          padding-bottom: 0px;
                                      }
                                      ''')

        self.middle_pick_button = flatten_widget.MFlattentButton(size=18)
        self.middle_pick_button.setObjectName('lineEdit_button')
        self.middle_pick_button.setIcon(maya_utilities.getIcon(ICONS_DIR + 'pick.svg', 18, 18))
        self.middle_pick_button.setIconSize(QSize(18, 18))

        layout = QHBoxLayout()
        self.middle_lineEdit.setLayout(layout)
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.middle_pick_button)
        self.addLine()

        # Ring
        self.ring_layout = QHBoxLayout()
        self.ring_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.ring_layout)

        self.ring_label = flatten_widget.MPointLabel(self)
        self.ring_label.setFont(font)
        self.ring_label.setText('Ring List')
        self.ring_label.setFixedWidth(140)
        self.ring_layout.addWidget(self.ring_label)

        self.ring_lineEdit = flatten_widget.MLineEdit()
        self.ring_lineEdit.setPlaceholderText('None')
        self.ring_lineEdit.setFont(font)
        self.ring_lineEdit.setObjectName('lineEdit')
        self.ring_layout.addWidget(self.ring_lineEdit)
        self.ring_lineEdit.setStyleSheet('''
                                      #lineEdit_button
                                      {
                                          background-color:transparent;
                                          color:none;
                                          border: none;
                                      }
                                      #lineEdit
                                      {
                                          border:none;
                                          background-color:transparent;
                                          border-bottom: 1px solid rgb(120, 120, 120);
                                          padding-bottom: 0px;
                                      }
                                      ''')

        self.ring_pick_button = flatten_widget.MFlattentButton(size=18)
        self.ring_pick_button.setObjectName('lineEdit_button')
        self.ring_pick_button.setIcon(maya_utilities.getIcon(ICONS_DIR + 'pick.svg', 18, 18))
        self.ring_pick_button.setIconSize(QSize(18, 18))

        layout = QHBoxLayout()
        self.ring_lineEdit.setLayout(layout)
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ring_pick_button)
        self.addLine()

        # Pinky
        self.pinky_layout = QHBoxLayout()
        self.pinky_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.pinky_layout)

        self.pinky_label = flatten_widget.MPointLabel(self)
        self.pinky_label.setFont(font)
        self.pinky_label.setText('Pinky List')
        self.pinky_label.setFixedWidth(140)
        self.pinky_layout.addWidget(self.pinky_label)

        self.pinky_lineEdit = flatten_widget.MLineEdit()
        self.pinky_lineEdit.setPlaceholderText('None')
        self.pinky_lineEdit.setFont(font)
        self.pinky_lineEdit.setObjectName('lineEdit')
        self.pinky_layout.addWidget(self.pinky_lineEdit)
        self.pinky_lineEdit.setStyleSheet('''
                                        #lineEdit_button
                                        {
                                            background-color:transparent;
                                            color:none;
                                            border: none;
                                        }
                                        #lineEdit
                                        {
                                            border:none;
                                            background-color:transparent;
                                            border-bottom: 1px solid rgb(120, 120, 120);
                                            padding-bottom: 0px;
                                        }
                                        ''')

        self.pinky_pick_button = flatten_widget.MFlattentButton(size=18)
        self.pinky_pick_button.setObjectName('lineEdit_button')
        self.pinky_pick_button.setIcon(maya_utilities.getIcon(ICONS_DIR + 'pick.svg', 18, 18))
        self.pinky_pick_button.setIconSize(QSize(18, 18))

        layout = QHBoxLayout()
        self.pinky_lineEdit.setLayout(layout)
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.pinky_pick_button)
        self.addLine()
        
        self.updateWidget()

        self.main_layout.addStretch()
    def addLine(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet('''
                                        border-top:1px solid rgb(60, 60, 60);
                                    ''')
        line.setFixedHeight(1)
        self.main_layout.addWidget(line)

    def connect(self):
        orient_list = ['Common', 'Parent', 'Free', 'World']
        self.orient_x_combo.currentIndexChanged.connect(lambda: self.block.setOrientX(orient_list[self.orient_x_combo.currentIndex()]))
        self.world_x_x_spin.valueChanged.connect(lambda: self.block.setWorldX([self.world_x_x_spin.value(), self.world_x_y_spin.value(), self.world_x_z_spin.value()]))
        self.world_x_y_spin.valueChanged.connect(lambda: self.block.setWorldX([self.world_x_x_spin.value(), self.world_x_y_spin.value(), self.world_x_z_spin.value()]))
        self.world_x_z_spin.valueChanged.connect(lambda: self.block.setWorldX([self.world_x_x_spin.value(), self.world_x_y_spin.value(), self.world_x_z_spin.value()]))
        self.orient_y_combo.currentIndexChanged.connect(lambda: self.block.setOrientY(orient_list[self.orient_y_combo.currentIndex()]))
        self.world_y_x_spin.valueChanged.connect(lambda: self.block.setWorldY([self.world_y_x_spin.value(), self.world_y_y_spin.value(), self.world_y_z_spin.value()]))
        self.world_y_y_spin.valueChanged.connect(lambda: self.block.setWorldY([self.world_y_x_spin.value(), self.world_y_y_spin.value(), self.world_y_z_spin.value()]))
        self.world_y_z_spin.valueChanged.connect(lambda: self.block.setWorldY([self.world_y_x_spin.value(), self.world_y_y_spin.value(), self.world_y_z_spin.value()]))
        self.name_lineEdit.textChanged.connect(self.block.setName)
        self.fat_spin.valueChanged.connect(self.block.setFat)
        self.segScaleComp_check.toggled.connect(self.block.setSegScaleComp)
        self.fingerShape_combo.currentIndexChanged.connect(self.block.setFKShape)

        self.finger_pick_button.clicked.connect(lambda: self.finger_lineEdit.setText(self.pickPivot()))
        self.finger_lineEdit.textChanged.connect(self.block.setFingerPivot)
        self.thumb_pick_button.clicked.connect(lambda: self.thumb_lineEdit.setText(self.pickFinger()))
        self.thumb_lineEdit.textChanged.connect(self.block.setThumbList)
        self.index_pick_button.clicked.connect(lambda: self.index_lineEdit.setText(self.pickFinger()))
        self.index_lineEdit.textChanged.connect(self.block.setIndexList)
        self.middle_pick_button.clicked.connect(lambda: self.middle_lineEdit.setText(self.pickFinger()))
        self.middle_lineEdit.textChanged.connect(self.block.setMiddleList)
        self.ring_pick_button.clicked.connect(lambda: self.ring_lineEdit.setText(self.pickFinger()))
        self.ring_lineEdit.textChanged.connect(self.block.setRingList)
        self.pinky_pick_button.clicked.connect(lambda: self.pinky_lineEdit.setText(self.pickFinger()))
        self.pinky_lineEdit.textChanged.connect(self.block.setPinkyList)

    def pickPivot(self):
        sel_list = mc.ls(sl=True)
        if sel_list:
            return sel_list[0]
        else:
            return ''

    def pickFinger(self):
        sel_list = mc.ls(sl=True, type='joint')
        if len(sel_list) > 2:
            return sel_list.join(';')
        else:
            return ''


    def updateWidget(self):
        block_joint = self.block.getJoint()
        self.orient_x_combo.setCurrentIndex(mc.getAttr(block_joint + '.orientX'))
        self.orient_y_combo.setCurrentIndex(mc.getAttr(block_joint + '.orientY'))
        world_x = mc.getAttr(block_joint + '.worldX')[0]
        self.world_x_x_spin.setValue(world_x[0])
        self.world_x_y_spin.setValue(world_x[1])
        self.world_x_z_spin.setValue(world_x[2])
        world_y = mc.getAttr(block_joint + '.worldY')[0]
        self.world_y_x_spin.setValue(world_y[0])
        self.world_y_y_spin.setValue(world_y[1])
        self.world_y_z_spin.setValue(world_y[2])
        name = mc.getAttr(block_joint + '.name')
        self.name_lineEdit.setText(name)
        fat = mc.getAttr(block_joint + '.fat')
        self.fat_spin.setValue(fat)
        segScaleComp = mc.getAttr(block_joint + '.segScaleComp')
        self.segScaleComp_check.setChecked(segScaleComp)
        finger_shape = mc.getAttr(block_joint + '.fingerShape')
        self.fingerShape_combo.setCurrentIndex(finger_shape)
        finger_pivot = mc.getAttr(block_joint + '.fingerPivot')
        self.finger_lineEdit.setText(finger_pivot)
        thumb_list = mc.getAttr(block_joint + '.thumbList')
        self.thumb_lineEdit.setText(thumb_list)
        index_list = mc.getAttr(block_joint + '.indexList')
        self.index_lineEdit.setText(index_list)
        middle_list = mc.getAttr(block_joint + '.middleList')
        self.middle_lineEdit.setText(middle_list)
        ring_list = mc.getAttr(block_joint + '.ringList')
        self.ring_lineEdit.setText(ring_list)
        pinky_list = mc.getAttr(block_joint + '.pinkyList')
        self.pinky_lineEdit.setText(pinky_list)
