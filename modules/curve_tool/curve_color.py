#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as mc
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import maya_widgets.color_picker
# reload(maya_widgets.color_picker)
from maya_widgets.color_picker import *
from maya_widgets.flatten_widget import *
from functools import partial

COlOR_ROW_NUM = 4
class CurveColor(QWidget):
    def __init__(self, parent=None):
        super(CurveColor, self).__init__(parent)
        # self.setMaximumWidth(300)
        self.setupUI()

    def setupUI(self):
        color_file = 'D:\Project\RigTools\Resources\data\pre_data.json'

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.pre_rgb_widget = QWidget()
        self.pre_rgb_layout = QGridLayout()
        self.pre_rgb_layout.setVerticalSpacing(5)
        self.pre_rgb_layout.setHorizontalSpacing(5)
        self.pre_rgb_widget.setLayout(self.pre_rgb_layout)


        color_list = maya_utilities.importData(color_file)
        for i in range(len(color_list)):
            row = i / COlOR_ROW_NUM
            column = i % COlOR_ROW_NUM
            color_button = MColorButton(color=color_list[i], size=30)
            self.pre_rgb_layout.addWidget(color_button, row, column)
            color_button.clicked.connect(partial(self.setCurveColor, color_list[i]))

        self.scroll_area = QScrollArea()
        self.scroll_area.setMinimumWidth(160)
        self.scroll_area.setFrameStyle(QFrame.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_layout.addWidget(self.scroll_area)
        self.scroll_area.setWidget(self.pre_rgb_widget)
        self.scroll_bar = self.scroll_area.verticalScrollBar()
        self.scroll_bar.setStyleSheet('''
                                                QScrollBar:vertical
                                                {
                                                    border: none;
                                                    background: transparent;
                                                    width: 10px;
                                                    margin: 5px 0 5px 0;
                                                }
                                                QScrollBar::handle:vertical
                                                {
                                                    background-color: #484848;
                                                    min-height: 10px;
                                                    border-radius: 5px;
                                                    border: none;
                                                }
                                                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical 
                                                {
                                                    height: 0px;
                                                }
                                                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
                                                {
                                                    background: transparent;
                                                }
                                                ''')


        self.color_picker_widget = MColorPicker()
        self.main_layout.addWidget(self.color_picker_widget)
        self.color_picker_widget.colorChanged.connect(lambda: self.setCurveColor(self.color_picker_widget.getColor()))

    def setCurveColor(self, color):
        # print self.color_picker_widget.getColor()
        sel_list = mc.ls(sl=True)
        if sel_list:
            for sel in sel_list:
                color = [i / 255.0 for i in color]
                shape = mc.listRelatives(sel, shapes=True)[0]
                mc.setAttr(shape + '.overrideEnabled', True)
                mc.setAttr(shape + '.overrideRGBColors', 1)
                mc.setAttr(shape + '.overrideColorRGB', color[0], color[1], color[2])
        mc.select(sel_list)



