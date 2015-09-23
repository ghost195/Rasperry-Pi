# Eine Datei als Befehlszeilenparamete öffnen und einlesen
import sys

if(len(sys.argv)!=2):
    print("Usage: python Datei_einlesen.py filename")
    sys.exit()

scriptname = sys.argv[0]
filename = sys.argv[1]

file = open(filename, "r")
lines = file.readlines()
file.close()

for line in lines:
    print(line)
