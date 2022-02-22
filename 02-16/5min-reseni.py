osoba = {
    "jméno": "Pavel",
    "věk": 29,
    "sport": ["fotbal", "basketbal", "hokej"],
    "muž": True,
    "pije-pivo": False
}

osoba["výška"] = 176

for klic in osoba.keys():
    print(klic)

for hodnota in osoba.values():
    print(hodnota)

for klic, hodnota in osoba.items():
    print(f"{klic}---{hodnota}")

for dvojice in osoba.items():
    print(dvojice[0])  