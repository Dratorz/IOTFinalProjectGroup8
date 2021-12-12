# IOTFinalProjectGroup8_Pi
Repository for the IOT Final Project using a DHT11 sensor to capture temperature and humidity and send it to a webservice hosted on pythonanywhere.com. The webservice is accessed by the Android app which displays the readings and other statistics.

This repository is for the Pi's code.

Follow this tutorial to set up your PI:
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

Then run these commands:
pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2

You can use the crontab file to decide when you want each job to 
run. Modify your crontab file by executing crontab -e in your 
terminal. The first part with the '*'s decides the schedule, the
second part is the location of your python executable, and the
third part is the location of your script.