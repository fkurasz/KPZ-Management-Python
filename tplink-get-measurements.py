from pyHS100 import SmartPlug, SmartBulb
from pprint import pformat as pf
from time import gmtime, strftime, sleep
from datetime import datetime
from influxdb import InfluxDBClient
import os


#database connection
client = InfluxDBClient(host = "localhost", port="8086")
client.create_database("display_measurements")
client.switch_database("display_measurements")


# tplink connection
plug = SmartPlug("192.168.0.32")
print("Tp-Link HS110 status: ",plug.state)


amount = 200

while True:
    table = input("Measurement: ")
    if(table == 'q'):
        break

    for i in range(1,amount+1):
        plug = SmartPlug("192.168.0.32")
        all_informations = str(plug.get_emeter_realtime())

        now = datetime.now()

        current_time = now.strftime("%Y-%m-%d %H:%M:%S")


        splitted=all_informations.split(' ')

        voltage_mv = splitted[1][:-1]
        current_ma = splitted[3][:-1]
        power_mw = splitted[5][:-1]
        total_wh = splitted[7][:-1]

        print("Number: ", i)
        #print("Date  : ", current_time.split(' ')[0])
        print("Time  : ", current_time.split(' ')[1])
        print("V [mV]: ", voltage_mv)
        print("I [mA]: ", current_ma)
        print("W [mW]: ", power_mw)
        print("-------------------------------------")

        json_body = [
        {
            "measurement": table,
            "fields": {
                "voltage_mv": voltage_mv,
                "current_ma": current_ma,
                "power_mw": power_mw
            }
        }]
        client.write_points(json_body)

        if i != amount:
            sleep(1)

    duration = 0.1  # seconds
    freq = 300  # Hz
    for i in range(1,4):
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        sleep(0.1)


