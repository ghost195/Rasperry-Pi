from random import randint
import rrdtool
import time

fname = 'zufall.rrd'
gfnamezz_3H = '/var/www/wetterchards/zufall3h.png'
gfnamezz_6H = '/var/www/wetterchards/zufall6.png'


def get_random():
    value = randint(0,250)
    return value



def graph_erzeugen_3h_zz():
    rrdtool.graph(gfnamezz_3H ,
                  '--start' , '-10800' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'O2' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'O2' ,
                  '--alt-autoscale' , 
                  '--alt-y-grid' , 
                  '--units-exponent' , '0' ,
                  'DEF:zufall=%s:zufall:MAX' % fname ,
                  'LINE1:zufall#FF0000:o2 MAX')
    
    
def graph_erzeugen_6h_zz():
    rrdtool.graph(gfnamezz_6H ,
                  '--start' , '-86000' ,
                  '--end' , 'now' ,
                  '-w 1280' , '-h 720' ,
                  '--slope-mode',              
                  '--vertical-label' , 'O2' ,
                  '--imgformat' , 'PNG' ,
                  '--title' , 'O2' ,
                  '--alt-autoscale' , 
                  '--alt-y-grid' , 
                  '--units-exponent' , '0' ,
                  'DEF:zufall=%s:zufall:MAX' % fname ,
                  'LINE1:zufall#FF0000:o2 MAX')    




while True:
    
    
    zufall = get_random()
    print  zufall
    time.sleep(20)
    rrdtool.update('zufall.rrd','N:'+`zufall`)
    time.sleep(3)
    graph_erzeugen_3h_zz()
    time.sleep(25)
    graph_erzeugen_6h_zz()

    
    
    