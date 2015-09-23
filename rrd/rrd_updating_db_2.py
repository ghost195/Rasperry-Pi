import rrdtool
import os
import time

i = 1

while i < 50:
    # Daten in rrd Datenbank eintragen, N steht fuer Now also jetzt aktueller Timestamp
    rrdtool.update('temperatures.rrd', 'N:'+`i`)
    print(i)
    i = i + 0.5
    time.sleep(30)
                   
