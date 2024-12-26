class Banka:
    def __init__(self, smetka, korisnik, balans=0):
        self.__smetka = smetka
        self.korisnik = korisnik
        self.__balans = balans
        self.__istorija=[]
        self.__kredit_podignat= False

    def uplata(self, iznos):
        self.__balans += iznos
        self.__istorija.append(f"Uplata: {iznos}")
        print(f"Uplateno {iznos} na smetkata")
        if self.__balans >0:
            self.__kredit_podignat = False

    def isplata(self, iznos):
        if iznos <= self.__balans:

            self.__balans -= iznos
            self.__istorija.append(f"Isplata: {iznos}")
            print(f"Povlekovte {iznos} od smetkata")

        else:
            print("Nema dovolno pari na smetkata za ovaa isplata")

            if not self.__kredit_podignat:
                odgovor = input("Dali sakate da podignite kredit? (y/n): ").lower()

                if odgovor == "y":
                    self.__balans -=iznos
                    self.__kredit_podignat=True
                    self.__istorija.append(f"Kredit i isplata: {iznos}")
                    print(f"Podignavte kredit i povlekovte {iznos} od smetkata")
                else:
                    print("Isplatata e otkazhana")
            else:
                print("Vekje imate podignato kredit.")
    def get_balans(self):
        return self.__balans

    def get_smetka(self):
        return self.__smetka

    def proveri_balans(self):
        print(f"Preostanati pari na smetkata: {self.__balans}")

    def istorija_transakcii(self):
        print("Istorija na transkacii:")
        for transkacija in self.__istorija:
            print(transkacija)

moja_smetka = Banka("123456", "Dimitar", 1000)
print (moja_smetka.get_smetka())
