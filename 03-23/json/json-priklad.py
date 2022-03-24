import json

data = {
    "jmeno": "Petr",
    "vek": 23,
    "cislo": 25.0,
    "sporty": ["fotbal", "basketbal", "hokej"],
    "pije pivo": True,
    "znamky": (1,1,2,3,5),
    "domaci zvire": {
        "jmeno": "Rex",
        "rasa": "labrador",
        "povolani": "hlidac"
    }
}

with open("data.json", "w") as infile:
    json.dump(data, infile, indent=4)

retezec = json.dumps(data, indent=4)

print(retezec)