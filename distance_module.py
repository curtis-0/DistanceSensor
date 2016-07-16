# Script Name	: distance_module.py
# Author		: Curtis Handley
# Created		: 16 Jul 2016
# Version		: 1.0

# Description	: Measure the distance between a the Ultrasonic emitter and an object.

import RPi.GPIO as GPIO
import time
import requests
import json

# Being module

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)

time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150
distance = round(distance, 2)

print("Distance:", distance, "cm")

url = 'http://luah.co.uk/'
payload = {'distance': distance}

# GET
r = requests.get(url)

# GET with params in URL
r = requests.get(url, params=payload)

# POST with form-encoded data
r = requests.post(url, data=payload)

# POST with JSON 
r = requests.post(url, data=json.dumps(payload))

GPIO.cleanup()

# End 