import subprocess
import smtplib
import socket
import datetime
import sys
from email.mime.text import MIMEText

# Accountinformationen zum Senden der E-Mail
Empfaenger = 'Phil198@hotmail.de'
Absender = 'raspi198@gmx.de'
Passwort = 'Rasp&E&198'
smtpserver = smtplib.SMTP('mail.gmx.net', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo

# In Account einloggen
smtpserver.login(Absender, Passwort)

# Aktuelles Datum holen
Datum = datetime.date.today()

# Text



#Wert = str(sys.argv[1])  #Das kann man gebrauchen um dem Skript eine Variable mit zu übergeben 
#Wert += " "
#Wert += str(sys.argv[2])

Wert = str("Mein Inhalt")
msg = MIMEText(Wert)

# Betreff + Datum
msg['Subject'] = 'Nachricht vom Raspberry Pi - %s' % Datum.strftime('%b %d %Y')

# Absender
msg['From'] = Absender

#Empfaenger
msg['To'] = Empfaenger

# E-Mail abschicken
smtpserver.sendmail(Absender, [Empfaenger], msg.as_string())
smtpserver.quit()