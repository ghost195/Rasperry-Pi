#!/usr/bin/env python

import subprocess

command = "cd /home/pi/lol_dht22/"  # the shell command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
output = process.communicate()

print output[0]


command = "sudo ./loldht 7"  # the shell command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
output = process.communicate()
print output[0]
