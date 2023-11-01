#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import maya.cmds as mc
import maya.mel as mel
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import modules.maya_utilities as maya_utilities
from modules.maya_utilities import *
from maya_widgets.flatten_widget import *

# 一行放多少个button
CURVE_ROW_NUM = 8
IMAGE_PATH = 'D:\Project\RigTools\Resources\icons\ctrls'
CURVE_PATH = 'D:\Project\RigTools\Resources\data\curve_data.json'


class CurveCreator(QWidget):
    def __init__(self, parent=None):
        super(CurveCreator, self).__init__(parent)
        self.setMinimumHeight(150)
        self.setMaximumHeight(150)
        self.setMinimumWidth(330)
        self.setupUI()
        self.connect()
    def setupUI(self):
        self.main_layout = QGridLayout(self)
        self.main_layout.setVerticalSpacing(16)
        self.main_layout.setHorizontalSpacing(8)
        # self.main_layout.setContentsMargins(8, 0, 8, 0)

        self.rootShape_button = CurveButton(32, 24, 24, 'rootShape.svg')
        self.main_layout.addWidget(self.rootShape_button, 0, 0)


        self.halfSphereSquare_button = CurveButton(32, 24, 24, 'halfSphereSquare.svg')
        self.main_layout.addWidget(self.halfSphereSquare_button, 0, 1)

        self.switchShape_button = CurveButton(32, 32, 32, 'switchShape.svg')
        self.main_layout.addWidget(self.switchShape_button, 0, 2)

        self.fkShape_button = CurveButton(32, 26, 26, 'fkShape.svg')
        self.main_layout.addWidget(self.fkShape_button, 0, 3)

        self.splineSec_button = CurveButton(32, 24, 24, 'splineSecShape.svg')
        self.main_layout.addWidget(self.splineSec_button, 0, 4)

        self.triangle_button = CurveButton(32, 28, 28, 'triangle.svg')
        self.main_layout.addWidget(self.triangle_button, 0, 5)

        self.crossShape_button = CurveButton(32, 32, 32, 'crossShape.svg')
        self.main_layout.addWidget(self.crossShape_button, 0, 6)

        self.star_button = CurveButton(32, 28, 28, 'starShape.svg')
        self.main_layout.addWidget(self.star_button, 0, 7)

        self.rollShape_button = CurveButton(32, 28, 28, 'rollShape.svg')
        self.main_layout.addWidget(self.rollShape_button, 1, 0)

        self.poleShape_button = CurveButton(32, 26, 26, 'poleShape.svg')
        self.main_layout.addWidget(self.poleShape_button, 1, 1)

        self.gravityShape_button = CurveButton(32, 28, 28, 'gravityShape.svg')
        self.main_layout.addWidget(self.gravityShape_button, 1, 2)

        self.aimShape_button = CurveButton(32, 30, 30, 'aimShape.svg')
        self.main_layout.addWidget(self.aimShape_button, 1, 3)

        self.bendyShape_button = CurveButton(32, 24, 24, 'bendyShape.svg')
        self.main_layout.addWidget(self.bendyShape_button, 1, 4)

        self.mainShape_button = CurveButton(32, 26, 26, 'mainShape.svg')
        self.main_layout.addWidget(self.mainShape_button, 1, 5)

        self.partShape_button = CurveButton(32, 26, 26, 'partShape.svg')
        self.main_layout.addWidget(self.partShape_button, 1, 6)

        self.scapulaShape_button = CurveButton(32, 30, 30, 'scapulaShape.svg')
        self.main_layout.addWidget(self.scapulaShape_button, 1, 7)

        self.headShape_button = CurveButton(32, 28, 28, 'headShape.svg')
        self.main_layout.addWidget(self.headShape_button, 2, 0)

        self.ikShape_button = CurveButton(32, 28, 28, 'ikShape.svg')
        self.main_layout.addWidget(self.ikShape_button, 2, 1)

    def connect(self):
        self.rootShape_button.clicked.connect(lambda: self.createCurve('RootShape'))
        self.mainShape_button.clicked.connect(lambda: self.createCurve('MainShape'))
        self.switchShape_button.clicked.connect(lambda: self.createCurve('SwitchShape'))
        self.fkShape_button.clicked.connect(lambda: self.createCurve('FKShape'))
        self.splineSec_button.clicked.connect(lambda: self.createCurve('SplineSecShape'))
        self.crossShape_button.clicked.connect(lambda: self.createCurve('CrossShape'))
        self.rollShape_button.clicked.connect(lambda: self.createCurve('RollShape'))
        # self.poleShape_button.clicked.connect(lambda: self.createCurve('PoleShape'))
        # self.gravityShape_button.clicked.connect(lambda: self.createCurve('GravityShape'))
        self.aimShape_button.clicked.connect(lambda: self.createCurve('AimShape'))
        self.bendyShape_button.clicked.connect(lambda: self.createCurve('BendyShape'))
        self.mainShape_button.clicked.connect(lambda: self.createCurve('MainShape'))
        self.partShape_button.clicked.connect(lambda: self.createCurve('PartShape'))
        self.scapulaShape_button.clicked.connect(lambda: self.createCurve('ScapulaShape'))
        self.headShape_button.clicked.connect(lambda: self.createCurve('HeadShape'))
        self.ikShape_button.clicked.connect(lambda: self.createCurve('IKShape'))

    def createCurve(self, data_type):
        data = importData(CURVE_PATH)
        sel_list = mc.ls(sl=True)
        if sel_list:
            for sel in sel_list:
                shape = mc.listRelatives(sel, shapes=True)
                if shape:
                    curve = sel
                    mc.delete(shape)
                    new_curve = mc.curve(n=data_type, knot=data[data_type]['knot'], point=data[data_type]['point'], degree=data[data_type]['degree'])
                    new_shape = mc.rename(mc.listRelatives(new_curve, shapes=True)[0], new_curve + 'Shape')
                    mc.matchTransform(new_curve, curve)
                    mc.parent(new_shape, curve, shape=True, relative=True)
                    mc.delete(new_curve)
                    mc.select(clear=True)
        else:
            curve = mc.curve(n=data_type, knot=data[data_type]['knot'], point=data[data_type]['point'],
                     degree=data[data_type]['degree'])
            print data_type, data[data_type]['knot'], data[data_type]['degree'], data[data_type]['point']
            mc.rename(mc.listRelatives(curve, shapes=True)[0], curve+'Shape')
        mc.select(sel_list)

class CurveButton(MFlattentButton):
    def __init__(self, size, width, height, image, parent=None):
        super(CurveButton, self).__init__(parent, size)
        icon_file = os.path.join(IMAGE_PATH, image)
        icon = maya_utilities.getIcon(icon_file, width, height)
        self.setIcon(icon)
        self.setIconSize(QSize(width, height))
