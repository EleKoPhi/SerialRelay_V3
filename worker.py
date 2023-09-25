from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class runable(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(runable, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.kwargs = kwargs

    def run(self):
        self.fn(*self.args, **self.kwargs)