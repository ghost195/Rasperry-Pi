#!/usr/bin/python
import dhtreader

type = 22
pin = 4

dhtreader.init()


def getTemp():
   


    data = dhtreader.read(type, pin)
    if data != None:           
        feuchtigkeit = data[1]
        feuchtigkeit1 = round(feuchtigkeit, 3)
        Temperatur = data[0]
        Temperatur1 = round(Temperatur, 3)
        print(feuchtigkeit1)
        print(Temperatur1)
        print(data)
        


getTemp()
