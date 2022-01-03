
def pozdrav(jmeno):
    print("")
    print("Ahoj", jmeno)
    print(jmeno + ", odlož si, šatník je vlevo.")
    print("Pokračuj dál, v hale je občerstvení.")

def scitej(a, b):
    print("Sčítám čísla", a, "a", b)
    soucet = a + b
    return "Součet je " + str(soucet)

prvni_vysledek = scitej(56, 3)
print(scitej(5, 3))
print(scitej(5, 8))
