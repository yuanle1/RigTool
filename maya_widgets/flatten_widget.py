#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from modules import maya_utilities as maya_utilities
# reload(maya_utilities)
class MFlattentButton(QPushButton):
    def __init__(self, parent=None, size=None):
        super(MFlattentButton, self).__init__(parent)
        self.setCursor(Qt.PointingHandCursor)
        if size:
            self.setFixedSize(QSize(size, size))
            self.setObjectName('flatten_widget')
        self.setStyleSheet('''
                                #flatten_widget
                                {
                                    background-color:transparent;
                                    color:none;
                                    border: none;
                                }
                                #flatten_widget:hover
                                {
                                    border:1px groove #525257;
                                }
                                #flatten_widget:pressed 
                                {
                                    border:1px groove #525257;
                                }
                                #flatten_widget:disabled 
                                {
                                    background-color:transparent;
                                    color:none;
                                    border: none;
                                }
                            ''')
class MColorButton(QPushButton):
    def __init__(self, parent=None, size=None, color=(0, 0, 0)):
        super(MColorButton, self).__init__(parent)
        if size:
            self.setMinimumSize(QSize(size, size))
            self.setMaximumSize(QSize(size, size))
        self.setObjectName('color_button')
        print color
        # {{为转义{
        self.setStyleSheet('''
                                #color_button
                                {{
                                    background-color: rgb{0};
                                    border-radius: {1}px;
                                    border:2px solid transparent;                  
                                }}
                                #color_button:hover
                                {{
                                    background-color: rgb{0};
                                    border-radius: {1}px;
                                    border:None;
                                }}
                  
                            '''.format(tuple(color), size / 2))

class MFlattentCheck(QRadioButton):
    def __init__(self, parent=None):
        super(MFlattentCheck, self).__init__(parent)
        self.setObjectName('MFlattentCheck')
        # font = maya_utilities.font
        # font.setPointSize(8)
        # self.setFont(font)
        self.setStyleSheet('''
                            #MFlattentCheck
                            {
                                spacing: 5px;
                            }
                            #MFlattentCheck:indicator
                            {
                                width:8px;
                                height:8px;
                                border-radius:4px;
                            }

                            MFlattentCheck:indicator:checked
                            {
                                background-color:#8b8b8b;
                            }
                            MFlattentCheck:indicator:unchecked  
                            {
                                background-color:#2a2a2a;
                            }
                            MFlattentCheck:indicator:unchecked:hover
                            {
                                background-color:#3c3c3c;
                            }
                        ''')

class MLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MLineEdit, self).__init__(parent)
        self.setObjectName('MLineEdit')
        font = maya_utilities.font
        font.setPointSize(8)
        self.setFont(font)
        self.setStyleSheet('''
                               border:2px solid;
                               background-color:transparent;
                               border-color:rgb(80,80,80);
                               border-radius:0px;
                           ''')
        self.editingFinished.connect(lambda: self.clearFocus())

    def contextMenuEvent(self, event):
        pass


class MComboBox(QComboBox):
    def __init__(self, width=None, image=None, parent=None, border=1, color=[67, 67, 67]):
        super(MComboBox, self).__init__(parent)
        # font = maya_utilities.font
        # font.setPointSize(8)
        # self.setFont(font)
        self.setObjectName('MComboBox')
        image = 'D:/Project/RigTools/Resources/icons/down_line.png'
        width = 7
        # 必须设置
        self.setView(QListView())
        bar = QScrollBar()
        bar.setObjectName('bar')
        self.view().setVerticalScrollBar(bar)
        self.setStyleSheet('''
                            #MComboBox 
                            {
                                border: %spx solid rgb(80, 80, 80);
                                background-color: rgb(%s, %s, %s);
                                border-radius: 3px;
                                padding-top:1px;
                                padding-bottom:1px;
                                padding-left:5px;
                            }
                            #MComboBox:hover
                            {
                                background-color: rgb(76,76,76);
                            }
                            #MComboBox::drop-down {
                                
                                subcontrol-position: right;
                                border:none;
                            }
                            #MComboBox::down-arrow {
                                
                                image: url(%s);/*自定义图片填充*/
                                width: %spx;
                	            height: %spx;
                            }
                            /* 下拉后，整个下拉窗体样式 */
                            #MComboBox QAbstractItemView {
                                border:1px solid rgb(161,163,161);/*边框宽度、线形、颜色*/
                                background-color: rgb(60, 60, 60);/*背景颜色*/
                            }
                            #MComboBox QAbstractItemView:item:hover {              
                                 background-color: rgb(114,133,131);
            
                            }
                            #MComboBox QAbstractItemView:item:selected {              
                                 background-color: rgb(114,133,131);
            
                            }
                            
                            #bar:vertical
                            {
                                border: none;
                                background: transparent;
                                width: 8px;
                                margin: 0x 0 0px 0;
                            }
                            #bar::handle:vertical
                            {
                                background-color: rgb(78,91,100);
                         
                                border-radius: 4px;
                                border: none;
                            }
                            #bar::add-line:vertical, QScrollBar::sub-line:vertical 
                            {
                                height: 0px;
                            }
                            #bar::add-page:vertical, QScrollBar::sub-page:vertical
                            {
                                background: transparent;
                            }
                            ''' % (border, color[0], color[1], color[2], image, width, width))
    def wheelEvent(self, event):
        pass
