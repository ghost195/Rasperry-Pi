#!/usr/local/bin/python
import sys
sys.path.append('/path/to/rrdtool/lib/python2.6/site-packages/')
import rrdtool, tempfile
import time, random

stime = int(time.time()) - 5 * 86400
dpoints = 1000
etime = stime + (dpoints * 300)
fname = 'wetter.rrd'
gfname = 'test.png'
gfnameL = 'Druck.png'
gfnameULH = 'Licht.png'

 
rrdtool.graph(gfname ,
              '--start' , '-10800' ,
              '--end' , 'now' ,
              '-w 785' , '-h 350' ,
              '--slope-mode',              
              '--vertical-label' , 'Temperatur' ,
              '--imgformat' , 'PNG' ,
              '--title' , 'Temperatur / Feuchtigkeit der letzten 3 Stunden' ,
              '--lower-limit' , '0' ,
              'DEF:temp0=%s:temp0:MAX' % fname ,
			  'DEF:feucht0=%s:feucht0:MAX' % fname ,
              'LINE1:temp0#FF0000:Temperatur',
			  'LINE2:feucht0#CC0099:Feuchtigkeit')


rrdtool.graph(gfnameL ,
              '--start' , '-10800' ,
              '--end' , 'now' ,
              '-w 785' , '-h 350' ,
              '--slope-mode',              
              '--vertical-label' , 'Druck' ,
              '--imgformat' , 'PNG' ,
              '--title' , 'Luftdruck der letzten 3 Stunden' ,
              '--lower-limit' , '950' ,
			  '--upper-limit' , '1100', 
			  '--alt-autoscale',
			  '--units-exponent' , '0',
			  '--y-grid' , '3:2', 
              'DEF:druck0=%s:druck0:MAX' % fname ,
              'LINE1:druck0#FF0000:Luftdruck')	


rrdtool.graph(gfnameULH ,
              '--start' , '-10800' ,
              '--end' , 'now' ,
              '-w 785' , '-h 350' ,
              '--slope-mode',              
              '--vertical-label' , 'Temperatur' ,
              '--imgformat' , 'PNG' ,
              '--title' , 'Temperatur / Feuchtigkeit der letzten 3 Stunden' ,
              '--lower-limit' , '0' ,
              'DEF:ldr0=%s:ldr0:MAX' % fname ,
			  'DEF:uv0=%s:uv0:MAX' % fname ,
              'LINE1:ldr0#FF0000:Helligkeit',
			  'LINE2:uv0#CC0099:UV')			  


	  
			  
