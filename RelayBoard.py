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

    def __init__(self):
        super(RelayBoard, self).__init__()

        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "usbserial-240" in port.name:
                print(port)
                self.SerialConnection = serial.Serial(port.device, timeout=1, baudrate=9600)
                time.sleep(0.1)
                self.SerialConnection.write(self.initCmd)
                time.sleep(0.1)
                self.SerialConnection.write(self.initCmd_3)
            else:
                self.connectionStatus = False

        time.sleep(1)
        self.SerialConnection.write(self.startupCmd)

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

    def SetRelayState(self, channel, status):
        
        bit = channel - 1
        if status == True:
            self.relayState = self.clear_bit(self.relayState,bit)
        if status == False:
            self.relayState = self.set_bit(self.relayState, bit)

    def SendStateToBoard(self):
        print(self.relayState)
        self.SerialConnection.write(self.relayState.to_bytes(1,"big"))