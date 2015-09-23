#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import sys module
import sys

# Open 1-wire slaves list for reading
file = open('/sys/devices/w1_bus_master1/w1_master_slaves')

# Read 1-wire slaves list
w1_slaves = file.readlines()

# Close 1-wire slaves list
file.close()

# Print header for results table
print("Sensor ID       | Temperature")
print("-----------------------------")

# Repeat following steps with each 1-wire slave
for line in w1_slaves:
     w1_slave = line.split("\n")[0]
     file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')
     filecontent = file.read()
     file.close()
     stringvalue = filecontent.split("\n")[1].split(" ")[9]
     temperature = float(stringvalue[2:]) / 1000
     print(str(w1_slave) + " | %5.3f °C" % temperature)
sys.exit(0)
    
