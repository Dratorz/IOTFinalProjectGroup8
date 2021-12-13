from DAL.DBReading import DBReading
from Entities.Reading import Reading
import time
import sys
from datetime import datetime
import board
import adafruit_dht
#from DAL.DBTemp import DBTemp

done = False
time_interval = 5
dht_max_retries = 15
dht_current_retries = 0

dhtDevice = adafruit_dht.DHT11(board.D4)
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
        post_reading()
        done = True
    except RuntimeError as error:
        dht_current_retries += 1
        print(datetime.now())
        print(error.args[0])
        if dht_current_retries == dht_max_retries:
            error_report['logs'].append("Couldn't read from sensor after 15 retries.")
            done = True
        
    time.sleep(time_interval)

dhtDevice.exit()
sys.exit()
    
