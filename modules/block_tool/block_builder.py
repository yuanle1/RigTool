#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import maya.cmds as mc

import modules.maya_utilities as maya_utilities
import block_utilities

import maya_widgets.flatten_widget as flatten_widget
import maya_widgets.switch_button as switch_button
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
        self.main_root_layout.addLayout(self.main_control_grid)

        self.name_label = QLabel()
        self.name_label.setFont(font)
        self.name_label.setText('Name:')
        self.name_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
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
        self.main_count_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
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
        self.root_control_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.root_control_grid.addWidget(self.root_control_label, 0, 0)

        self.root_control_check = switch_button.MSwitch()
        self.root_control_check.setChecked(True)
        self.root_control_grid.addWidget(self.root_control_check, 0, 1)

        self.gravity_control_label = QLabel()
        self.gravity_control_label.setFont(font)
        self.gravity_control_label.setText('Gravity Control:')
        self.gravity_control_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
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
    def connect(self):
        pass


    def addShadow(self, widget):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 0)
        shadow.setBlurRadius(5)
        shadow.setColor(QColor(40, 40, 40))
        widget.setGraphicsEffect(shadow)

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
        self.setIcon(maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/build/{}.svg'.format(self.icon), 22, 22))
        self.setIconSize(QSize(22, 22))
        self.setFixedSize(QSize(30, 30))

    def enterEvent(self, event):
        self.setIcon(maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/build/{}.svg'.format(self.icon), 24, 24))
        self.setIconSize(QSize(24, 24))

    def leaveEvent(self, event):
        self.setIcon(maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/build/{}.svg'.format(self.icon), 22, 22))
        self.setIconSize(QSize(22, 22))

