import dhtreader
import time

type = 22
pin = 4

data1 = 12.454554545454
data2 = round(data1,0)
data3 = "%.4f" % data1

dhtreader.init()

i = 1


while i < 20:
    
   
    data = dhtreader.read(type, pin)
    if data != None:           
        #feuchtigkeit = data[1]
        #Temperatur = data[0]
        i = i+1
        #print(feuchtigkeit)
        #print(Temperatur)
        print(data)
        time.sleep(2)
    
    


