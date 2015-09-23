
import MySQLdb
import sys





import os
import sys
import shutil
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import Adafruit_BMP.BMP085 as BMP085
import time
import read_mcp3008
import spidev

global Sommerzeit 
Sommerzeit = 7200000
global Winterzeit
Winterzeit = 3600000
global aktuelle_Zeit
aktuelle_Zeit  = Sommerzeit
#=============================LDR2=================================
spi = spidev.SpiDev()
spi.open(0,0)


#=============================BMP085=================================
sensor = BMP085.BMP085()

#=============================DHT22==================================
import dhtreader
type = 22
pin = 22
dhtreader.init()

def get_Pressur():
    Druck = sensor.read_pressure()
    Druck = Druck/100
    return Druck
    
def get_Temp():
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
	   


def get_LDR():
    
    LDR =  read_mcp3008.readAnalogData(0, 11, 10, 9, 8)
    return LDR


def get_LDR2():
    
    UV = read_mcp3008.readAnalogData(2, 11, 10, 9, 8)
    return UV
        



def get_O2():
    # use chip select CE0, channel 0
    
    O2 = read_mcp3008.readAnalogData(1, 11, 10, 9, 8)
    return O2
        
def get_unixtime():
    timestamp = int(time.time())
    timestamp  = (timestamp *1000) + aktuelle_Zeit 
    #print timestamp  
    return timestamp
#=======================================================================




def update():
    
    
    feucht, temp = get_Temp()
    Druck = get_Pressur()
    LDR = get_LDR()
    UV = get_LDR2()
    O2 = get_O2()
    time = get_unixtime()
    
    try:
        db = MySQLdb.connect(
        host = '87.106.13.169', 
        user = 'wetterpi198', 
        passwd = 'Raspi19822', 
        db = 'wetterpi198')
    

    except ValueError:
        print "Es ist der %02i.%02i.%04i." " %02i.%02i"  % (tag,monat,jahr,Stunde,Minute)  + "      Datenbankfehler"
        update()
        exit()
        
        
    query = """INSERT INTO wetter (UnixTime, Temperatur, Druck, Feuchtigkeit, Helligkeit, UV, O2) VALUES ('%s','%s','%s','%s','%s','%s','%s')""" % (time, temp, Druck, feucht, LDR, UV, O2)
    #print query
    cursor = db.cursor() 

    cursor.execute(query)
    db.commit()
    cursor.close()   
    db.close()

GPIO.setwarnings(False)
update()
exit()