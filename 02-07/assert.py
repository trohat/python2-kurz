cislo = 5 * 6

cislo += 10

cislo *= 2

assert cislo == 80

try: 
    assert cislo == 70
except AssertionError:
    print("Číslo není stejné jako 70")

print("Vše v pořádku")

try:
    assert cislo <= 3 and cislo >=1
except:
    print("Zadal jsi špatné číslo")


