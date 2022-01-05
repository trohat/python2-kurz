"""
def pozdrav(jmeno : str, jmeno2 : int):
    if type(jmeno2) != type(1):
        print("Chyba")
        return
    print("ahoj")
    print(jmeno)
    print(jmeno2)
    print("občerstvení je za rohem vlevo")

# funkci volám pomocí závorek!!!!!!!
pozdrav("abc", 1)

print("ahoj", "Pavle", "prase", sep="*", end="konec")
print()
"""

# dva typy argumentů
# positional arguments - args
# keyword arguments - kwargs


def scitej(a,b,c):
    return a + b + c

def scitej2(a,b,c):
    soucet = a + b + c  
    return soucet  

vysledek = scitej(7,8,9)

novy_vysledek = scitej(vysledek, vysledek, vysledek)
print(novy_vysledek)

def diskriminant(a, b ,c):
    d = (b ** 2) - (4 * a * c)
    return d

print(diskriminant(1, 3, 2))


def odd_numbers(start, stop):
    for i in range(start, stop):
        if i % 2 == 1:
            numbs = numbs + i
    return numbs

print(odd_numbers(5, 15))

def vytiskni(pocet, znak, smer):
    pass

vytiskni(23, "#", "horizontal")
vytiskni(23, "x", "vertical")
vytiskni(4, "b", "vertical")

print("5" * 9, "4" * 3, sep="", end="\n")

