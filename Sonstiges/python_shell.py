import os

command = " "                           
while (command != "exit"):              #Solange bis exit eingetippt wird
    command = raw_input("Kommando: ")   #Eingabe der Tastatur, ein Befehl eingeben
    handle = os.popen(command)          #Kommando an system uebergeben und Ergebniss in handle schreieben
    line = " "
    while line:                         #Solange Zeileneinlesen bis keine mehr vorhanden
        line = handle.read()        
        print line
    handle.close()

print "Ciao, that's it!"
