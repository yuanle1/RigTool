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


class FootBlock(QWidget):
    def __init__(self, parent=None, block=None):
        super(FootBlock, self).__init__(parent)
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



        # Heel
        self.heel_layout = QHBoxLayout()
        self.heel_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.heel_layout)

        self.heel_label = flatten_widget.MPointLabel(self)
        self.heel_label.setFont(font)
        self.heel_label.setText('Heel Pivot')
        self.heel_label.setFixedWidth(140)
        self.heel_layout.addWidget(self.heel_label)

        self.heel_lineEdit = flatten_widget.MLineEdit()
        self.heel_lineEdit.setPlaceholderText('None')
        self.heel_lineEdit.setFont(font)
        self.heel_lineEdit.setObjectName('lineEdit')
        self.heel_layout.addWidget(self.heel_lineEdit)
        self.heel_lineEdit.setStyleSheet('''
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

        self.heel_pick_button = flatten_widget.MFlattentButton(size=18)
        self.heel_pick_button.setObjectName('lineEdit_button')
        self.heel_pick_button.setIcon(maya_utilities.getIcon(ICONS_DIR + 'pick.svg', 18, 18))
        self.heel_pick_button.setIconSize(QSize(18, 18))

        layout = QHBoxLayout()
        self.heel_lineEdit.setLayout(layout)
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.heel_pick_button)
        self.addLine()

        # FootOuter
        self.footOuter_layout = QHBoxLayout()
        self.footOuter_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.footOuter_layout)

        self.footOuter_label = flatten_widget.MPointLabel(self)
        self.footOuter_label.setFont(font)
        self.footOuter_label.setText('Foot Outer Pivot')
        self.footOuter_label.setFixedWidth(140)
        self.footOuter_layout.addWidget(self.footOuter_label)

        self.footOuter_lineEdit = flatten_widget.MLineEdit()
        self.footOuter_lineEdit.setPlaceholderText('None')
        self.footOuter_lineEdit.setFont(font)
        self.footOuter_lineEdit.setObjectName('lineEdit')
        self.footOuter_layout.addWidget(self.footOuter_lineEdit)
        self.footOuter_lineEdit.setStyleSheet('''
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

        self.footOuter_pick_button = flatten_widget.MFlattentButton(size=18)
        self.footOuter_pick_button.setObjectName('lineEdit_button')
        self.footOuter_pick_button.setIcon(maya_utilities.getIcon(ICONS_DIR + 'pick.svg', 18, 18))
        self.footOuter_pick_button.setIconSize(QSize(18, 18))

        layout = QHBoxLayout()
        self.footOuter_lineEdit.setLayout(layout)
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.footOuter_pick_button)
        self.addLine()

        # FootInner
        self.footInner_layout = QHBoxLayout()
        self.footInner_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.footInner_layout)

        self.footInner_label = flatten_widget.MPointLabel(self)
        self.footInner_label.setFont(font)
        self.footInner_label.setText('Foot Inner Pivot')
        self.footInner_label.setFixedWidth(140)
        self.footInner_layout.addWidget(self.footInner_label)

        self.footInner_lineEdit = flatten_widget.MLineEdit()
        self.footInner_lineEdit.setPlaceholderText('None')
        self.footInner_lineEdit.setFont(font)
        self.footInner_lineEdit.setObjectName('lineEdit')
        self.footInner_layout.addWidget(self.footInner_lineEdit)
        self.footInner_lineEdit.setStyleSheet('''
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

        self.footInner_pick_button = flatten_widget.MFlattentButton(size=18)
        self.footInner_pick_button.setObjectName('lineEdit_button')
        self.footInner_pick_button.setIcon(maya_utilities.getIcon(ICONS_DIR + 'pick.svg', 18, 18))
        self.footInner_pick_button.setIconSize(QSize(18, 18))

        layout = QHBoxLayout()
        self.footInner_lineEdit.setLayout(layout)
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.footInner_pick_button)
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
        self.orient_x_combo.currentIndexChanged.connect(
            lambda: self.block.setOrientX(orient_list[self.orient_x_combo.currentIndex()]))
        self.world_x_x_spin.valueChanged.connect(lambda: self.block.setWorldX(
            [self.world_x_x_spin.value(), self.world_x_y_spin.value(), self.world_x_z_spin.value()]))
        self.world_x_y_spin.valueChanged.connect(lambda: self.block.setWorldX(
            [self.world_x_x_spin.value(), self.world_x_y_spin.value(), self.world_x_z_spin.value()]))
        self.world_x_z_spin.valueChanged.connect(lambda: self.block.setWorldX(
            [self.world_x_x_spin.value(), self.world_x_y_spin.value(), self.world_x_z_spin.value()]))
        self.orient_y_combo.currentIndexChanged.connect(
            lambda: self.block.setOrientY(orient_list[self.orient_y_combo.currentIndex()]))
        self.world_y_x_spin.valueChanged.connect(lambda: self.block.setWorldY(
            [self.world_y_x_spin.value(), self.world_y_y_spin.value(), self.world_y_z_spin.value()]))
        self.world_y_y_spin.valueChanged.connect(lambda: self.block.setWorldY(
            [self.world_y_x_spin.value(), self.world_y_y_spin.value(), self.world_y_z_spin.value()]))
        self.world_y_z_spin.valueChanged.connect(lambda: self.block.setWorldY(
            [self.world_y_x_spin.value(), self.world_y_y_spin.value(), self.world_y_z_spin.value()]))
        self.name_lineEdit.textChanged.connect(self.block.setName)
        self.fat_spin.valueChanged.connect(self.block.setFat)
        self.segScaleComp_check.toggled.connect(self.block.setSegScaleComp)
        self.heel_lineEdit.textChanged.connect(self.block.setHeelPivot)
        self.footInner_lineEdit.textChanged.connect(self.block.setFootInnerPivot)
        self.footOuter_lineEdit.textChanged.connect(self.block.setFootOuterPivot)

        self.heel_pick_button.clicked.connect(lambda: self.heel_lineEdit.setText(self.pickPivot()))
        self.footInner_pick_button.clicked.connect(lambda: self.footInner_lineEdit.setText(self.pickPivot()))
        self.footOuter_pick_button.clicked.connect(lambda: self.footOuter_lineEdit.setText(self.pickPivot()))


    def pickPivot(self):
        sel_list = mc.ls(sl=True)
        if sel_list:
            return sel_list[0]
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
        heel_pivot = mc.getAttr(block_joint + '.heelPivot')
        self.heel_lineEdit.setText(heel_pivot)
        footOuter_pivot = mc.getAttr(block_joint + '.footOuterPivot')
        self.footOuter_lineEdit.setText(footOuter_pivot)
        footInner_pivot = mc.getAttr(block_joint + '.footInnerPivot')
        self.footInner_lineEdit.setText(footInner_pivot)