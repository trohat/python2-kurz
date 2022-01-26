srazky_celkem = {}

while True:
    mesto = input("Zadej mesto: ")
    if mesto == "":
        break

    nove_zadane_srazky = int(input("Zadej kolik napršelo: "))

    puvodni_srazky = srazky_celkem.get(mesto, 0)

    srazky_celkem[mesto] = puvodni_srazky + nove_zadane_srazky

#tisknu až tady
for mesto, srazek in srazky_celkem.items():
    print(f"{mesto} : {srazek}")

