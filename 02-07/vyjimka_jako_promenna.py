seznam = [1,5,6,8,1,2,3,9,4,5,6]

try:
    print(seznam[50])

except IndexError as promenna:
    print(f"Vznikla chyba, popis chyby zde: {promenna}")
