import serial.tools.list_ports
import time
import sys

# 0 = On
# 1 = Off


realyState = 0x00

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def TurnOn(channel):
    return clear_bit(realyState, channel)

def TurnOff(channel):
    return set_bit(realyState, channel)


ports = serial.tools.list_ports.comports()
for port in ports:

    if "usbserial-240" in port.name:
        print(port)
        SerialConnection = serial.Serial(port.device, timeout=2, baudrate=9600)
        #cmd = 0x51
        #time.sleep(1)
        #SerialConnection.write(cmd.to_bytes(1,"big"))

        cmd = realyState
        SerialConnection.write(cmd.to_bytes(1,"big"))

        while(True):

            for i in range(0,8):
                realyState = TurnOn(i)
                print(realyState)
                SerialConnection.write(realyState.to_bytes(1,"big"))
                time.sleep(1)

            for i in range(0,8):
                realyState = TurnOff(7-i)
                print(realyState)
                SerialConnection.write(realyState.to_bytes(1,"big"))
                time.sleep(1)



