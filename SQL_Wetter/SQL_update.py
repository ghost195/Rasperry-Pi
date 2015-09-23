
import MySQLdb
import sys



import os
import time
import sys
import shutil
import RPi.GPIO as GPIO
import dhtreader
from datetime import datetime
import Adafruit_BMP.BMP085 as BMP085
from _ast import Str
from mcp3008 import *
sensor = BMP085.BMP085()
import spidev
spi = spidev.SpiDev()
spi.open(0,0)


type = 22
pin = 22
dhtreader.init()




#============================SENSOREN AUSLESEN===============================================
#============================O2========================================================
def get_O2():
    # use chip select CE0, channel 0
    try:
        chan = 1
        response = spi.xfer2([1, 128+(chan<<4), 0])
        value = (response[1] & 3) * 256 + response[2]
        return value
    except KeyboardInterrupt:
        spi.close()




#============================UV=======================================================
def get_UV():
    try:
        chan = 2
        response = spi.xfer2([1, 128+(chan<<4), 0])
        value = (response[1] & 3) * 256 + response[2]
        return value
    except KeyboardInterrupt:
        spi.close()


#===========================LDR==============================================================
def get_LDR():
   
    zaehler = 1
    mcp = MCP3008()
    LDR_CHANNEL = 0
    analog_wert = mcp.analog_read(LDR_CHANNEL)
    return analog_wert



#===========================TEMP UND FEUCHTE================================================

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

#=================================DRUCK======================================================

def get_Pressur():
    Pressur = sensor.read_pressure()
    Pressur = float(Pressur)
    Pressur = Pressur/100
    #print Pressur
    return Pressur


#=======================================================================






def update():
    feucht, temp = getTemp()
    Druck = get_Pressur()
    LDR = get_LDR()
    UV = get_UV()
    O2 = get_O2()
    
    
    
    #print temp
    #print feucht
    #print Druck
    #print LDR
    #print UV
    #print O2
    
    try:
        db = MySQLdb.connect(
        host = '87.106.13.169', 
        user = 'wetterpi198', 
        passwd = 'Raspi19822', 
        db = 'wetterpi198')
    

    except ValueError:
        print("Fehler")
        update()
    

    query = """INSERT INTO wetter (Temperatur, Druck, Feuchtigkeit, Helligkeit, UV, O2) VALUES ('%s','%s','%s','%s','%s','%s')""" % (temp, Druck, feucht, LDR, UV, O2)
    #print query
    cursor = db.cursor() 

    cursor.execute(query)
    db.commit()
    cursor.close()

    #db.execute("SELECT * FROM wetter")

    #for row in db.fetchall() :
    #    print row[0]
    time.sleep(40)


    
    
    
while True:
    update()    
    
    
    
    
    



