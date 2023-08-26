#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class MRoundWidget(QWidget):
    def __init__(self, parent=None):
        super(MRoundWidget, self).__init__(parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        rect = self.rect()
        color = QColor(50, 50, 50)
        brush = QBrush(color)
        painter.setBrush(brush)
        painter.drawRoundedRect(rect, 10, 10)

        painter.end()