class Konto:
        angelegteKonten=0

        def __init__(self,inhaber,autorisiert=["Bankangestellter"],startkap=0):
                self.__inhaber=inhaber
                self.__autorisiert=autorisiert
                self.__kontostand=startkap
                Konto.angelegteKonten+=1

        def __del__(self):
                Konto.angelegteKonten-=1

        def einzahlen(self,betrag):
                if (type(betrag)==float or type(betrag)==int or type(betrag)==long) and betrag>0:
                        self.__kontostand +=betrag
                        print "Neuer Kontostand:    ",self.__kontostand
                else:
                        print "FEHLER: Falsche Betragsangabe"
                return self.__kontostand

        def auszahlen(self,betrag,initiator):
                if not initiator in self.__autorisiert:
                        print initiator+" ist nicht berechtigt"
                elif self.__kontostand < betrag:
                        print "Es befinden sich nur noch %10.2f Euro auf dem Konto" % self.__kontostand
                else:
                        self.__kontostand -=betrag
                return self.__kontostand

        def abfrage(self):
                return self.__kontostand
