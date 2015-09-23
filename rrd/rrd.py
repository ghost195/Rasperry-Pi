#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, os, rrdtool, time, sys




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


rrdtool.update(temperatur.rdd 920804700:12345)
timer.sleep(2)
