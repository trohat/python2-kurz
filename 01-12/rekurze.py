def pozdrav():
    print("mám tě rád")
    print("všichni tě mají rádi")
    pozdrav()

#pozdrav()

def faktorial(cislo):
    if cislo <= 1:
        return 1
    return cislo * faktorial(cislo - 1)

print(faktorial(6))