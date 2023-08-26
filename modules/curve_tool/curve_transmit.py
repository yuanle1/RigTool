#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import modules.maya_utilities as maya_utilities
# reload(maya_utilities)
from maya_widgets.flatten_widget import *


class CurveTransmit(QWidget):
    def __init__(self, parent=None):
        super(CurveTransmit, self).__init__(parent)
        self.setMinimumHeight(150)
        self.setMaximumHeight(150)
        self.setMinimumWidth(330)
        self.setupUI()


    def setupUI(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.button_layout = QHBoxLayout()
        self.button_layout.setContentsMargins(8, 0, 8, 0)
        self.button_layout.setSpacing(2)
        self.main_layout.addLayout(self.button_layout)

        self.add_button = MFlattentButton(size=20)
        self.add_button.setIcon(maya_utilities.getIcon('D:\Project\RigTools\Resources\icons\\add.svg', 16, 16))
        self.add_button.setIconSize(QSize(16, 16))
        self.button_layout.addWidget(self.add_button)

        self.replace_button = MFlattentButton(size=20)
        self.replace_button.setIcon(maya_utilities.getIcon('D:\Project\RigTools\Resources\icons\\replace.svg', 16, 16))
        self.replace_button.setIconSize(QSize(16, 16))
        self.button_layout.addWidget(self.replace_button)

        self.share_button = MFlattentButton(size=20)
        self.share_button.setIcon(maya_utilities.getIcon('D:\Project\RigTools\Resources\icons\\share.svg', 16, 16))
        self.share_button.setIconSize(QSize(16, 16))
        self.button_layout.addWidget(self.share_button)

        self.delete_button = MFlattentButton(size=20)
        self.delete_button.setIcon(maya_utilities.getIcon('D:\Project\RigTools\Resources\icons\\delete.svg', 16, 16))
        self.delete_button.setIconSize(QSize(16, 16))
        self.button_layout.addWidget(self.delete_button)
        self.button_layout.addStretch()


        self.side1_layout = QHBoxLayout()
        self.side1_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.side1_layout)

        self.side1_label = QLabel()
        self.side1_label.setText('Side 1:    ')
        self.side1_layout.addWidget(self.side1_label)

        self.side1_lineEdit = QLineEdit()
        self.side1_lineEdit.setObjectName('side1_lineEdit')
        self.side1_lineEdit.setStyleSheet('''
                                            #side1_lineEdit 
                                            {
                                                border:1px solid;
                                                border-color:rgb(80, 80, 80);
                                                border-radius:1px;
                                            }
                                            ''')
        self.side1_layout.addWidget(self.side1_lineEdit)

        self.side2_layout = QHBoxLayout()
        self.side2_layout.setContentsMargins(8, 0, 0, 0)
        self.main_layout.addLayout(self.side2_layout)

        self.side2_label = QLabel()
        self.side2_label.setText('Side 2:    ')
        self.side2_layout.addWidget(self.side2_label)

        self.side2_lineEdit = QLineEdit()
        self.side2_lineEdit.setObjectName('side2_lineEdit')
        self.side2_lineEdit.setStyleSheet('''
                                            #side2_lineEdit
                                            {
                                                border:1px solid;
                                                border-color:rgb(80, 80, 80);
                                                border-radius:1px;
                                            }
                                            ''')
        self.side2_layout.addWidget(self.side2_lineEdit)

        self.grid_layout = QGridLayout()
        self.grid_layout.setContentsMargins(8, 5, 5, 5)
        self.grid_layout.setVerticalSpacing(5)
        self.main_layout.addLayout(self.grid_layout)

        # across

        self.across_buttonGroup = QButtonGroup()

        self.across_label = QLabel()
        self.across_label.setText('Across:')
        self.across_label.setMinimumWidth(55)
        self.across_label.setMaximumWidth(55)
        self.grid_layout.addWidget(self.across_label, 0, 0)

        self.xy_radio = MFlattentCheck()
        self.xy_radio.setText('XY')
        self.across_buttonGroup.addButton(self.xy_radio)
        self.grid_layout.addWidget(self.xy_radio, 0, 1)

        self.yz_radio = MFlattentCheck()
        self.yz_radio.setText('YZ')

        self.across_buttonGroup.addButton(self.yz_radio)
        self.grid_layout.addWidget(self.yz_radio, 0, 2)
        self.yz_radio.setChecked(True)

        self.xz_radio = MFlattentCheck()
        self.xz_radio.setText('XZ')
        self.across_buttonGroup.addButton(self.xz_radio)
        self.grid_layout.addWidget(self.xz_radio, 0, 3)

        # space
        self.space_buttonGroup = QButtonGroup()

        self.space_label = QLabel()
        self.space_label.setText('Space:')
        self.space_label.setMinimumWidth(55)
        self.space_label.setMaximumWidth(55)
        self.grid_layout.addWidget(self.space_label, 1, 0)

        self.ws_radio = MFlattentCheck()
        self.ws_radio.setChecked(True)
        self.ws_radio.setText('World')
        self.grid_layout.addWidget(self.ws_radio, 1, 1)


        self.os_radio = MFlattentCheck()
        self.os_radio.setText('Object')
        self.grid_layout.addWidget(self.os_radio, 1, 2)

        self.mirror_button = QPushButton()
        self.mirror_button.setText('Mirror')

        self.hsv_layout = QVBoxLayout()
        self.main_layout.addLayout(self.hsv_layout)

        self.hsv_layout.addWidget(self.mirror_button)

