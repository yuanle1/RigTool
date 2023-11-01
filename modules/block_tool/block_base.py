#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import maya.cmds as mc

import modules.maya_utilities as maya_utilities
import maya_widgets.flatten_widget as flatten_widget
import maya_widgets.switch_button as switch_button
reload(switch_button)
import block_utilities
reload(block_utilities)
import fk_widget
import ik_widget
import spline_widget
import end_widget
import child_widget
import hand_widget
import foot_widget

reload(fk_widget)
reload(ik_widget)
reload(spline_widget)
reload(end_widget)
reload(child_widget)
reload(hand_widget)
reload(foot_widget)

ICON_DIC = {'Spline': 'Spline.svg', 'IK': 'IK.svg', 'FK': 'FK.svg', 'End': 'End.png', 'Child': 'Child.svg',
            'None': 'None.svg', 'Aim': 'Aim.svg', 'Hand': 'Hand.svg', 'Foot': 'Foot.svg'}
SIZE_DIC = {'Spline': [26, 26], 'IK': [26, 26], 'FK': [26, 26], 'End': [26, 26], 'Child': [26, 26],
            'None': [30, 30], 'Aim': [26, 26], 'Hand': [26, 26], 'Foot': [26, 2]}
SIDE_LIST = ['M', 'L', 'R']

