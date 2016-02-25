# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.v1.ui'
#
# Created: Sun Feb 21 18:08:39 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(315, 132)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 281, 83))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_scraper_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.open_scraper_button.setObjectName("open_scraper_button")
        self.verticalLayout.addWidget(self.open_scraper_button)
        self.load_urls_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.load_urls_button.setObjectName("load_urls_button")
        self.verticalLayout.addWidget(self.load_urls_button)
        self.clear_urls_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.clear_urls_button.setObjectName("clear_urls_button")
        self.verticalLayout.addWidget(self.clear_urls_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 315, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Main window", None, QtGui.QApplication.UnicodeUTF8))
        self.open_scraper_button.setText(QtGui.QApplication.translate("MainWindow", "Open Scraper Window", None, QtGui.QApplication.UnicodeUTF8))
        self.load_urls_button.setText(QtGui.QApplication.translate("MainWindow", "Load urls", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_urls_button.setText(QtGui.QApplication.translate("MainWindow", "Clear urls", None, QtGui.QApplication.UnicodeUTF8))

