#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *



class MSwitchCircle(QWidget):
    def __init__(self, radius, parent=None):
        super(MSwitchCircle, self).__init__(parent)
        self.resize(radius * 2, radius * 2)
        self.animation = QPropertyAnimation(self, 'pos')
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.setDuration(300)

        self.off_color = QColor(150, 150, 150)
        self.on_color = QColor(118, 221, 218)
        self.checked = False
        self.radius = radius


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        if self.checked:
            painter.setBrush(self.on_color)
        else:
            painter.setBrush(self.off_color)
        painter.drawEllipse(QPoint(self.radius, self.radius), self.radius, self.radius)
        painter.end()

    def setCheced(self, checked):
        self.checked = checked
        self.update()



class MSwitch(QCheckBox):
    def __init__(self, parent=None):
        super(MSwitch, self).__init__(parent)
        self.setFixedSize(27, 14)

        self.border_size = 4

        self.bg_rect = self.rect().adjusted(self.border_size / 2, self.border_size / 2, -self.border_size / 2, -self.border_size / 2)
        self.setCursor(Qt.PointingHandCursor)
        radius = (self.bg_rect.height() - self.bg_rect.y()) / 2

        self.circle = MSwitchCircle(radius, self)
        self.circle.move(self.height() / 2 - radius + 1, self.height() / 2 - radius)
        self.move_range = (self.x(), self.width())
        self.animation = QPropertyAnimation(self.circle, 'pos')
        self.checked = False

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(QColor('#858786'), self.border_size / 2))
        self.bg_rect = self.rect().adjusted(2, 2, -2, -2)
        radius = self.height() / 2 - 2

        painter.drawRoundedRect(self.bg_rect, radius, radius)

    def mousePressEvent(self, event):
        self.setChecked(not self.checked)

    def setChecked(self, checked, *args, **kwargs):
        super(MSwitch, self).setChecked(checked, *args, **kwargs)
        if self.animation.state() != QAbstractAnimation.Running:
            if self.checked != checked:
                self.circle.setCheced(checked)
                if checked:
                    self.animation.setStartValue(QPoint(4, 3))
                    self.animation.setEndValue(QPoint(15, 3))
                else:
                    self.animation.setStartValue(QPoint(15, 3))
                    self.animation.setEndValue(QPoint(4, 3))
                self.animation.start()
            self.checked = checked
    def isChecked(self):
        return self.checked


class MComboBox(QComboBox):
    def __init__(self, image=None, width=8, parent=None):
        super(MComboBox, self).__init__(parent)
        self.setObjectName('MComboBox')
        self.setStyleSheet('''
                                #QComboBox
                                {{
                                    border:1px solid rgb(80,80,80);                         
                                    border-radius:3px;
                                    background-color:transparent;
                                }}

                                #QComboBox:drop-down
                                {{
                                    image: url({0});
                                    subcontrol-position: right;
                                    width:{1}px;
                                    padding-right:2px;
                                }}
                            '''.format(image, width))