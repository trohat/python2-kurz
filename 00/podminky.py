vek = int(input("Kolik ti je let?"))

napoj = input("Co rád piješ?")

penezenka = 10

if vek >= 18:
    print("Skvělé, pojď dovnitř!")
    print("Vítáme tě tu")
    if not napoj == "pivo":
        print("Ty nepijes pivo? Fakt???")
    if napoj == "pivo":
        print("Máme tu tři druhy piva")
        print("Kozel, Radegast a Plzeň")
        pivo = input("Které pivo si dáš??")
        if pivo == "Kozel":
            print("Pochuntej si na Kozlovi")
            penezenka = penezenka - 5
        elif pivo == "Radegast":
            penezenka = penezenka - 6
        elif pivo == "Plzeň":
            penezenka = penezenka - 8
    else:
        print("Co jiného si dáš? Víno, rum?")
        print("Máme tu doutníky...")
elif vek >= 15:
    print("Pojď dovnitř, máme tu tři druhy limonády!")
elif vek >= 10:
    print("Pojď dovnitř, máme tu skvělý ovocný džus!")
else: 
    print("Bohužel tu pro tebe nic nemáme")


if ((vek >= 20) and (vek <= 25)) or ((vek >=40) and (vek <= 45)):
    print("Máme pro tebe speciální nabídku")


if vek >= 60 or vek <= 10:
    print("Máme tu něco pro děti a starší lidi")

print("konec programu")

