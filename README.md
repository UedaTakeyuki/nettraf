# nettraf
record network traffic log for each network interface from /proc/net/dev to /var/log/nettraf

## how to use
```
python -m /home/pi/nettraf/nettraf
```

## log file
Log files are created under /var/log/nettraf as follows:

```
pi@raspberrypi:~/nettraf $ ls /var/log/nettraf
eth0  lo  wlan0
```

These 3 files, each file is related to /proc/net/dev file

```
pi@raspberrypi:~/nettraf $ cat /proc/net/dev
Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
  eth0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
    lo:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
 wlan0: 2801213   22537    0    0    0     0          0       761 20308513   22499    0    0    0     0       0          0
```

## log file content

The file is recorded as .csv style of timestamp and /proc/net/dev lines without interface name and with replace continuous blank to "," as followns

```
pi@raspberrypi:~/nettraf $ cat /var/log/nettraf/wlan0 
2018-10-14 16:50:01.534098,,2704021,21597,0,0,0,0,0,757,20064126,21862,0,0,0,0,0,0
2018-10-14 16:55:01.710930,,2787937,22401,0,0,0,0,0,757,20299651,22428,0,0,0,0,0,0
2018-10-14 17:00:01.859301,,2830684,22703,0,0,0,0,0,761,20485441,22687,0,0,0,0,0,0
```

### reguraly logging
Set this on the crontab at root user, for example, edit crontab at root user as follow:

```
sudo crontab -e
```

Then, add a line to the end of this as follows:

```
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
*/5 * * * * python -m /home/pi/nettraf/nettraf

```

So, logfile is taken in 5 minutes interval.
