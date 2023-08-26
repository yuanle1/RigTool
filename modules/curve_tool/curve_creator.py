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

        self.roundSquare_button = CurveButton(32, 24, 24, 'roundSquare.svg')
        self.main_layout.addWidget(self.roundSquare_button, 0, 0)


        self.halfSphereSquare_button = CurveButton(32, 24, 24, 'halfSphereSquare.svg')
        self.main_layout.addWidget(self.halfSphereSquare_button, 0, 1)

        self.capsule_button = CurveButton(32, 32, 32, 'capsule.svg')
        self.main_layout.addWidget(self.capsule_button, 0, 2)

        self.sphere_button = CurveButton(32, 26, 26, 'sphere.svg')
        self.main_layout.addWidget(self.sphere_button, 0, 3)

        self.square_button = CurveButton(32, 24, 24, 'square.svg')
        self.main_layout.addWidget(self.square_button, 0, 4)

        self.triangle_button = CurveButton(32, 28, 28, 'triangle.svg')
        self.main_layout.addWidget(self.triangle_button, 0, 5)

        self.cross_button = CurveButton(32, 32, 32, 'cross.svg')
        self.main_layout.addWidget(self.cross_button, 0, 6)

        self.star_button = CurveButton(32, 28, 28, 'star.svg')
        self.main_layout.addWidget(self.star_button, 0, 7)

    def connect(self):
        self.star_button.clicked.connect(lambda: self.createCurve('star'))
        self.cross_button.clicked.connect(lambda: self.createCurve('cross'))
        self.triangle_button.clicked.connect(lambda: self.createCurve('triangle'))
        self.square_button.clicked.connect(lambda: self.createCurve('square'))
        self.sphere_button.clicked.connect(lambda: self.createCurve('sphere'))
        self.capsule_button.clicked.connect(lambda: self.createCurve('capsule'))
        self.halfSphereSquare_button.clicked.connect(lambda: self.createCurve('halfSphereSquare'))
        self.roundSquare_button.clicked.connect(lambda: self.createCurve('roundSquare'))

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
            mc.rename(mc.listRelatives(curve, shapes=True)[0], curve+'Shape')
        mc.select(sel_list)

class CurveButton(MFlattentButton):
    def __init__(self, size, width, height, image, parent=None):
        super(CurveButton, self).__init__(parent, size)
        icon_file = os.path.join(IMAGE_PATH, image)
        icon = maya_utilities.getIcon(icon_file, width, height)
        self.setIcon(icon)
        self.setIconSize(QSize(width, height))
