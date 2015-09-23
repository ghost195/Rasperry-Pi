import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

data = rrdtool.fetch('temperatures_all.rrd',"MAX","-r", "60" , "-s" ,"-60")
i = 0
while i < 100:
    GPIO.output(25, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(25, GPIO.LOW)
    time.sleep(0.05)
    i = i+1
