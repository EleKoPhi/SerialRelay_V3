from sys import argv, exit
from ClampControl_v2 import QtWidgets
from Application import ApplicationWindow


def main():
    app = QtWidgets.QApplication(argv)
    application = ApplicationWindow()
    application.show()
    exit(app.exec_())
