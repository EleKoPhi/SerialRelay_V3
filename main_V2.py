from PyQt5 import QtWidgets
from pathlib import Path
from RelayBoard import *
from ClampControl_v2 import *
import threading
from defines import *
from program import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import json
import sys
import os
import threading
from UiToPy import *
from config import *


class ApplicationWindow(QtWidgets.QMainWindow):
    _cButtons = []
    _cDescriptions = []
    _preDefinedPrograms = []
    _programButtons = []

    def __init__(self):
        # Basic Pyqt commands to setup an application window
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_ClampSimulator()
        self.ui.setupUi(self)

        # Load some basic configurations
        self.config = config()

        # Stack repeating element to list, this will ease handling
        self.stackToList(self._cButtons, "C{}Button", 8)
        self.stackToList(self._cDescriptions, "C{}Label", 8)
        self.stackToList(self._programButtons, "programButton{}", 6)

        # Load the predefined channel description to the related labels
        self.loadChannelDescription()

        # Load the predefined programs from the programs.json file
        self.loadPrograms()

        # Create a object of the RelayBoard Class. This represents the relay board
        self.Board = RelayBoard()

        # Configute GUI to predefined state
        self.deactivateAllButtons()
        self.uncheckAllChanelButtons()

        self.setSystemStatus("No Connection!", "red")

        self.addPortToMenueBar()
        self.ui.menuSetting.aboutToShow.connect(self.addPortToMenueBar)

        # 1000ms Timer to check if serial device is still pressent
        self.setUpConnectionCheckTimer(1000)

        print(self.channelConnectFunction())

    def stackToList(self, stackList, objectName, max):
        for element in range(max):
            uiElement = objectName.format(str(element + 1))
            exec("stackList.append(self.ui.{})".format(uiElement))
            print(uiElement)

    def loadPrograms(self):
        self.loardProgramsDefinition()
        self.loadProgramsToGui()
        self.connectPrograms()

    def loadProgramsToGui(self):
        for program in self._preDefinedPrograms:
            self._programButtons[program.ID].setText(program.Name)
            if program.event == "Single":
                self._programButtons[program.ID].setCheckable(False)
            else:
                self._programButtons[program.ID].setCheckable(True)

    def connectPrograms(self):
        for program in self._preDefinedPrograms:
            self._programButtons[program.ID].clicked.connect(
                self.executeProgrammFactory(program.ProgramDefinition)
            )

    def loardProgramsDefinition(self):
        with open("programs.json", "r") as f:
            programJson = json.load(f)

        for programdefinition in programJson["Programs"]:
            self._preDefinedPrograms.append(program(programdefinition))

    def loadChannelDescription(self):
        for index, label in enumerate(self._cDescriptions):
            channel = index + 1
            label.setText(self.config.getChannelDescription(channel))

    def setUpConnectionCheckTimer(self, interval):
        # Create, configure and start timer
        self.connectionCheckTimer = QTimer()
        self.connectionCheckTimer.timeout.connect(
            self.Board.checkIfConnectionStillPressent
        )
        self.connectionCheckTimer.setInterval(interval)
        self.connectionCheckTimer.start()

        # Connect timer to sync connection function
        self.Board.StatusSignal.connect(lambda: self.syncConnectionStatus())

    def syncConnectionStatus(self):
        if self.Board.connectionStatus:
            self.setSystemStatus("Connected", "green")
            self.activateAllButtons()
        else:
            self.setSystemStatus("No Connection!", "red")
            self.deactivateAllButtons()

    def executeProgrammFactory(self, definition):
        def executeProgram():
            for index, element in enumerate(definition):
                channel = index + 1
                if element == 1:
                    element = ON
                    self.setChecked(channel)
                else:
                    element = OFF
                    self.setUnChecked(channel)

                self.Board.setRelayState(channel, element)
                self.Board.sendStateToHardware()

        return executeProgram

    def activateAllButtons(self):
        for button in self._cButtons:
            button.setEnabled(True)

        for program in self._preDefinedPrograms:
            self._programButtons[program.ID].setEnabled(True)

    def deactivateAllButtons(self):
        for button in self._cButtons:
            button.setEnabled(False)

        for programButton in self._programButtons:
            programButton.setEnabled(False)

    def activateSingleChanelButton(self, channel):
        self._cButtons[channel - 1].setEnabled(True)

    def deactivateSingleChanelButton(self, channel):
        self._cButtons[channel - 1].setEnabled(False)

    def checkAllChanelButtons(self):
        for button in self._cButtons:
            button.setChecked(True)

    def setChecked(self, channel):
        self._cButtons[self.channelToIndex(channel)].setChecked(True)

    def setUnChecked(self, channel):
        self._cButtons[self.channelToIndex(channel)].setChecked(False)

    def indexToChannel(self, index):
        return index + 1

    def channelToIndex(self, channel):
        return channel - 1

    def uncheckAllChanelButtons(self):
        for button in self._cButtons:
            button.setChecked(False)

    def setSystemStatus(self, msg, color):
        self.ui.SystemOutput.setText(msg)
        self.ui.SystemOutput.setStyleSheet("background-color: " + color)

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(
            self,
            "QUIT",
            "Are you sure want to stop process?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        )

        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def channelConnectFunction(self):
        for button in self._cButtons:
            button.clicked.connect(self.syncButtons)

    def syncButtons(self):
        for index, button in enumerate(self._cButtons):
            channel = index + 1
            if button.isChecked():
                self.Board.setRelayState(channel, ON)
                button.setText("C{}: {}".format(channel, "ON "))
            else:
                self.Board.setRelayState(channel, OFF)
                button.setText("C{}: {}".format(channel, "OFF"))

        self.Board.sendStateToHardware()

    def addPortToMenueBar(self):
        self.ui.menuSetting.clear()
        self.ui.MenueBarElements = {}

        for port in self.Board.getPossiblePortList():
            self.ui.MenueBarElements[port.name] = [port, QtWidgets.QAction(self)]
            self.ui.MenueBarElements[port.name][1].setObjectName(port.name)
            self.ui.MenueBarElements[port.name][1].setText(port.name)
            self.ui.menuSetting.addAction(self.ui.MenueBarElements[port.name][1])
            self.ui.MenueBarElements[port.name][1].triggered.connect(self.tryToConnect)

    @QtCore.pyqtSlot()
    def tryToConnect(self):
        portElementKey = self.sender()
        port = self.ui.MenueBarElements[portElementKey.text()][0]
        print("Connect to:" + port.name)
        if self.Board.connectToPort(port):
            self.setSystemStatus("Connected", "green")
        else:
            self.setSystemStatus("No Connection!", "red")


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
