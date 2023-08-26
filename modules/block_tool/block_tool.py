#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import modules.maya_utilities as maya_utilities
import block_outliner
reload(block_outliner)
import block_base
reload(block_base)
import block_builder
reload(block_builder)
import block_utilities
reload(block_utilities)
import fk_widget
import ik_widget
import spline_widget
import end_widget
import child_widget
import hand_widget
import foot_widget

reload(fk_widget)
reload(ik_widget)
reload(spline_widget)
reload(end_widget)
reload(child_widget)
reload(hand_widget)
reload(foot_widget)
WIDGET_DIC = {'Spline': spline_widget.SplineBlock, 'IK': ik_widget.IKBlock, 'FK': fk_widget.FKBlock,
              'End': end_widget.EndBlock, 'Child': child_widget.ChildBlock, 'None': 'None.svg',
              'Hand': hand_widget.HandBlock, 'Foot': foot_widget.FootBlock}


class BlockToolWin(QMainWindow):
    def __init__(self, parent=maya_utilities.maya_main_window()):
        super(BlockToolWin, self).__init__(parent)
        self.resize(500, 500)
        self.block_widget = None
        self.setupUI()
        self.connect()

    def setupUI(self):
        self.setStyleSheet('''background-color:rgb(45, 45, 45);''')

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('zhangjiaqi')



        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_layout = QHBoxLayout(self.main_widget)
        self.main_layout.setSpacing(2)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.tab_frame = QFrame(self.main_widget)
        self.tab_frame.setFixedWidth(45)
        self.tab_frame.setStyleSheet('''
                                                background-color:rgb(54, 54, 54)
                                            ''')
        self.main_layout.addWidget(self.tab_frame)


        self.tab_layout = QVBoxLayout(self.main_widget)
        self.tab_layout.setContentsMargins(0, 0, 0, 0)
        self.tab_frame.setLayout(self.tab_layout)

        self.button_group = QButtonGroup()

        self.library_tab = QPushButton(self.tab_frame)
        self.library_tab.setObjectName('library_tab')
        self.library_tab.setCheckable(True)
        self.library_tab.setChecked(True)
        self.library_tab.setFixedSize(self.tab_frame.width(), self.tab_frame.width())
        icon = maya_utilities.getIcon('D:\\Project\\RigTools\\Resources\\icons\\library.svg', self.tab_frame.width() * 0.6, self.tab_frame.width() * 0.6)
        self.library_tab.setIcon(icon)
        self.library_tab.setIconSize(QSize(self.tab_frame.width() * 0.6, self.tab_frame.width() * 0.6))
        self.library_tab.setStyleSheet('''
                                        #library_tab:checked
                                        {
                                            border: none;
                                            border-left:3px solid rgb(166, 150, 104);
                                            background-color: rgb(60, 60, 60);
                                        }
                                        #library_tab:checked:hover
                                        {
                                            border: none;
                                            border-left:3px solid rgb(166, 150, 104);
                                            background-color: rgb(60, 60, 60);
                                        }
                                        #library_tab:hover
                                        {
                                            border: none;
                                            border-left:3px outset transparent;
                                            background-color: rgb(60, 60, 60);
                                        }
                                        #library_tab
                                        {
                                            border:none;
                                            background-color:transparent;
                                            border-left:3px outset transparent;
                                        }
                                        ''')
        self.tab_layout.addWidget(self.library_tab)
        self.button_group.addButton(self.library_tab)

        self.block_tab = QPushButton(self.tab_frame)
        self.block_tab.setObjectName('block_tab')
        self.block_tab.setCheckable(True)
        self.block_tab.setFixedSize(self.tab_frame.width(), self.tab_frame.width())
        icon = maya_utilities.getIcon('D:\\Project\\RigTools\\Resources\\icons\\block.svg', self.tab_frame.width() * 0.6, self.tab_frame.width() * 0.6)
        self.block_tab.setIcon(icon)
        self.block_tab.setIconSize(QSize(self.tab_frame.width() * 0.6, self.tab_frame.width() * 0.6))
        self.block_tab.setStyleSheet('''
                                                #block_tab:checked
                                                {
                                                    border: none;
                                                    border-left:3px solid rgb(166, 150, 104);
                                                    background-color: rgb(60, 60, 60);
                                                }
                                                #block_tab:checked:hover
                                                {
                                                    border: none;
                                                    border-left:3px solid rgb(166, 150, 104);
                                                    background-color: rgb(60, 60, 60);
                                                }
                                                #block_tab:hover
                                                {
                                                    border: none;
                                                    border-left:3px outset transparent;
                                                    background-color: rgb(60, 60, 60);
                                                }
                                                #block_tab
                                                {
                                                    border:none;
                                                    background-color:transparent;
                                                    border-left:3px outset transparent;
                                                }
                                                ''')
        self.tab_layout.addWidget(self.block_tab)
        self.button_group.addButton(self.block_tab)

        self.main_splitter = QSplitter(Qt.Horizontal)
        self.main_layout.addWidget(self.main_splitter)

        self.block_outliner_widget = block_outliner.BlockOutliner()
        self.main_splitter.addWidget(self.block_outliner_widget)

        self.right_widget = QWidget()
        self.main_splitter.addWidget(self.right_widget)

        self.block_layout = QVBoxLayout()
        self.block_layout.setContentsMargins(8, 0, 8, 0)
        self.block_layout.setSpacing(2)
        self.right_widget.setLayout(self.block_layout)

        self.block_base_widget = block_base.BlockBase()
        self.block_layout.addWidget(self.block_base_widget)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet('''
                                                            border-top:1px solid rgb(60, 60, 60);
                                                        ''')
        line.setFixedHeight(1)
        self.block_layout.addWidget(line)

        self.block_layout.addStretch()

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet('''
                                                    border-top:1px solid rgb(60, 60, 60);
                                                ''')
        line.setFixedHeight(1)
        self.block_layout.addWidget(line)

        self.block_builder_widget = block_builder.BlockBuilder()
        self.block_layout.addWidget(self.block_builder_widget)





    def connect(self):
        pass
        # self.block_outliner_widget.block_tree.currentItemChanged.connect(lambda: self.block_attr_widget.refreshBlockWidget(self.block_outliner_widget.getCurrentBlock()))
        # # self.block_attr_widget.button.clicked.connect(lambda : block_utilities.updateBlockOrient(self.block_outliner_widget.getAllBlocks()))
        # self.block_attr_widget.mirror_check.toggled.connect(lambda: self.block_outliner_widget.setCurrentBlockMirror(not self.block_attr_widget.mirror_check.isChecked()))
        # side_list = ['M', 'L', 'R']
        # self.block_attr_widget.side_cmobo.currentIndexChanged.connect(lambda: self.block_outliner_widget.setCurrentBlockSide(side_list[self.block_attr_widget.side_cmobo.currentIndex()]))

        self.block_outliner_widget.block_tree.currentItemChanged.connect(lambda :self.refreshBlockWidget(self.block_outliner_widget.getCurrentBlock()))
        self.block_builder_widget.reorient_button.clicked.connect(lambda :block_utilities.updateBlockOrient(self.block_outliner_widget.getAllBlocks()))

    def showMessage(self):
        self.statusBar.showMessage('zhangjiaqi')



    def refreshBlockWidget(self, block):
        function = block.getFunction()
        self.block_base_widget.setJoint(block.getJoint())
        self.block_base_widget.setFunction(function)
        self.block_base_widget.setMirror(block.getMirror())
        self.block_base_widget.setSide(block.getSide())
        self.block_base_widget.setModules(function)

        if self.block_widget:
            self.block_widget.deleteLater()
        self.block_widget = WIDGET_DIC[function](block=block)
        self.block_layout.insertWidget(2, self.block_widget)

