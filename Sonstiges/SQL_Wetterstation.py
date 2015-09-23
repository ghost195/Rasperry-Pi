#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import time
import sys
from datetime import datetime
import RPi.GPIO as GPIO


i = 0
temp=""

con = mdb.connect('localhost', 'wetterpi', 'raspi22', 'Wetterstation');




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
        #print(str(w1_slave) + " | %5.3f Â°C" % temperature)
        temp = (temperature)
       

        


def schreiben():
    with con:
        cur = con.cursor()
        #Nachkoma stellen abschneiden
        temp_nachkomma = "%5.1f" % temp
        #Temperatur in String konvertieren
        strtemp = str(temp_nachkomma)
        #SQL string zusammenbauen
        stringsql ="INSERT INTO Wetter(Temperatur) VALUES('" + strtemp + "')"
        
        print(stringsql)
        #Befehl an DB schicken
        cur.execute(stringsql)
         

       
        


        


while i < 500:
    tempsensorauslesen()
    schreiben()
    time.sleep(2)
    i = i + 1
    
