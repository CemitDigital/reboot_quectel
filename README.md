# reboot_quectel
Python3 script to reboot Quectel LTE of connection drops

You need:
Python3
pyserial

add a job in Crontab to check connection every 5 minutes

Open Crontab editor:
$ crontab -e
Add a new line:

*/5 * * * * python3 reboot_quectel.py

To test of string is sent over serial. Run the reboot_quectel_now.py script:

$ python3 reboot_quectel_now.py
