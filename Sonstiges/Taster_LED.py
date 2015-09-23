import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.OUT)

count = 0

while True:
    inputValue = GPIO.input(24)
    if(inputValue == True):
        count = count + 1
        print("Taster " + str(count) + " gedruekt" )
        GPIO.output(25, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(25, GPIO.LOW)
    time.sleep(.01)
    
    
    
