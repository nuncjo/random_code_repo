# -*- coding:utf-8 -*-

from queue import Queue

from PyQt4.QtCore import *

import requests


class ScraperThread(QThread):

    result_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(ScraperThread, self).__init__(parent)
        self._queue = Queue()
        self._stop = False

    def run(self):
        self._stop = False
        while not self._queue.empty() and not self._stop:
            processed_url = self._queue.get()
            result = requests.get(processed_url)
            self.result_signal.emit({'headers': result.headers})

    def clear_queue(self):
        self._queue = Queue()

    @property
    def queue(self):
        return self._queue

    @queue.setter
    def queue(self, urls):
        for url in urls:
            self._queue.put(url.strip())

    @property
    def stop(self):
        return self._stop

    @stop.setter
    def stop(self, stop):
        self._stop = stop