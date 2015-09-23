#!/usr/bin/env python

import sys

def read_temp():
   sens= subprocess.Popen(
       ["/home/pi/lol_dht22/"],
       stdout = subprocess.PIPE,
       stderr = subprocess.PIPE)
   out, error = sens.communicate()
   return out

out = read_temp()
print out
