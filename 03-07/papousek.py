class Papousek:

    # obecně: statická proměnná (tj. patří celé třídě)
    # v Pythonu bych tomu řekl spíše třídní proměnná (class variable)
    pocet_papousku = 0

    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva
        self.__class__.pocet_papousku += 1

    def __str__(self):
        return f"Jmenuju se {self.jmeno}!"
    
    def zpivej(self):
        print("Dej mi peníze!!!")

    @staticmethod 
    def vypis_pocet_papousku_staticka_metoda():
        print(f"Už bylo vytvořeno {Papousek.pocet_papousku} papoušků. - statická metoda")

    @classmethod 
    def vypis_pocet_papousku(cls, velikost_bot):
        print(f"Už bylo vytvořeno {cls.pocet_papousku} papoušků. - třídní metoda")


Papousek.vypis_pocet_papousku(15)
Papousek.vypis_pocet_papousku_staticka_metoda()
#STATIKA

p1 = Papousek("Boris", "zelený")

print(p1.jmeno)
print(p1.barva)

p2 = Papousek("Richard", "zelený")

p3 = Papousek("Karel", "červený")

p3 = Papousek("Jára", "červený")

Papousek("Maxim", "černý")

#print(Papousek.pocet_papousku)

print(p2.__class__)
Papousek.vypis_pocet_papousku()
Papousek.vypis_pocet_papousku_staticka_metoda()