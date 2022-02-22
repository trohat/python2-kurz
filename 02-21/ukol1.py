with open("abc.txt", "r") as soubor_na_cteni, open("sem_to_zapis.txt", "w") as soubor_na_zapis:

    for line in soubor_na_cteni:
        soubor_na_zapis.write(line)


with open("sem_to_zapis.txt") as soubor_pro_vypis_do_terminalu:
    print("Vypisuji výsledek:")

    print(soubor_pro_vypis_do_terminalu.read())

# with = context management