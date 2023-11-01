#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from functools import partial
import math
import modules.maya_utilities as maya_utilities
# reload(maya_utilities)
from maya_widgets.flatten_widget import *


class MColorCircle(QWidget):
    valueChanged = Signal()
    colorChanged = Signal()
    def __init__(self, parent=None, size=300):
        super(MColorCircle, self).__init__(parent=None)
        self.setStyleSheet('''background-color:rgb(50, 50, 50);''')
        self.setMinimumSize(QSize(size, size))
        self.setMaximumSize(QSize(size, size))

        self.size = size
        self.center = QPoint(self.size / 2.0, self.size / 2.0)

        # self.hue_radius = int(self.size / 2)
        # self.bg_radius = int(self.hue_radius * 0.82)
        # x = int(self.center.x() - (self.bg_radius / math.sqrt(2)) * 0.9)
        # y = int(self.center.y() - (self.bg_radius / math.sqrt(2)) * 0.9)
        # width = int((self.bg_radius / math.sqrt(2)) * 0.9 * 2)
        # height = int((self.bg_radius / math.sqrt(2)) * 0.9 * 2)
        self.hue_radius = 50
        self.bg_radius = 40
        x = 25
        y = 25
        width = 50
        height = 50

        self.sv_rect = QRect(x, y, width, height)
        self.sv_rect = QRect(25, 25, 50, 50)

        self.color_picker_size = 10
        self.color_picker_radius = 5
        self.color_picker = QLabel(self)
        self.color_picker.setAlignment(Qt.AlignCenter)
        self.color_picker.resize(self.color_picker_size, self.color_picker_size)
        self.color_picker.setStyleSheet('''
                                        background-color: transparent;
                                        border-radius:{0}px;
                                        border:{1}px solid white;
                                        '''.format(5, 2))
        self.color_picker.setAcceptDrops(True)
        # self.color_picker.move(self.sv_rect.x() - self.color_picker_radius, self.sv_rect.y() - self.color_picker_radius)
        self.color_picker.move(25 - 5, 75 - 5)

        self.hue_picker_size = 10
        self.hue_picker_radius = 5
        self.hue_motion_radius = 45
        self.hue_picker = QLabel(self)
        self.hue_picker.setAlignment(Qt.AlignCenter)
        self.hue_picker.resize(self.hue_picker_size, self.hue_picker_size)
        self.hue_picker.setStyleSheet('''
                                                background-color: transparent;
                                                border-radius:{0}px;
                                                border:{1}px solid white;
                                                '''.format(5, 2))

        self.hue_picker.setAcceptDrops(True)
        self.hue_picker.move(QPoint(self.center.x() - int(self.hue_motion_radius * math.cos(math.radians(180))) - self.hue_picker_radius,
                                    self.center.y() - int(self.hue_motion_radius * math.sin(math.radians(180))) - self.hue_picker_radius))

        self.hue = 0
        self.drag_color_picker = False
        self.drag_hue_picker = False

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(painter.Antialiasing)

        # 色相圆盘
        hue_color_list = [QColor(255, 0, 0), QColor(255, 255, 0), QColor(0, 255, 0), QColor(0, 255, 255),
                          QColor(0, 0, 255), QColor(255, 0, 255)]
        self.hue_conicalGradient = QConicalGradient(self.center, 0)
        interval = 1.0 / 6
        for i in range(len(hue_color_list)):
            self.hue_conicalGradient.setColorAt(interval * i, hue_color_list[i])
        self.hue_conicalGradient.setColorAt(1.0, hue_color_list[0])
        painter.setBrush(self.hue_conicalGradient)
        painter.drawEllipse(self.rect())

        # 两个圆盘叠成圆环
        # 背景圆盘
        self.bg_conicalGradient = QConicalGradient(self.center, 0)
        bg_palette = self.palette()
        bg_color = bg_palette.color(QPalette.Background)
        self.bg_conicalGradient.setColorAt(0.0, bg_color)
        self.bg_conicalGradient.setColorAt(1.0, bg_color)
        painter.setBrush(self.bg_conicalGradient)
        painter.drawEllipse(self.center, self.bg_radius, self.bg_radius)

        # 饱和度，亮度画布
        self.h_linearGradient = QLinearGradient(self.sv_rect.topLeft(), self.sv_rect.topRight())
        self.h_linearGradient.setColorAt(0, QColor(255, 255, 255))
        color = QColor()
        color.setHsv(self.hue, 255, 255)
        self.h_linearGradient.setColorAt(1, color)
        painter.fillRect(self.sv_rect, self.h_linearGradient)

        self.v_linearGradient = QLinearGradient(self.sv_rect.topLeft(), self.sv_rect.bottomLeft())
        self.v_linearGradient.setColorAt(0, QColor(0, 0, 0, 0))
        self.v_linearGradient.setColorAt(1, QColor(0, 0, 0, 255))
        painter.fillRect(self.sv_rect, self.v_linearGradient)


        painter.end()

    def getBGRadius(self):
        return self.bg_radius + self.hue_picker.rect().center().x()

    #
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # sv画布
            if self.sv_rect.contains(event.pos()):
                self.color_picker.move(
                    QPoint(event.pos().x() - self.color_picker_radius, event.pos().y() - self.color_picker_radius))
                self.drag_color_picker = True
            if self.childAt(event.pos()) == self.color_picker:
                # 判断鼠标在画布外，但是却在label内的情况，也就是label有部分在画布外的情况
                self.drag_color_picker = True
            self.colorChanged.emit()

            # 圆环
            dis = distance((event.pos().x(), event.pos().y()), (self.center.x(), self.center.y()))
            if self.bg_radius <= dis <= self.hue_radius:
                relative_pos = QPoint(event.pos() - self.center)
                angle = math.degrees(math.atan2(relative_pos.y(), relative_pos.x())) + 180
                self.hue_picker.move(
                    QPoint(self.center.x() - self.hue_motion_radius * math.cos(
                        math.radians(angle)) - self.hue_picker_radius,
                           self.center.y() - self.hue_motion_radius * math.sin(
                               math.radians(angle)) - self.hue_picker_radius))
                self.drag_hue_picker = True
                self.valueChanged.emit()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # 画布
            if self.drag_color_picker:
                self.color_picker.raise_()
                if self.sv_rect.contains(event.pos()):
                    self.color_picker.move(event.pos().x() - self.color_picker_radius,
                                           event.pos().y() - self.color_picker_radius)
                elif event.pos().x() < self.sv_rect.x() and event.pos().y() > self.sv_rect.y() and event.pos().y() < self.sv_rect.y() + self.sv_rect.height():
                    # 左
                    self.color_picker.move(self.sv_rect.x() - self.color_picker_radius,
                                           event.pos().y() - self.color_picker_radius)
                elif event.pos().y() < self.sv_rect.y() and event.pos().x() > self.sv_rect.x() and event.pos().x() < self.sv_rect.x() + self.sv_rect.width():
                    # 上
                    self.color_picker.move(event.pos().x() - self.color_picker_radius,
                                           self.sv_rect.y() - self.color_picker_radius)
                elif event.pos().x() > self.sv_rect.x() and event.pos().y() > self.sv_rect.y() and event.pos().y() < self.sv_rect.y() + self.sv_rect.height():
                    # 右
                    self.color_picker.move(self.sv_rect.x() + self.sv_rect.width() - self.color_picker_radius,
                                           event.pos().y() - self.color_picker_radius)
                elif event.pos().y() > self.sv_rect.y() and event.pos().x() > self.sv_rect.x() and event.pos().x() < self.sv_rect.x() + self.sv_rect.width():
                    # 下
                    self.color_picker.move(event.pos().x() - self.color_picker_radius,
                                           self.sv_rect.y() + self.sv_rect.height() - self.color_picker_radius)
                elif event.pos().x() < self.sv_rect.x() and event.pos().y() < self.sv_rect.y():
                    # 左上
                    self.color_picker.move(self.sv_rect.x() - self.color_picker_radius,
                                           self.sv_rect.y() - self.color_picker_radius)
                elif event.pos().x() > self.sv_rect.x() + self.sv_rect.width() and event.pos().y() < self.sv_rect.y():
                    # 右上
                    self.color_picker.move(self.sv_rect.x() + self.sv_rect.width() - self.color_picker_radius,
                                           self.sv_rect.y() - self.color_picker_radius)
                elif event.pos().x() < self.sv_rect.x() and event.pos().y() > self.sv_rect.y() + self.sv_rect.height():
                    # 左下
                    self.color_picker.move(self.sv_rect.x() - self.color_picker_radius,
                                           self.sv_rect.y() + self.sv_rect.height() - self.color_picker_radius)
                elif event.pos().x() > self.sv_rect.x() + self.sv_rect.width() and event.pos().y() > self.sv_rect.y() + self.sv_rect.height():
                    # 右下
                    self.color_picker.move(self.sv_rect.x() + self.sv_rect.width() - self.color_picker_radius,
                                           self.sv_rect.y() + self.sv_rect.height() - self.color_picker_radius)
            self.colorChanged.emit()

            # 圆环
            if self.drag_hue_picker:
                self.hue_picker.raise_()
                relative_pos = QPoint(event.pos() - self.center)
                angle = math.degrees(math.atan2(relative_pos.y(), relative_pos.x())) + 180
                self.hue_picker.move(
                    QPoint(round(self.center.x() - self.hue_motion_radius * math.cos(
                        math.radians(angle))) - self.hue_picker_radius,
                           round(self.center.y() - self.hue_motion_radius * math.sin(
                               math.radians(angle))) - self.hue_picker_radius))
                if round(math.degrees(math.atan2(relative_pos.y(), relative_pos.x()))) > 0:
                    self.hue = round(math.degrees(math.atan2(relative_pos.y(), relative_pos.x())))
                else:
                    self.hue = round(math.degrees(math.atan2(relative_pos.y(), relative_pos.x()))) + 360
                self.update()
                self.valueChanged.emit()

    def mouseReleaseEvent(self, event):
        self.drag_color_picker = False
        self.drag_hue_picker = False

    def setHue(self, hue):
        self.hue = hue
        self.hue_picker.raise_()
        angle = hue - 180
        self.hue_picker.move(
            QPoint(round(self.center.x() - self.hue_motion_radius * math.cos(math.radians(angle))) - self.hue_picker_radius,
                   round(self.center.y() + self.hue_motion_radius * math.sin(math.radians(angle))) - self.hue_picker_radius))
        self.update()

    def getHue(self):
        relative_pos = QPoint(self.hue_picker.pos() + QPoint(self.hue_picker_radius, self.hue_picker_radius) - self.center)
        if round(math.degrees(math.atan2(relative_pos.y(), relative_pos.x()))) > 0:
            return round(math.degrees(math.atan2(relative_pos.y(), relative_pos.x())))
        else:
            return round(math.degrees(math.atan2(relative_pos.y(), relative_pos.x())) + 360)

    def setSaturation(self, saturation):
        self.color_picker.move(self.sv_rect.y() + self.sv_rect.height() * saturation / 100 - self.color_picker_radius, self.color_picker.y())

    def getSaturation(self):
        return int((self.sv_rect.y() + self.sv_rect.height() - self.color_picker_radius - self.color_picker.pos().y()) / float(self.sv_rect.height()) * 100)



    def setValue(self, value):
        self.color_picker.move(self.color_picker.x(), self.sv_rect.x() + self.sv_rect.width() - self.sv_rect.width() * value / 100 - self.color_picker_radius)

    def getValue(self):
        return int((self.color_picker.pos().x() + self.color_picker_radius - self.sv_rect.x()) / float(self.sv_rect.width()) * 100)



