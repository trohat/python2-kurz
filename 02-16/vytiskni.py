with open("novy.txt", "r") as soubor:
    for radek in soubor:
        radek = radek.strip("\n")
        if radek.endswith("radek"):
            print(radek, end="")

# with = context manager, který se postará o zavření souboru



