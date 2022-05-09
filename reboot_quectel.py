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
    print(datetime.now(), "Power cycling USB")
    try:
        os.system("sudo uhubctl -l 1-1 -a 2")
        print(datetime.now(), "Power cycle USB successful.")
        time.sleep(180)
    except:
        print(datetime.now(), "Power cycle USB failed")

def restart_quectel_CM():
    print(datetime.now(), "Starting restart of quectel-CM.")
    try:
        PID = pgrep.pgrep("quectel-CM")
#        print(PID[0])
        PID1=PID[0]
#        print(PID1)
        os.system(f"sudo kill -INT {PID1}")
        os.system(f"sudo wait {PID1}")
        time.sleep(5)
        os.system("/home/cemit/qmi/quectel-CM/quectel-CM -s internet.public")
        print(datetime.now(), "Restart of quectel-CM done.")
        time.sleep(10)
    except:
        print(datetime.now(), "Restarting of quectel-CM failed.")


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
            restart_quectel_CM()
        if fail_count == (35):
            restart_quectel_CM()
        if fail_count == (50):
            restart_quectel_CM()

        if fail_count >= 70:
            #Power cycle all USB port on RPi 4B
            power_cycle_usb()
            quit()
        time.sleep(10)
