import serial.tools.list_ports
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5 import *
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit

import serial.tools.list_ports
import time
import sys


class RelayBoard(QObject):

    relayState = 0xFF
    serialConnection = None

    initCmd = bytearray([0x50, 0x51])

    initCmd_1 = 0x50
    initCmd_2 = 0x51
    initCmd_3 = 0xFF

    startupCmd = bytearray([0x51, 0x00])

    connectionStatus = False
    connectionCounter = 0

    possiblePorts = []

    checkConnection = True

    StatusSignal = pyqtSignal(bool)

    def __init__(self):
        super(RelayBoard, self).__init__()
        self.getPossiblePortList()
        self.SerialConnection = None

    def connectToPort(self, port):

        try:
            self.SerialConnection = serial.Serial(port.device, timeout=1, baudrate=9600)
        except:
            return False

        self.SerialConnection.write(self.initCmd)
        self.SerialConnection.write(self.initCmd_3)
        self.SerialConnection.write(self.startupCmd)
        self.TurnAllOff()
        time.sleep(1)
        self.TurnAllOn()

        return True

    def checkIfConnectionStillPressent(self):
        #No connection established
        if self.SerialConnection == None:
            self.connectionStatus = False
            self.StatusSignal.emit(self.connectionStatus)
            return False
                
        #Check port elements and return true if port still exists
        for port in self.getPossiblePortList():
            if self.SerialConnection.name.endswith(port.name):
                self.connectionStatus = True
                self.StatusSignal.emit(self.connectionStatus)
                return True
                
        #If established port is no longer pressent return false
        self.connectionStatus = False
        self.StatusSignal.emit(self.connectionStatus)
        return False

    def getPossiblePortList(self):
        self.possiblePorts = serial.tools.list_ports.comports()
        return self.possiblePorts

    def set_bit(self, value, bit):
        return value | (1<<bit)

    def clear_bit(self, value, bit):
        return value & ~(1<<bit)

    def TurnAllOff(self):
        self.relayState = 0xFF
        self.SerialConnection.write(self.relayState.to_bytes(1,"big"))

    def TurnAllOn(self):
        self.relayState = 0x00
        self.SerialConnection.write(self.relayState.to_bytes(1,"big"))

    def TurnOn(self, channel):
        bitPossition = channel - 1
        self.relayState = self.clear_bit(self.relayState, bitPossition)
        self.SerialConnection.write(self.relayState)

    def TurnOff(self, channel):
        bitPossition = channel - 1
        self.relayState = self.set_bit(self.relayState, bitPossition)
        self.SerialConnection.write(self.relayState)

    def setRelayState(self, channel, status):
        
        bit = channel - 1
        if status == True:
            self.relayState = self.clear_bit(self.relayState,bit)
        if status == False:
            self.relayState = self.set_bit(self.relayState, bit)

    def sendStateToHardware(self):
        print(self.relayState)
        self.SerialConnection.write(self.relayState.to_bytes(1,"big"))

#b = RelayBoard()
#b.connectToPort(None)
