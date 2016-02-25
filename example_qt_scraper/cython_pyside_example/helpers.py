# -*- coding:utf-8 -*-

from PySide.QtGui import *


def load_txt_file(obj):
    try:
        filename = QFileDialog.getOpenFileName(obj, 'Open file', filter='Text files (*.txt)')
        if filename[0]:
            with open(filename[0]) as f:
                return f.readlines()
        else:
            return []
    except Exception as err:
        QMessageBox.information(obj, 'Error', repr(err))
        return []

