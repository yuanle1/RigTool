#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from maya_widgets import flatten_widget as flatten_widget
from maya_widgets import round_widget as round_widget
from modules import maya_utilities as maya_utilities

import maya.cmds as mc

# reload(flatten_widget)
# reload(round_widget)
# reload(maya_utilities)

class NameAdd(round_widget.MRoundWidget):
    def __init__(self, parent=None):
        super(NameAdd, self).__init__(parent)

        self.setupUI()
        self.connect()

    def setupUI(self):
        font = maya_utilities.font
        title_font = maya_utilities.getFont()
        # font.setPointSize(8)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(6, 4, 14, 3)
        self.main_layout.setSpacing(4)
        self.setLayout(self.main_layout)

        self.title_layout = QHBoxLayout()
        self.main_layout.addLayout(self.title_layout)

        self.title_label = QLabel()
        self.title_label.setFixedWidth(26)
        self.title_label.setText('Add')
        title_font.setPointSize(10)
        title_font.setStyleStrategy(QFont.PreferAntialias)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet('''
                                            color:#a9a084;
                                        ''')

        self.title_layout.addWidget(self.title_label)

        self.title_line = QFrame()
        self.title_line.setFrameShape(QFrame.HLine)
        self.title_layout.addWidget(self.title_line)
        self.title_line.setFixedHeight(2)
        self.title_line.setStyleSheet('''
                                            background-color: #a9a084;
                                      ''')

        self.prefix_layout = QHBoxLayout()
        self.prefix_layout.setContentsMargins(6, 0, 0, 0)
        self.main_layout.addLayout(self.prefix_layout)

        self.prefix_label = QLabel()
        self.prefix_label.setText('Prefix :')
        font.setPointSize(8)
        self.prefix_label.setFont(font)
        self.prefix_label.setMinimumWidth(46)
        self.prefix_layout.addWidget(self.prefix_label)


        self.prefix_lineEdit = flatten_widget.MLineEdit()
        self.prefix_layout.addWidget(self.prefix_lineEdit)

        self.subfix_layout = QHBoxLayout()
        self.subfix_layout.setContentsMargins(6, 0, 0, 0)
        self.main_layout.addLayout(self.subfix_layout)

        self.subfix_label = QLabel()
        self.subfix_label.setText('Subfix :')
        font.setPointSize(8)
        self.subfix_label.setFont(font)
        self.subfix_label.setMinimumWidth(46)
        self.subfix_layout.addWidget(self.subfix_label)

        self.subfix_lineEdit = flatten_widget.MLineEdit()
        self.subfix_layout.addWidget(self.subfix_lineEdit)

        self.check_layout = QHBoxLayout()
        self.main_layout.addLayout(self.check_layout)
        self.check_layout.setContentsMargins(60, 5, 5, 0)

        self.selected_check = flatten_widget.MFlattentCheck()
        self.selected_check.setText('Selected')
        self.selected_check.setChecked(True)
        self.check_layout.addWidget(self.selected_check)

        self.hierarchy_check = flatten_widget.MFlattentCheck()
        self.hierarchy_check.setText('Hierarchy')
        self.check_layout.addWidget(self.hierarchy_check)

        self.all_check = flatten_widget.MFlattentCheck()
        self.all_check.setText('All')
        self.check_layout.addWidget(self.all_check)

        self.button_layout = QHBoxLayout()
        self.button_layout.setContentsMargins(8, 0, 0, 5)
        self.main_layout.addLayout(self.button_layout)

        self.add_button = QPushButton()
        self.add_button.setText('Add')
        font.setPointSize(8)
        self.add_button.setFont(font)
        self.add_button.setObjectName('add_button')
        self.add_button.setMinimumHeight(25)
        self.button_layout.addWidget(self.add_button)
        self.add_button.setStyleSheet('''
                                        #add_button
                                        {
                                            color:rgb(200, 200, 200);
                                            background-color:rgb(73, 73, 73);
                                            border-radius:3px;
                                            border:2px solid rgb(80, 80, 80);
                                        }
                                        #add_button:hover
                                        {
                                            color:rgb(200, 200, 200);
                                            background-color:rgb(85,94,96);
                                            border-radius:3px;
                                            border:2px solid rgb(80, 80, 80);
                                        }
                                        #add_button:pressed
                                        {
                                            color:rgb(200, 200, 200);
                                            background-color:rgb(85,102,114);
                                            border-radius:3px;
                                            border:2px solid rgb(80, 80, 80);
                                        }
                                        ''')
        self.main_layout.addStretch()

    def connect(self):
        self.add_button.clicked.connect(self.add)

    def add(self):
        with maya_utilities.Undoable():
            prefix_text = self.prefix_lineEdit.text()
            subfix_text = self.subfix_lineEdit.text()
            ori_list = mc.ls(sl=True, uuid=True)
            sel_list = []
            if self.selected_check.isChecked():
                sel_list = mc.ls(sl=True, transforms=True)
            elif self.hierarchy_check.isChecked():
                mc.select(hi=True)
                sel_list = mc.ls(sl=True, transforms=True)
            elif self.all_check.isChecked():
                mc.select(allDagObjects=True, hi=True)
                sel_list = mc.ls(sl=True, transforms=True)

            uuid_list = mc.ls(sel_list, uuid=True)

            for uuid in uuid_list:
                long_name = mc.ls(uuid, long=True)[0]
                short_name = long_name.split('|')[-1]
                mc.select(long_name)
                mc.rename(prefix_text + short_name + subfix_text)
            mc.select(clear=True)

            # for uuid in uuid_list:
            #     mc.select(mc.ls(uuid)[0], add=True)
            for uuid in ori_list:
                mc.select(mc.ls(uuid)[0], add=True)