class BlockBase(QWidget):
    def __init__(self, parent=None):
        super(BlockBase, self).__init__(parent)
        self.block_widget = None
        self.setupUI()
        self.connect()

    def setupUI(self):
        font = maya_utilities.font
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 10, 15, 5)
        self.main_layout.setSpacing(7)

        self.title_layout = QHBoxLayout()
        self.main_layout.addLayout(self.title_layout)

        self.module_button = QPushButton()
        self.module_button.setObjectName('module_button')
        self.module_button.setFixedSize(QSize(45, 45))
        self.title_layout.addWidget(self.module_button)

        icon = ICON_DIC['None']
        icon_size = SIZE_DIC['None']
        icon = maya_utilities.getIcon('D:\\Project\\RigTools\\Resources\\icons\\blocks\\{}'.format(icon), icon_size[0],
                                      icon_size[1])
        self.module_button.setIcon(icon)
        self.module_button.setIconSize(QSize(icon_size[0], icon_size[1]))
        self.module_button.setStyleSheet('''
                                            #module_button
                                            {
                                                background-color:rgb(38, 38, 38);
                                                border:2px solid rgb(50, 50, 50);
                                                border-radius:8px
                                            }
                                            #module_button:hover
                                            {
                                                background-color:rgb(66, 66, 66);
                                            }
                                            #module_button:pressed
                                            {
                                                background-color:rgb(62, 62, 62);
                                            }
                                            ''')


        self.block_layout = QVBoxLayout()
        self.title_layout.addLayout(self.block_layout)

        self.block_label = QLabel()
        font.setPointSize(10)
        self.block_label.setFont(font)
        self.block_label.setText('None')
        self.block_label.setStyleSheet('''
                                            border-bottom:1px solid rgb(60, 60, 60);
                                            padding-bottom:2px
                                        ''')
        self.block_layout.addWidget(self.block_label)

        self.base_layout = QHBoxLayout()
        self.base_layout.setContentsMargins(4, 0, 0, 0)
        self.block_layout.addLayout(self.base_layout)

        self.function_label = QLabel()
        font.setPointSize(8)
        self.function_label.setFont(font)
        self.function_label.setText('Function:None')
        self.base_layout.addWidget(self.function_label)
        self.base_layout.addStretch()

        self.side_label = QLabel()
        self.side_label.setFont(font)
        self.side_label.setText('Side :')
        self.base_layout.addWidget(self.side_label)

        self.side_cmobo = flatten_widget.MComboBox()
        self.side_cmobo.setFixedSize(36, 14)
        self.side_cmobo.setFont(font)
        self.side_cmobo.addItems(['M', 'L', 'R'])
        self.side_cmobo.setCurrentIndex(-1)
        self.base_layout.addWidget(self.side_cmobo)
        self.base_layout.addStretch()

        self.mirror_label = QLabel()
        self.mirror_label.setFont(font)
        self.mirror_label.setText('Mirror :')
        self.base_layout.addWidget(self.mirror_label)

        self.mirror_check = switch_button.MSwitch()
        self.base_layout.addWidget(self.mirror_check)
        self.base_layout.addStretch()


        self.main_menu = QMenu(self)
        self.main_menu.setFont(font)
        self.main_menu.setFixedWidth(70)
        self.main_menu.setContentsMargins(1, 1, 1, 1)
        self.main_menu.setStyleSheet('''
                                          #main_menu
                                          {
                                              border: 0px;
                                              border-radius: 0px;
                                              color:rgb(200,200,200);
                                              background-color:rgb(66, 66, 66)
                                          }
                                          #main_menu:item
                                          {
                                              border: 0px;
                                              padding:0px 25px;
                                              margin:1px 1px 1px 1px;                              
                                              width:20px;
                                              height:20px;
                                              background-color:rgb(76,76,76);
                                          }
                                          #main_menu:item:selected
                                          {
                                                background-color:rgb(98,98,98);
                                                
                                          }
                                          #main_menu:icon
                                          {
                                               padding-left: 10px;

                                          }
                                          #main_menu:separator 
                                          {
                                            background-color:rgb(100, 100, 100);
                                            height:2px;
                                            margin:1px 2px 1px 2px;
                                          }
                                      ''')
        self.main_menu.setObjectName('main_menu')

        fk_icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'blocks/' + ICON_DIC['FK'], 14, 14)
        self.fk_action = QAction(fk_icon, 'FK', self)
        self.fk_action.setFont(font)
        self.main_menu.addAction(self.fk_action)

        ik_icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'blocks/' + ICON_DIC['IK'], 14, 14)
        self.ik_action = QAction(ik_icon, 'IK', self)
        self.ik_action.setFont(font)
        self.main_menu.addAction(self.ik_action)

        spline_icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'blocks/' + ICON_DIC['Spline'], 14, 14)
        self.spline_action = QAction(spline_icon, 'Spline', self)
        self.spline_action.setFont(font)
        self.main_menu.addAction(self.spline_action)

        self.main_menu.addSeparator()

        child_icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'blocks/' + ICON_DIC['Child'], 14, 14)
        self.child_action = QAction(child_icon, 'Child', self)
        self.child_action.setFont(font)
        self.main_menu.addAction(self.child_action)

        end_icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'blocks/' + ICON_DIC['End'], 14, 14)
        self.end_action = QAction(end_icon, 'End', self)
        self.end_action.setFont(font)
        self.main_menu.addAction(self.end_action)

        self.main_menu.addSeparator()

        aim_icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'blocks/' + ICON_DIC['Aim'], 14, 14)
        self.aim_action = QAction(aim_icon, 'Aim', self)
        self.aim_action.setFont(font)
        self.main_menu.addAction(self.aim_action)

        hand_icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'blocks/' + ICON_DIC['Hand'], 14, 14)
        self.hand_action = QAction(hand_icon, 'Hand', self)
        self.hand_action.setFont(font)
        self.main_menu.addAction(self.hand_action)

        foot_icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'blocks/' + ICON_DIC['Foot'], 14, 14)
        self.foot_action = QAction(foot_icon, 'Foot', self)
        self.foot_action.setFont(font)
        self.main_menu.addAction(self.foot_action)

    def connect(self):
        self.module_button.clicked.connect(self.createMenu)



    def createMenu(self):
        self.main_menu.exec_(self.mapToGlobal(QPoint(self.module_button.x(), self.module_button.y() + self.module_button.height())))

    def setCurrentBlockMirror(self, block, mirror):
        if block:
            block.setMirror(mirror)

    def setCurrentBlockSide(self, block, side):
        if block:
            block.setSide(side)


    def setFunction(self, function):
        self.function_label.setText('Function: {}'.format(function))

    def setJoint(self, joint):
        self.block_label.setText(joint)

    def setMirror(self, mirror):
        self.mirror_check.setChecked(mirror)

    def setSide(self, side):
        self.side_cmobo.setCurrentIndex(SIDE_LIST.index(side))

    def setModules(self, function):
        icon = ICON_DIC[function]
        icon_size = SIZE_DIC[function]
        icon = maya_utilities.getIcon('D:\\Project\\RigTools\\Resources\\icons\\blocks\\{}'.format(icon), icon_size[0],
                                      icon_size[1])
        self.module_button.setIcon(icon)
        self.module_button.setIconSize(QSize(icon_size[0], icon_size[1]))

    def setBlockFucntion(self, block, function, tree):
        block_utilities.clearBlockAttr(block)
        block_joint = block.getJoint()
        mc.setAttr(block_joint + '.otherType', function, type='string')
        # block_utilities.ensureBlockAttrs(block_joint)
        # blocks = tree.getAllBlocks()
        # index = blocks.index(block)
        # tree.currentItem().block = block_utilities.blockInstance(block_joint)
        # blocks[index] = tree.currentItem().block

