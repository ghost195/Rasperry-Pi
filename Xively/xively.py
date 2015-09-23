#!/usr/bin/env python
import time
import os
import eeml
import sys
import syslog
import json
import dhtreader
import random
from datetime import datetime

type = 22
pin = 4
dhtreader.init()




def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def getTemp():
    check = False
    
    while check == False:
        
        data = dhtreader.read(type, pin)
        if data != None:
           
            feuchtigkeit = data[1]
            feuchtigkeit1 = round(feuchtigkeit, 3)
            Temperatur = data[0]
            Temperatur1 = round(Temperatur, 3)
            #print feuchtigkeit1
            #print Temperatur1
            check = True
            
            return feuchtigkeit1, Temperatur1
        else:
            check = False
            #Wenn Objekt None ist dann wird nichts zuruekgegeben deswegen muss die Schleife nochmals durchlaufen


API_KEY = '6sEVeTgPjqsZF9k71G5Rd88lKd8GJZvCgeCPN1ghWH8gFfMZ'
FEED = 1652750452
API_URL = '/v2/feeds/{feednum}.xml' .format(feednum = FEED)


log = open("Temp_log.txt", "w")

while True:
      
    
    Feucht, Temp = getTemp()
    print Feucht
    print Temp
    CPU_temp = getCPUtemperature()
    
    # open up your feed
    pac = eeml.Pachube(API_URL, API_KEY)

    #compile data
    
    now = str(datetime.now())
    log.write(now + " " + str(Temp) + "\n")
    log.write(now + " " + str(Feucht) + "\n")
    
    
    
    pac.update([eeml.Data("Temperatur", Temp, unit=eeml.Celsius())])
    pac.update([eeml.Data("Feuchtigkeit", Feucht)])
    pac.update([eeml.Data("CPU_Temperature", CPU_temp, unit=eeml.Celsius())])
    #pac.update([eeml.Data("Disk_free", DISK_free, unit=eeml.Celsius())])
    #pac.update([eeml.Data("RAM__Used", RAM_used, unit=eeml.Celsius())])
    #pac.update([eeml.Data("RAM_Free", RAM_free, unit=eeml.Celsius())])

    # send data to cosm
    pac.put()
    time.sleep(10)
log.flush()
log.close()