class MHueSlider(QWidget):

    valueChanged = Signal()

    def __init__(self, parent=None, width=300, height=24):
        super(MHueSlider, self).__init__(parent)
        self.setMinimumSize(QSize(108, 14))
        self.setMaximumSize(QSize(108, 14))
        self.slider_rect = QRect(2, 2, 104, 10)
        self.handle = QLabel(self)
        self.handle.resize(4, 14)
        self.handle.move(2 - self.handle.rect().width() / 2, 0)
        self.handle.setStyleSheet('''
                                            background-color:white;
                                            border-radius:2px;
                                                ''')
        self.hue = 0
        self.saturation = 0
        self.value = 0

        self.drag_handle = False

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(painter.Antialiasing)

        # 色相圆盘
        hue_color_list = [QColor(255, 0, 0), QColor(255, 255, 0), QColor(0, 255, 0), QColor(0, 255, 255),
                          QColor(0, 0, 255), QColor(255, 0, 255)]
        self.hue_linearGradient = QLinearGradient(self.slider_rect.topLeft(), self.slider_rect.topRight())
        interval = 1.0 / 6
        for i in range(len(hue_color_list)):
            self.hue_linearGradient.setColorAt(interval * i, hue_color_list[i])
        self.hue_linearGradient.setColorAt(1.0, hue_color_list[0])
        painter.fillRect(self.slider_rect, self.hue_linearGradient)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.slider_rect.contains(event.pos()):
                self.handle.raise_()
                self.drag_handle = True
                self.handle.move(event.pos().x() - self.handle.rect().width() / 2, 0)
                self.valueChanged.emit()

            if self.childAt(event.pos()) == self.handle:
                self.drag_handle = True

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.drag_handle:
                self.handle.raise_()
                if self.slider_rect.x() < event.pos().x() < self.slider_rect.x() + self.slider_rect.width():
                    self.handle.move(event.pos().x() - self.handle.rect().width() / 2, 0)
                elif event.pos().x() < self.slider_rect.x():
                    self.handle.move(self.slider_rect.x() - self.handle.rect().width() / 2, 0)
                elif event.pos().x() > self.slider_rect.x() + self.slider_rect.width():
                    self.handle.move(self.slider_rect.x() + self.slider_rect.width() - self.handle.rect().width() / 2, 0)
                self.valueChanged.emit()


    def mouseReleaseEvent(self, event):
        self.value = False

    def setHue(self, hue):
        hue = 1 - hue / 360.0
        self.handle.move(round(self.slider_rect.x() + self.slider_rect.width() * hue - self.handle.rect().width() / 2.0), 0)

    def getHue(self):
        return round((self.handle.pos().x() + self.handle.rect().width() / 2.0 - self.slider_rect.x()) / float(self.slider_rect.width()) * 360.0)


