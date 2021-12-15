from DAL.DBReading import DBReading
from Entities.Reading import Reading
import requests
import time
import sys
from datetime import datetime

check_network = True
online = False
check_max_retries = 15
check_current_retries = 0


while check_network:
    print("Checking if the PI is online")
    try:
        response = requests.get('https://www.google.com', timeout=3)
        if response.status_code == 200:
            print("PI is online")
            check_network = False
            online = True
    except:
        print("Failed to reach network, retrying for the {} time...".format(check_current_retries))
        check_current_retries += 1
        # record logs into an error_report
        if check_current_retries == check_max_retries:
            print("Failed to reach network after {} retries.".format(post_current_retries))
            check_network = False

if online == False:
    sys.exit()
else:    
    readings = DBReading()
    
    offline_readings = readings.select_readings(False)
    check_ws = True
    check_current_retries = 0
    
    while check_ws:
        
        response = requests.post('http://chunk3r.pythonanywhere.com/create/',
                        json=offline_readings,
                        timeout=3)
        if response.status_code == 201 or response.status_code == 200:
            check_ws = False
        else:
            check_current_retries += 1
            print("Failed to reach web service, retrying {}...".format(check_current_retries))
            # record logs into an error_report
            if check_current_retries == check_max_retries:
                print("Failed to reach web service after {} retries.".format(check_current_retries))
                check_ws = False
                
sys.exit()


