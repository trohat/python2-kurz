# úkol: napiš funkci, která vezme jako parametr list a sečte čísla v něm

def soucet_listu_rychle(seznam):
    return sum(seznam)

def soucet_listu_pomalu(seznam):
    vysledek = 0
    for cislo in seznam:
        vysledek = vysledek + cislo
    return vysledek

print(soucet_listu_rychle([4,7,9,1]))

# vypiš počet záporných čísel v seznamu

def pocet_zapornych_cisel(seznam):
    pocet = 0
    for cislo in seznam:
        if (cislo < 0):
            pocet = pocet + 1
    return pocet

print(pocet_zapornych_cisel([-5, 7, -1, 6, 6, -1]))