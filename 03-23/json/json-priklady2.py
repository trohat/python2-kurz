import json

with open("data.json") as infile:
    print(json.load(infile))

retezec = '{"jmeno": "Alík", "rasa": "bernardyn"}'

slovnik = json.loads(retezec)

print(slovnik)
print(slovnik["jmeno"])