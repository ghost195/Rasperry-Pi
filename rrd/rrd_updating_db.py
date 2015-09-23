import sys
import time
import random
import rrdtool
 
total_input_traffic = 0
total_output_traffic = 0
print("klklkl") 
while 1:
    total_input_traffic += random.randrange(1000, 1500)
    total_output_traffic += random.randrange(1000, 3000)
    ret = rrdtool.update('net.rrd','N:' + `total_input_traffic` + ':' + `total_output_traffic`);
    if ret:
        print rrdtool.error()
        print("Hallo")
        time.sleep(10)