class MSaturationSlider(QWidget):
    valueChanged = Signal()
    def __init__(self, parent=None, width=300, height=24):
        super(MSaturationSlider, self).__init__(parent)
        self.setMinimumSize(QSize(108, 14))
        self.setMaximumSize(QSize(108, 14))
        self.slider_rect = QRect(2, 2, 104, 10)
        self.handle = QLabel(self)
        self.handle.resize(4, 14)
        self.handle.move(2 - self.handle.rect().width() / 2, 0)
        self.handle.setStyleSheet('''
                                                    background-color:white;
                                                    border-radius:2px;
                                                    ''')
        self.hue = 0
        self.saturation = 0
        self.value = 0

        self.drag_handle = False

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(painter.Antialiasing)

        # 色相圆盘
        self.saturation_linearGradient = QLinearGradient(self.slider_rect.topLeft(), self.slider_rect.topRight())
        color = QColor()
        color.setHsv(self.hue, 0, self.value)
        self.saturation_linearGradient.setColorAt(0, color)
        color = QColor()
        color.setHsv(self.hue, 255, self.value)
        self.saturation_linearGradient.setColorAt(1, color)
        painter.fillRect(self.slider_rect, self.saturation_linearGradient)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.slider_rect.contains(event.pos()):
                self.handle.raise_()
                self.drag_handle = True
                self.handle.move(event.pos().x() - self.handle.rect().width() / 2, 0)
                self.valueChanged.emit()
            if self.childAt(event.pos()) == self.handle:
                self.drag_handle = True

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.drag_handle:
                self.handle.raise_()
                if self.slider_rect.x() < event.pos().x() < self.slider_rect.x() + self.slider_rect.width():
                    self.handle.move(event.pos().x() - self.handle.rect().width() / 2, 0)
                elif event.pos().x() < self.slider_rect.x():
                    self.handle.move(self.slider_rect.x() - self.handle.rect().width() / 2, 0)
                elif event.pos().x() > self.slider_rect.x() + self.slider_rect.width():
                    self.handle.move(self.slider_rect.x() + self.slider_rect.width() - self.handle.rect().width() / 2, 0)
                self.valueChanged.emit()

    def mouseReleaseEvent(self, event):
        self.drag_handle = False

    def setSaturation(self, saturation):
        saturation = saturation / 100.0
        self.handle.move(round(self.slider_rect.x() + self.slider_rect.width() * saturation - self.handle.rect().width() / 2), 0)
    def getSaturation(self):
        return round((self.handle.pos().x() + self.handle.rect().width() / 2.0 - self.slider_rect.x()) / self.slider_rect.width() * 100.0)

    def setHue(self, hue):
        self.hue = hue
        self.update()

    def setValue(self, value):
        self.value = value / 100.0 * 255
        self.update()

