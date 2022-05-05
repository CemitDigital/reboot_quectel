import os
import time
import serial

from datetime import datetime

portwrite = "/dev/ttyUSB2"
fail_count = 0


def reboot_sixfab():
    try:
        ser = serial.Serial(portwrite, baudrate=115200, timeout=5, rtscts=True, dsrdtr=True)
        ser.write("AT+CFUN=1,1\r\n".encode())
        ser.close()
        print(datetime.now(), "Sending AT+FUN=1,1 successful.")
    except:
        print(datetime.now(), "Sending AT+FUN=1,1 failed")

def power_cycle_usb():
    try:
        os.system("sudo uhubctl -l 1-1 -a 2")
        print(datetime.now(), "Power cycle USB successful.")
    except:
        print(datetime.now(), "Power cycle USB failed")



if __name__ == '__main__':
    print(datetime.now(), "Starting reboot_quectel.py")
    while True:
        response = os.system("ping -c 2 -I wwan0 8.8.8.8")
        if response == 0:
            print(datetime.now(), "Ping successful. Quitting.")
            quit()
        else:
            fail_count += 1
            print(datetime.now(), "Ping failed times=" + str(fail_count))
        if fail_count == (20):
            print(datetime.now(), "Restarting qmi_reconnect service.")
            os.system("sudo service qmi_reconnect restart")
            time.sleep(40)
        if fail_count == (35):
            print(datetime.now(), "Restarting qmi_reconnect service.")
            os.system("sudo service qmi_reconnect restart")
            time.sleep(40)
        if fail_count == (50):
            print(datetime.now(), "Restarting qmi_reconnect service.")
            os.system("sudo service qmi_reconnect restart")
            time.sleep(40)
#        if fail_count == (35):
#            print(datetime.now(), "Rebooting Queltec LTE.")
#            reboot_sixfab()
#            time.sleep(40)            
        if fail_count >= 70:
            print(datetime.now(), "Power cycling USB")
            #Power cycle all USB port on RPi 4B
            power_cycle_usb()
            time.sleep(180)
            quit()
        time.sleep(10)
