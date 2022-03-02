


class Auto:
    def __init__(self, znacka, barva):
        self.znacka = znacka
        self.barva = barva

    def __str__(self):
        return f"{self.barva.capitalize()} {self.znacka} a jsem opravdické auto."

class Clovek:
    def __init__(self, jmeno: str, vaha: int, auto: Auto):
        self.jmeno = jmeno
        self.vaha = vaha
        self.auto = auto

    def __str__(self):
        return f"Jsem {self.jmeno} a mám {self.auto}."

punta = Auto("škodovka", "modrá")

bourak = Auto("merci", "růžový")

anicka = Clovek("Anna", 45, bourak)

pepa = Clovek("Pepík", 90, punta)

honza = Clovek("Honza", 43, Auto("trabant", "žlutý"))



print(anicka)
print(pepa)
print(honza)
print(anicka.jmeno)
print(anicka.vaha)
print(anicka.auto)
print(anicka.auto.barva)

print(honza.auto.barva)

"haoos-a"