
class Stan():

    def __init__(self):
        self.stan = []

    def dodaj_do_stanu(self, nr_kat):
        if not self.spr_czy_na_stanie(nr_kat):
            ks = Ksiazka(numer_kat=nr_kat)
            self.stan.append(ks)
            return True
        else:
            return False

    def spr_czy_na_stanie(self, nr_kat):
        for ksiazka in self.stan:
            if ksiazka.numer_kat == nr_kat:
                return True
            

class Ksiazka():

    def __init__(self, numer_kat):
        self.numer_kat = numer_kat
