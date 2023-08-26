#!/usr/bin/env python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import modules.maya_utilities as maya_utilities
# reload(maya_utilities)
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import maya_widgets.control_panel as control_panel
# reload(control_panel)

class CurveScale(QWidget):
    def __init__(self, parent=None):
        super(CurveScale, self).__init__(parent)
        self.setupUI()
        self.connect()
    def setupUI(self):
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.curve_sx_panel = control_panel.MControlPanel(hue=200, size=50)
        self.main_layout.addWidget(self.curve_sx_panel)
        self.curve_sy_panel = control_panel.MControlPanel(hue=200, size=50)
        self.main_layout.addWidget(self.curve_sy_panel)
        self.curve_sz_panel = control_panel.MControlPanel(hue=200, size=50)
        self.main_layout.addWidget(self.curve_sz_panel)
        self.curve_s_panel = control_panel.MControlPanel(hue=200, size=65)
        self.main_layout.addWidget(self.curve_s_panel)

    def connect(self):
        self.curve_sx_panel.valueChanged.connect(lambda: self.scale(0, self.curve_sx_panel.getFactor()))
        self.curve_sy_panel.valueChanged.connect(lambda: self.scale(1, self.curve_sy_panel.getFactor()))
        self.curve_sz_panel.valueChanged.connect(lambda: self.scale(2, self.curve_sz_panel.getFactor()))
        self.curve_s_panel.valueChanged.connect(lambda: self.scale(3, self.curve_s_panel.getFactor()))


    def scale(self, axis, factor):
        sel_list = mc.ls(sl=True)
        if sel_list:
            for sel in sel_list:
                shape = mc.listRelatives(sel, shapes=True)
                if shape:
                    curve = sel
                    points = mc.ls(curve + '.cv[*]', flatten=True)
                    mc.select(points)
                    if factor > 0:
                        factor = 1.1
                    else:
                        factor = 1 / 1.1
                    if axis == 0:
                        mc.scale(factor, 1, 1, r=True, os=True)
                    elif axis == 1:
                        mc.scale(1, factor, 1, r=True, os=True)
                    elif axis == 2:
                        mc.scale(1, 1,  factor, r=True, os=True)
                    elif axis == 3:
                        mc.scale(factor, factor, factor, r=True, os=True)
        mc.select(sel_list)



class CurveRotate(QWidget):
    def __init__(self, parent=None):
        super(CurveRotate, self).__init__(parent)
        self.setMaximumHeight(75)
        self.setupUI()
        self.connect()

    def setupUI(self):
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.curve_rx_panel = control_panel.MControlPanel(hue=60, size=50)
        self.main_layout.addWidget(self.curve_rx_panel)
        self.curve_ry_panel = control_panel.MControlPanel(hue=60, size=50)
        self.main_layout.addWidget(self.curve_ry_panel)
        self.curve_rz_panel = control_panel.MControlPanel(hue=60, size=50)
        self.main_layout.addWidget(self.curve_rz_panel)
        self.curve_r_panel = control_panel.MControlPanel(hue=60, size=65)
        self.main_layout.addWidget(self.curve_r_panel)

    def connect(self):
        self.curve_rx_panel.valueChanged.connect(lambda: self.rotate(0, self.curve_rx_panel.getFactor()))
        self.curve_ry_panel.valueChanged.connect(lambda: self.rotate(1, self.curve_ry_panel.getFactor()))
        self.curve_rz_panel.valueChanged.connect(lambda: self.rotate(2, self.curve_rz_panel.getFactor()))
        self.curve_r_panel.valueChanged.connect(lambda: self.rotate(3, self.curve_r_panel.getFactor()))


    def rotate(self, axis, factor):
        sel_list = mc.ls(sl=True)
        if sel_list:
            for sel in sel_list:
                shape = mc.listRelatives(sel, shapes=True)
                if shape:
                    curve = sel
                    points = mc.ls(curve + '.cv[*]', flatten=True)
                    mc.select(points)
                    # orientAxes = mc.xform(sel, q=True, rotation=True)
                    if axis == 0:
                        mc.rotate(45 * factor, 0, 0, r=True, os=True)
                    elif axis == 1:
                        mc.rotate(0, 45 * factor, 0, r=True, os=True)
                    elif axis == 2:
                        mc.rotate(0, 0, 45 * factor, r=True, os=True)
                    elif axis == 3:
                        mc.rotate(45 * factor, 45 * factor, 45 * factor, r=True, os=True)
        mc.select(sel_list)
class CurveTranslate(QWidget):
    def __init__(self, parent=None):
        super(CurveTranslate, self).__init__(parent)
        self.setupUI()
        self.connect()
    def setupUI(self):
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.curve_tx_panel = control_panel.MControlPanel(hue=0, size=50)
        self.main_layout.addWidget(self.curve_tx_panel)
        self.curve_ty_panel = control_panel.MControlPanel(hue=0, size=50)
        self.main_layout.addWidget(self.curve_ty_panel)
        self.curve_tz_panel = control_panel.MControlPanel(hue=0, size=50)
        self.main_layout.addWidget(self.curve_tz_panel)
        self.curve_t_panel = control_panel.MControlPanel(hue=0, size=65)
        self.main_layout.addWidget(self.curve_t_panel)

    def connect(self):
        self.curve_tx_panel.valueChanged.connect(lambda: self.translate(0, self.curve_tx_panel.getFactor()))
        self.curve_ty_panel.valueChanged.connect(lambda: self.translate(1, self.curve_ty_panel.getFactor()))
        self.curve_tz_panel.valueChanged.connect(lambda: self.translate(2, self.curve_tz_panel.getFactor()))
        self.curve_t_panel.valueChanged.connect(lambda: self.translate(3, self.curve_t_panel.getFactor()))

    def translate(self, axis, factor):
        sel_list = mc.ls(sl=True)
        if sel_list:
            for sel in sel_list:
                shape = mc.listRelatives(sel, shapes=True)
                if shape:
                    curve = sel
                    points = mc.ls(curve + '.cv[*]', flatten=True)
                    mc.select(points)
                    # orientAxes = mc.xform(sel, q=True, rotation=True)
                    if axis == 0:
                        mc.move(0.5 * factor, 0, 0, r=True, os=True)
                    elif axis == 1:
                        mc.move(0, 0.5 * factor, 0, r=True, os=True)
                    elif axis == 2:
                        mc.move(0, 0, 0.5 * factor, r=True, os=True)
                    elif axis == 3:
                        mc.move(0.5 * factor, 0.5 * factor, 0.5 * factor, r=True, os=True)
        mc.select(sel_list)