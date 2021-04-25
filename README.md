# KPZ-measurement #

Collecting data from Tp-Link HS110 and sending them to the database.

## How to use ##
### Requirements ###
You will need influx database.
```sudo apt-get install influxdb```

Clone this repository https://github.com/GadgetReactor/pyHS100 to your directory.

Clone my repository.

Write in terminal ```pyhs100```. You should get something like this:
```$ pyhs100
No --bulb nor --plug given, discovering..
Discovering devices for 3 seconds
== My Smart Plug - HS110(EU) ==
Device state: ON
IP address: 192.168.10.10
LED state: False
On since: 2017-03-26 18:29:17.242219
== Generic information ==
Time:         1970-06-22 02:39:41
Hardware:     1.0
Software:     1.0.8 Build 151101 Rel.24452
MAC (rssi):   50:C7:BF:XX:XX:XX (-77)
Location:     {'latitude': XXXX, 'longitude': XXXX}
== Emeter ==
Current state: {'total': 133.082, 'power': 100.418681, 'current': 0.510967, 'voltage': 225.600477}
```

Copy IP address which is 192.168.10.10 in this case and enter it on line 15 in tplink-get-measurements.py.

Now you can run the program by typing ```python3 tplink-get-measurements.py``` in the terminal.

