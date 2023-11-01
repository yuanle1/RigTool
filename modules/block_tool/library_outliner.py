#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import modules.maya_utilities as maya_utilities
import maya_widgets.flatten_widget as flatten_widget

import os
LIRBRARY_PATH = '/'.join(os.path.dirname(__file__).split('\\')[:-2]) + '/Resources/library/'

class LibraryOutliner(QWidget):
    def __init__(self, parent=None):
        super(LibraryOutliner, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        font = maya_utilities.font
        title_font = maya_utilities.getFontTitle()
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(5)
        self.main_layout.setContentsMargins(5, 10, 5, 5)

        self.title_layout = QHBoxLayout(self)
        self.title_layout.setContentsMargins(5, 0, 2, 0)
        self.main_layout.addLayout(self.title_layout)

        self.title_label = QLabel(self)
        title_font.setPointSize(11)
        self.title_label.setFont(title_font)
        self.title_label.setText('Outliner')
        self.title_label.setStyleSheet('''
                                                color:rgb(134,134,134);  
                                            ''')
        self.title_layout.addWidget(self.title_label)
        self.title_layout.setSpacing(12)
        self.title_layout.addStretch()

        self.save_button = flatten_widget.MFlattentButton(size=14)
        self.save_button.setIcon(maya_utilities.getIcon('D:\Project\RigTools\Resources\icons\\block_save.svg', 12, 12))
        self.save_button.setIconSize(QSize(12, 12))
        self.title_layout.addWidget(self.save_button)

        self.remove_button = flatten_widget.MFlattentButton(size=14)
        self.remove_button.setIcon(
            maya_utilities.getIcon('D:\Project\RigTools\Resources\icons\\block_remove.svg', 14, 14))
        self.remove_button.setIconSize(QSize(14, 14))
        self.title_layout.addWidget(self.remove_button)

        self.reset_button = flatten_widget.MFlattentButton(size=14)
        self.reset_button.setIcon(
            maya_utilities.getIcon('D:\Project\RigTools\Resources\icons\\block_reload.svg', 14, 14))
        self.reset_button.setIconSize(QSize(14, 14))
        self.title_layout.addWidget(self.reset_button)

        self.search_layout = QHBoxLayout(self)
        self.search_layout.setContentsMargins(2, 0, 0, 1)
        self.main_layout.addLayout(self.search_layout)

        self.search_lineEdit = flatten_widget.MSearchLineEdit()
        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setFixedHeight(20)
        self.search_layout.addWidget(self.search_lineEdit)

        self.positive_order_button = flatten_widget.MFlattentButton(size=20)
        self.positive_order_button.setIcon(
            maya_utilities.getIcon('D:\Project\RigTools\Resources\icons\\positive_order.svg', 14, 14))
        self.positive_order_button.setIconSize(QSize(20, 20))
        self.search_layout.addWidget(self.positive_order_button)

        self.reverse_order_button = flatten_widget.MFlattentButton(size=20)
        self.reverse_order_button.setIcon(
            maya_utilities.getIcon('D:\Project\RigTools\Resources\icons\\reverse_order.svg', 14, 14))
        self.reverse_order_button.setIconSize(QSize(20, 20))
        self.search_layout.addWidget(self.reverse_order_button)



        self.library_tree = QTreeWidget(self)
        font.setPointSize(10)
        self.library_tree.setFont(font)
        self.library_tree.setHeaderHidden(True)
        self.library_tree.setFocusPolicy(Qt.NoFocus)
        self.main_layout.addWidget(self.library_tree)
        self.library_tree.setStyleSheet('''
                                         QTreeWidget
                                         {
                                             border-top:1px solid rgb(60, 60, 60);

                                         }
                                         QTreeWidget:item
                                         {
                                             background-color: rgb(45, 45, 45);
                                             padding-left:2px;
                                             border-bottom:1px solid rgb(60, 60, 60);
                                         }
                                         QTreeWidget:item:has-children
                                         {
                                             background-color: rgb(45, 45, 45);
                                             padding-left:2px
                            
                                         }
                                        QTreeWidget:item:!has-children
                                         {
                                             background-color: rgb(45, 45, 45);
                                             padding-left:20px
                             
                                         }
                                         QTreeWidget:item:selected
                                         {
                                             background-color: rgb(77,80,82);
                                             
                                         }
                                   
                         
                                         QTreeWidget:branch:selected
                                         {
                                             background-color: rgb(77,80,82);
                                         }


                                         QTreeWidget::branch:open:has-children
                                         {
                                             image:none;
                                         }
                                         QTreeWidget::branch:closed:has-children
                                         {
                                             image:none

                                         }
                                         QScrollBar:vertical
                                         {
                                             background: transparent;
                                             width: 10px;
                                             margin: 2px 0px 2px 0;
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
        self.main_layout.addStretch()
        self.library_tree.setIndentation(0)
        for library_type in os.listdir(LIRBRARY_PATH):
            type_item = QTreeWidgetItem()
            type_item.setText(0, library_type)
            type_item.setSizeHint(0, QSize(0, 26))
            self.library_tree.addTopLevelItem(type_item)
            icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'blocks/file.svg', 20, 20)
            self.library_tree.setIconSize(QSize(20, 20))
            type_item.setIcon(0, icon)

            path = os.listdir(os.path.join(LIRBRARY_PATH, library_type))
            for library_type_file in path:
                library_type_file = library_type_file.split('.')[0]
                file_item = QTreeWidgetItem()
                file_item.setText(0, library_type_file)
                file_item.setSizeHint(0, QSize(0, 26))
                type_item.addChild(file_item)
                icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'block.svg', 16, 16)
                self.library_tree.setIconSize(QSize(16, 16))
                file_item.setIcon(0, icon)









