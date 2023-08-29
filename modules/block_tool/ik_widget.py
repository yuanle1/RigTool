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





class IKBlock(QWidget):
    def __init__(self, parent=None, block=None):
        super(IKBlock, self).__init__(parent)
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
        self.name_lineEdit.setFont(font)
        self.name_lineEdit.setText('Default')
        self.name_lineEdit.setStyleSheet('''
                                                            color:rgb(120, 120, 120);
                                                            border:none;
                                                            background-color:transparent;
                                                            border-bottom: 1px solid rgb(120, 120, 120);
                                                            padding-bottom: 0px;
                                                        ''')
        self.name_layout.addWidget(self.name_lineEdit)
        self.addLine()

        ## Subdivide
        self.subdivide_layout = QHBoxLayout()
        self.subdivide_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.subdivide_layout)

        self.subdivide_label = flatten_widget.MPointLabel(self)
        self.subdivide_label.setFont(font)
        self.subdivide_label.setText('Subdivide')
        self.subdivide_label.setFixedWidth(140)
        self.subdivide_layout.addWidget(self.subdivide_label)

        self.subdivide_spin = flatten_widget.MSpinBox()
        self.subdivide_layout.addWidget(self.subdivide_spin)
        self.addLine()

        # ## IKControl
        # self.ikControl_layout = QHBoxLayout()
        # self.ikControl_layout.setContentsMargins(8, 0, 0, 0)
        # self.main_layout.addLayout(self.ikControl_layout)
        #
        # self.ikControl_label = flatten_widget.MPointLabel(self)
        # self.ikControl_label.setFont(font)
        # self.ikControl_label.setText('IK Control')
        # self.ikControl_label.setFixedWidth(140)
        # self.ikControl_layout.addWidget(self.ikControl_label)
        #
        # self.ikControl_check = switch_button.MSwitch()
        # self.ikControl_check.setChecked(True)
        # self.ikControl_layout.addWidget(self.ikControl_check)
        # self.ikControl_layout.addStretch()
        # self.addLine()

        ## secondControl
        self.secControl_layout = QHBoxLayout()
        self.secControl_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.secControl_layout)

        self.secControl_label = flatten_widget.MPointLabel(self)
        self.secControl_label.setFont(font)
        self.secControl_label.setText('Sec Control')
        self.secControl_label.setFixedWidth(140)
        self.secControl_layout.addWidget(self.secControl_label)

        self.secControl_check = switch_button.MSwitch()
        self.secControl_check.setChecked(True)
        self.secControl_layout.addWidget(self.secControl_check)
        self.secControl_layout.addStretch()
        self.addLine()

        ## IKShape
        self.ikShape_layout = QHBoxLayout()
        self.ikShape_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.ikShape_layout)

        self.ikShape_label = flatten_widget.MPointLabel(self)
        self.ikShape_label.setFont(font)
        self.ikShape_label.setText('IK Shape')
        self.ikShape_label.setFixedWidth(140)
        self.ikShape_layout.addWidget(self.ikShape_label)

        self.ikShape_combo = flatten_widget.MComboBox(color=[59, 59, 59], border=1)
        self.ikShape_combo.setFont(font)
        self.ikShape_combo.addItems(['FK', 'IK', 'Spline', 'Main'])
        self.ikShape_layout.addWidget(self.ikShape_combo)
        self.addLine()

        ## SecShape
        self.secShape_layout = QHBoxLayout()
        self.secShape_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.secShape_layout)

        self.secShape_label = flatten_widget.MPointLabel(self)
        self.secShape_label.setFont(font)
        self.secShape_label.setText('Sec Shape')
        self.secShape_label.setFixedWidth(140)
        self.secShape_layout.addWidget(self.secShape_label)

        self.secShape_combo = flatten_widget.MComboBox(color=[59, 59, 59], border=1)
        self.secShape_combo.setFont(font)
        self.secShape_combo.addItems(['FKSec', 'IKSec', 'SplineSec', 'MainSec'])
        self.secShape_layout.addWidget(self.secShape_combo)
        self.addLine()

        self.updateWidget()
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
        self.subdivide_spin.valueChanged.connect(self.block.setSubdivide)

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
        subdivide = mc.getAttr(block_joint + '.subdivide')
        self.subdivide_spin.setValue(subdivide)
        ik_shape = mc.getAttr(block_joint + '.ikShape')
        self.ikShape_combo.setCurrentIndex(ik_shape)
        sec_shape = mc.getAttr(block_joint + '.secShape')
        self.secShape_combo.setCurrentIndex(sec_shape)