import os
from datetime import datetime
from time import sleep
import random
global res

 

def Funktion1():
    Funktion2()
   


def Funktion2():
    getCPUtemp()
    

def getCPUtemp():
    global res
    res = os.popen('vcgencmd measure_temp').readline()
    
    
       


    

log = open("log.txt", "w")
i = 0
res = ""
while i < 10000:
    getCPUtemp()
    now = str(res)
    log.write(now + "\n")
    print(now)
    print(i)
    i = i+1
log.flush()
log.close()


