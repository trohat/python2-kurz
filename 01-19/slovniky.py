anglictina = {
    "jablko": "apple",
    "dům": "house",
    "stůl": "table",
    "kniha": "book",
    "dveře": "door"
}

# co můžu použít jako klíč - cokoliv co je IMMUTABLE a HASHABLE
slovnik = {
    2: "dvojka",
    "s": "písmeno s",
    True: "boolean hodnota pravda",
    (1,2,3): "seznam tří čísel",
    (1,2,3,7): "tuple s vnořeným listem"
}

print(anglictina["dům"])

anglictina["stůl"] = "elephant"

anglictina["židle"] = "chair"

preklad = input("Jaké slovíčko chceš přeložit?")

print(anglictina[preklad])

print(anglictina["jab" + "lko"])

"""
if "velbloud" in anglictina:
    print(anglictina["velbloud"])
else:
    print("Není ve slovníku")
"""
print(anglictina.get("velbloud", "Není ve slovníku"))
print(anglictina.get("jablko", "Není ve slovníku"))
print(anglictina.get("dveře", "Není ve slovníku"))
print(anglictina.get("odpadkový koš", "Není ve slovníku"))
# když tam není tak vrať výchozí hodnotu

print(anglictina.setdefault("velbloud", "camel"))
# když tam není, tak ho vytvoř

print(anglictina["velbloud"])

for key, value in anglictina.items():
    print(key, value)

for dvojice in anglictina.items():
    print(dvojice)