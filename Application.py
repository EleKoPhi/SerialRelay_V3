from PyQt5 import QtWidgets
from RelayBoard import *
from ClampControl_v2 import *
from defines import *
from program import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import json
import sys
from UiToPy import *
from config import *
import logging, sys
from thread import *

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class ApplicationWindow(QtWidgets.QMainWindow):
    _cButtons = []
    _cDescriptions = []
    _preDefinedPrograms = []
    _programButtons = []

    _stopProgram = QtCore.pyqtSignal()
    _startProgram = QtCore.pyqtSignal()
    _resetProgram = QtCore.pyqtSignal()
    _programFinished = QtCore.pyqtSignal()

    _executeProgram = False
    _programStatus = "programFinished"

    def __init__(self):
        # Basic Pyqt commands to setup an application window
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_ClampSimulator()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()

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

        # Configure GUI to predefined state
        self.deactivateAllButtons()
        self.uncheckAllChanelButtons()

        self.setSystemStatus("No Connection!", "red")

        self.addPortToMenuBar()
        self.ui.menuSetting.aboutToShow.connect(self.addPortToMenuBar)

        # 1000ms Timer to check if serial device is still present
        self.setUpConnectionCheckTimer(1000)

        self._stopProgram.connect(self.stopProgram)
        self._startProgram.connect(self.startProgram)
        self._resetProgram.connect(self.resetProgram)
        self._programFinished.connect(self.programFinished)

        self.channelConnectFunction()

        self.ui.CmdSendButton.clicked.connect(self.sendCmdButtonPressed)
        self.ui.CmdInput.returnPressed.connect(self.sendCmdButtonPressed)

        self.ui.actionHelp_2.triggered.connect(self.showTheAboutPopUp)

    @QtCore.pyqtSlot()
    def stopProgram(self):
        # This function is executed when ever the program stop signal is emitted
        # Setting the following variables is killing all running program threads
        self._programStatus = "stopProgram"
        self._executeProgram = False

    @QtCore.pyqtSlot()
    def startProgram(self):
        # This function is executed when ever the program start signal is emitted
        # If a program is currently running -> Stop it by emitting the stop program signal
        self._stopProgram.emit()
        self._programStatus = "startProgram"

    @QtCore.pyqtSlot()
    def resetProgram(self):
        # This function is executed when ever the program reset signal is emitted
        # Currently no functionality
        self._programStatus = "resetProgram"

    @QtCore.pyqtSlot()
    def programFinished(self):
        # This function is executed when ever the program finished signal is emitted
        # Currently no functionality
        self._programStatus = "programFinished"

    def sendCmdButtonPressed(self):
        # cmd Type
        # + Adds to active channels
        # - Removes active channels
        # None Removes non defined channels and adds defined on

        # validate input

        ## Helper Functions ##

        def checkIfDigitInRange(digit):
            if int(digit) in range(1, 9):
                return True
            else:
                return False

        def activateChannel(channel):
            self.setChecked(int(channel))
            self.Board.setRelayState(int(channel), ON)

        def deactivateChannel(channel):
            self.setUnChecked(int(channel))
            self.Board.setRelayState(int(channel), OFF)

        ## Helper Functions ##

        cmd = self.ui.CmdInput.text()
        cmdType = None

        if cmd.startswith("+") or cmd.startswith("-"):
            cmdType = cmd[0]
            cmd = cmd[1:]
            if cmd.isdigit():
                for digit in cmd:
                    if checkIfDigitInRange(digit):
                        continue
                    else:
                        logging.error("Invalid CMD")
                        return False
            else:
                return False

        elif cmd.isdigit():
            for digit in cmd:
                if checkIfDigitInRange(digit):
                    continue
                else:
                    logging.error("Invalid CMD")
                    return False
        else:
            logging.error("Invalid CMD")
            return False

        # If a cmd is send during program execution
        self._stopProgram.emit()
        self.ui.progressBar.setValue(0)
        self.resetProgramButtons()

        for channel in cmd:
            if cmdType == "+":
                activateChannel(channel)
            elif cmdType == "-":
                deactivateChannel(channel)
            else:
                continue

        if cmdType == None:
            for channel in range(1, 9):
                if str(channel) in cmd:
                    activateChannel(channel)
                else:
                    deactivateChannel(channel)

        self.Board.sendStateToHardware()

    def stackToList(self, stackList, objectName, max):
        # This function allows to load predefined elements to a new list
        # Doing so eases the handling for multiple buttons
        for element in range(max):
            uiElement = objectName.format(str(element + 1))
            exec("stackList.append(self.ui.{})".format(uiElement))

    def loadPrograms(self):
        # Get program definition
        self.loadProgramsDefinition()
        # Connect program to GUI
        self.loadProgramsToGui()
        # Connect program to slot
        self.connectPrograms()

    def loadProgramsToGui(self):
        # Load the program name to the GUI button
        for program in self._preDefinedPrograms:
            self._programButtons[program.ID].setText(program.Name)

    def connectPrograms(self):
        # Connect the loaded program to the related button
        for program in self._preDefinedPrograms:
            self._programButtons[program.ID].clicked.connect(
                self.executeProgramFactory(
                    program.ProgramDefinition, program.event, program.ID
                )
            )

    def loadProgramsDefinition(self):
        # Open the file and load as json
        with open(PROGRAMSFILENAME, "r") as f:
            programJson = json.load(f)
        # Iterate thru all programs and create program elements
        for programDefinition in programJson["Programs"]:
            self._preDefinedPrograms.append(program(programDefinition))

    def resetProgramButtons(self):
        # Set all program buttons to unchecked
        for _programButton in self._programButtons:
            _programButton.setChecked(False)

    def loadChannelDescription(self):
        # Load the cannel descriptions from the config.py file
        for index, _cDescriptions in enumerate(self._cDescriptions):
            channel = self.indexToChannel(index)
            _cDescriptions.setText(self.config.getChannelDescription(channel))

    def setUpConnectionCheckTimer(self, interval):
        # Create, configure and start timer
        self.connectionCheckTimer = QTimer()
        self.connectionCheckTimer.timeout.connect(
            self.Board.checkIfConnectionStillPresent
        )
        self.connectionCheckTimer.setInterval(interval)
        self.connectionCheckTimer.start()

        # Connect timer to sync connection function
        self.Board.StatusSignal.connect(lambda: self.syncConnectionStatus())

    def syncConnectionStatus(self):
        # This function syncs the system status with the
        # board connection status

        if self.Board.connectionStatus:
            # If a connection is established ->  enable all active buttons
            self.setSystemStatus("Connected", "green")
            self.activateAllButtons()
        else:
            # If no connection is established -> disable all buttons
            self.setSystemStatus("No Connection!", "red")
            self.deactivateAllButtons()

    def runPredefinedProgram(self, program):
        logging.debug(program)
        runnedTime = 0
        setCounter = 0
        # Todo: Estimate required resolution based on the program definition
        resolution = 0.01

        # Set progress bar to 0
        self.ui.progressBar.setValue(0)

        # Estimate run time of program for progress bar1
        runTime = program[-1][0] - program[0][0]

        # Execute the initial program definition of t = 0
        self.executeChannelSet(program[setCounter][1])
        setCounter = setCounter + 1

        # As long _executeProgram is True the program is executed
        while self._executeProgram:
            # To reduce CPU load, the program is only updated at a preestimated resolution
            runnedTime = runnedTime + resolution

            # If more time is elapsed than defined, load the next definition
            if runnedTime > program[setCounter][0]:
                self.executeChannelSet((program[setCounter][1]))
                setCounter += 1

            time.sleep(resolution)

            # Set progress bar in relation to the run time
            self.ui.progressBar.setValue(int((runnedTime / runTime) * 100))

            # Update GUI
            QApplication.processEvents()
            if runnedTime > runTime:
                self._executeProgram = False
                break

        self._programFinished.emit()

    def executeProgramFactory(self, definition, event, id):
        # Function Type: Program Execution
        # This function returns a function that executes a pre defined function

        def executeProgram():
            # There are two types of programs.
            # TimeBased - A program that is executed over time
            # The time based program is a set of single event definitions with time information
            # Singe - A one time definition of a relay configuration

            # First reset all buttons
            self.resetProgramButtons()
            # Check the program button of the executed program
            self._programButtons[id].setChecked(True)

            # If an program is already running, we emit the stopProgram signal
            # and force the running program to stop
            if self._programStatus == "startProgram":
                self._stopProgram.emit()
                logging.info("Stopped running program")

            if event == "TimeBased":
                # Set the program status to startProgram
                self._programStatus = "startProgram"
                self._executeProgram = True
                # Create a new thread, to avoid a freezing GUI
                runningProgram = myThread(self.runPredefinedProgram(definition))
                # Start the created thread
                self.threadpool.start(runningProgram)
            else:
                # If the program definition is a single event this part is executed
                # Iterate thru the definition
                for index, element in enumerate(definition):
                    channel = self.indexToChannel(index)
                    # Sync GUI
                    if element == ON:
                        self.setChecked(channel)
                    else:
                        self.setUnChecked(channel)
                    # Send configuration to board
                    self.Board.setRelayState(channel, element)

                # Activate the relay state
                # Here the channels are switched
                self.Board.sendStateToHardware()
                self.ui.progressBar.setValue(0)

        return executeProgram

    def controlRelayState(self, definition):
        # Function Type: Helper Function
        # Send the definition to the relay board
        for index, state in enumerate(definition):
            self.Board.setRelayState(self.indexToChannel(index), state)
        self.Board.sendStateToHardware()

    def controlGuiAppearance(self, definition):
        # Function Type: Helper Function
        # Sync GUI with relay definition
        # If a channel is switched programmatically also the GUI has to be updated
        # and the channel buttons have the be set or unset

        for index, state in enumerate(definition):
            if state == 1:
                self.setChecked(self.indexToChannel(index))
            else:
                self.setUnChecked(self.indexToChannel(index))

    def executeChannelSet(self, definition):
        # Function Type: Helper Function
        # This function allows to execute a relay definition
        # a relay definition is a array of n elements.

        # Send the definition to the relay board
        self.controlRelayState(definition)
        # Send the definition to the GUI
        self.controlGuiAppearance(definition)

    def activateAllButtons(self):
        # Function Type: Helper Function
        # Enable GUI Buttons

        # All channel buttons can be enabled
        for button in self._cButtons:
            button.setEnabled(True)

        # Enable ony program buttons with an defined function
        for program in self._preDefinedPrograms:
            self._programButtons[program.ID].setEnabled(True)

        self.ui.CmdSendButton.setEnabled(True)
        self.ui.CmdInput.setEnabled(True)

    def deactivateAllButtons(self):
        # Function Type: Helper Function
        # Disable all GUI Buttons

        for button in self._cButtons:
            button.setEnabled(False)

        for programButton in self._programButtons:
            programButton.setEnabled(False)

        self.ui.CmdSendButton.setEnabled(False)
        self.ui.CmdInput.setEnabled(False)

    def activateSingleChanelButton(self, channel):
        # Function Type: Helper Function
        # Activate a singe button
        self._cButtons[self.channelToIndex(channel)].setEnabled(True)

    def deactivateSingleChanelButton(self, channel):
        # Function Type: Helper Function
        # Enable a singe button
        self._cButtons[self.channelToIndex(channel)].setEnabled(False)

    def setChecked(self, channel):
        # Function Type: Helper Function
        # Set a defined channel button to checked and updates the displayed text
        self._cButtons[self.channelToIndex(channel)].setChecked(True)
        self._cButtons[self.channelToIndex(channel)].setText(
            "C{}: {}".format(channel, "ON ")
        )

    def setUnChecked(self, channel):
        # Function Type: Helper Function
        # Set a defined channel button to unchecked and updates the displayed text
        self._cButtons[self.channelToIndex(channel)].setChecked(False)
        self._cButtons[self.channelToIndex(channel)].setText(
            "C{}: {}".format(channel, "OFF ")
        )

    def indexToChannel(self, index):
        # Function Type: Helper Function
        # Converts the list index to a channel
        return index + 1

    def channelToIndex(self, channel):
        # Function Type: Helper Function
        # Converts the channel to a list index
        return channel - 1

    def uncheckAllChanelButtons(self):
        # Function Type: Helper Function
        # Set all buttons to unchecked
        for button in self._cButtons:
            button.setChecked(False)

    def checkAllChanelButtons(self):
        # Function Type: Helper Function
        # Set all buttons to checked
        for button in self._cButtons:
            button.setChecked(True)

    def setSystemStatus(self, msg, color):
        # Function Type: Helper Function
        # This function takes a string and a color and updates the system output
        self.ui.SystemOutput.setText(msg)
        self.ui.SystemOutput.setStyleSheet("background-color: " + color)

    def closeEvent(self, event):
        # Function Type: Pop Up Handler
        # This function is called when ever we want to close the application

        # Only aks if a connection is established. If no connection is present,
        # just close the application
        if self.Board.connectionStatus == True:
            close = QtWidgets.QMessageBox.question(
                self,
                "QUIT",
                "Are you sure want to close the application?\nThis will open all active relays.",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            )
        else:
            # If no connection is present, simply close the application
            close = QtWidgets.QMessageBox.Yes

        # Reaction due to selection is pop up
        if close == QtWidgets.QMessageBox.Yes:
            # Close application
            event.accept()
        else:
            # Close pop up and continue application
            event.ignore()

    def channelConnectFunction(self):
        # Function Type: Helper function
        # This function connect the syncButtons function to all GUI buttons
        # that where loaded the the _cButtons list

        # Iterate thu all buttons and connect the syncButtons function
        for button in self._cButtons:
            # Every time a _cButton is clicked the syncButtons function shall be executed
            button.clicked.connect(self.syncButtons)

    def syncButtons(self):
        # Function Type: Board Control
        # This function is called when ever you kick a channel button
        # It check's if a button is kicked and sends the update to the relay Board

        # The fist part of the function is to ensure no program is running
        # and update the GUI

        # Call the stopProgram signal every time a button is clicked
        # to ensure that, if an button is clicked during program execution,
        # the running program is stopped.
        self._stopProgram.emit()

        # Every time a channel button is clicked, we are sure that no program is selected
        # So we can reset all checked program buttons
        self.resetProgramButtons()

        # No program is executed -> Reset the progressbar to 0%
        self.ui.progressBar.setValue(0)

        # Reprint the GUI, as some parts may have been updated programmatically
        QApplication.processEvents()

        # Iterate over all Buttons, as we use the same function for all Buttons
        for index, button in enumerate(self._cButtons):
            # Convert the index to the related channel
            # Channels start with 1, the index with 0
            channel = self.indexToChannel(index)

            if button.isChecked():
                # If a button is checked, update the relay state to ON
                self.Board.setRelayState(channel, ON)
                # Update the displayed text to ON
                button.setText("C{}: {}".format(channel, "ON "))
            else:
                # If a button is not checked, update the relay state of OFF
                self.Board.setRelayState(channel, OFF)
                # Update the displayed text to OFF
                button.setText("C{}: {}".format(channel, "OFF"))

        # After the relay state is synced with the selected buttons / channels we send
        # the updated relay state to your hardware. This is the moment the relay switches
        self.Board.sendStateToHardware()

    def addPortToMenuBar(self):
        # Function Type: GUI Update
        # This function adds all present serial devices to the menu bar
        # This function is called every time the connection button of the menu bar is clicked

        # Remove all old elements from the bar
        # Maybe some devices where disconnected and are no longer available
        # The Clear function removes all elements from the GUI
        self.ui.menuSetting.clear()

        # The following line cleans our dictionary
        self.ui.MenuBarElements = {}

        # We get all serial devices from our Board and iterate over all elements
        for port in self.Board.getPossiblePortList():
            # Create a new dictionary entity with two elements - The serial element and the related menu bar element
            self.ui.MenuBarElements[port.name] = [port, QtWidgets.QAction(self)]
            # Name the menu bar element like the serial port element
            self.ui.MenuBarElements[port.name][1].setObjectName(port.name)
            # Set the shown text of the menu bar element to the same name as the serial port name
            self.ui.MenuBarElements[port.name][1].setText(port.name)
            # Add the Widget to your menu bar
            self.ui.menuSetting.addAction(self.ui.MenuBarElements[port.name][1])
            # Connect the related function
            self.ui.MenuBarElements[port.name][1].triggered.connect(self.tryToConnect)

    @QtCore.pyqtSlot()
    def showTheAboutPopUp(self):
        aboutMsgBox = QMessageBox()
        aboutMsgBox.setWindowTitle("About this application")
        aboutMsgBox.setText(
            "Description: Simple Relay / Clamp Control\nSuggested HW: ICSE014A\nRevision: 1.0.0\nCreated By: Philipp Mochti\nCMD Input:\n+12 will switch channel 1 and 2 on\n-12 will switch channel 1 and 2 off\n12 will switch all channels off except channel 1 and 2. These will be activated"
        )

        popup = myThread(aboutMsgBox.exec_())
        self.threadpool.start(popup)

    @QtCore.pyqtSlot()
    def tryToConnect(self):
        # Function Type: Establish Serial Connection
        # This function is called when the GUI tries to establish a new serial connection
        portElementKey = self.sender()
        # Get the related serial port from our sender name
        port = self.ui.MenuBarElements[portElementKey.text()][0]
        logging.info("Connect to:" + port.name)

        # Update the system status
        if self.Board.connectToPort(port):
            self.setSystemStatus(CONNECTED, GREEN)
            self.activateAllButtons()
        else:
            self.setSystemStatus(NOT_CONNECTED, RED)
