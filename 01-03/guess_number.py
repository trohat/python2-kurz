import random

cislo = random.randint(1,50)

#pokusu = 0
while True:
    tip = int(input("Hádej jaké si myslím číslo: "))
    #pokusu = pokusu + 1
    if tip == 0:
        print("Cislo je", cislo)
        print("Konec programu")
        break
    elif tip == cislo:
        print("Uhodl jsi!!")
        #print("Počet pokusů je", pokusu)
        break
    elif tip < cislo:
        print("Hledané číslo je větší")
    elif tip > cislo:
        print("Hledané číslo je menší")
    else:
        print("Chyba programu")



