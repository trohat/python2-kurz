# REGULÁRNÍ VÝRAZY
# REGEX = REGULÁRNÍ VÝRAZ

import re

retezec = "Slon je šedivý, má chobot a kly. Jeho telefon je abcabc-123456. Žije v Africe."

#print(retezec.find("chobot"))
# \d = jakákoliv číslice
# r = raw string

regex = re.compile(r"(abc)-?(\d+)")

vysledek = regex.search(retezec)
print(vysledek.groups())
print(f"Předvolba je {vysledek.group(1)}")
print(f"Samotné číslo je {vysledek.group(2)}")

print(f"Celé tel. číslo je {vysledek.group()}")
print(f"Celé tel. číslo je {vysledek.group(0)}")

ret2 = "U nás bydlí zelený páv."
# hledám slovo páv nebo právo

regex2 = re.compile(r"pr?ávo?")

vysledek = regex2.search(ret2)

print(vysledek.group())

ret3 = "Máme doma modrý plot."
# hledám slovo plot nebo plod
# svislítko znamená "nebo"
regex7 = re.compile(r"jablko|hruška")
regex3 = re.compile(r"plo(d|t)")

vysledek3 = regex3.search(ret3)
print(vysledek3.group())

"""
? - 0x - 1x znak předtím
+ - 1x - nekonečnokrát znak předtím
* - 0x - nekonečnokrát znak předtím
| - nebo
\d - číslice
\w - číslice, písmeno nebo podtržítko
\s - bílý znak (mezera, tabulátor nebo nový řádek)
\b - hranice slova
^ - začátek řetězce
$ - konec řetězce
() - skupina
{} - kolikrát je ten znak předtím
[] - výčet (tj. cokoliv ze znaků v závorkách)
[^] - výčet, ale negace (tj. cokoliv kromě znaků v závorkách)
"""


