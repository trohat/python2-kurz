with open("abc.txt", "r") as soubor_na_cteni:
    obsah_souboru = soubor_na_cteni.readlines()

obsah_souboru.reverse()

with open("sem_to_zapis.txt", "w") as soubor_na_zapis:
    soubor_na_zapis.writelines(obsah_souboru)

with open("sem_to_zapis.txt") as soubor_pro_vypis_do_terminalu:
    print("Vypisuji výsledek:")

    print(soubor_pro_vypis_do_terminalu.read())