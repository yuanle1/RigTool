#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import modules.maya_utilities as maya_utilities
class LibraryInfo(QWidget):
    def __init__(self, parent=None):
        super(LibraryInfo, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        font = maya_utilities.font

        font_db = QFontDatabase()
        font_id = font_db.addApplicationFont('D:\\Project\\RigTools\\Resources\\font\\Roboto-Regular.ttf')
        font_families = font_db.applicationFontFamilies(font_id)[0]
        font1 = QFont(font_families)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(5)
        self.main_layout.setContentsMargins(10, 20, 10, 5)

        self.title_layout = QHBoxLayout()
        self.main_layout.addLayout(self.title_layout)


        self.title_icon = QLabel()
        pixmap = QPixmap(maya_utilities.ICONS_DIR + 'block.svg')
        fitPixmap = pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.title_icon.setPixmap(fitPixmap)
        self.title_icon.setFixedWidth(30)
        self.title_icon.setFixedHeight(30)
        self.title_icon.setStyleSheet('''
                                            color:rgb(160,194,211);
                                        ''')
        self.title_layout.addWidget(self.title_icon)
        self.title_layout.setSpacing(10)

        self.title_label = QLabel()
        font1.setPointSize(12)
        self.title_label.setFont(font1)
        self.title_label.setText('Human')
        self.title_label.setStyleSheet('''
                                        border-bottom:1px solid rgb(60, 60, 60);
                                        padding-bottom:2px
                                    ''')
        self.title_layout.addWidget(self.title_label)

        self.main_layout.addStretch()



        font1.setPointSize(10)
        self.describe_textEdit = QTextEdit()
        self.describe_textEdit.setFont(font1)
        self.describe_textEdit.setStyleSheet('''
                                            background-color:rgb(55, 55, 55);
                                            border-radius:8px;
                                            border:1px solid rgb(60, 60, 60);
                                            color:(80, 80, 80);
                                        ''')
        self.main_layout.addWidget(self.describe_textEdit)

        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(5)
        self.main_layout.addLayout(self.button_layout)

        font.setPointSize(10)
        self.export_button = QPushButton()
        self.export_button.setFont(font)
        self.export_button.setMinimumHeight(24)
        self.export_button.setObjectName('button')
        self.export_button.setText('Export')
        icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'blocks/Export.svg', 14, 14)
        print maya_utilities.ICONS_DIR + 'block/Export.svg'
        self.export_button.setIcon(icon)
        self.export_button.setIconSize(QSize(14, 14))
        self.export_button.setStyleSheet('''
                                              #button
                                              {
                                                  color:rgb(180, 180, 180);
                                                  background-color:rgb(61, 61, 61);
                                                  border-radius:3px;
                                                  border:1px solid rgb(71, 71, 71);
                                              } 
                                              #button:hover
                                              {
                                                  background-color:rgb(91, 93, 95)
                                              }
                                              #button:press
                                              {
                                                  background-color:rgb(91, 93, 95)
                                              }
                                          ''')
        self.button_layout.addWidget(self.export_button)

        self.import_button = QPushButton()
        self.import_button.setFont(font)
        self.import_button.setMinimumHeight(24)
        self.import_button.setObjectName('button')
        self.import_button.setText('Import')
        icon = maya_utilities.getIcon(maya_utilities.ICONS_DIR + 'blocks/Import.svg', 14, 14)
        self.import_button.setIcon(icon)
        self.import_button.setIconSize(QSize(14, 14))
        self.import_button.setStyleSheet('''
                                              #button
                                              {
                                                  color:rgb(180, 180, 180);
                                                  background-color:rgb(61, 61, 61);
                                                  border-radius:3px;
                                                  border:1px solid rgb(71, 71, 71);
                                              } 
                                              #button:hover
                                              {
                                                  background-color:rgb(91, 93, 95)
                                              }
                                              #button:press
                                              {
                                                  background-color:rgb(91, 93, 95)
                                              }
                                          ''')
        self.button_layout.addWidget(self.import_button)