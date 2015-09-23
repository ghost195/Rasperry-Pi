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
from mcp3008 import *
sensor = BMP085.BMP085()
import spidev
spi = spidev.SpiDev()
spi.open(0,0)


fname = 'temperatures_all.rrd'
gfnameT_3H = '/var/www/wetterchards/temp_3H.png'
gfnameT_24H = '/var/www/wetterchards/temp_24H.png'
gfnameF_3H = '/var/www/wetterchards/feucht_3H.png'
gfnameF_24H = '/var/www/wetterchards/feucht_24H.png'
gfnameD_3H = '/var/www/wetterchards/druck_3H.png'
gfnameD_24H = '/var/www/wetterchards/druck_24H.png'
gfnameLDR_3H = '/var/www/wetterchards/ldr_3H.png'
gfnameLDR_24H = '/var/www/wetterchards/ldr_24H.png'
gfnameUV_3H = '/var/www/wetterchards/uv_3H.png'
gfnameUV_24H = '/var/www/wetterchards/uv_24H.png'
gfnameO2_3H = '/var/www/wetterchards/o2_3H.png'
gfnameO2_24H = '/var/www/wetterchards/o2_24H.png'
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




#====================================DRUCK_GTAPH================================

def graph_erzeugen_3h_DRUCK():
    rrdtool.graph(gfnameD_3H ,
                  '--start' , '-10800' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'Luftdruck in hPa' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'Luftdruckverlauf' ,
                  '--units-exponent' , '0' ,
                  'DEF:druck=%s:druck:MAX' % fname ,
                  'LINE1:druck#FF0000:druck MAX')
    
def graph_erzeugen_24h_DRUCK():
    rrdtool.graph(gfnameD_24H ,
                  '--start' , '-86400' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'Luftdruck in hPa' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'Luftdruckverlauf' ,
                  '--units-exponent' , '0' ,
                  'DEF:druck=%s:druck:AVERAGE' % fname ,
                  'LINE1:druck#FF0000:druck  MAX')




#====================================TEMP_GRAPH====================================
def graph_erzeugen_3h_TEMP():
    rrdtool.graph(gfnameT_3H ,
                  '--start' , '-10800' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'Temperatur' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'Temperaturverlauf' ,
                  '--lower-limit' , '-20' ,
                  'DEF:temp0=%s:temp0:MAX' % fname ,
                  'LINE1:temp0#FF0000:temp 0 MAX')

def graph_erzeugen_24h_TEMP():
    rrdtool.graph(gfnameT_24H ,
                  '--start' , '-86400' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'Temperatur' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'Temperaturverlauf' ,
                  '--lower-limit' , '-20' ,
                  'DEF:temp0=%s:temp0:AVERAGE' % fname ,
                  'LINE1:temp0#FF0000:temp 0 AVERAGE')

#=====================================FEUCHT_GRAPH=============================

def graph_erzeugen_3h_FEUCHT():
    rrdtool.graph(gfnameF_3H ,
                  '--start' , '-10800' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'Feuchtigkeit' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'Feuchtigkeitsverlauf' ,
                  '--alt-autoscale' , 
                  '--alt-y-grid' , 
                  '--units-exponent' , '0' ,
                  'DEF:feucht=%s:feucht:MAX' % fname ,
                  'LINE1:feucht#0000FF:feucht 1 MAX')

def graph_erzeugen_24h_FEUCHT():
    rrdtool.graph(gfnameF_24H ,
                  '--start' , '-86400' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'Feuchtigkeit' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'Feuchtigkeitsverlauf' ,
                  '--alt-autoscale' , 
                  '--alt-y-grid' , 
                  '--units-exponent' , '0' ,
                  'DEF:feucht=%s:feucht:AVERAGE' % fname ,
                  'LINE1:feucht#0000FF:feucht 1 AVERAGE')


#==========================================LDR GRAPH==========================================

def graph_erzeugen_3h_LDR():
    rrdtool.graph(gfnameLDR_3H ,
                  '--start' , '-10800' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'Helligkeit' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'Helligkeit' ,
                  '--alt-autoscale' , 
                  '--alt-y-grid' , 
                  '--units-exponent' , '0' ,
                  'DEF:ldr=%s:ldr:MAX' % fname ,
                  'LINE1:ldr#FF0000:ldr MAX')


