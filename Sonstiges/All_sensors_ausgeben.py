import dhtreader
import Adafruit_BMP.BMP085 as BMP085
import spidev
import time
import os
import eeml
import sys
import syslog
import json
import random
import pylcdlib
from datetime import datetime


type = 22
pin = 4
dhtreader.init()

spi = spidev.SpiDev()
spi.open(0,0)



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



def getPressur():
    sensor = BMP085.BMP085()
    #print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
    #print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())
    #print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
    #print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())
    pressur = (sensor.read_pressure()/100)
    return pressur
    

def getAnalog(channel):
    try:
        chan = channel
        response = spi.xfer2([1, 128+(chan<<4), 0])
        value = (response[1] & 3) * 256 + response[2]
        #print value
        return value
        time.sleep(1)
    except KeyboardInterrupt:
        spi.close()

def setDisplay(String, Name, Einheit):
    
    lcd = pylcdlib.lcd(0x27,1)
    lcd.lcd_write(0x01);
    Einheit1 = str(Einheit)
    Beschriftung = str(Name)
    Druck = String
    Druck_str = str(Druck) + Einheit1
    lcd.lcd_puts(Name ,1) #display "Raspberry Pi" on line 1
    lcd.lcd_puts(Druck_str,2) #display "Take a byte!" on line 2
    lcd.lcd_backlight(1)
    

#============================================================



API_KEY = '6sEVeTgPjqsZF9k71G5Rd88lKd8GJZvCgeCPN1ghWH8gFfMZ'
FEED = 1652750452
API_URL = '/v2/feeds/{feednum}.xml' .format(feednum = FEED)



while True:
      
    
    Feucht, Temp = getTemp()
    print  Feucht
    setDisplay(Feucht, "Luftfeuchte", "  %")
    time.sleep(2)
    print  Temp
    setDisplay(Temp, "Temperatur", "  C")
    time.sleep(2)
    Pressur = getPressur()
    print   Pressur
    setDisplay(Pressur, "Luftdruck", "  hPa")
    time.sleep(2)
    
    
    
    
 
    # LDR Lichtwiderstand
    Analog0 = getAnalog(0)
    print Analog0
    setDisplay(Analog0, "Helligkeit", " ")
    time.sleep(2)
    # Sauerstoff Guete
    Analog1 = getAnalog(1)
    print Analog1
    setDisplay(Analog1, "Sauerstoff Guete", " ")
    time.sleep(2)
    # UV
    Analog2 = getAnalog(2)
    print Analog2
    setDisplay(Analog2, "UV", " ")
    #CPU_temp = getCPUtemperature()
    
    # open up your feed
    pac = eeml.Pachube(API_URL, API_KEY)

    #compile data
    
    
    
    
    
    pac.update([eeml.Data("Temperatur", Temp, unit=eeml.Celsius())])
    pac.update([eeml.Data("Feuchtigkeit", Feucht)])
    pac.update([eeml.Data("Luftdruck", Pressur)])
    pac.update([eeml.Data("Helligkeit", Analog0)])
    pac.update([eeml.Data("Sauerstoff", Analog1)])
    pac.update([eeml.Data("UV", Analog2)])
    #pac.update([eeml.Data("CPU_Temperature", CPU_temp, unit=eeml.Celsius())])
    #pac.update([eeml.Data("Disk_free", DISK_free, unit=eeml.Celsius())])
    #pac.update([eeml.Data("RAM__Used", RAM_used, unit=eeml.Celsius())])
    #pac.update([eeml.Data("RAM_Free", RAM_free, unit=eeml.Celsius())])

    # send data to cosm
    pac.put()
    time.sleep(5)

