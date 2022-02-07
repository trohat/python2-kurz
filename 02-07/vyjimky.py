try:
    delenec = int(input("Zadej první číslo:"))
    delitel = int(input("Zadej druhé číslo:"))
    vysledek = delenec / delitel
    print(f"Výsledek je {vysledek}")    

# tato část se vykoná pouze když program vyhodí výjimku (tj. vznikne chyba)
# což je ale super, protože jinak by celý program spadnul
except ZeroDivisionError:
    print("Nelze dělit nulou")

except ValueError:
    print("Nelze převést na číslo")

except:
    print("Vznikla neznámá chyba")

print("Program úspěšně skončil")

# výjimka = Exception

