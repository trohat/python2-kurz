"""
hele komentář
ještě jeden komentář
další komentář
"""

retezec = r"ahoj dnes jdu jíst seno jak se máš"

# escape sekvence

# \n = nový řádek
# \t = tabulátor

# s R na začátku - raw string - escape sekvence ztrácí význam
print(retezec)

jiny_retezec = """hurá trojité uvozovky"""
jeste_jiny_retezec = '''řádek
další řádek
ještě další řádek
'''

print(jeste_jiny_retezec)

vek = 25
jmeno = "Petr"
print(f"Moje jméno je {jmeno} a je mi {vek * 3}. To jsem mladej, co? :)")

retezec = "ahoj dnes jdu jíst"

seznam = [2, 5, 9, 8]

print(retezec[2])

#STRINGY JSOU IMMUTABLE, TEDY NEMĚNNÉ