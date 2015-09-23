import sys
sys.path.append('/path/to/rrdtool/lib/python2.6/site-packages/')
import rrdtool, tempfile
import time, random

stime = int(time.time()) - 5 * 86400
dpoints = 1000
etime = stime + (dpoints * 300)
fname = 'wetter.rrd'
gfname = 'test.png'


 
rrdtool.graph(gfname ,
              '--start' , '-200' ,
              '--end' , 'now' ,
              '-w 785' , '-h 350' ,
              '--slope-mode',              
              '--vertical-label' , 'Temperatur' ,
              '--imgformat' , 'PNG' ,
              '--title' , 'Speeds' ,
              '--lower-limit' , '0' ,
              'DEF:temp0=%s:temp0:AVERAGE' % fname ,
              'LINE1:temp0#FF0000:temp 1')
        
