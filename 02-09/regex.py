# REGULÁRNÍ VÝRAZY
# REGEX = REGULÁRNÍ VÝRAZ

import re

retezec = "Slon je šedivý, má chobot a kly. Jeho telefon je 777-123456. Žije v Africe."

#print(retezec.find("chobot"))
# \d = jakákoliv číslice
# r = raw string

regex = re.compile(r"(\d{3})-(\d{6})")

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
\w - číslice, písmeno nebo podtržítko (word character)
\s - bílý znak (mezera, tabulátor nebo nový řádek)
\b - hranice slova
^ - začátek řetězce
$ - konec řetězce
() - skupina
{4} - kolikrát je ten znak předtím
[abc] - výčet (tj. cokoliv ze znaků v závorkách)
[^abc] - negovaný výčet (tj. cokoliv kromě znaků v závorkách)
"""

regex5 = re.compile("chobot")

vysledek5 = regex5.search("Veverka má zrzavý ocas.")

#print(vysledek5.group())

reg = re.compile(r"\d{3}-\d{3}-\d{3}\b")

text = """RegExr was created by; gskinner.com, and is prou7dly hosted by Media Temple.

123-234-232    +420 234-232-222"""

vysl = reg.findall(text)

print(vysl)


