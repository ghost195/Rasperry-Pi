from datetime import datetime
from time import sleep
import random

log = open("log.txt", "w")
i = 0
while i in range(5):
    now = str(datetime.now())
    data = random.randint(0, 1024)
    log.write(now + " " + str(data) + "\n")
    print(".")
log.flush()
log.close()
