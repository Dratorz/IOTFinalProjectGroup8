import time
import sys
from datetime import datetime
import requests
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
my_header = {'Content-Type': 'application/json'}

error_report = {
    "httpStatus": 0,
    "logs": [],
    "message": "",
    "url":""
}

def post_reading():
    reading_object = {
        "Humidity": humidity,
        "Celsius": temperature_c,
        "Fahrenheit": temperature_f,
        "Time": timestamp.strftime("%Y/%m/%d, %H:%M:%S")
    }
    sent = False
    
    while not sent:
        try:
            requests.get('https://www.google.com', timeout=5)
            response = requests.post('http://chunk3r.pythonanywhere.com/create/',
                                json=reading_object,
                                timeout=5)
            print(reading_object)
            
            if response.status_code == 404:
                print('[404]-> NOT FOUND')
            elif response.status_code == 200:
                sent = True
                print('OK')
                
            else:
                print(response.status_code)
        except:
            print("Offline")
            #save reading and offline status to local db
        

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
        if dht_current_retries == 15:
            error_report['logs'].append("Couldn't read from sensor after 15 retries.")
            done = True
        
    time.sleep(time_interval)

dhtDevice.exit()
sys.exit()
    
