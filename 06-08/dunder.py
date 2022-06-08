class Hroch:
    def __init__(self, jmeno, delka_ocasu):
        self.jmeno = jmeno
        self.delka_ocasu = delka_ocasu

    def __len__(self):
        return self.delka_ocasu

    def __add__(self, other):
        return "Právě se někdo pokusil sčítat hrochy."

    def __mul__(self, other):
        self.delka_ocasu += 5
        other.delka_ocasu -= 10
        return self.delka_ocasu * other.delka_ocasu

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.jmeno):
            raise StopIteration
        return self.jmeno[self.index]

    def __str__(self):
        return f"Jsem {self.jmeno} a mám {self.delka_ocasu}cm dlouhý ocas."

adam = Hroch("Adam", 20)
borek = Hroch("Bořek", 15)

print(adam)
print(borek)

print(len(adam))

print(adam + borek)

vysledek = adam * borek

print(adam)
print(borek)
print(vysledek)

for x in adam:
    print(x)
