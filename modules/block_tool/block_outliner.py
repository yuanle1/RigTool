#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import maya.cmds as mc

import modules.maya_utilities as maya_utilities
import block_utilities

reload(block_utilities)
import maya_widgets.flatten_widget as flatten_widget

import block_info
reload(block_info)

ICON_DIC = {'Spline': 'Spline.svg', 'IK': 'IK.svg', 'FK': 'FK.svg', 'End': 'End.png', 'Child': 'Child.svg',
            'None': 'None.svg', 'Hand': 'Hand.svg', 'Foot': 'Foot.svg'}
SIZE_DIC = {'Spline': [12, 12], 'IK': [12, 12], 'FK': [12, 12], 'End': [12, 12], 'Child': [12, 12],
            'None': [12, 12], 'Hand': [14, 14], 'Foot': [16, 16]}

class BlockOutliner(QWidget):
    currentItemChanged = Signal()
    changed = Signal()
    def __init__(self, parent=None):
        super(BlockOutliner, self).__init__(parent)
        self.blocks = []
        self.setupUI()
        self.connect()


    def setupUI(self):
        # self.setStyleSheet('''background-color:rgb(50, 50, 50);''')
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

        # self.line = QFrame()
        # self.line.setFrameShape(QFrame.HLine)
        # self.line.setStyleSheet('''
        #                             background-color:rgb(60, 60, 60);
        #                         ''')
        # self.line.setFixedHeight(1)
        # self.main_layout.addWidget(self.line)

        self.block_tree = QTreeWidget(self)
        font.setPointSize(9)
        # title_font.setPointSize(8)
        self.block_tree.setFont(font)

        # font1 = QFont('Microsoft YaHei', 8, QFont.Normal)
        # self.block_tree.setFont(font1)

        self.block_tree.setHeaderHidden(True)
        self.block_tree.setFocusPolicy(Qt.NoFocus)
        self.block_tree.setStyleSheet('''
                                        QTreeWidget
                                        {
                                            border-top:1px solid rgb(60, 60, 60);
                                            
                                        }
                                        QTreeWidget:item[text]
                                        {
                                            padding-left: 20px;
                                        }
                                        QTreeWidget:item:selected
                                        {
                                            background-color: rgb(77,80,82);
                                            border: none;
                                        }
                                        QTreeWidget:branch:selected
                                        {
                                            background-color: rgb(77,80,82);
                                            border: none;
                                        }


                                        QTreeWidget::branch:open:has-children
                                        {
                                            image:url(D:/Project/RigTools/Resources/icons/blocks/down.svg)


                                        }
                                        QTreeWidget::branch:closed:has-children
                                        {
                                            image:url(D:/Project/RigTools/Resources/icons/blocks/right.svg)

                                        }

                                        QScrollBar:vertical
                                        {
                                            border: none;
                                            background: transparent;
                                            width: 10px;
                                            margin: 2px 0 2px 0;
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

        font.setPointSize(8)
        self.block_tree.setIndentation(15)
        self.main_layout.addWidget(self.block_tree)
        self.refreshOutliner()
        self.block_info_widget = block_info.BlockInfo()
        self.main_layout.addWidget(self.block_info_widget)

    def connect(self):
        self.search_lineEdit.textChanged.connect(self.search)

    def showParent(self, item):
        if item:
            parent_item = item.parent()
            if parent_item:
                parent_item.setHidden(False)
                self.showParent(parent_item)


    def search(self, search_text, item=None):
        if item:
            if search_text.lower() in item.text(0).lower():
                item.setHidden(False)
                self.showParent(item)
            else:
                item.setHidden(True)
            for i in range(item.childCount()):
                child_item = item.child(i)
                self.search(search_text, item=child_item)
        else:
            for i in range(self.block_tree.topLevelItemCount()):
                self.search(search_text, self.block_tree.topLevelItem(i))

    def refreshOutliner(self):
        block_utilities.ensureAllBlockAttrs()
        if not mc.objExists('Block'):
            return
        mc.select('Block', hi=True)
        block_joints = mc.ls(sl=True, type='joint')

        item_dic = {}
        for block_joint in block_joints:
            block = block_utilities.blockInstance(block_joint)
            parent = mc.listRelatives(block_joint, p=True, type='joint') or [None]
            parent = parent[0]
            block_item = QTreeWidgetItem()
            block_item.setSizeHint(0, QSize(0, 18))
            block_item.setText(0, block_joint)
            block_item.block = block


            if not parent:
                self.block_tree.addTopLevelItem(block_item)
            else:
                parent_item = item_dic[parent]
                parent_item.addChild(block_item)
                block.setParentBlock(parent_item.block)
                parent_item.block.addChildrenBlock(block)

            self.blocks.append(block)

            function = block.getFunction()
            icon = ICON_DIC[function]
            icon_size = SIZE_DIC[function]
            icon = maya_utilities.getIcon('D:\\Project\\RigTools\\Resources\\icons\\blocks\\{}'.format(icon), icon_size[0], icon_size[1])
            block_item.setIcon(0, icon)
            self.block_tree.setIconSize(QSize(icon_size[0], icon_size[1]))

            item_dic[block_joint] = block_item

        block_utilities.ensureAllBlockInfo(self.getAllBlocks())
        self.block_tree.expandAll()
        mc.select(clear=True)


    def getCurrentBlock(self):
        if self.block_tree.currentItem():
            return self.block_tree.currentItem().block
        else:
            return None


    def getAllBlocks(self):
        return self.blocks

