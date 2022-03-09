class Papousek:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva

    def __str__(self):
        return f"Jmenuju se {self.jmeno}!"


class Klec():
    velikost = 3

    def __init__(self):
        self.papousci = []

    def pridej_papouska(self, papousek):
        if (len(self.papousci) < self.__class__.velikost):
            self.papousci.append(papousek)
            print(f"Přidán papoušek {papousek}")
        else:
            print(f"Papouška {papousek} nelze přidat, je plno.")

    def __str__(self):
        return f"Jsem klec a jsou ve mě {len(self.papousci)} papoušci."


class VelkaKlec(Klec):
    velikost = 5

boris = Papousek("Boris", "zelený")
rick = Papousek("Rick", "fialový")
richie = Papousek("Richard", "fialový")
amber = Papousek("Amber", "červená")
jumbo = Papousek("Jumbo", "strakatý")
dumbo = Papousek("Dumbo", "zelenobílý")

moje_klec = Klec()

moje_velka_klec = VelkaKlec()

moje_velka_klec.pridej_papouska(boris)
moje_velka_klec.pridej_papouska(rick)
moje_velka_klec.pridej_papouska(richie)
moje_velka_klec.pridej_papouska(amber)
moje_velka_klec.pridej_papouska(jumbo)
moje_velka_klec.pridej_papouska(dumbo)

print(moje_velka_klec)