import Klassenbeispiel as classbsp

kontoSchwarz=classbsp.Konto("Schwarz",["Schwarz","Bankangestellter","Papa"],10)
print kontoSchwarz.einzahlen(1499.00)
print kontoSchwarz.auszahlen(1000, "Freundin")
print kontoSchwarz.abfrage()
print kontoSchwarz.auszahlen(1600, "Papa")
print kontoSchwarz.auszahlen(900, "Schwarz")

print "Anzahl der Konten  :",classbsp.Konto.angelegteKonten

kontoWeiss=classbsp.Konto("Weiss")

print "Anzahl der Konten  :",classbsp.Konto.angelegteKonten

print "Kontostand von Schwarz :",kontoSchwarz.abfrage()
print "Kontostand von Weiss :",kontoWeiss.abfrage()

del(kontoWeiss)

print "Anzahl der Konten  :",classbsp.Konto.angelegteKonten
