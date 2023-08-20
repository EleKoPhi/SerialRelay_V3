from PyQt5 import QtWidgets
from pathlib import Path
from RelayBoard import *
from ClampControl import *

import sys
import os

import threading

from UiToPy import *


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        self.name = 0
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Board = RelayBoard()
        self.SyncActive = False

        self.Board.TurnAllOff()

        self.ui.StatusLabel.setText("System Status: Connected")
        self.ui.StatusLabel.setStyleSheet("background-color: green")

        self.ui.C1Button.clicked.connect(lambda: self.CButtonEvent())
        self.ui.C2Button.clicked.connect(lambda: self.CButtonEvent())
        self.ui.C3Button.clicked.connect(lambda: self.CButtonEvent())
        self.ui.C4Button.clicked.connect(lambda: self.CButtonEvent())
        self.ui.C5Button.clicked.connect(lambda: self.CButtonEvent())
        self.ui.C6Button.clicked.connect(lambda: self.CButtonSyncedEvent())
        self.ui.C7Button.clicked.connect(lambda: self.CButtonSyncedEvent())
        self.ui.C8Button.clicked.connect(lambda: self.CButtonEvent())

        self.ui.SwitchAllOnButton.clicked.connect(self.AllOnButtonEvent)
        self.ui.SwitchAllOffButton.clicked.connect(self.AllOffButtonEvent)
        self.ui.CmdSendButton.clicked.connect(self.CmdButtonPressed)
        self.ui.SyncClamp15CheckBox.clicked.connect(self.syncButtonPressed)

    def AllOnButtonEvent(self):
        self.Board.TurnAllOn()
        self.ui.C1Button.setChecked(True)
        self.ui.C2Button.setChecked(True)
        self.ui.C3Button.setChecked(True)
        self.ui.C4Button.setChecked(True)
        self.ui.C5Button.setChecked(True)
        self.ui.C6Button.setChecked(True)
        self.ui.C7Button.setChecked(True)
        self.ui.C8Button.setChecked(True)

    def AllOffButtonEvent(self):
        self.Board.TurnAllOff()
        self.ui.C1Button.setChecked(False)
        self.ui.C2Button.setChecked(False)
        self.ui.C3Button.setChecked(False)
        self.ui.C4Button.setChecked(False)
        self.ui.C5Button.setChecked(False)
        self.ui.C6Button.setChecked(False)
        self.ui.C7Button.setChecked(False)
        self.ui.C8Button.setChecked(False)

    def CButtonSyncedEvent(self):

        if self.SyncActive == True and self.ui.SyncClamp15CheckBox.isChecked():
            self.ui.C7Button.setChecked(False)
            self.ui.C6Button.setChecked(False)
            self.CButtonEvent()
            self.SyncActive = False
            return

        if self.ui.C7Button.isChecked() and self.ui.SyncClamp15CheckBox.isChecked():
            self.SyncActive = True
            self.ui.C6Button.setChecked(True)
            self.CButtonEvent()
            return

        if self.ui.C6Button.isChecked() and self.ui.SyncClamp15CheckBox.isChecked():
            self.SyncActive = True
            self.ui.C7Button.setChecked(True)
            self.CButtonEvent()
            return

        self.CButtonEvent()

    def setChannelButton(self, channel, state):
        if channel == 1:
            self.ui.C1Button.setChecked(state)
        if channel == 2:
            self.ui.C2Button.setChecked(state)
        if channel == 3:
            self.ui.C3Button.setChecked(state)
        if channel == 4:
            self.ui.C4Button.setChecked(state)
        if channel == 5:
            self.ui.C5Button.setChecked(state)
        if channel == 6:
            self.ui.C6Button.setChecked(state)
        if channel == 7:
            self.ui.C7Button.setChecked(state)
        if channel == 8: 
            self.ui.C8Button.setChecked(state)

    def SyncRelayStateWithButtons(self):
        state = self.Board.relayState
        print(self.Board.relayState)
        for channel, bit in enumerate(format(state, "b")):
            if bit == "0":
                self.setChannelButton(8 - channel, True)
            else:
                self.setChannelButton(8 - channel, False)

    def CButtonEvent(self):

        self.Board.SetRelayState(1, self.ui.C1Button.isChecked())
        self.Board.SetRelayState(2, self.ui.C2Button.isChecked())
        self.Board.SetRelayState(3, self.ui.C3Button.isChecked())
        self.Board.SetRelayState(4, self.ui.C4Button.isChecked())
        self.Board.SetRelayState(5, self.ui.C5Button.isChecked())
        self.Board.SetRelayState(6, self.ui.C6Button.isChecked())
        self.Board.SetRelayState(7, self.ui.C7Button.isChecked())
        self.Board.SetRelayState(8, self.ui.C8Button.isChecked())
        self.Board.SendStateToBoard()

    def CmdButtonPressed(self):
        cmd = self.ui.CmdInput.text()
        cmd_processed = cmd.split(",")

        processed = []

        for element in cmd_processed:
            new_element = element.replace(" ", "")
            new_element = new_element.lower()

            if new_element.startswith("t") or new_element.startswith("c") or new_element == "":
                processed.append(new_element)
            else:
                print("invalid cmd!")
                return

        print(processed)

        for channel in range(1,9):
            self.Board.SetRelayState(channel,False)
        timeBuffer_t0 = 0
        timeBuffer_t1 = 0

        for element in processed:
            if element.startswith("t0"):
                continue

            if element.startswith("t"):
                self.Board.SendStateToBoard()
                print("Sync")
                self.SyncRelayStateWithButtons()    

                timeBuffer_t1 = int(element[1])
                time.sleep(timeBuffer_t1-timeBuffer_t0)
                timeBuffer_t0 = timeBuffer_t1

                for channel in range(1,9):
                    self.Board.SetRelayState(channel,False)

            if element.startswith("c"):
                self.Board.SetRelayState(int(element[1]),True)

        self.SyncRelayStateWithButtons()    
        self.Board.SendStateToBoard()
        
    def syncButtonPressed(self):
        if self.ui.C7Button.isChecked() and self.ui.C6Button.isChecked() and self.ui.SyncClamp15CheckBox.isChecked():
            self.SyncActive = True

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
