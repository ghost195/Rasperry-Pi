#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)



temp =""

def tempsensorauslesen():
    
    global temp
    file = open('/sys/devices/w1_bus_master1/w1_master_slaves')
    w1_slaves = file.readlines()
    file.close()
    for line in w1_slaves:
        w1_slave = line.split("\n")[0]
        file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')
        filecontent = file.read()
        file.close()
        stringvalue = filecontent.split("\n")[1].split(" ")[9]
        temperature = float(stringvalue[2:]) / 1000
        #print(str(w1_slave) + " | %5.3f °C" % temperature)
        temp = (temperature)
        
    
    return temp
GPIO.output(25, GPIO.HIGH)

log = open("temp.txt", "w")

i=0
while i < 36000:
    print(temp)
    
    tempsensorauslesen()
    time.sleep(1)
    now = str(datetime.now())
    tempi = str(temp)
    log.write(now + "   " + tempi + "\n")
    i = i + 1
log.flush()
log.close()
GPIO.output(25, GPIO.LOW)
  
    
        
