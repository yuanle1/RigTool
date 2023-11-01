#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import modules.maya_utilities as maya_utilities
reload(maya_utilities)

import maya.cmds as mc
import maya_widgets.switch_button as switch_button
class BlockInfo(QWidget):
    def __init__(self, parent=None):
        super(BlockInfo, self).__init__(parent)

        self.setupUI()
        self.connect()

    def setupUI(self):
        font = maya_utilities.font
        font.setPointSize(8)

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.block_display_frame = QFrame()
        self.block_display_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.block_display_frame.setFixedHeight(55)
        self.block_display_frame.setMinimumWidth(100)
        self.main_layout.addWidget(self.block_display_frame)
        self.block_display_frame.setStyleSheet('''
                                                        background-color:rgb(54, 54, 54);
                                                        border-radius: 5px;
                                                        ''')

        self.block_display_grid = QGridLayout()
        self.block_display_grid.setContentsMargins(5, 5, 5, 20)
        self.block_display_frame.setLayout(self.block_display_grid)

        self.block_size_label = QLabel()
        self.block_size_label.setFont(font)
        self.block_size_label.setText('Joint Size:')
        self.block_size_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.block_display_grid.addWidget(self.block_size_label, 0, 0)

        self.block_size_slider = QSlider()
        self.block_size_slider.setMinimum(1)
        self.block_size_slider.setStyleSheet('''
                                                        QSlider:groove:horizontal
                                                        {
                                                            height:2px;
                                                            background-color:rgb(80, 80, 80);
                                                        }

                                                        QSlider::handle:horizontal
                                                        {
                                                            width:10px;
                                                            margin-top:-4px;
                                                            margin-bottom:-4px;
                                                            border-radius:5px;
                                                            background:rgb(160, 160, 160)

                                                        }
                                                        ''')
        self.block_size_slider.setOrientation(Qt.Horizontal)
        self.block_display_grid.addWidget(self.block_size_slider, 0, 1)

        self.block_axis_label = QLabel()
        self.block_axis_label.setFont(font)
        self.block_axis_label.setText('Joint Axis:')
        self.block_axis_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.block_display_grid.addWidget(self.block_axis_label, 1, 0)

        self.block_axis_check = switch_button.MSwitch()
        self.block_display_grid.addWidget(self.block_axis_check, 1, 1)
        # self.block_display_grid.setColumnStretch(self.block_display_grid.columnCount(), 1)
        # self.block_display_grid.setRowStretch(self.block_display_grid.rowCount(), 1)
        # self.block_display_grid.setColumnStretch(1, 1)

        self.block_info_frame = QFrame()
        self.block_info_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.block_info_frame.setFixedHeight(55)
        self.block_info_frame.setMinimumWidth(100)
        self.main_layout.addWidget(self.block_info_frame)
        self.block_info_frame.setStyleSheet('''
                                                                background-color:rgb(54, 54, 54);
                                                                border-radius: 5px;
                                                                ''')
        self.block_info_grid = QGridLayout()
        self.block_info_grid.setContentsMargins(6, 5, 2, 5)
        self.block_info_frame.setLayout(self.block_info_grid)

        self.block_label = QLabel()
        self.block_label.setFont(font)
        self.block_label.setText('Block:')
        self.block_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.block_info_grid.addWidget(self.block_label, 0, 0)

        self.block_num_label = QLabel()
        self.block_num_label.setFont(font)
        self.block_num_label.setText('   38')
        self.block_info_grid.addWidget(self.block_num_label, 0, 1)

        self.joint_label = QLabel()
        self.joint_label.setFont(font)
        self.joint_label.setText('Joint:')
        self.joint_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.block_info_grid.addWidget(self.joint_label, 1, 0)

        self.joint_num_label = QLabel()
        self.joint_num_label.setFont(font)
        self.joint_num_label.setText('   90')
        self.block_info_grid.addWidget(self.joint_num_label, 1, 1)

        self.effective_label = QLabel()
        self.effective_label.setFont(font)
        self.effective_label.setText('Joint(Effective):')
        self.effective_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.block_info_grid.addWidget(self.effective_label, 2, 0)

        self.effective_num_label = QLabel()
        self.effective_num_label.setFont(font)
        self.effective_num_label.setText('   73')
        self.block_info_grid.addWidget(self.effective_num_label, 2, 1)

    def connect(self):
        self.block_size_slider.valueChanged.connect(self.block_size_value_changed)
        self.block_axis_check.toggled.connect(self.block_axis_display)

    def block_size_value_changed(self):
        mc.jointDisplayScale(self.block_size_slider.value() * 0.01)

    def block_axis_display(self):
        with maya_utilities.Undoable():
            if not mc.objExists('Block'):
                return
            blocks = mc.listRelatives('Block', ad=True, type='joint') or []
            for block in blocks:
                mc.setAttr(block + '.displayLocalAxis', not self.block_axis_check.isChecked())


    def updateInfo(self, blocks):
        if not mc.objExists('Block'):
            return
        mc.select('Block', hi=True)
        self.block_num_label.setText('   {}'.format(len(mc.ls(sl=True, type='joint'))))
        joint_num = 0
        effective_num = 0
        for block in blocks:
            joint_num += 1
            joint_num += block.getSubdivide()
            if block.getMirror():
                joint_num += 1
                joint_num += block.getSubdivide()
            if block.getFunction() != 'End':
                effective_num += 1
                effective_num += block.getSubdivide()
                if block.getMirror():
                    effective_num += 1
                    effective_num += block.getSubdivide()
        self.joint_num_label.setText('   {}'.format(joint_num))
        self.effective_num_label.setText('   {}'.format(effective_num))
        mc.select(clear=True)