#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from modules import maya_utilities as maya_utilities
from maya_widgets import flatten_widget as flatten_widget
from maya_widgets import switch_button as switch_button

# reload(maya_utilities)
# reload(flatten_widget)
# reload(switch_button)

UPPER_CASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWER_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
class NameText(QFrame):
    def __init__(self, parent=None):
        super(NameText, self).__init__(parent)
        self.setupUI()
        self.connect()

    def setupUI(self):
        font = maya_utilities.font
        self.setFixedSize(QSize(86, 86))
        self.setObjectName('NameText')
        self.drag_flag = False
        self.setStyleSheet('''
                            #NameText
                            {
                                background-color: rgb(60, 60, 60);
                                border:2px solid rgb(97,97,97);
                                border-radius: 5px;
                            }
                            ''')
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 2, 5, 5)
        self.main_layout.setSpacing(0)

        self.title_layout = QHBoxLayout()
        self.title_layout.setContentsMargins(0, 0, 5, 10)
        self.title_layout.setSpacing(23)
        self.main_layout.addLayout(self.title_layout)

        self.title_label = QLabel()
        pixmap = QPixmap('D:/Project/RigTools/Resources/icons/letter_T.png')
        fitPixmap = pixmap.scaled(15, 15, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.title_label.setPixmap(fitPixmap)
        self.title_label.setFixedWidth(16)
        self.title_label.setFixedHeight(16)
        self.title_label.setStyleSheet('''
                                            color:rgb(195,223,177);
                                        ''')
        self.title_layout.addWidget(self.title_label)

        self.main_layout.addStretch()

        self.title_line = QFrame()
        self.title_line.setFrameShape(QFrame.HLine)
        self.title_line.setFixedHeight(2)
        self.title_line.setStyleSheet('''
                                            background-color: rgb(141,159,121);
                                            border-radius:1px;
                                      ''')
        self.title_layout.addWidget(self.title_line)

        self.text_lineEdit = flatten_widget.MLineEdit()
        self.text_lineEdit.setText('Cube')
        self.text_lineEdit.setFont(font)
        self.text_lineEdit.setStyleSheet('''
                                                border:none;
                                                background-color:transparent;
                                                border-bottom: 2px solid rgb(126,129,122);
                                                padding-bottom: -2px;
                                            ''')
        self.main_layout.addWidget(self.text_lineEdit)

        self.main_layout.addStretch()

        self.use_own_name_layout = QHBoxLayout()
        self.use_own_name_layout.setContentsMargins(16, 0, 0, 0)
        # self.main_layout.addLayout(self.use_own_name_layout)

        self.use_own_name_label = QLabel()
        font.setPointSize(-1)
        # self.use_own_name_label.setFont(font)
        self.use_own_name_label.setText('own :')
        self.use_own_name_layout.addWidget(self.use_own_name_label)

        self.use_own_name_check = switch_button.MSwitch()
        self.use_own_name_layout.addWidget(self.use_own_name_check)


        self.dash_layout = QHBoxLayout()
        self.dash_layout.setContentsMargins(22, 5, 0, 0)
        self.main_layout.addLayout(self.dash_layout)

        self.dash_label = QLabel()
        font.setPointSize(-1)
        self.dash_label.setFont(font)
        self.dash_label.setText('"_" :')
        self.dash_layout.addWidget(self.dash_label)

        self.dash_check = switch_button.MSwitch()
        self.dash_layout.addWidget(self.dash_check)

        self.main_menu = QMenu(self)
        # self.main_menu.setFont(font)
        self.main_menu.setFixedSize(80, 40)
        self.main_menu.setObjectName('main_menu')
        self.main_menu.setStyleSheet('''
                                          #main_menu
                                          {
                                              color:rgb(172,172,172);
                                          }
                                          #main_menu:item
                                          {
                                              padding:0px 25px;
                                              height:20px;
                                              width:40px;
                                          }
                                          #main_menu:item:selected
                                          {
                                                background-color:rgb(105,121,122);
                                                
                                          }
                                          #main_menu:icon
                                          {
                                               padding-left: 8px;
                                          }
                                      ''')

        reset_icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/restore.png', 12, 12)
        self.reset_action = QAction(reset_icon, 'Reset', self)
        self.main_menu.addAction(self.reset_action)

        remove_icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/remove.svg', 12, 12)
        self.remove_action = QAction(remove_icon, 'Remove', self)
        self.main_menu.addAction(self.remove_action)


    def connect(self):
        self.use_own_name_check.stateChanged.connect(self.showLineEdit)
        self.reset_action.triggered.connect(self.reset_component)
        self.remove_action.triggered.connect(self.remove_component)

    def remove_component(self):
        self.deleteLater()
        # self.parent().layout().removeWidget(self)

    def reset_component(self):
        # self.parent().layout().removeWidget(self)
        self.deleteLater()
        new_component_widget = NameText(self.parent())
        self.parent().layout().insertWidget(self.parent().layout().indexOf(self), new_component_widget)

    def showLineEdit(self, state):
        self.text_lineEdit.setEnabled(not state)

    def mousePressEvent(self, event):
        if QRect(0, 0, self.width(), 20).contains(event.pos()):
            if event.buttons() == Qt.LeftButton:
                self.setCursor(Qt.ClosedHandCursor)
                self.drag_flag = True
                self.origin_mouse_global_x = event.globalX()
                self.origin_mouse_global_y = event.globalY()

                self.origin_widget_x = self.x()
                self.origin_widget_y = self.y()

        if event.buttons() == Qt.RightButton:
            self.main_menu.exec_(QCursor().pos())

    def mouseMoveEvent(self, event):
        if self.drag_flag:
            move_x = event.globalX() - self.origin_mouse_global_x
            move_y = event.globalY() - self.origin_mouse_global_y

            dest_x = self.origin_widget_x + move_x
            dest_y = self.origin_widget_y + move_y
            self.move(dest_x, dest_y)
            self.raise_()
        else:
            if QRect(0, 0, self.width(), 20).contains(event.pos()):
                self.setCursor(Qt.PointingHandCursor)

    def mouseReleaseEvent(self, event):
        if self.drag_flag:
            self.setCursor(Qt.ArrowCursor)
            layout = self.parent().layout()
            widgets = []
            for i in [NameText, NameNumber, NameLetter, NameOrigin]:
                widgets.extend(self.parent().findChildren(i))
            widgets.sort(key=self.sort)
            for i in range(len(widgets)):
                layout.insertWidget(i, widgets[i])
            self.drag_flag = False
            self.raise_()

    def sort(self, widget):
        return widget.x()

    def useDash(self):
        return self.dash_check.isChecked()

    def useOwn(self):
        return self.use_own_name_check.isChecked()

    def getText(self):
        return self.text_lineEdit.text()

class NameNumber(QFrame):
    def __init__(self, parent=None):
        super(NameNumber, self).__init__(parent)
        self.setupUI()
        self.connect()
        self.drag_flag = False

    def setupUI(self):
        font = maya_utilities.font
        self.setFixedSize(QSize(86, 86))
        self.setObjectName('NameNumber')

        self.setStyleSheet('''
                            #NameNumber
                            {
                                background-color: rgb(60, 60, 60);
                                border:2px solid rgb(97,97,97);
                                border-radius: 5px;
                            }
                            ''')
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 2, 0, 5)
        self.main_layout.setSpacing(2)

        self.title_layout = QHBoxLayout()
        self.title_layout.setContentsMargins(0, 0, 10, 2)
        self.title_layout.setSpacing(23)
        self.main_layout.addLayout(self.title_layout)

        self.title_label = QLabel()
        pixmap = QPixmap('D:/Project/RigTools/Resources/icons/number_2.png')
        fitPixmap = pixmap.scaled(14, 14, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.title_label.setPixmap(fitPixmap)
        self.title_label.setFixedWidth(16)
        self.title_label.setFixedHeight(16)
        self.title_label.setStyleSheet('''
                                            color:rgb(160,194,211);
                                        ''')
        self.title_layout.addWidget(self.title_label)


        self.title_line = QFrame()
        self.title_line.setFrameShape(QFrame.HLine)
        self.title_line.setFixedHeight(2)
        self.title_line.setStyleSheet('''
                                            background-color: rgb(108,134,151);
                                            border-radius:1px;
                                      ''')
        self.title_layout.addWidget(self.title_line)

        self.spin_layout = QGridLayout()
        self.spin_layout.setContentsMargins(0, 0, 5, 0)
        self.spin_layout.setVerticalSpacing(4)
        self.main_layout.addLayout(self.spin_layout)

        self.start_label = QLabel()
        self.start_label.setText(' Start :')
        font.setPointSize(-1)
        self.start_label.setFont(font)
        self.start_label.setFixedWidth(34)
        self.spin_layout.addWidget(self.start_label, 0, 0)

        self.start_spin = flatten_widget.MSpinBox()
        self.start_spin.setValue(1)
        self.start_spin.setFixedSize(36, 16)
        self.spin_layout.addWidget(self.start_spin, 0, 1)

        self.digits_label = QLabel()
        self.digits_label.setText('Digits :')
        font.setPointSize(-1)
        self.digits_label.setFont(font)
        self.digits_label.setFixedWidth(34)
        self.spin_layout.addWidget(self.digits_label, 1, 0)

        self.digits_spin = flatten_widget.MSpinBox()
        self.digits_spin.setValue(2)
        self.digits_spin.setMinimum(1)
        self.digits_spin.setFixedSize(36, 16)
        self.spin_layout.addWidget(self.digits_spin, 1, 1)

        self.main_layout.addStretch()

        self.dash_layout = QHBoxLayout()
        self.dash_layout.setContentsMargins(20, 5, 5, 0)
        self.main_layout.addLayout(self.dash_layout)

        self.dash_label = QLabel()
        font.setPointSize(-1)
        self.dash_label.setFont(font)
        self.dash_label.setText('"_" :')
        self.dash_layout.addWidget(self.dash_label)

        self.dash_check = switch_button.MSwitch()
        self.dash_layout.addWidget(self.dash_check)

        self.main_menu = QMenu(self)
        self.main_menu.setFont(font)
        self.main_menu.setFixedSize(80, 40)
        self.main_menu.setObjectName('main_menu')
        self.main_menu.setStyleSheet('''
                                                  #main_menu
                                                  {
                                                      color:rgb(172,172,172);
                                                  }
                                                  #main_menu:item
                                                  {
                                                      padding:0px 25px;
                                                      height:20px;
                                                      width:40px;
                                                  }
                                                  #main_menu:item:selected
                                                  {
                                                        background-color:rgb(105,121,122);

                                                  }
                                                  #main_menu:icon
                                                  {
                                                       padding-left: 8px;
                                                  }
                                              ''')

        reset_icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/restore.png', 12, 12)
        self.reset_action = QAction(reset_icon, 'Reset', self)
        self.main_menu.addAction(self.reset_action)

        remove_icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/remove.svg', 12, 12)
        self.remove_action = QAction(remove_icon, 'Remove', self)
        self.main_menu.addAction(self.remove_action)

    def connect(self):
        self.reset_action.triggered.connect(self.reset_component)
        self.remove_action.triggered.connect(self.remove_component)

    def remove_component(self):
        self.deleteLater()
        # self.parent().layout().removeWidget(self)

    def reset_component(self):
        # self.parent().layout().removeWidget(self)
        self.deleteLater()
        new_component_widget = NameNumber(self.parent())
        self.parent().layout().insertWidget(self.parent().layout().indexOf(self), new_component_widget)

    def mousePressEvent(self, event):
        if QRect(0, 0, self.width(), 20).contains(event.pos()):
            if event.buttons() == Qt.LeftButton:
                self.setCursor(Qt.ClosedHandCursor)
                self.drag_flag = True
                self.origin_mouse_global_x = event.globalX()
                self.origin_mouse_global_y = event.globalY()

                self.origin_widget_x = self.x()
                self.origin_widget_y = self.y()

        if event.buttons() == Qt.RightButton:
            self.main_menu.exec_(QCursor().pos())

    def mouseMoveEvent(self, event):
        if self.drag_flag:
            move_x = event.globalX() - self.origin_mouse_global_x
            move_y = event.globalY() - self.origin_mouse_global_y

            dest_x = self.origin_widget_x + move_x
            dest_y = self.origin_widget_y + move_y
            self.move(dest_x, dest_y)
            self.raise_()
        else:
            if QRect(0, 0, self.width(), 20).contains(event.pos()):
                self.setCursor(Qt.PointingHandCursor)

    def mouseReleaseEvent(self, event):
        if self.drag_flag:
            self.setCursor(Qt.ArrowCursor)
            layout = self.parent().layout()
            widgets = []
            for i in [NameText, NameNumber, NameLetter, NameOrigin]:
                widgets.extend(self.parent().findChildren(i))
            widgets.sort(key=self.sort)
            for i in range(len(widgets)):
                layout.insertWidget(i, widgets[i])
            self.drag_flag = False
            self.raise_()

    def sort(self, widget):
        return widget.x()

    def useDash(self):
        return self.dash_check.isChecked()

    def getStartNum(self):
        return self.start_spin.value()

    def getDigits(self):
        return self.digits_spin.value()
class NameLetter(QFrame):
    def __init__(self, parent=None):
        super(NameLetter, self).__init__(parent)
        self.setupUI()
        self.loadLetter(UPPER_CASE)
        self.connect()
        self.drag_flag = False

    def setupUI(self):
        font = maya_utilities.font
        self.setFixedSize(QSize(86, 86))
        self.setObjectName('NameLetter')
        self.setStyleSheet('''
                               #NameLetter
                               {
                                   background-color: rgb(60, 60, 60);
                                   border:2px solid rgb(97,97,97);
                                   border-radius: 5px;
                               }
                               ''')
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 2, 0, 5)
        self.main_layout.setSpacing(2)

        self.title_layout = QHBoxLayout()
        self.title_layout.setContentsMargins(0, 0, 10, 0)
        self.title_layout.setSpacing(23)
        self.main_layout.addLayout(self.title_layout)

        self.title_label = QLabel()

        pixmap = QPixmap('D:/Project/RigTools/Resources/icons/letter_A.png')
        fitPixmap = pixmap.scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.title_label.setPixmap(fitPixmap)
        self.title_label.setFixedWidth(16)
        self.title_label.setFixedHeight(16)
        self.title_label.setStyleSheet('''
                                               color:rgb(179,137,147);
                                           ''')
        self.title_layout.addWidget(self.title_label)

        self.title_line = QFrame()
        self.title_line.setFrameShape(QFrame.HLine)
        self.title_line.setFixedHeight(2)
        self.title_line.setStyleSheet('''
                                               background-color: rgb(131,100,102);
                                               border-radius:1px;
                                         ''')
        self.title_layout.addWidget(self.title_line)

        self.start_layout = QHBoxLayout()
        self.start_layout.setContentsMargins(2, 0, 5, 0)
        self.start_layout.setSpacing(0)
        self.main_layout.addLayout(self.start_layout)

        self.start_label = QLabel()
        self.start_label.setText('Start :')
        font.setPointSize(-1)
        self.start_label.setFont(font)
        self.start_label.setFixedWidth(34)
        self.start_layout.addWidget(self.start_label)

        self.letter_combo = flatten_widget.MComboBox(width=7, image='D:/Project/RigTools/Resources/icons/down_line.png')
        self.letter_combo.setFixedSize(36, 16)
        self.start_layout.addWidget(self.letter_combo)

        self.case_layout = QHBoxLayout()
        self.case_layout.setContentsMargins(15, 5, 0, 0)
        self.main_layout.addLayout(self.case_layout)

        self.upperCase_check = flatten_widget.MFlattentCheck()
        self.upperCase_check.setText('A')
        self.upperCase_check.setChecked(True)
        self.case_layout.addWidget(self.upperCase_check)

        self.lowerCase_check = flatten_widget.MFlattentCheck()
        self.lowerCase_check.setText('a')
        self.case_layout.addWidget(self.lowerCase_check)

        self.main_layout.addStretch()

        self.dash_layout = QHBoxLayout()
        self.dash_layout.setContentsMargins(20, 5, 5, 0)
        self.main_layout.addLayout(self.dash_layout)

        self.dash_label = QLabel()
        font.setPointSize(-1)
        self.dash_label.setFont(font)
        self.dash_label.setText('"_" :')
        self.dash_layout.addWidget(self.dash_label)

        self.dash_check = switch_button.MSwitch()
        self.dash_layout.addWidget(self.dash_check)

        self.main_menu = QMenu(self)
        self.main_menu.setFont(font)
        self.main_menu.setFixedSize(80, 40)
        self.main_menu.setObjectName('main_menu')
        self.main_menu.setStyleSheet('''
                                                  #main_menu
                                                  {
                                                      color:rgb(172,172,172);
                                                  }
                                                  #main_menu:item
                                                  {
                                                      padding:0px 25px;
                                                      height:20px;
                                                      width:40px;
                                                  }
                                                  #main_menu:item:selected
                                                  {
                                                        background-color:rgb(105,121,122);

                                                  }
                                                  #main_menu:icon
                                                  {
                                                       padding-left: 8px;
                                                  }
                                              ''')

        reset_icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/restore.png', 12, 12)
        self.reset_action = QAction(reset_icon, 'Reset', self)
        self.main_menu.addAction(self.reset_action)

        remove_icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/remove.svg', 12, 12)
        self.remove_action = QAction(remove_icon, 'Remove', self)
        self.main_menu.addAction(self.remove_action)
    def loadLetter(self, item_list):
        current_index = self.letter_combo.currentIndex()
        if current_index == -1:
            current_index = 0
        self.letter_combo.clear()
        self.letter_combo.addItems(item_list)
        self.letter_combo.setCurrentIndex(current_index)

    def connect(self):
        self.reset_action.triggered.connect(self.reset_component)
        self.remove_action.triggered.connect(self.remove_component)
        self.upperCase_check.clicked.connect(lambda: self.loadLetter(UPPER_CASE))
        self.lowerCase_check.clicked.connect(lambda: self.loadLetter(LOWER_CASE))

    def remove_component(self):
        self.deleteLater()
        # self.parent().layout().removeWidget(self)

    def reset_component(self):
        # self.parent().layout().removeWidget(self)
        self.deleteLater()
        new_component_widget = NameLetter(self.parent())
        self.parent().layout().insertWidget(self.parent().layout().indexOf(self), new_component_widget)

    def mousePressEvent(self, event):
        if QRect(0, 0, self.width(), 20).contains(event.pos()):
            if event.buttons() == Qt.LeftButton:
                self.setCursor(Qt.ClosedHandCursor)
                self.drag_flag = True
                self.origin_mouse_global_x = event.globalX()
                self.origin_mouse_global_y = event.globalY()

                self.origin_widget_x = self.x()
                self.origin_widget_y = self.y()

        if event.buttons() == Qt.RightButton:
            self.main_menu.exec_(QCursor().pos())

    def mouseMoveEvent(self, event):
        if self.drag_flag:
            move_x = event.globalX() - self.origin_mouse_global_x
            move_y = event.globalY() - self.origin_mouse_global_y

            dest_x = self.origin_widget_x + move_x
            dest_y = self.origin_widget_y + move_y
            self.move(dest_x, dest_y)
            self.raise_()
        else:
            if QRect(0, 0, self.width(), 20).contains(event.pos()):
                self.setCursor(Qt.PointingHandCursor)

    def mouseReleaseEvent(self, event):
        if self.drag_flag:
            self.setCursor(Qt.ArrowCursor)
            layout = self.parent().layout()
            widgets = []
            for i in [NameText, NameNumber, NameLetter, NameOrigin]:
                widgets.extend(self.parent().findChildren(i))
            widgets.sort(key=self.sort)
            for i in range(len(widgets)):
                layout.insertWidget(i, widgets[i])
            self.drag_flag = False
            self.raise_()

    def sort(self, widget):
        return widget.x()

    def useDash(self):
        return self.dash_check.isChecked()

    def getLetter(self):
        return self.letter_combo.currentText()

