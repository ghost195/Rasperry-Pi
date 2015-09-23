import MySQLdb
import sys
import pylcdlib
import time
import os

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.output(17, GPIO.HIGH)
GPIO.output(18, GPIO.LOW)

lcd = pylcdlib.lcd(0x27,1)

def Interrupt(channel):
    print "Du hast mich gedruekt"
    print "Der Rasperry Pi wird jetzt heruntergefahren"
    info1 = "PC herunterfahren"
    Lcd_anzeigen("INFO", info1) 
    time.sleep(2)
    os.system("sudo shutdown -h 0")


GPIO.add_event_detect(24, GPIO.RISING, callback = Interrupt, bouncetime = 200)   


def Lcd_anzeigen(Was, Wert):
    
    
    lcd.lcd_write(0x01);
    lcd.lcd_puts(Was,1) #display "Raspberry Pi" on line 1
    lcd.lcd_puts(Wert,2) #display "Take a byte!" on line 2
    

def MySQL_read():
    
    try:
        db = MySQLdb.connect(
        host = '87.106.13.169', 
        user = 'wetterpi198', 
        passwd = 'Raspi19822', 
        db = 'wetterpi198')
    

    except ValueError:
        print "Fehler Bei dem Versuch die Verbindung aufzubauen"
       
        exit()
        
        
  
    
    cursor = db.cursor()
    cursor.execute("SELECT Temperatur FROM wetter ORDER BY UnixTime DESC Limit 1")
    result = cursor.fetchall()
    db.commit()
    Temp = result
    Temp1 = str(Temp)           # in String umwandeln
    Temp2 = Temp1[2:6]          # String ausschneiden von 2 bis 6te Ziffer
    #print Temp2
    
    
    
    
    cursor.execute("SELECT Feuchtigkeit FROM wetter ORDER BY UnixTime DESC Limit 1")
    result = cursor.fetchall()
    db.commit()
    Feuchtigkeit = result
    Feuchtigkeit1 = str(Feuchtigkeit)
    Feuchtigkeit2 = Feuchtigkeit1[2:6]
    #print Feuchtigkeit2 
    
    
    
    cursor.execute("SELECT Druck FROM wetter ORDER BY UnixTime DESC Limit 1")
    result = cursor.fetchall()
    Druck = result
    db.commit()
    
    Druck1 = str(Druck)
    Druck2 = Druck1[2:6]
    #print Druck2
    db.close()
    return Temp2, Feuchtigkeit2, Druck2
        
    

        
while True:
    try:
        Temp, Feucht, Druck = MySQL_read()
        Lcd_anzeigen("Temperatur", Temp)
        time.sleep(10)
        Lcd_anzeigen("Feuchtigkeit", Feucht)
        time.sleep(10)
        Lcd_anzeigen("Luftdruck", Druck)
        time.sleep(10)
    except ValueError:
        print "oops Ein Fehler ist passiert irgendwo zwischen auslesen und Anzeigen"

