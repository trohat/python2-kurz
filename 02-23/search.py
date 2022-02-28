seznam = [ 6, 8 , 9, 13]

#je osmička v seznamu???

#find, index, in - funguje, ale pojďme si to teď zakázat používat

hledana_promenna = 8

for index, cislo in enumerate(seznam):
    if cislo == hledana_promenna:
        print("Hurá, nalezeno na indexu {index}, můžeme skončit")
        break
    print("Smutné, není tu")


# časová složitost???? 2 * n => n = lineární
# proto se tomu říká lineární vyhledávání

# binární vyhledávání - logaritmická složitost
