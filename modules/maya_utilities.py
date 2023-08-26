#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys, os
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from shiboken2 import wrapInstance
from maya import OpenMayaUI as omui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import maya.cmds as mc

class IsolateViews:
    def __enter__(self):
        if not mc.ogs(q=True, pause=True):
            mc.ogs(pause=True)
        self.resetAutoKey = mc.autoKeyframe(q=True, state=True)

    def __exit__(self, *args):
        mc.autoKeyframe(state=self)
        if mc.ogs(q=True, pause=True):
            mc.ogs(pause=True)

class Undoable:
    def __enter__(self):
        mc.undoInfo(openChunk=True)

    def __exit__(self, *args):
        mc.undoInfo(closeChunk=True)



def maya_main_window():
    maya_main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(maya_main_window_ptr), QWidget)

def get_fileName_list(path, file_type):
    file_name_list = []
    for file_name in os.listdir(path):
        if file_name.endswith(file_type):
            file_name_list.append(file_name)
    return file_name_list

def getIcon(path, width, height):
    image = QImage(path)
    pixmap = QPixmap(image)
    fitPixmap = pixmap.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    return QIcon(fitPixmap)

def importData(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            return data
    except Exception as D:
        print e
        return None

def expoxtData(file, data):
    try:
        with open(file, 'w') as f:
            json.dump(data, f)
    except Exception as D:
        print e

font_db = QFontDatabase()
font_id = font_db.addApplicationFont('D:\\Project\\RigTools\\Resources\\font\\SF-Pro-Rounded-Semibold.ttf')
font_families = font_db.applicationFontFamilies(font_id)[0]
font = QFont(font_families)


def getFont():
    font_db = QFontDatabase()
    font_id = font_db.addApplicationFont('D:\\Project\\RigTools\\Resources\\font\\SF-Pro-Rounded-Semibold.ttf')
    font_families = font_db.applicationFontFamilies(font_id)[0]
    font = QFont(font_families)
    return font

def getFontTitle():
    font_db = QFontDatabase()
    font_id = font_db.addApplicationFont('D:\\Project\\RigTools\\Resources\\font\\Fact-Regular.ttf')
    font_families = font_db.applicationFontFamilies(font_id)[0]
    font = QFont(font_families)
    return font

