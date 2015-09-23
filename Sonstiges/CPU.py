import os

def getCPUtemp():
    res = os.popen('vcgencmd measure_temp').readline()
    print res

getCPUtemp()
