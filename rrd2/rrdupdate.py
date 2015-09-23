import rrdtool
import os
import time
import sys
import shutil
import RPi.GPIO as GPIO
import dhtreader
from datetime import datetime
import Adafruit_BMP.BMP085 as BMP085
from _ast import Str
sensor = BMP085.BMP085()
import spidev
spi = spidev.SpiDev()
spi.open(0,0)
import read_mcp3008

type = 22
pin = 22
dhtreader.init()

#============================SENSOREN AUSLESEN===============================================
#============================O2========================================================
def get_O2():
    value = 0
    value = read_mcp3008.readAnalogData(1, 11, 10, 9, 8)
    #print value
    return value




#============================UV=======================================================
def get_UV():
    value = 0
    value = read_mcp3008.readAnalogData(2, 11, 10, 9, 8)
    #print value
    return value
 


#===========================LDR==============================================================
def get_LDR():
    value = 0
    value = read_mcp3008.readAnalogData(0, 11, 10, 9, 8)
    #print value
    return value



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




def load_Values():
    feucht, temp = getTemp()
    Druck = get_Pressur()
    LDR = get_LDR()
    UV = get_UV()
    O2 = get_O2()
    return feucht,temp,Druck,LDR,UV,O2



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
    
test()