# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scrape_dialog.v1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(482, 475)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.result_plain_text_edit = QtGui.QPlainTextEdit(Dialog)
        self.result_plain_text_edit.setObjectName(_fromUtf8("result_plain_text_edit"))
        self.verticalLayout.addWidget(self.result_plain_text_edit)
        self.start_button = QtGui.QPushButton(Dialog)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.verticalLayout.addWidget(self.start_button)
        self.stop_button = QtGui.QPushButton(Dialog)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.verticalLayout.addWidget(self.stop_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Scraper dialog", None))
        self.start_button.setText(_translate("Dialog", "Start", None))
        self.stop_button.setText(_translate("Dialog", "Stop", None))

