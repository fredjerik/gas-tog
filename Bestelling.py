class Bestelling:
    def __int__(self, id, gebruikersid, datum,tijd, choco_id, veld):
        self.gebruikers = gebruikersid
        self.timestap = (tijd, datum)
        self.chocolademelkid = choco_id
        self.veld = veld
        self.zoeksleutel = id
