seznam = [ 5, 8, 14, 22, 21, 3, 8, 96]

#seznam_stringu = 

#for cislo in seznam:
#    seznam_stringu.append(str(cislo))

novy_seznam = ", ".join([
    str(cislo)
    for cislo in seznam
])

print(novy_seznam)

retezec = "10 abc 20 de44 30 55fg 40"

def secti_cisla(ret):
    #soucet = 0
    #for neco in ret.split():
    #    if neco.isdigit():
    #        soucet += int(neco)
    return sum([
        int(neco)
        for neco in ret.split()
        if neco.isdigit()
    ])

print(secti_cisla(retezec))

cislo = 5

def funkce(data, data2, data3):
    #data = "to co přišlo v závorce při volání funkce"
    data2 = "to druhé v závorce"
    data3 = "to třetí v závorce"
    print("Ahoj")
    print("slon")
    print(data+4)

funkce(cislo, 5, 7)

funkce(3, 10, 12)

seznam = [ 2, 7, 25, 9, 10]

slovnik = {
    cislo : cislo ** 2
    for cislo in seznam
}

print(slovnik)

slovnik2 = {
    "jablko" : "apple",
    "dveře" : "door",
    "stůl" : "table",
    "slon" : "elephant"
}

def otoc_slovnik(slv):
    return {
        hodnota : klic
        for klic, hodnota in slv.items()
    }


slozity_seznam = [[1,2], [3,4,5,6]]

novy_seznam = []

for jednoduchy_seznam in slozity_seznam:
    for cislo in jednoduchy_seznam:
        novy_seznam.append(cislo)

print(novy_seznam)  

def plochy_seznam(szn):
    return [
        cislo
        for jednoduchy_seznam in szn
        for cislo in jednoduchy_seznam
    ]

print("Plochý seznam pomocí funkce")
print(plochy_seznam(slozity_seznam))