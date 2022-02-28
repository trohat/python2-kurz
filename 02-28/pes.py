#třída je pouze vzor, otisk nebo plánek
class Pes:
    #dunder metody
    def __init__(self, jmeno, povolani, vaha):
        self.jmeno = jmeno
        self.povolani = povolani
        self.vaha = vaha
        
    def stekej(self):
        print("Haf haf haf")

    def kousej(self):
        print("Chramst chramst chramst")

    def __str__(self):
        return f"Jmenuji se {self.jmeno} a jsem {self.povolani}."

alik1 = Pes("Alík", "mazlící pes", 15)

print(alik1)

alik1.stekej()

alik1.kousej()

print(alik1.jmeno)   

alik1.jmeno = "Max"

print(alik1.jmeno)

alik1.povolani = "hlídací pes"

alik7 = Pes("Rex", "malinké štěně", 5)

alik7.povolani = "záchranný pes"
alik7.vaha = 20

alik7.stekej()

print(alik1)

print(alik7)

alik23 = Pes("Peter", "musí chytit vlak", 80)

print(alik23)