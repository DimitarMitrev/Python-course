class Vozilo:
    def __init__(self, trkala, vrati, gorivo, potrosuvacka):
        self.trkala = trkala
        self.vrati = vrati
        self.gorivo = gorivo
        self.potrosuvacka = potrosuvacka

    def vozi(self):
        print("voziloto pomina 1km")
        self.gorivo -= self.potrosuvacka


class Avtomobil(Vozilo):
    def __init__(self, trkala, vrati, gorivo, potrosuvacka, marka):
        super().__init__(trkala, vrati, gorivo, potrosuvacka)
        self.marka = marka

    def marka(self):
        print(self.marka)


# vozilo = Vozilo(4,4,100,20)
# vozilo.vozi()

moj_avtomobil = Avtomobil(4, 2, 100, 20, "bmw")
moj_avtomobil.vozi()
print(moj_avtomobil.gorivo)