from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.shopping_basket = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        amount = 0
        for item in self.shopping_basket.values():
            amount = amount + item.lukumaara()
        return amount
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        price = 0
        for item in self.shopping_basket.values():
            price = price + item.hinta()
        return price

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() in self.shopping_basket:
            item = self.shopping_basket[lisattava.nimi()]
            item.muuta_lukumaaraa(1)
            self.shopping_basket.update({lisattava.nimi(): item})
        else:
            self.shopping_basket[lisattava.nimi()] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        if poistettava.nimi() in self.shopping_basket:
            item = self.shopping_basket[poistettava.nimi()]
            item.muuta_lukumaaraa(-1)
            if item.lukumaara() == 0:
                self.shopping_basket.pop(poistettava.nimi())
            else:
                self.shopping_basket.update({poistettava.nimi(): item})

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return [item for item in self.shopping_basket.values()]
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
