class Avtomobil:
    def __init__(self, boja, marka, mocnost, gorivo):
        self.boja = boja
        self.marka = marka
        self.mocnost = mocnost
        self.gorivo = gorivo
        self.potroshuvachka = 20
        self.max_gorivo=100
    def vozi(self):
        if self.gorivo >= self.potroshuvachka:
            self.gorivo -= self.potroshuvachka
            print("sme pominale 2 kilometri")

    def nadopolni_gorivo(self, kolichina):
        if self.gorivo+kolichina > self.max_gorivo:
            print("nemate dovolno mesto za taja kolicina na gorivo")
        else:
            self.gorivo += kolichina

    def proveri_gorivo(self):
        print(f"Preostanato gorivo: {self.gorivo}.")

moj_avtomobil = Avtomobil("Crvena", "Audi", 250, 10)