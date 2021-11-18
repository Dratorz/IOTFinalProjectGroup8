import time
from datetime import datetime
import requests
import board
import adafruit_dht


dhtDevice = adafruit_dht.DHT11(board.D17, use_pulseio=False)

time_interval = 10
humidity = 0.0
temperature_c = 0.0
temperature_f = 0.0
timestamp = ''
my_header = {'Content-Type': 'application/json'}

def post_reading():
    reading_object = {
        "humidity": humidity,
        "temperature_c": temperature_c,
        "temperature_f": temperature_f,
        "timestamp": timestamp.strftime("%Y/%m/%d, %H:%M:%S")
        }
    
    try:
        requests.get('https://www.google.com', timeout=2)
        response = requests.post('http://chunk3r.pythonanywhere.com/create',
                            json=reading_object,
                            timeout=3)
        
        if response.status_code == 404:
            print('[404]-> NOT FOUND')
        elif response.status_code == 200:
            print('OK')
            print(reading_object)
        else:
            print(response.status_code)
    except:
        print("Offline")   

while True:  
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = (temperature_c * (9/5)) + 32
        humidity = dhtDevice.humidity
        timestamp = datetime.now()
        print("\n {}".format(timestamp))
        print("C Temp: {0:.1f}\tF Temp: {1:.1f}\tHumidity: {2:.1f}%".format(temperature_c,
                                                                            temperature_f,
                                                                            humidity))
        post_reading()
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(time_interval)
    
