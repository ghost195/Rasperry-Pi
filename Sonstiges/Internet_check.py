import os
from time import  *

def isConnectionOk(reference):
    
    lt = localtime()
    jahr, monat, tag, Stunde, Minute = lt[0:5]
    
    hostname = "google.com" #example
    response = os.system("ping -c 1 " + hostname)

#and then check the response...
    if response == 0:
        print hostname, 'is up!'
        print "Es ist der %02i.%02i.%04i." " %02i.%02i"  % (tag,monat,jahr,Stunde,Minute)  + "      interneverbindung besteht"
      
    else:
        print hostname, "Es ist der %02i.%02i.%04i." " %02i.%02i"  % (tag,monat,jahr,Stunde,Minute)  + "      interneverbindung besteht"
    
    


isConnectionOk("www.google.de")
exit()