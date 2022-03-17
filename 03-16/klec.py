class Papousek:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva

    def __str__(self):
        return f"Jmenuju se {self.jmeno}!"


class Klec():
    def __init__(self):
        self.papousci = []

    def pridej_papouska(self, *args, **kwargs):
        print(args)
        print("Na dalším řádku jsou kwargs, tedy keyword arguments")
        print(kwargs)
        for papousek in args:
            self.papousci.append(papousek)

    def __str__(self):
        return f"Jsem klec a jsou ve mě tito papoušci: {', '.join(self.papousci)}."


kl1 = Klec()

kl1.pridej_papouska()

kl1.pridej_papouska("ara", jmeno="Boris", vek=5, barva="zlatá")

kl1.pridej_papouska("ara2", "ara3", "ara4")

kl1.pridej_papouska("afa", "afa2", "afa3", "afa4")

#positional arguments = args
#keyword arguments = kwargs

print(kl1)