from PyQt5 import QtWidgets
from pathlib import Path

import sys
import os

import threading

ui_file = r"/Users/philippmochti/Documents/PlatformIO/Projects/ClampControl/ClampControl_v2.ui"


def trans_py_file(filename):
    return os.path.splitext(filename)[0] + '.py'


def convert_ui_to_py():
    py_file = trans_py_file(ui_file)

    if Path(py_file).exists():
        Path(py_file).unlink()
        print("Remove existing .py file")

    cmd = 'pyuic5 -o {py_file} {ui_file}'.format(py_file=py_file, ui_file=ui_file)
    print("Convert .ui file: " + ui_file)
    print("To .py file: " + py_file)

    os.system(cmd)

convert_ui_to_py()
