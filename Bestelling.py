class Bestelling:
    """ Je krijgt een bestelling
        :param id: id van de bestelling,
               gebruikersid: id van de gebruiker,
               datum: data voor timestap
               tijd: tijd voor timestap
               choco_id: id van de chocolademelk
               veld: is de chocomelk afgehaald ofni
        :return None
        precondition: niks is None
        postcondition: Stock is aangepast
        """

    def __int__(self, id, gebruikersid, datum,tijd, choco_id, veld):
        self.gebruikers = gebruikersid
        self.timestap = (tijd, datum)
        self.chocolademelkid = choco_id
        self.veld = veld
        self.zoeksleutel = id

    def b_afgewerkt(self):
        """
        b_afgewerkt
        :return: None
        pre: bestelling bestaat
        post: bestelling is afgewerkt (afgehaald blijft False tenzij later opgehaald)
        """
        print("Bestelling is afgewerkt en wordt bewaard in de BST.")
