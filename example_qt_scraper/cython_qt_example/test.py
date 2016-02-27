# -*- coding:utf-8 -*-

import sys
import unittest
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt

from main import MainWindow

app = QApplication(sys.argv)


class MainWindowTest(unittest.TestCase):

    def setUp(self):
        self.form = MainWindow()

    def test_scrape_process(self):

        urls = ['http://www.pythonic.me',
                'http://www.onet.pl',
                'http://www.wp.pl',
                'http://www.allegro.pl',
                'http://www.wykop.pl']

        urls_number = len(urls)

        self.form.show()
        QTest.qWaitForWindowShown(self.form)

        self.form.load_urls(urls)
        self.assertIn('urls in queue', self.form.statusBar().currentMessage())
        self.assertEqual(urls_number, len(self.form.scraper_dialog.urls))

        QTest.mouseClick(self.form.open_scraper_button, Qt.LeftButton)
        QTest.qWaitForWindowShown(self.form.scraper_dialog)
        QTest.mouseClick(self.form.scraper_dialog.start_button, Qt.LeftButton)

        while self.form.scraper_dialog.scraper_thread.isRunning():
            QApplication.processEvents()

        self.assertIn('keep-alive', self.form.scraper_dialog.result_plain_text_edit.toPlainText())


if __name__ == "__main__":
    unittest.main()