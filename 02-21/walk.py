import os

for path, dirnames, filenames in os.walk(os.curdir):
   print("Cesta je " + path)
   print("Adresáře jsou " + str(dirnames))
   print("Soubory jsou " + str(filenames))