seznam = [ 1, 7, 6, -4, -9, -3, 8, 15]

print(seznam[5])
print(len(seznam))
print(max(seznam))
print(sum(seznam))
"""
vysledek = 0

for cislo in seznam:
    if cislo > 0:
        vysledek += cislo

print(vysledek)
"""
def vyber_pouze_kladna_cisla(seznam):
    novy_seznam = []
    for cislo in seznam:
        if cislo > 0:
            novy_seznam.append(cislo)
    return novy_seznam

def vyber_pouze_suda_cisla(seznam):
    novy_seznam = []
    for cislo in seznam:
        if cislo % 2 == 0:
            novy_seznam.append(cislo)
    return novy_seznam

print(vyber_pouze_kladna_cisla(seznam))
print(vyber_pouze_suda_cisla(seznam))
print(vyber_pouze_kladna_cisla(vyber_pouze_suda_cisla(seznam)))
