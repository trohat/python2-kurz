class Zoo:
    def __init__(self):
        self.klece_v_zoo = []

    def pridej_klec_do_zoo(self, klec):
        self.klece_v_zoo.append(klec)

    def zvire_podle_barvy(self, barva):
        neexistuje = True
        for klec in self.klece_v_zoo:
            for zvire in klec.zvirata:
                if zvire.barva == barva:
                    print(zvire)
                    neexistuje = False
        if neexistuje:
            print("Není takové zvíře")

    

