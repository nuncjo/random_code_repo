# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scrape_dialog.v1.ui'
#
# Created: Sun Feb 21 18:09:17 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(482, 475)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_plain_text_edit = QtGui.QPlainTextEdit(Dialog)
        self.result_plain_text_edit.setObjectName("result_plain_text_edit")
        self.verticalLayout.addWidget(self.result_plain_text_edit)
        self.start_button = QtGui.QPushButton(Dialog)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        self.stop_button = QtGui.QPushButton(Dialog)
        self.stop_button.setObjectName("stop_button")
        self.verticalLayout.addWidget(self.stop_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Scraper dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.start_button.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.stop_button.setText(QtGui.QApplication.translate("Dialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))

