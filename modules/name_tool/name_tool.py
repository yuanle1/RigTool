#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import maya.cmds as mc
import maya.mel as mel
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from modules import maya_utilities as maya_utilities
import name_add
import name_replace
import name_rename
# reload(maya_utilities)
# reload(name_add)
# reload(name_replace)
# # reload(name_rename)

class NameToolWin(QMainWindow):
    def __init__(self, parent=maya_utilities.maya_main_window()):
        super(NameToolWin, self).__init__(parent)
        self.setupUI()
        self.resize(400, 200)
        self.installEventFilter(self)

    def setupUI(self):
        self.setObjectName('RenameToolWin')
        self.setStyleSheet('''
                                #RenameToolWin
                                {
                                background-color:rgb(34, 34, 34);
                                }
                            ''')

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(4, 5, 4, 5)

        self.name_add_widget = name_add.NameAdd()
        self.main_layout.addWidget(self.name_add_widget)

        self.name_replace_widget = name_replace.NameReplace()
        self.main_layout.addWidget(self.name_replace_widget)

        self.name_rename_widget = name_rename.NameRename()
        self.main_layout.addWidget(self.name_rename_widget)


        self.main_layout.addStretch()