def graph_erzeugen_24h_LDR():
    rrdtool.graph(gfnameLDR_24H ,
                  '--start' , '-86400' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'Helligkeit' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'Helligkeit' ,
                  '--alt-autoscale' , 
                  '--alt-y-grid' , 
                  '--units-exponent' , '0' ,
                  'DEF:ldr=%s:ldr:AVERAGE' % fname ,
                  'LINE1:ldr#0000FF:ldr 1 AVERAGE')


#===========================================UV=======================================
def graph_erzeugen_3h_UV():
    rrdtool.graph(gfnameUV_3H ,
                  '--start' , '-10800' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'UV' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'UV' ,
                  '--alt-autoscale' , 
                  '--alt-y-grid' , 
                  '--units-exponent' , '0' ,
                  'DEF:uv=%s:uv:MAX' % fname ,
                  'LINE1:uv#FF0000:uv MAX')
    

def graph_erzeugen_24h_UV():
    rrdtool.graph(gfnameUV_24H ,
                  '--start' , '-86400' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'UV' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'UV' ,
                  '--lower-limit' , '0' ,
                  'DEF:uv=%s:uv:AVERAGE' % fname ,
                  'LINE1:uv#0000FF:uv 1 AVERAGE')

#==================================================O2================================
def graph_erzeugen_3h_O2():
    rrdtool.graph(gfnameO2_3H ,
                  '--start' , '-10800' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'O2' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'O2' ,
                  '--alt-autoscale' , 
                  '--alt-y-grid' , 
                  '--units-exponent' , '0' ,
                  'DEF:o2=%s:o2:MAX' % fname ,
                  'LINE1:o2#FF0000:o2 MAX')
    

def graph_erzeugen_24h_O2():
    rrdtool.graph(gfnameO2_24H ,
                  '--start' , '-86400' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'O2' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'O2' ,
                  'DEF:o2=%s:o2:AVERAGE' % fname ,
                  'LINE1:o2#0000FF:o2 1 AVERAGE')
#==========================================================================================    


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
        
   

update()  
time.sleep(2)
graph_erzeugen_3h_TEMP()
graph_erzeugen_24h_TEMP()
  

#==============================================
"""
log = open("Temp_log.txt", "w")

i = 12

while True:
    
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

    #now = str(datetime.now())
    #log.write(now + " " + str(temp) + "\n")
    #log.write(now + " " + str(feucht) + "\n")
    #log.write(now + " " + str(Druck) + "\n")
    #log.write(now + " " + str(LDR) + "\n")
    time.sleep(2)
    #rrdtool.update('temperatures_all.rrd','N:'+`temp`)
    rrdtool.update('temperatures_all.rrd','N:'+`temp`+":"+`feucht`+":"+`Druck`+":"+`LDR`+":"+`UV`+":"+`O2`)
    
    time.sleep(1)
    graph_erzeugen_3h_TEMP()
    #print "3h_Temp"
    time.sleep(10)
    graph_erzeugen_3h_DRUCK()
    #print "3h_Druck"
    time.sleep(11)
    graph_erzeugen_3h_FEUCHT()
    #print "3h_Feucht"
    #print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" 
    #print feucht
    time.sleep(10)
    graph_erzeugen_3h_LDR()
    #print "3h_LDR"
    time.sleep(10)
    graph_erzeugen_3h_UV()
    #print "3h_UV"
    time.sleep(10)
    graph_erzeugen_3h_O2()
    #print "3h_O2"
    time.sleep(1)
    #print i
    if i == 2:
        graph_erzeugen_24h_FEUCHT()
        #print "24_Feucht"
        time.sleep(1)
    
    if i == 4:
        graph_erzeugen_24h_DRUCK()
        #print "24_Druck"
        time.sleep(1)
    
    if i == 6:
        graph_erzeugen_24h_LDR()
        #print "24_LDR"
        time.sleep(1)
         
    if i == 8:
        graph_erzeugen_24h_UV()
        #print "24_UV"
        time.sleep(1)
    
    if i == 10:         
        graph_erzeugen_24h_O2()
        #print "24_O2"
        time.sleep(1)
        
    if i == 12:
                
        #print "24_Temp"
        graph_erzeugen_24h_TEMP()
        time.sleep(1)
        
        
        i = 0
    i = i+1
"""
