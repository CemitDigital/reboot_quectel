import os
import time
import serial

portwrite = "/dev/ttyUSB2"
fail_count = 0


def reboot_sixfab():
    ser = serial.Serial(portwrite, baudrate=115200, timeout=5, rtscts=True, dsrdtr=True)
    ser.write("AT+CFUN=1,1\r\n".encode())
    ser.close()


if __name__ == '__main__':
    while True:
        response = os.system("ping -c 2 -I wwan0 8.8.8.8")
        print(response)
        if response == 0:
            print("Ping successful. Quitting.")
            quit()
        elif response != 0:
            fail_count += 1
            print("Ping failed=" + str(fail_count))
        if fail_count >= 20:
            print("Rebooting Queltec LTE")
            reboot_sixfab()
            quit()
        time.sleep(5)