class MSpinBox(QSpinBox):
    def __init__(self, up_image=None, down_image=None, parent=None):
        super(MSpinBox, self).__init__(parent)
        up_image = 'D:/Project/RigTools/Resources/icons/up_line.png'
        down_image = 'D:/Project/RigTools/Resources/icons/down_line.png'
        font = maya_utilities.font
        font.setPointSize(8)
        self.setFont(font)
        self.setObjectName('MSpinBox')
        self.setStyleSheet('''
                                MSpinBox
                                {{
                                    border:1px solid rgb(80,80,80);                         
                                    border-radius:3px;
                                    background-color:transparent;
                                }}

                                MSpinBox:up-arrow
                                {{
                                    image: url({0});
                                    padding-right: -4px;
                                    padding-top: -2px;
                                }}
                                MSpinBox:up-button
                                {{
                                    width:10px;
                                }}
                                MSpinBox:down-arrow
                                {{
                                    image: url({1});
                                    padding-right: -4px;
                                    padding-bottom: -2px;
                                }}
                                MSpinBox:down-button
                                {{
                                    width:10px;
                                }}
                        '''.format(up_image, down_image))

        self.editingFinished.connect(lambda: self.clearFocus())
    


    def contextMenuEvent(self, event):
        pass


class MDoubleSpinBox(QDoubleSpinBox):
    def __init__(self, up_image=None, down_image=None, parent=None):
        super(MDoubleSpinBox, self).__init__(parent)
        up_image = 'D:/Project/RigTools/Resources/icons/up_line.png'
        down_image = 'D:/Project/RigTools/Resources/icons/down_line.png'
        font = maya_utilities.font
        font.setPointSize(8)
        self.setFont(font)
        self.setMinimum(float('-inf'))
        self.setMaximum(float('inf'))
        self.setObjectName('MDoubleSpinBox')
        self.setStyleSheet('''
                                MDoubleSpinBox
                                {{
                                    border:1px solid rgb(80,80,80);                         
                                    border-radius:3px;
                                    background-color:transparent;
                                }}

                                MDoubleSpinBox:up-arrow
                                {{
                                    image: url({0});
                                    padding-right: -4px;
                                    padding-top: -2px;
                                }}
                                MDoubleSpinBox:up-button
                                {{
                                    width:10px;
                                }}
                                MDoubleSpinBox:down-arrow
                                {{
                                    image: url({1});
                                    padding-right: -4px;
                                    padding-bottom: -2px;
                                }}
                                MDoubleSpinBox:down-button
                                {{
                                    width:10px;
                                }}
                        '''.format(up_image, down_image))

        self.editingFinished.connect(lambda: self.clearFocus())



    def contextMenuEvent(self, event):
        pass
class MSearchLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MSearchLineEdit, self).__init__(parent)
        # font = maya_utilities.font
        # font.setPointSize(8)
        # self.setFont(font)
        self.setObjectName('MSearchLineEdit')
        self.setStyleSheet('''
                            #MSearchLineEdit
                            {
                                background-image: url('D:/Project/RigTools/Resources/icons/search.svg');
                                padding-left:18px;
                                background-repeat: no-repeat;
                                background-position: center left;
                                border:none;
                                background-color:rgb(38,38,38);
                                border-color:rgb(80,80,80);
                                border-radius:8px;
                            }
                            ''')
        self.editingFinished.connect(self.clearFocus)


class MPointLabel(QLabel):
    def __init__(self, parent=None):
        super(MPointLabel, self).__init__(parent)
        self.setStyleSheet('''
                                background-image:url(D:/Project/RigTools/Resources/icons/point.svg);
                                background-repeat: no-repeat; 
                                background-position: left center ;
                                padding-left:8px;
                            ''')





























