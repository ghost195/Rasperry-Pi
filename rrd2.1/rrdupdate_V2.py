import MySQLdb
import sys
import rrdtool
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
        

	
	
def update():
	
	feucht, temp = get_Temp()
	print temp
	
	
	rrdtool.update('wetter.rrd','N:'+`temp`)
		
   
	
""""	
def update():
    feucht, temp, Druck, LDR, UV, O2 = load_Values()
    rrdtool.update('temperatures_all.rrd','N:'+`temp`+":"+`feucht`+":"+`Druck`+":"+`LDR`+":"+`UV`+":"+`O2`)


def test():
    Druck = get_Pressur()
    feucht, temp = getTemp()
    LDR = get_LDR()
    UV = get_UV()
    O2 = get_O2()
    data = "N:%.2f:%.2f:%.2f:%.2f:%.2f:%.2f" % (temp, feucht, Druck, LDR, UV, O2)
    rrdtool.update("%s/temperatures_all.rrd" % (os.path.dirname(os.path.abspath(__file__))),data)
    #rrdtool.update('temperatures_all.rrd','N:'+`temp`+":"+`feucht`+":"+`Druck`+":"+`LDR`+":"+`UV`+":"+`O2`)
    
    f = open('/home/pi/Programmierung/cron.txt','a')
    f.write('test11111\n')
    f.close()

"""	
	
update()