class MValueSlider(QWidget):
    valueChanged = Signal()
    def __init__(self, parent=None, width=300, height=24):
        super(MValueSlider, self).__init__(parent)
        self.setMinimumSize(QSize(108, 14))
        self.setMaximumSize(QSize(108, 14))
        self.slider_rect = QRect(2, 2, 104, 10)
        self.handle = QLabel(self)
        self.handle.resize(4, 14)
        self.handle.move(2 - self.handle.rect().width() / 2, 0)
        self.handle.setStyleSheet('''
                                                    background-color:white;
                                                    border-radius:2px;
                                                    ''')
        self.hue = 0
        self.saturation = 0
        self.value = 0
        self.drag_handle = False

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(painter.Antialiasing)

        self.value_linearGradient = QLinearGradient(self.slider_rect.topLeft(), self.slider_rect.topRight())
        color = QColor()
        color.setHsv(self.hue, self.saturation, 0)
        self.value_linearGradient.setColorAt(0, color)
        color = QColor()
        color.setHsv(self.hue, self.saturation, 255)
        self.value_linearGradient.setColorAt(1, color)
        painter.fillRect(self.slider_rect, self.value_linearGradient)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.slider_rect.contains(event.pos()):
                self.handle.raise_()
                self.drag_handle = True
                self.handle.move(event.pos().x() - self.handle.rect().width() / 2, 0)
                self.valueChanged.emit()
            if self.childAt(event.pos()) == self.handle:
                self.drag_handle = True

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.drag_handle:
                self.handle.raise_()
                if self.slider_rect.x() < event.pos().x() < self.slider_rect.x() + self.slider_rect.width():
                    self.handle.move(event.pos().x() - self.handle.rect().width() / 2, 0)
                elif event.pos().x() < self.slider_rect.x():
                    self.handle.move(self.slider_rect.x() - self.handle.rect().width() / 2, 0)
                elif event.pos().x() > self.slider_rect.x() + self.slider_rect.width():
                    self.handle.move(self.slider_rect.x() + self.slider_rect.width() - self.handle.rect().width() / 2, 0)
                self.valueChanged.emit()

    def mouseReleaseEvent(self, event):
        self.drag_handle = False

    def setValue(self, value):
        value = value / 100.0
        self.handle.move(round(self.slider_rect.x() + self.slider_rect.width() * value - self.handle.rect().width() / 2), 0)

    def getValue (self):
        return round((self.handle.pos().x() + self.handle.rect().width() / 2.0 - self.slider_rect.x()) / self.slider_rect.width() * 100.0)

    def setHue(self, hue):
        self.hue = hue
        self.update()
    def setSaturation(self, saturation):
        self.saturation = saturation / 100.0 * 255
        self.update()
