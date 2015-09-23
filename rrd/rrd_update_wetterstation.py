import rrdtool
import os
import time
import sys
import shutil
import RPi.GPIO as GPIO


fname = 'temperatures.rrd'
gfname = '/var/www/Web/test.png'
gfname24 = '/var/www/Web/test24.png'


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
        
        temp = (temperature)


def graph_erzeugen_3h():
    rrdtool.graph(gfname ,
                  '--start' , '-10800' ,
                  '--end' , 'now' ,
                  '-w 785' , '-h 350' ,
                  '--slope-mode',              
                  '--vertical-label' , 'Temperatur' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'Temperaturverlauf' ,
                  '--lower-limit' , '0' ,
                  'DEF:temp1=%s:temp1:MAX' % fname ,
                  'LINE1:temp1#FF0000:temp 1')




def graph_erzeugen_24h():
    rrdtool.graph(gfname24 ,
                  '--start' , '-86400' ,
                  '--end' , 'now' ,
                  '-w 785' , '-h 350' ,
                  '--slope-mode',              
                  '--vertical-label' , 'Temperatur' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'Temperaturverlauf' ,
                  '--lower-limit' , '0' ,
                  'DEF:temp1=%s:temp1:MAX' % fname ,
                  'LINE1:temp1#FF0000:temp 1')

    
    

i = 0

while i < 1 :
    tempsensorauslesen()
    rrdtool.update('temperatures.rrd', 'N:'+`temp`)
    

    
    print(i)

    #i = i + 1
    graph_erzeugen_3h()
    graph_erzeugen_24h()
    time.sleep(60)
    
 
