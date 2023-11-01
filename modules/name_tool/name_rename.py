#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from maya_widgets import flatten_widget as flatten_widget
from maya_widgets import round_widget as round_widget
from modules import maya_utilities as maya_utilities
import name_component
import maya.cmds as mc
# reload(flatten_widget)
## reload(round_widget)
# reload(maya_utilities)
# # reload(name_component)

class NameRename(round_widget.MRoundWidget):
    def __init__(self, parent=None):
        super(NameRename, self).__init__(parent)
        self.setupUI()
        self.connect()

    def setupUI(self):
        font = maya_utilities.font
        title_font = maya_utilities.getFont()

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(6, 4, 14, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        self.title_layout = QHBoxLayout()
        self.main_layout.addLayout(self.title_layout)

        self.title_label = QLabel()
        self.title_label.setFixedWidth(52)
        self.title_label.setText('Rename')
        title_font.setPointSize(10)
        title_font.setStyleStrategy(QFont.PreferAntialias)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet('''
                                                    color:rgb(126,152,159);
                                                ''')

        self.title_layout.addWidget(self.title_label)

        self.title_line = QFrame()
        self.title_line.setFrameShape(QFrame.HLine)
        self.title_layout.addWidget(self.title_line)
        self.title_line.setFixedHeight(2)
        self.title_line.setStyleSheet('''
                                                    background-color: rgb(126,152,159);
                                              ''')

        self.layout = QHBoxLayout()
        self.layout.addStretch(1)
        self.layout.setContentsMargins(0, 0, 10, 4)
        self.layout.setSpacing(16)
        self.main_layout.addLayout(self.layout)

        self.add_button = flatten_widget.MFlattentButton(size=14)
        self.add_button.setIcon(maya_utilities.getIcon('D:\Project\RigTools\Resources\icons\\add_cross.svg', 14, 14))
        self.add_button.setIconSize(QSize(14, 14))
        self.layout.addWidget(self.add_button)

        self.restore_button = flatten_widget.MFlattentButton(size=14)
        self.restore_button.setIcon(maya_utilities.getIcon('D:\Project\RigTools\Resources\icons\\restore.png', 12, 12))
        self.restore_button.setIconSize(QSize(12, 12))
        self.layout.addWidget(self.restore_button)

        self.layout2 = QHBoxLayout()
        self.layout2.setContentsMargins(10, 0, 4, 0)
        self.main_layout.addLayout(self.layout2)

        self.rename_frame = QFrame()
        self.rename_frame.setObjectName('rename_frame')
        self.layout2.addWidget(self.rename_frame)
        self.rename_frame.setMinimumHeight(96)
        self.rename_frame.setStyleSheet('''
                                            #rename_frame
                                            {
                                                border:2px solid rgb(80, 80, 80);
                                                border-radius: 10px;
                                            }
                                        ''')
        self.rename_layout = QHBoxLayout()
        self.rename_layout.setSpacing(2)
        self.rename_layout.setContentsMargins(2, 0, 2, 0)
        self.rename_frame.setLayout(self.rename_layout)

        self.name_text_widget = name_component.NameText(self.rename_frame)
        self.rename_layout.addWidget(self.name_text_widget)

        self.name_number_widget = name_component.NameNumber(self.rename_frame)
        self.rename_layout.addWidget(self.name_number_widget)

        self.name_letter_widget = name_component.NameLetter(self.rename_frame)
        self.rename_layout.addWidget(self.name_letter_widget)

        # self.name_origin_widget = name_component.NameOrigin(self.rename_frame)
        # self.rename_layout.addWidget(self.name_origin_widget)

        # self.rename_spacer = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # self.rename_spacer.spa('rename_spacer')
        # self.rename_layout.addItem(self.rename_spacer)

        self.rename_layout.addStretch()

        self.check_layout = QHBoxLayout()
        self.main_layout.addLayout(self.check_layout)
        self.check_layout.setContentsMargins(60, 10, 5, 0)

        self.check_ground = QButtonGroup()

        self.selected_check = flatten_widget.MFlattentCheck()
        self.selected_check.setText('Selected')
        self.selected_check.setChecked(True)
        self.check_layout.addWidget(self.selected_check)
        self.check_ground.addButton(self.selected_check)

        self.hierarchy_check = flatten_widget.MFlattentCheck()
        self.hierarchy_check.setText('Hierarchy')
        self.check_layout.addWidget(self.hierarchy_check)
        self.check_ground.addButton(self.hierarchy_check)

        self.two_dimensional_check = flatten_widget.MFlattentCheck()
        self.two_dimensional_check.setText('Two-dimensional')
        self.check_layout.addWidget(self.two_dimensional_check)
        self.check_ground.addButton(self.two_dimensional_check)

        self.button_layout = QHBoxLayout()
        self.button_layout.setContentsMargins(8, 5, 0, 5)
        self.main_layout.addLayout(self.button_layout)

        self.rename_button = QPushButton()
        self.rename_button.setText('Rename')
        font.setPointSize(8)
        self.rename_button.setFont(font)
        self.rename_button.setObjectName('rename_button')
        self.rename_button.setMinimumHeight(25)
        self.button_layout.addWidget(self.rename_button)
        self.rename_button.setStyleSheet('''
                                                #rename_button
                                                {
                                                    color:rgb(200, 200, 200);
                                                    background-color:rgb(73, 73, 73);
                                                    border-radius:3px;
                                                    border:2px solid rgb(80, 80, 80);
                                                }
                                                #rename_button:hover
                                                {
                                                    color:rgb(200, 200, 200);
                                                    background-color:rgb(85,94,96);
                                                    border-radius:3px;
                                                    border:2px solid rgb(80, 80, 80);
                                                }
                                                #rename_button:pressed
                                                {
                                                    color:rgb(200, 200, 200);
                                                    background-color:rgb(85,102,114);
                                                    border-radius:3px;
                                                    border:2px solid rgb(80, 80, 80);
                                                }
                                                ''')
        self.main_layout.addStretch()


        self.main_menu = QMenu(self)
        self.main_menu.setFont(font)
        self.main_menu.setFixedSize(82, 82)
        self.main_menu.setObjectName('main_menu')
        self.main_menu.setStyleSheet('''
                                          #main_menu
                                          {
                                              border: 2px solid rgb(159,167,163);
                                              border-radius: 0px;
                                              color:rgb(172,172,172);
                                          }
                                          #main_menu:item
                                          {
                                              border: 2px solid rgb(186,186,186);
                                              padding:0px 25px;
                                              border-radius: 4px;
                                              margin:1px 1px 1px 1px;
                                              width:20px;
                                              height:20px;
                                          }
                                          #main_menu:item:selected
                                          {
                                                background-color:rgb(105,121,122);
                                          }
                                          #main_menu:icon
                                          {
                                               padding-left: 5px;
                                          
                                          }
                                      ''')

        text_icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/letter_T.png', 16, 16)
        self.text_action = QAction(text_icon, 'Text', self)
        self.main_menu.addAction(self.text_action)

        number_icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/number_2.png', 14, 14)
        self.number_action = QAction(number_icon, 'Number', self)
        self.main_menu.addAction(self.number_action)

        letter_icon = maya_utilities.getIcon('D:/Project/RigTools/Resources/icons/letter_A.png', 20, 20)
        self.letter_action = QAction(letter_icon, 'Letter', self)
        self.main_menu.addAction(self.letter_action)


    def connect(self):
        self.add_button.clicked.connect(self.create_menu)
        # self.restore_button.clicked.connect(self)
        self.text_action.triggered.connect(lambda: self.add_component(name_component.NameText))
        self.number_action.triggered.connect(lambda: self.add_component(name_component.NameNumber))
        self.letter_action.triggered.connect(lambda: self.add_component(name_component.NameLetter))
        self.rename_button.clicked.connect(self.rename)
    def add_component(self, component_type):
        component_widgets = []
        for i in [name_component.NameText, name_component.NameNumber, name_component.NameLetter]:
            component_widgets.extend(self.rename_frame.findChildren(i))
        component_widget = component_type(self.rename_frame)
        self.rename_layout.insertWidget(len(component_widgets), component_widget)

    def create_menu(self):
        self.main_menu.exec_(self.mapToGlobal(QPoint(self.add_button.x(), self.add_button.y() + self.add_button.height())))

    def sort(self, widget):
        return self.rename_layout.indexOf(widget)

    def renameDuplicate(self):
        sel_list = mc.ls(selection=True)
        for obj in sel_list:
            # 获取物体的基本名称
            base_name = obj.split("|")[-1]
            # 检查是否有重名物体
            duplicates = mc.ls(base_name)
            if len(duplicates) > 1:
                # 对重名物体进行重命名
                for i, dup in enumerate(duplicates):
                    new_name = "{}_{}".format(base_name, i + 1)
                    mc.rename(dup, new_name)
        mc.select(clear=True)

    def rename(self):
        with maya_utilities.Undoable():
            ori_list = mc.ls(sl=True, uuid=True)
            component_widgets = []
            for i in [name_component.NameText, name_component.NameNumber, name_component.NameLetter]:
                component_widgets.extend(self.rename_frame.findChildren(i))
            if not component_widgets:
                return
            component_widgets.sort(key=self.sort)
            first_base = None
            second_base = None
            third_base = None
            NameNumber = name_component.NameNumber
            NameLetter = name_component.NameLetter
            NameText = name_component.NameText
            for component_widget in component_widgets:
                component_type = type(component_widget)
                if component_type == NameLetter or component_type == NameNumber:
                    first_base = component_widget
                    break
                elif component_type == NameText:
                    if not component_widget.useOwn():
                        if ',' in component_widget.getText() or ';' in component_widget.getText():
                            first_base = component_widget
                            break

            if first_base:
                for component_widget in component_widgets:
                    if component_widget == first_base:
                        continue
                    component_type = type(component_widget)
                    if component_type == NameLetter or component_type == NameNumber:
                        second_base = component_widget
                        break
                    elif component_type == NameText:
                        if not component_widget.useOwn():
                            if ',' in component_widget.getText() or ';' in component_widget.getText():
                                second_base = component_widget
                                break
            if second_base:
                for component_widget in component_widgets:
                    if component_widget == first_base or component_widget == second_base:
                        continue
                    component_type = type(component_widget)
                    if component_type == NameLetter or component_type == NameNumber:
                        third_base = component_widget
                        break
                    elif component_type == NameText:
                        if not component_widget.useOwn():
                            if ',' in component_widget.getText() or ';' in component_widget.getText():
                                third_base = component_widget
                                break

            sel_list = mc.ls(sl=True, sn=False, transforms=True)
            if not sel_list:
                return
            if self.selected_check.isChecked():
                rename_list = sel_list
            else:
                mc.select(hi=True)
                rename_list = mc.ls(sl=True, sn=False, transforms=True)
            uuid_list = mc.ls(rename_list, uuid=True)
            # 去重命名
            self.renameDuplicate()
            for uuid in uuid_list:
                mc.select(mc.ls(uuid)[0], add=True)
            rename_list = mc.ls(sl=True)

            if self.selected_check.isChecked() or self.hierarchy_check.isChecked():
                for i, rename_obj in enumerate(rename_list):
                    new_name = ''
                    for component_widget in component_widgets:
                        component_type = type(component_widget)
                        if component_type == NameText:
                            if component_widget.useOwn():
                                new_name += rename_obj
                            else:
                                text = component_widget.getText()
                                if component_widget == first_base:
                                    separator = text.split(',')
                                    separator = [item.split(';') for item in separator]
                                    separator_list = []
                                    for item in separator:
                                        separator_list.extend(item)
                                    if i < len(separator_list):
                                        new_name += separator_list[i]
                                    else:
                                        new_name += separator_list[-1]
                                else:
                                    new_name += text
                        elif component_type == NameNumber:
                            start_num = component_widget.getStartNum()
                            digits_num = component_widget.getDigits()
                            if component_widget == first_base:
                                new_name += str(start_num + i).zfill(digits_num)
                            else:
                                new_name += str(start_num).zfill(digits_num)
                        elif component_type == NameLetter:
                            letter = component_widget.getLetter()
                            if component_widget == first_base:
                                new_name += chr(ord(letter) + i)
                            else:
                                new_name += letter
                        if component_widget.useDash():
                            new_name += '_'
                    mc.rename(rename_obj, new_name)

            else:
                top_list = []
                for obj in rename_list:
                    if len(set(mc.ls(obj, long=True)[0].split('|')) & set(rename_list)) == 1:
                        top_list.append(obj)
                for i, top_obj in enumerate(top_list):
                    new_name = ''
                    for component_widget in component_widgets:
                        component_type = type(component_widget)
                        if component_type == NameText:
                            if component_widget.useOwn():
                                new_name += top_obj
                            else:
                                text = component_widget.getText()
                                separator = text.split(',')
                                separator = [item.split(';') for item in separator]
                                separator_list = []
                                for item in separator:
                                    separator_list.extend(item)
                                if component_widget == first_base:
                                    if i < len(separator_list):
                                        new_name += separator_list[i]
                                    else:
                                        new_name += separator_list[-1]
                                elif component_widget == second_base:
                                    if i < len(separator_list):
                                        new_name += separator_list[i]
                                    else:
                                        new_name += separator_list[-1]
                                else:
                                    new_name += text
                        elif component_type == NameNumber:
                            start_num = component_widget.getStartNum()
                            digits_num = component_widget.getDigits()
                            if component_widget == first_base:
                                new_name += str(start_num + i).zfill(digits_num)
                            else:
                                new_name += str(start_num).zfill(digits_num)
                        elif component_type == NameLetter:
                            letter = component_widget.getLetter()
                            if component_widget == first_base:
                                new_name += chr(ord(letter) + i)
                            else:
                                new_name += letter
                        if component_widget.useDash():
                            new_name += '_'

                    top_obj = mc.rename(top_obj, new_name)
                    children = mc.listRelatives(top_obj, ad=True, type='transform') or []
                    parent_depth = len(mc.ls(top_obj, long=True)[0].split('|'))
                    depth_list = []
                    for child in children:
                        new_name = ''
                        child_depth = len(mc.ls(child, long=True)[0].split('|'))
                        depth = child_depth - parent_depth
                        breadth = 1 + depth_list.count(depth)
                        depth_list.append(depth)

                        for component_widget in component_widgets:
                            component_type = type(component_widget)
                            if component_type == NameText:
                                if component_widget.useOwn():
                                    new_name += top_obj
                                else:
                                    text = component_widget.getText()
                                    separator = text.split(',')
                                    separator = [item.split(';') for item in separator]
                                    separator_list = []
                                    for item in separator:
                                        separator_list.extend(item)
                                    if component_widget == first_base:
                                        if i < len(separator_list):
                                            new_name += separator_list[i]
                                        else:
                                            new_name += separator_list[-1]
                                    elif component_widget == second_base:
                                        if depth < len(separator_list):
                                            new_name += separator_list[depth]
                                        else:
                                            new_name += separator_list[-1]
                                    elif component_widget == third_base:
                                        if breadth < len(separator_list):
                                            new_name += separator_list[breadth-1]
                                        else:
                                            new_name += separator_list[-1]
                                    else:
                                        new_name += text
                            elif component_type == NameNumber:
                                start_num = component_widget.getStartNum()
                                digits_num = component_widget.getDigits()
                                if component_widget == first_base:
                                    new_name += str(start_num + i).zfill(digits_num)
                                elif component_widget == second_base:
                                    new_name += str(start_num + depth).zfill(digits_num)
                                elif component_widget == third_base:
                                    new_name += str(start_num + breadth - 1).zfill(digits_num)
                                else:
                                    new_name += str(start_num).zfill(digits_num)
                            elif component_type == NameLetter:
                                letter = component_widget.getLetter()
                                if component_widget == first_base:
                                    new_name += chr(ord(letter) + i)
                                elif component_widget == second_base:
                                    new_name += chr(ord(letter) + depth)
                                elif component_widget == third_base:
                                    new_name += chr(ord(letter) + breadth - 1)
                                else:
                                    new_name += letter
                            if component_widget.useDash():
                                new_name += '_'
                        top_obj = mc.rename(child, new_name)

            mc.select(clear=True)
            # for uuid in uuid_list:
            #     mc.select(mc.ls(uuid)[0], add=True)
            for uuid in ori_list:
                mc.select(mc.ls(uuid)[0], add=True)



































