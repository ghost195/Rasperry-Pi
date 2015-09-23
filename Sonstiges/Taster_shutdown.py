# Simple script for shutting down the raspberry Pi at the press of a button.
# by Inderpreet Singh
 
import RPi.GPIO as GPIO
import time
import os
 

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, True)
 

def Shutdown(channel):
 os.system("sudo shutdown -h now")
 

while True:
    if not (GPIO.input(24)):
        print "HHHH"
        GPIO.output(23, False)
        time.sleep(.1)
        GPIO.output(23, True)
        time.sleep(.1)
        GPIO.output(23, False)
        time.sleep(.1)
        GPIO.output(23, True)
        os.system("piusvd stop")
        os.system("sudo shutdown -h now")
    time.sleep(.5)
