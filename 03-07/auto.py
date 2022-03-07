class Motor:
    def __init__(self, type, hp):
        self.typ = type
        self.vykon = hp

    # podobné jako metoda __str__
    def __repr__(self):
        return f"Motor typu {self.typ} o výkonu {self.vykon}."


m1 = Motor("hybrid", 250)

print(m1)

class Auto:
    def __init__(self, model, motor):
        """
        motor musí být instance třídy Motor (toto je pouze poznámka pro programátora,
        Python to nijak nevynucuje)
        """
        self.model = model
        self.motor = motor
        self.ujeto = 0
        print("právě bylo vytvořeno nové auto")

    def __repr__(self):
        return f"Auto značky {self.model} s motorem {self.motor}."

a1 = Auto("Volkswagen", m1)

print(a1)

a2 = Auto("Škoda", Motor("benzín", 400))

print(a2)

a2.motor.typ = "elektro"

print(a2)

m1.typ = "plyn"
a1.motor.typ = "nový plyn"

# tohle bylo skládání objektů, nebo též kompozice 
# často je to lepší, než dědičnost (tu budeme brát někdy příště)