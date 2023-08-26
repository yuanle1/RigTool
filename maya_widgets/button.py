from PySide2 import QtWidgets, QtGui, QtCore

class MButton(QtWidgets.QPushButton):
    def __init__(self, **kwargs):
        parent = kwargs.get('p', kwargs.get('parent', None))
        objectName = kwargs.get('objName', kwargs.get('objectName', None))
        text = kwargs.get('t', kwargs.get('text', 'Button'))
        toolTip = kwargs.get('tt', kwargs.get('toolTip', ''))
        icon = kwargs.get('icon', None)
        super(QtWidgets)