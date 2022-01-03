"""
sirka = input("Zadej šířku obdélníka:")
sirka = int(sirka)

vyska = int(input("Zadej výšku obdélníka:"))

obsah = sirka * vyska

print("Obsah obdélníka je", obsah)
"""

cislo = int(input("Zadej trojciferné číslo: "))

cifra1 = cislo // 100
cifra3 = cislo % 10
cifra2 = (cislo - (cifra1 * 100)) // 10

print("", 
    cifra1, 
    cifra2, 
    cifra3, 
    cifra1 + cifra2 + cifra3, 
    sep="\n\t\t")

    
