# -*- coding:utf-8 -*-

from PySide.QtGui import *

from gui.scrape_dialog import Ui_Dialog
from scraper_thread import ScraperThread


class ScraperDialog(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(ScraperDialog, self).__init__(parent)
        self.setupUi(self)

        self._urls = []

        self.scraper_thread = ScraperThread()
        self.start_button.clicked.connect(self.start_scraper)
        self.stop_button.clicked.connect(self.stop_scraper)
        self.scraper_thread.result_signal.connect(self.update_result_text_edit)

    def start_scraper(self):
        self.scraper_thread.queue = self._urls
        self.scraper_thread.start()

    def stop_scraper(self):
        self.scraper_thread.stop = True

    def clear_urls(self):
        self._urls = []
        self.scraper_thread.clear_queue()

    def update_result_text_edit(self, result):
        sb = self.result_plain_text_edit.verticalScrollBar()
        sb.setValue(sb.maximum())
        self.result_plain_text_edit.insertPlainText('{}{}'.format(result.get('headers', 'Fail'), '\n'))

    @property
    def urls(self):
        return self._urls

    @urls.setter
    def urls(self, urls):
        self._urls.extend(urls)

    @urls.getter
    def urls(self):
        return self._urls
