#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from functools import partial


class MTabWidget(QWidget):
    def __init__(self, parent=None):
        super(MTabWidget, self).__init__(parent=None)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(5)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.tab_layout = QHBoxLayout()
        self.tab_layout.setContentsMargins(0, 0, 0, 0)

        self.content_layout = QVBoxLayout()
        self.main_layout.addLayout(self.tab_layout)
        self.main_layout.addLayout(self.content_layout)
        self.tab_list = []
        self.tab_dic = {}
        self.temp_tab = None

    def addTab(self, widget, title):
        tab = QPushButton()
        tab.setCheckable(True)
        tab.setChecked(False)
        tab.setText(title)
        tab.setMinimumWidth(55)
        tab.setMinimumHeight(25)
        tab.setObjectName('tab')
        tab.setStyleSheet('''
                            #tab:checked
                            {
                                border: none;
                                border-bottom:3px outset #4e85bb;
                            }
                            #tab
                            {
                                border: none;
                                border-bottom:3px outset #7b7a65;
                            }
                            ''')
        self.tab_list.append(tab)
        self.tab_dic[tab] = widget
        self.tab_layout.addWidget(tab)
        self.tab_dic[tab].setVisible(False)
        self.content_layout.addWidget(self.tab_dic[tab])
        tab.clicked.connect(partial(self.change_content, tab))

    def change_content(self, tab):
        self.temp_tab.setChecked(False)
        self.tab_dic[self.temp_tab].setVisible(False)
        tab.setChecked(True)
        self.tab_dic[tab].setVisible(True)
        self.temp_tab = tab

    def addStretch(self, index=None):
        if index == None:
            self.tab_layout.addStretch()
        else:
            self.tab_layout.addStretch(index)

    def setCurrentIndex(self, index):
        self.temp_tab = self.tab_list[index]
        self.tab_list[index].click()


