import RPi.GPIO as GPIO
import time
import pylcdlib
import os

lcd = pylcdlib.lcd(0x27,1)
lcd.lcd_write(0x01);


# Variable Counter definieren
Counter = 0

# SoC als Pinreferenz waehlen
GPIO.setmode(GPIO.BCM)  

# Pin 24 vom SoC als Input deklarieren und Pull-Down Widerstand aktivieren
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  

# ISR
def Interrupt(channel):  
    # Zugriff auf globale Variablen
    global Counter

    # Counter um eins erhoehen und ausgeben
    Counter = Counter + 1
    print "Counter " + str(Counter) 
    time.sleep(1)
    lcd.lcd_puts("Tschuess",1) #display "Raspberry Pi" on line 1
    lcd.lcd_backlight(1)
    os.system("shutdown now -f")
    
# Interrupt Event hinzufuegen. Pin 24, auf steigende Flanke reagieren und ISR "Interrupt" deklarieren
GPIO.add_event_detect(24, GPIO.RISING, callback = Interrupt, bouncetime = 200)   
  
# Endlosschleife
while True:
    time.sleep(1)