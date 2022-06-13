import itertools

for cislo in itertools.count(50, 5):
    if cislo > 100:
        break
    print(cislo)