class NameOrigin(QFrame):
    def __init__(self, parent=None):
        super(NameOrigin, self).__init__(parent)
        self.setupUI()
        self.drag_flag = False

    def setupUI(self):
        font = maya_utilities.font
        self.setFixedSize(QSize(86, 86))
        self.setObjectName('NameLetter')
        self.setStyleSheet('''
                                       #NameLetter
                                       {
                                           background-color: rgb(60, 60, 60);
                                           border:2px solid rgb(97,97,97);
                                           border-radius: 5px;
                                       }
                                       ''')
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 2, 0, 5)
        self.main_layout.setSpacing(2)

        self.title_layout = QHBoxLayout()
        self.title_layout.setContentsMargins(0, 0, 10, 0)
        self.title_layout.setSpacing(23)
        self.main_layout.addLayout(self.title_layout)

        self.title_label = QLabel()
        pixmap = QPixmap('D:/Project/RigTools/Resources/icons/temp.svg')
        fitPixmap = pixmap.scaled(14, 14, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.title_label.setPixmap(fitPixmap)
        self.title_label.setFixedWidth(16)
        self.title_label.setFixedHeight(16)
        self.title_label.setStyleSheet('''
                                                       color:#9d539e;
                                                   ''')
        self.title_layout.addWidget(self.title_label)

        self.title_line = QFrame()
        self.title_line.setFrameShape(QFrame.HLine)
        self.title_line.setFixedHeight(2)
        self.title_line.setStyleSheet('''
                                                       background-color: #2aa1df;
                                                       border-radius:1px;
                                                 ''')
        self.title_layout.addWidget(self.title_line)

        self.self_label_layout = QHBoxLayout()
        self.self_label_layout.setContentsMargins(0, 2, 5, 0)
        self.main_layout.addLayout(self.self_label_layout)

        self.self_label = QLabel()
        self.self_label.setPixmap(QPixmap('D:/Project/RigTools/Resources/icons/self.svg'))
        self.self_label.setScaledContents(True)
        self.self_label.setFixedSize(36, 36)
        self.self_label_layout.addWidget(self.self_label)

        self.main_layout.addStretch()

        self.dash_layout = QHBoxLayout()
        self.dash_layout.setContentsMargins(20, 5, 5, 0)
        self.main_layout.addLayout(self.dash_layout)

        self.dash_label = QLabel()
        font.setPointSize(-1)
        self.dash_label.setFont(font)
        self.dash_label.setText('"_" :')
        self.dash_layout.addWidget(self.dash_label)

        self.dash_check = switch_button.MSwitch()
        self.dash_layout.addWidget(self.dash_check)

    def mousePressEvent(self, event):
        if QRect(0, 0, self.width(), 20).contains(event.pos()):
            if event.buttons() == Qt.LeftButton:
                self.setCursor(Qt.ClosedHandCursor)
                self.drag_flag = True
                self.origin_mouse_global_x = event.globalX()
                self.origin_mouse_global_y = event.globalY()

                self.origin_widget_x = self.x()
                self.origin_widget_y = self.y()

    def mouseMoveEvent(self, event):
        if self.drag_flag:
            move_x = event.globalX() - self.origin_mouse_global_x
            move_y = event.globalY() - self.origin_mouse_global_y

            dest_x = self.origin_widget_x + move_x
            dest_y = self.origin_widget_y + move_y
            self.move(dest_x, dest_y)
            self.raise_()
        else:
            if QRect(0, 0, self.width(), 20).contains(event.pos()):
                self.setCursor(Qt.PointingHandCursor)

    def mouseReleaseEvent(self, event):
        if self.drag_flag:
            self.setCursor(Qt.ArrowCursor)
            layout = self.parent().layout()
            widgets = []
            for i in [NameText, NameNumber, NameLetter, NameOrigin]:
                widgets.extend(self.parent().findChildren(i))
            widgets.sort(key=self.sort)
            for i in range(len(widgets)):
                layout.insertWidget(i, widgets[i])
            self.drag_flag = False
            self.raise_()

    def sort(self, widget):
        return widget.x()

    def useDash(self):
        return self.dash_check.isChecked()
