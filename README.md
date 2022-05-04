# reboot_quectel
Python3 script to reboot and Quectel LTE and power cycle USB hub when connection drops

You need:
Python3
run-one
pyserial

add a job in Crontab to check connection every 5 minutes

Open Crontab editor:
$ sudo crontab -e
Add a new line:

*/1 * * * * bash /home/cemit/run-one/run-one python3 /home/cemit/reboot_quectel.py >> /home/cemit/reboot_quectel.py.log
