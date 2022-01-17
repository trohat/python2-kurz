

# DICTIONARY - slovník

anglictina = {
    "apple": "jablko",
    "car": "auto",
    "book": "kniha",
    "table": "stůl",
    "flower": "květina"
}

pavluv_slovnik = {
    "jmeno": "Pavel",
    "vek" : 35,
    "oblíbená barva": "žlutá",
    "výška": 180,
    "pije_rád_pivo": True,
    5: "nevím co sem napsat"
}


slovnik = {
    "klíč" : "hodnota"
}

klice = pavluv_slovnik.keys()

hodnoty = pavluv_slovnik.values()

dvojice = pavluv_slovnik.items()

for klic in pavluv_slovnik.keys():
    print(klic)

for hodnota in pavluv_slovnik.values():
    print(hodnota)

for klic, hodnota in pavluv_slovnik.items():
    print(klic, hodnota)