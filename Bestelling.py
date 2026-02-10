class Bestelling:
    def __init__(self, id, gebruikersid, datum, tijd, chocolademelkid):
        self.Gebruikersid = gebruikersid
        self.Timestamp = (tijd, datum)
        self.ChocolademelkID = chocolademelkid
        self.Afgehaald = False
        self.Zoeksleutel = id