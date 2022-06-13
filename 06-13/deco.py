import functools

def muj_dekorator(fce):
    @functools.wraps(fce)
    def wrapper(*args, **kwargs):
        print("Tohle se stane před funkcí - obal")
        vysledek = fce(*args, **kwargs)
        print("Tohle se stane po funkci - obal")
        return vysledek
    return wrapper

@muj_dekorator
def pozdrav(jmeno, prijmeni, vek):
    """tohle je funkce, která umí pozdravit"""
    print(f"ahoj {jmeno} {prijmeni}, jak se máš, dnes ti je {vek} let")
    return 42

#pozdrav = muj_dekorator(pozdrav)

cislo = pozdrav("Honza", "Novotny", vek=29)

print(cislo)
print()
print()
print()

def udelej_dvakrat(fce):
    @functools.wraps(fce)
    def dvakrat_wrapper(*args, **kwargs):
        fce(*args, **kwargs)
        vysledek = fce(*args, **kwargs)
        return vysledek
    return dvakrat_wrapper

@udelej_dvakrat
def stekej():
    print("haf haf haf haf")
    print("konec štěkání")
    print()


stekej()

"""
příklady na dekorátory, co jsme už brali:
@login_required

@staticmethod
@classmethod
"""