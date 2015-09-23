import Adafruit_BMP.BMP085 as BMP085
import time
import read_mcp3008
import spidev


#=============================LDR2=================================
spi = spidev.SpiDev()
spi.open(0,0)


#=============================BMP085=================================
sensor = BMP085.BMP085()

#=============================DHT22==================================
import dhtreader
type = 22
pin = 22
dhtreader.init()

def get_Pressur():
    print "====================Druck============================="
    print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
    print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())
    print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
    print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())
    
    
    
    
def get_Temp():
    print "====================DHT22============================="
    data = dhtreader.read(type, pin)
    if data != None:           
        feuchtigkeit = data[1]
        feuchtigkeit1 = round(feuchtigkeit, 3)
        Temperatur = data[0]
        Temperatur1 = round(Temperatur, 3)
        print(feuchtigkeit1)
        print(Temperatur1)
        print(data)
        


def get_LDR():
    print "====================LDR============================="
    zaehler = 1
   
    while zaehler < 15:
        print read_mcp3008.readAnalogData(0, 11, 10, 9, 8)
        zaehler = zaehler +1



def get_LDR2():
    print "====================LDR2============================="
    zaehler = 1
    while zaehler < 15:  
        print read_mcp3008.readAnalogData(2, 11, 10, 9, 8)
        zaehler = zaehler +1
        



def get_O2():
    # use chip select CE0, channel 0
    print "=====================O2============================="
    zaehler = 1
    while zaehler < 15:
        print read_mcp3008.readAnalogData(1, 11, 10, 9, 8)
        zaehler = zaehler +1
       
                
                
                


get_Pressur()
time.sleep(2)
get_Temp()
time.sleep(2)
get_LDR()
time.sleep(2)
get_LDR2()
time.sleep(2)
get_O2()
