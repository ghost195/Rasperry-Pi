import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

i = 0
while i < 900:
    GPIO.output(25, GPIO.HIGH)
    time.sleep(0.50)
    GPIO.output(25, GPIO.LOW)
    time.sleep(1.05)
    i = i+1
