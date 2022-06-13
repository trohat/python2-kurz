# FIRST CLASS CITIZEN

def pozdrav(jmeno):
    print(f"Ahoj {jmeno}, jak se máš?")

hroch = pozdrav

hroch()

def pozdrav_slusne(prijmeni):
    print(f"Dobrý den pane/paní {prijmeni}, jak se máte?")

def funkce_co_zdravi(f, jmeno):
    return f(jmeno)

def pocasi(kod):
    def slunecno():
        print("Dnes je sluníčko")

    def destivo():
        print("Dnes prší")

    print("skončila funkce počasí")

    if kod == 1:
        return slunecno
    else:
        return destivo

predpoved = pocasi(1)

predpoved()

