#### Python script restoring WAN connection after Cable modem reset.

Tested on a custom built BBrouter on x86 server with Alma Linux 8.4

Prerequisit:
* $ sudo pip3 install pythonping
* $ sudo dnf install crontabs


Setup Cron:
* $ systemctl enable --now crond.service
* $ sudo crontab -u root -e

Tested Cronetab as follows:
--
[root@linux03-ushome recovWAN]# crontab -u root -l
\# Example of job definition:
\# .---------------- minute (0 - 59)
\# | .------------- hour (0 - 23)
\# | | .---------- day of month (1 - 31)
\# | | | .------- month (1 - 12) OR jan,feb,mar,apr ...
\# | | | | .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
\# | | | | |
\# * * * * * command to be executed
0,10,20,30,40,50 * * * * /usr/sbin/recovWAN.py >> /var/log/recovWAN.log 2>&1

cat /var/log/recovWAN.log
[root@linux03-ushome log]# tail -f recovWAN.log 
22/06/24 14:50:01 - ping Reply from 8.8.8.8, 29 bytes in 11.03ms
 00: 8.8.8.8 Success. exit.
22/06/24 15:00:01 - ping Reply from 8.8.8.8, 29 bytes in 13.69ms
 00: 8.8.8.8 Success. exit.
22/06/24 15:10:02 - ping Reply from 8.8.8.8, 29 bytes in 11.19ms
 00: 8.8.8.8 Success. exit.
22/06/24 15:20:02 - ping Reply from 8.8.8.8, 29 bytes in 11.04ms
 00: 8.8.8.8 Success. exit.
22/06/24 15:30:01 - ping Reply from 8.8.8.8, 29 bytes in 10.22ms
 00: 8.8.8.8 Success. exit.
22/06/24 15:40:02 - ping Request timed out
 00: 8.8.8.8 False Continue.
Request timed out
 01: 1.1.1.1 False Continue.
Rebooting WAN enp1s0 with '/usr/sbin/ifdown enp1s0 && sleep 10 && /usr/sbin/ifup enp1s0'...
Connection 'enp1s0' successfully deactivated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/41903)
Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/41949)
22/06/24 15:50:02 - ping Reply from 8.8.8.8, 29 bytes in 9.38ms
 00: 8.8.8.8 Success. exit.
