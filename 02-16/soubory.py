import os

os.getcwd() # current working directory 

os.curdir # opět current directory, ale teď relativně
# aktuální adresář = "."
os.pardir # parent directory
# rodičovský adresář ".."

soubor = open("novy.txt")
# módy pro otevírání souborů:
# r - read (není nutné psát, je to výchozí chování)
# w - write
# a - append


obsah_souboru = soubor.read()
obsah_souboru_jako_list = soubor.readlines()

print(obsah_souboru_jako_list)

soubor.close()

soubor2 = open("novy7.txt", "w")

soubor2.write("ahoj\n")
soubor2.write("dobry den\n")
soubor2.write("jak se mate\n")

soubor_pro_cteni = open("novy7.txt", "r")
print(soubor_pro_cteni.read())
soubor_pro_cteni.close()

soubor2.close()

soubor3 = open("novy7.txt", "a")

soubor3.write("Tohle je ctvrty radek souboru")
soubor3.close()










