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


class SplineBlock(QWidget):
    def __init__(self, parent=None, block=None):
        super(SplineBlock, self).__init__(parent)
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
        self.secControl_check.setChecked(False)
        self.secControl_layout.addWidget(self.secControl_check)
        self.secControl_layout.addStretch()
        self.addLine()

        ## SplineShape
        self.splineShape_layout = QHBoxLayout()
        self.splineShape_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.splineShape_layout)

        self.splineShape_label = flatten_widget.MPointLabel(self)
        self.splineShape_label.setFont(font)
        self.splineShape_label.setText('Spline Shape')
        self.splineShape_label.setFixedWidth(140)
        self.splineShape_layout.addWidget(self.splineShape_label)

        self.splineShape_combo = flatten_widget.MComboBox(color=[59, 59, 59], border=1)
        self.splineShape_combo.setFont(font)
        self.splineShape_combo.addItems(['FK', 'IK', 'Spline', 'Main'])
        self.splineShape_layout.addWidget(self.splineShape_combo)
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
        self.fat_spin.valueChanged.connect(self.block.setFat)
        self.secControl_check.toggled.connect(self.block.setSecondControl)
        self.splineShape_combo.currentIndexChanged.connect(self.block.setSplineShape)
        self.secShape_combo.currentIndexChanged.connect(self.block.setSecShape)

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
        fat = mc.getAttr(block_joint + '.fat')
        self.fat_spin.setValue(fat)
        sec_control = mc.getAttr(block_joint + '.secControl')
        self.secControl_check.setChecked(sec_control)
        spline_shape = mc.getAttr(block_joint + '.splineShape')
        self.splineShape_combo.setCurrentIndex(spline_shape)
        sec_shape = mc.getAttr(block_joint + '.secShape')
        self.secShape_combo.setCurrentIndex(sec_shape)