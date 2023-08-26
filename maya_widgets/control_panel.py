#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class MControlPanel(QWidget):
    valueChanged = Signal()
    def __init__(self, parent=None, hue=0, size=300):
        super(MControlPanel, self).__init__(parent)
        self.hue = hue
        self.setMinimumSize(QSize(size, size))
        self.setMaximumSize(QSize(size, size))
        self.size = size
        self.handle_size = self.size / 5.0
        self.handle_raidus = self.handle_size / 2.0
        self.motion_radius = self.size / 3.0
        self.handle = MAlphaHandle(self, self.handle_size)

        self.handle_center = QPoint(self.handle_size / 2.0, self.handle_size / 2.0)
        self.center = QPoint(self.size / 2.0, self.size / 2.0)

        self.handle.move(QPoint(self.center.x() - self.motion_radius * math.cos(math.radians(270)) - self.handle_raidus, self.center.y() - self.motion_radius * math.sin(math.radians(270)) - self.handle_raidus))
        # signal
        self.enter = False
        self.temp_angle = -90
        self.drag = False

        # factor
        self.factor = 1

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(painter.Antialiasing)
        self.linearGradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomRight())
        color = QColor()
        color.setHsv(self.hue, 90, 255)
        self.linearGradient.setColorAt(0, color)
        color = QColor()
        color.setHsv(self.hue, 90, 200)
        self.linearGradient.setColorAt(1, color)

        painter.setBrush(self.linearGradient)
        painter.drawEllipse(self.rect())

        painter.end()

    def enterEvent(self, event):
        self.enter = True


    def leaveEvent(self, event):
        self.enter = False

    def mousePressEvent(self, event):
        # 点击的是handle
        if event.buttons() == Qt.LeftButton and self.childAt(event.pos()) == self.handle:
            self.drag = True

    def mouseMoveEvent(self, event):
        if self.drag:
            relative_pos = QPoint(event.pos() - self.center)
            self.temp_angle = math.degrees(math.atan2(relative_pos.y(), relative_pos.x())) + 180
            if self.temp_angle % 45 == 0:
                n = int(self.temp_angle / 45)
                self.handle.move(
                    QPoint(
                        self.center.x() - self.motion_radius * math.cos(math.radians(n * 45)) - self.handle_raidus,
                        self.center.y() - self.motion_radius * math.sin(math.radians(n * 45)) - self.handle_raidus))
                self.valueChanged.emit()

    def mouseReleaseEvent(self, event):
        self.drag = False

    def wheelEvent(self, event):
        if self.enter:
            # 鼠标滚轮滑动，小指针转45度
            if event.angleDelta().y() > 0:
                self.temp_angle += 45
                self.factor = 1
            else:
                self.temp_angle -= 45
                self.factor = -1
            self.handle.move(
                QPoint(self.center.x() - self.motion_radius * math.cos(math.radians(self.temp_angle)) - self.handle_raidus,
                       self.center.y() - self.motion_radius * math.sin(math.radians(self.temp_angle)) - self.handle_raidus))
            self.valueChanged.emit()

    def getFactor(self):
        return self.factor

class MAlphaHandle(QWidget):
    def __init__(self, parent=None, size=10):
        super(MAlphaHandle, self).__init__(parent)
        self.resize(size, size)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(painter.Antialiasing)
        center = QPoint(self.rect().center().x() + 1, self.rect().center().y() + 1)
        self.radialGradient = QRadialGradient(center, self.rect().center().x())
        self.radialGradient.setColorAt(0, QColor(100, 100, 100, 40))
        self.radialGradient.setColorAt(1, QColor(20, 20, 20, 40))

        painter.setBrush(self.radialGradient)
        painter.drawEllipse(self.rect())

        painter.setRenderHint(painter.Antialiasing)
        painter.end()






