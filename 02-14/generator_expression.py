# udělej druhé mocniny čísel v seznamu a pak jejich součet

seznam = [ 1,2,3,4,5,6]

def suma(seznam):
    return sum(
        cislo ** 2
        for cislo in seznam
    )
#print(f"Vytvořený objekt je {druhe_mocniny}")

# vedle list comprehension máme ještě 
# generator expression 
# jsou dobré v tom, že šetří paměť

print(f"Suma je {suma(seznam)}")
