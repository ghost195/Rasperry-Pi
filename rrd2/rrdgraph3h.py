import rrdtool
import os
import time
import sys

fname = 'temperatures_all.rrd'

gfnameF_3H = '/var/www/wetterchards/feucht_3H.png'




x = 720
y = 500 





ret = rrdtool.graph("fffffeuch.png", "--end", "now", "--start", "-10800", "--width", "400", "DEF:feucht=temperatures_all.rrd:feucht:MAX", "LINE1:feucht#0000FF:feucht 1 MAX")


f = open('/home/pi/Programmierung/cron.txt','a')
f.write('graph\n')
f.close()






