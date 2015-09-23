import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.OUT)

count = 0


i = 0

while True:
    GPIO.output(25, GPIO.HIGH)
    time.sleep(0.50)
    GPIO.output(25, GPIO.LOW)
    time.sleep(1.05)
    


    inputValue = GPIO.input(24)
    
    if(inputValue == True):
        while i < 20:
            GPIO.output(25, GPIO.HIGH)
            time.sleep(0.10)
            GPIO.output(25, GPIO.LOW)
            time.sleep(0.20)
            i = i + 1
        count = count + 1
        print("Taster " + str(count) + " gedruekt" )
        os.system("shutdown now -f")
    time.sleep(1)
    


