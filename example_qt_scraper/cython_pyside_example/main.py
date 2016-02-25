# -*- coding:utf-8 -*-

import sys

from PySide.QtGui import *

from gui.main_window import Ui_MainWindow
from scraper import ScraperDialog
import helpers


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.scraper_dialog = ScraperDialog()

        self.open_scraper_button.clicked.connect(self.show_scraper_dialog)
        self.load_urls_button.clicked.connect(self.load_urls)
        self.clear_urls_button.clicked.connect(self.clear_urls)

    def show_scraper_dialog(self):
        if self.scraper_dialog.urls:
            self.scraper_dialog.show()
        else:
            QMessageBox.information(self, 'Warning', 'Load some urls first!')

    def load_urls(self, urls=None):
        self.scraper_dialog.urls = self.load_urls_list(urls)
        self.update_statusbar()

    def load_urls_list(self, urls=None):
        urls = urls or []
        if not urls:
            return helpers.load_txt_file(self)
        else:
            return urls

    def clear_urls(self):
        self.scraper_dialog.clear_urls()
        self.update_statusbar()

    def update_statusbar(self):
        if self.scraper_dialog:
            self.statusBar().showMessage('{} urls in queue'.format(len(self.scraper_dialog.urls)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())