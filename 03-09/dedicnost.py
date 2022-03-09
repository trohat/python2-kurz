class Clovek:
    """
    tohle je třída pro vytváření lidí, dnes ji budu používat převážně pro dědění
    tohle je docstring, tedy dokumentační řetězec
    """

    def __init__(self, jmeno, vek):
        """init metoda, Python ji volá sám"""
        self.jmeno = jmeno
        self.vek = vek

    def pozdrav(self):
        """postavička potká jinou postavičku a pozdraví ji"""
        print("Dobrý den!")

    def spi(self):
        """postavička vydává zvuky typické při spánku"""
        print("Chrrrrr")

    def __str__(self):
        return f"Já jsem {self.jmeno}"




class Programator(Clovek):

    def __init__(self, jmeno, vek=40, jazyk="Python"):
        jmeno = "Superman " + jmeno
        super().__init__(jmeno, vek + 5)
        self.jazyk = jazyk

    def pij_kafe(self):
        print("Máme u nás ve firmě moc dobré kafe")

    def pozdrav(self):
        print("Ahoj")
        super().pozdrav()

    def spi(self):
        print("Spím a zdá se mi o objektech... OOP sny jsou super!")

    def __str__(self):
        return f"Jsem programátor {self.jmeno} a nejraději programuji v jazyku {self.jazyk}."


class Manazer(Clovek):

    def spi(self):
        print("Spím a zdá se mi, že ráno vyhodím půlku zaměstnanců.")

class Sportovec(Clovek):
    pass

pepa = Clovek("Josef", 18)
erik = Programator("Eric", 35, "JavaScript")
robert = Programator("Robert")
hugo = Manazer("Hugo", 50)
kyle = Sportovec("Kyle", 20)

seznam = [pepa, erik, robert, hugo, kyle]

for osoba in seznam:
    osoba.spi()