class MColorPicker(QWidget):
    colorChanged = Signal()
    def __init__(self, parent=None):
        super(MColorPicker, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(2)

        self.hue_layout = QHBoxLayout()
        self.hue_layout.setContentsMargins(0, 0, 0, 0)
        self.hue_layout.setSpacing(6)
        self.main_layout.addLayout(self.hue_layout)
        self.hue_label = QLabel()
        self.hue_label.setText('H')
        self.hue_label.setMinimumWidth(12)
        self.hue_layout.addWidget(self.hue_label)
        self.hue_slider = MHueSlider()
        self.hue_layout.addWidget(self.hue_slider)
        self.hue_lineEdit = QLineEdit()
        hue_validator = QIntValidator(0, 360, self.hue_lineEdit)
        self.hue_lineEdit.setValidator(hue_validator)
        self.hue_lineEdit.setMaximumHeight(16)
        self.hue_lineEdit.setText(str(0))
        self.hue_layout.addWidget(self.hue_lineEdit)
        self.hue_lineEdit.setStyleSheet('''
                                            border:1px solid;
                                            border-color:rgb(80, 80, 80);
                                            border-radius:1px;
                                            background-color:transparent;
                                        ''')
        # 拖动hue_slider
        self.hue_slider.valueChanged.connect(lambda: self.hue_lineEdit.setText(str(int(self.hue_slider.getHue())))) # hue_lineEdit改为对应值
        self.hue_slider.valueChanged.connect(lambda: self.saturation_slider.setHue(self.hue_slider.getHue()))       # saturation_slider的颜色改变
        self.hue_slider.valueChanged.connect(lambda: self.value_slider.setHue(self.hue_slider.getHue()))            # value_slider的颜色改变
        self.hue_slider.valueChanged.connect(lambda: self.color_circle.setHue(self.hue_slider.getHue()))            # color_circle色环的颜色改变
        self.hue_slider.valueChanged.connect(self.colorChanged.emit)
        # 修改hue_lineEdit的值
        self.hue_lineEdit.editingFinished.connect(lambda: self.hue_slider.setHue(int(self.hue_lineEdit.text())))    # hue_slider
        self.hue_lineEdit.editingFinished.connect(lambda: self.saturation_slider.setHue(self.hue_slider.getHue()))  # saturation_slider的颜色改变
        self.hue_lineEdit.editingFinished.connect(lambda: self.value_slider.setHue(self.hue_slider.getHue()))       # value_slider的颜色改变
        self.hue_lineEdit.editingFinished.connect(lambda: self.color_circle.setHue(self.hue_slider.getHue()))       # color_circle色环的颜色改变
        self.hue_lineEdit.editingFinished.connect(self.colorChanged.emit)

        self.saturation_layout = QHBoxLayout()
        self.saturation_layout.setContentsMargins(0, 0, 0, 0)
        self.saturation_layout.setSpacing(6)
        self.main_layout.addLayout(self.saturation_layout)
        self.saturation_label = QLabel()
        self.saturation_label.setText('S')
        self.saturation_label.setMinimumWidth(12)
        self.saturation_layout.addWidget(self.saturation_label)
        self.saturation_slider = MSaturationSlider()
        self.saturation_layout.addWidget(self.saturation_slider)
        self.saturation_lineEdit = QLineEdit()
        saturation_validator = QIntValidator(0, 100, self.saturation_lineEdit)
        self.saturation_lineEdit.setValidator(saturation_validator)
        self.saturation_lineEdit.setText(str(0))
        self.saturation_lineEdit.setMaximumHeight(16)
        self.saturation_layout.addWidget(self.saturation_lineEdit)
        self.saturation_lineEdit.setStyleSheet('''
                                                    border:1px solid;
                                                    border-color:rgb(80, 80, 80);
                                                    border-radius:1px;
                                                    background-color:transparent;
                                                ''')
        # 拖动saturation_slider
        self.saturation_slider.valueChanged.connect(lambda: self.saturation_lineEdit.setText(str(int(self.saturation_slider.getSaturation()))))   # saturation_lineEdit
        self.saturation_slider.valueChanged.connect(lambda: self.value_slider.setSaturation(self.saturation_slider.getSaturation()))              # value_slider
        self.saturation_slider.valueChanged.connect(lambda: self.color_circle.setSaturation(self.saturation_slider.getSaturation()))              # circle_color
        self.saturation_slider.valueChanged.connect(self.colorChanged.emit)

        # 修改saturation_lineEdit的值
        self.saturation_lineEdit.editingFinished.connect(lambda: self.saturation_slider.setSaturation(int(self.saturation_lineEdit.text())))      # saturation_slider
        self.saturation_lineEdit.editingFinished.connect(lambda: self.value_slider.setSaturation(int(self.saturation_lineEdit.text())))           # value_slider
        self.saturation_lineEdit.editingFinished.connect(lambda: self.color_circle.setSaturation(int(self.saturation_lineEdit.text())))           # circle_color
        self.saturation_lineEdit.editingFinished.connect(self.colorChanged.emit)

        self.value_layout = QHBoxLayout()
        self.value_layout.setContentsMargins(0, 0, 0, 0)
        self.value_layout.setSpacing(6)
        self.main_layout.addLayout(self.value_layout)
        self.value_label = QLabel()
        self.value_label.setText('V')
        self.value_label.setMinimumWidth(12)
        self.value_layout.addWidget(self.value_label)
        self.value_slider = MValueSlider()
        self.value_layout.addWidget(self.value_slider)
        self.value_lineEdit = QLineEdit()
        value_validator = QIntValidator(0, 100, self.value_lineEdit)
        self.value_lineEdit.setValidator(value_validator)
        self.value_lineEdit.setText(str(0))
        self.value_lineEdit.setMaximumHeight(16)
        self.value_layout.addWidget(self.value_lineEdit)
        self.value_lineEdit.setStyleSheet('''
                                                    border:1px solid;
                                                    border-color:rgb(80, 80, 80);
                                                    border-radius:1px;
                                                    background-color:transparent;
                                                ''')
        # 拖动value_slider
        self.value_slider.valueChanged.connect(lambda: self.value_lineEdit.setText(str(int(self.value_slider.getValue()))))     # value_lineEdit
        self.value_slider.valueChanged.connect(lambda: self.saturation_slider.setValue(self.value_slider.getValue()))           # saturation_slider
        self.value_slider.valueChanged.connect(lambda: self.color_circle.setValue(self.value_slider.getValue()))                # color_circle
        self.value_slider.valueChanged.connect(self.colorChanged.emit)
        # 修改value_lineEdit的值
        self.value_lineEdit.editingFinished.connect(lambda: self.value_slider.setValue(int(self.value_lineEdit.text())))
        self.value_lineEdit.editingFinished.connect(lambda: self.saturation_slider.setValue(int(self.value_lineEdit.text())))
        self.value_lineEdit.editingFinished.connect(lambda: self.color_circle.setValue(int(self.value_lineEdit.text())))
        self.value_lineEdit.editingFinished.connect(self.colorChanged.emit)

        self.circle_layout = QHBoxLayout()
        self.main_layout.addLayout(self.circle_layout)
        self.horizontal_spacer = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.circle_layout.addItem(self.horizontal_spacer)
        self.color_circle = MColorCircle(size=100)
        self.circle_layout.addWidget(self.color_circle)

        # 拖动圆环
        self.color_circle.valueChanged.connect(lambda: self.hue_slider.setHue(self.color_circle.getHue()))
        self.color_circle.valueChanged.connect(lambda: self.hue_lineEdit.setText((str(int(self.color_circle.getHue())))))
        self.color_circle.valueChanged.connect(self.colorChanged.emit)

        # 拖动画布
        self.color_circle.colorChanged.connect(lambda: self.saturation_slider.setSaturation(self.color_circle.getSaturation()))     # saturation_slider
        self.color_circle.colorChanged.connect(lambda: self.value_slider.setValue(self.color_circle.getValue()))                    # value_slider
        self.color_circle.colorChanged.connect(lambda: self.saturation_lineEdit.setText(str(self.color_circle.getSaturation())))    # saturation_lineEdit
        self.color_circle.colorChanged.connect(lambda: self.value_lineEdit.setText(str(self.color_circle.getValue())))              # value_lineEdit
        self.color_circle.colorChanged.connect(self.colorChanged.emit)

        self.add_pre_button_layout = QVBoxLayout()
        self.circle_layout.addLayout(self.add_pre_button_layout)
        self.vertical_spacer = QSpacerItem(0, 70, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.add_pre_button_layout.addItem(self.vertical_spacer)
        self.add_pre_button = MFlattentButton(size=18)
        path = 'D:\Project\RigTools\Resources\icons\\add_color.svg'
        icon = maya_utilities.getIcon(path, 18, 18)
        self.add_pre_button.setIcon(icon)
        self.add_pre_button.setIconSize(QSize(18, 18))
        self.add_pre_button_layout.addWidget(self.add_pre_button)

    def getColor(self):
        color = QColor()
        color.setHsv(int(self.hue_lineEdit.text()), int(self.saturation_lineEdit.text()) /100.0 * 255, int(self.value_lineEdit.text()) / 100.0 * 255)
        return [color.red(), color.green(), color.blue()]

def distance(pos1, pos2):
    return math.sqrt(pow(pos1[0] - pos2[0], 2) + pow(pos1[1] - pos2[1], 2))
