pocasi = {
    "pondělí": {
        "teplota": 20,
        "slovně": "slunečno",
        "rosný bod": 5
    },
    "úterý" : {
        "teplota": 25,
        "slovně": "ještě více slunečno",
        "rosný bod": 4
    },
    "středa" : {
        "teplota": {
            "ráno": 10,
            "poledne": 17,
            "večer": 15
        },
        "slovně": "deštivo",
        "rosný bod": 2
    }
}

pocasi["pondělí"]["teplota"]
pocasi["úterý"]["rosný bod"]
pocasi["středa"]["teplota"]["poledne"] = 18

for popis, hodnota in pocasi["pondělí"].items():
    print(popis, hodnota)

for popis, hodnota in pocasi["středa"].items():
    print(popis, hodnota)
