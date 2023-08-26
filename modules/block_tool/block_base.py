#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import timeit
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
            'None': 'None.svg', 'Hand': 'Hand.svg', 'Foot': 'Foot.svg'}
SIZE_DIC = {'Spline': [26, 26], 'IK': [26, 26], 'FK': [26, 26], 'End': [26, 26], 'Child': [26, 26],
            'None': [30, 30], 'Hand': [26, 26], 'Foot': [26, 2]}
SIDE_LIST = ['M', 'L', 'R']

class BlockBase(QWidget):
    def __init__(self, parent=None):
        super(BlockBase, self).__init__(parent)
        self.block_widget = None
        self.setupUI()

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

    def setFunction(self, function):
        self.block_label.setText('Function: {}'.format(function))

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




