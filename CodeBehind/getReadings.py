from DAL.DBReading import DBReading
from Entities.Reading import Reading
import time
import sys
from datetime import datetime
import board
import adafruit_dht

def get_serial():
    # Extract serial from cpuinfo file
    cpuserial = ""
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"
    
    return cpuserial

done = False
time_interval = 5
dht_max_retries = 15
dht_current_retries = 0

dhtDevice = adafruit_dht.DHT11(board.D27)
#temp_db = DBTemp()

humidity = 0.0
temperature_c = 0.0
temperature_f = 0.0
timestamp = ''


while not done:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = (temperature_c * (9/5)) + 32
        humidity = dhtDevice.humidity
        timestamp = datetime.now()
        print("\n {}".format(timestamp))
        print("C Temp: {0:.1f}\tF Temp: {1:.1f}\tHumidity: {2:.1f}%".format(temperature_c, temperature_f, humidity))
        done = True
    except RuntimeError as error:
        dht_current_retries += 1
        print(datetime.now())
        print(error.args[0])
        if dht_current_retries == dht_max_retries:
            done = True
        
    time.sleep(time_interval)

dhtDevice.exit()

done = False
time_interval = 2
db_max_retries = 15
db_current_retries = 0

cReading = Reading(get_serial(), datetime.now(), temperature_c, 1, 1)
fReading = Reading(get_serial(), datetime.now(), temperature_f, 1, 2)
hReading = Reading(get_serial(), datetime.now(), humidity, 2, 4)

while not done:
    try:
        readings = DBReading()
        readings.insert_reading(cReading)
        readings.insert_reading(fReading)
        readings.insert_reading(hReading)
        done=True
    except Exception as e:
        console.log(e)
        db_current_retries += 1
        if db_current_retries == db_max_retries:
            done = True
        

sys.exit()
    
