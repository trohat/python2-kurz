seznam = [ 2, 4, 5, 6, 7, 8, 10, 11]

"""
novy_seznam = []
for cislo in seznam:
    novy_seznam.append(cislo + 1)

print(novy_seznam)
"""

# LIST COMPREHENSIONS
novy_seznam = sum([ 
            cislo + 1 
            for cislo in seznam 
            ])

            

print(novy_seznam)

zvetseny_o_pet = []
for cislo in seznam:
    zvetseny_o_pet.append(cislo + 5)

print(zvetseny_o_pet)

zvetseny_o_pet_pomoc_comprehension = [ cislo + 5 for cislo in seznam ]

druhe_mocniny = []
for cislo in seznam:
    if cislo % 2 == 0:   # tohle vybere jen sudá čísla
        druhe_mocniny.append(cislo ** 2)

print(druhe_mocniny)

druhe_mocniny_pomoci_comprehension = [
    cislo ** 2
    for cislo in seznam
    if cislo % 2 == 0
]
# jmenuje se to list comprehension
print(druhe_mocniny_pomoci_comprehension)

seznam2 = ["ahoj", "ovoce", "zelenina", "brambory"]

seznam_pismen = []
for slovo in seznam2:
    for pismenko in slovo:
        seznam_pismen.append(pismenko)

print(seznam_pismen)

seznam_pismen_pomoci_comprehension = [ 
    pismeno 
    for slovo in seznam2 
    for pismeno in slovo 
    ]

print(seznam_pismen_pomoci_comprehension)

set_pismen_pomoci_comprehension = { 
    pismeno 
    for slovo in seznam2 
    for pismeno in slovo 
}
# předtím jsme měli LIST COMPREHENSION .... teď to je ale SET COMPREHENSION

print(set_pismen_pomoci_comprehension)

# též existují DICT COMPREHENSION
slovnik_pomoci_comprehension = {
    cislo : cislo ** 2
    for cislo in seznam
}
print(slovnik_pomoci_comprehension)