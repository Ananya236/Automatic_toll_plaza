import RPi.GPIO as r
import Adafruit_DHT as a
import time as t
pin=4
sensor=a.DHT11
while (1):
    hum,temp=a.read_retry(sensor,pin)
    if(hum is not None and temp is not None):
        print(hum)
        print(temp)

