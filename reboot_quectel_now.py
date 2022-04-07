import os
import time
import serial

portwrite = "/dev/ttyUSB2"
fail_count = 0


def reboot_sixfab():
    ser = serial.Serial(portwrite, baudrate=115200, timeout=5, rtscts=True, dsrdtr=True)
    ser.write("AT+CFUN=1,1\r\n".encode())
    ser.close()

print("Rebooting Queltec LTE")
reboot_sixfab()
