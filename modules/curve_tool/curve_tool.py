#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import maya.cmds as mc
import maya.mel as mel
from shiboken2 import wrapInstance
from maya import OpenMayaUI as omui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from maya_widgets.tab_widget import *
import curve_creator
# reload(curve_creator)
import curve_transmit
# reload(curve_transmit)
import curve_transform
# reload(curve_transform)
import curve_color
# reload(curve_color)
import modules.maya_utilities as maya_utilities
# reload(maya_utilities)

class CurveToolWin(QMainWindow):
    def __init__(self, parent=maya_utilities.maya_main_window()):
        super(CurveToolWin, self).__init__(parent)
        self.setupUI()
        self.resize(340, 500)
    def setupUI(self):
        self.setStyleSheet('''background-color:rgb(50, 50, 50);''')

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(3, 5, 5, 5)

        self.shape_tab = MTabWidget()
        self.main_layout.addWidget(self.shape_tab)

        self.curve_creator_widget = curve_creator.CurveCreator()
        self.curve_transmit_widget = curve_transmit.CurveTransmit()
        self.shape_tab.addTab(self.curve_creator_widget, 'Create')
        self.shape_tab.addTab(self.curve_transmit_widget, 'Transmit')
        self.shape_tab.setCurrentIndex(0)
        self.shape_tab.addStretch()

        self.transform_tab = MTabWidget()
        self.main_layout.addWidget(self.transform_tab)

        self.curve_s_widget = curve_transform.CurveScale()
        self.curve_r_widget = curve_transform.CurveRotate()
        self.curve_t_widget = curve_transform.CurveTranslate()

        self.transform_tab.addTab(self.curve_s_widget, 'Scale')
        self.transform_tab.addTab(self.curve_r_widget, 'Rotate')
        self.transform_tab.addTab(self.curve_t_widget, 'Translate')
        self.transform_tab.setCurrentIndex(0)
        self.transform_tab.addStretch()

        self.color_tab = MTabWidget()
        self.main_layout.addWidget(self.color_tab)

        self.curve_color_widget = curve_color.CurveColor()
        self.color_tab.addTab(self.curve_color_widget, 'RGB')
        self.color_tab.setCurrentIndex(0)
        self.color_tab.addStretch()













