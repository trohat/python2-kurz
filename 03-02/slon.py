class Slon:
    def __init__(self, jmeno, barva, vaha):
        self.jmeno = jmeno
        self.barva = barva
        self._vaha = vaha
        if self._vaha < 15:
            self.leta = True
        else:
            self.leta = False

    def zatrub(self):
        print("Tůůůů tůůůů tůůůů tůůů!!!!")

    def strikej_na_lidi(self):
        if self.barva == "růžový":
            print("Já jsem růžový, stříkat nebudu.")
        else:
            print("Všichni kolem jsou mokří od hlavy až k patě.")
        #po tom co někoho postříká, tak vždycky radostí zatroubí
        self.zatrub()

    def set_vaha(self, nova_vaha):
        self._vaha = nova_vaha
        if self._vaha < 15:
            self.leta = True
        else:
            self.leta = False

    def __str__(self):
        #print("Informace pro tebe: Zavolala se metoda __str__.")
        return f"Já jsem {self.barva} slon jménem {self.jmeno}."


jumbo = Slon("Jumbo", "růžový", 20)

dumbo = Slon("Dumbo", "fialový", 11)

print("Informace o slonovi:\n", jumbo)
print("Informace o dalším slonovi:\n", dumbo)

dumbo.strikej_na_lidi()
jumbo.strikej_na_lidi()

print(dumbo._vaha)
print(dumbo.leta)

print(jumbo._vaha)
print(jumbo.leta)

# dumbo.vaha = 23     --- domluvíme se, že tohle nebude povoleno
#řeklo by se, že to bude PRIVÁTNÍ atribut
# podtržítko na začátku - jen domluva, nic jsme tím DOOPRAVDY nezakázali
# ale znamená to, že bychom tu jméno proměnné (atributu) neměli používat
# proto používáme raději setter (metoda, jejíž jméno začíná na SET) 
# setter nastaví novou váhu a zároveň zkontroluje vše další, co je potřeba zkontrolovat
dumbo.set_vaha(23)

print(dumbo._vaha)
print(dumbo.leta)

