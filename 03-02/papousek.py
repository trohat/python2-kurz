class Papousek:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva

    def __str__(self):
        return self.jmeno

ara = Papousek("Pepík", "červená")
jumbo = Papousek("Honzík", "zelená")
boris = Papousek("Boris", "červená")
richard = Papousek("Ríša", "žlutá")

class Klec:
    def __init__(self):
        self.papousci = []

    def pridej_papouska(self, papousek: Papousek):
        """
        Přidá papouška do klece.
        """
        self.papousci.append(papousek)

    def __str__(self):
        if len(self.papousci) == 0:
            return "Jsem prázdná klec."
        obsah = ""
        for papousek in self.papousci:
            obsah += str(papousek) + ", "
        obsah = obsah[:-2]
        return f"Jsem klec na papoušky a uvnitř je {obsah}."

klec1 = Klec()

#klec1.papousci.append(boris)
klec1.pridej_papouska(boris)
#klec1.papousci.append(richard)
klec1.pridej_papouska(richard)

print(klec1)