class Werknemer:
    """ Werknemer toevoegen
                :param id: id van de Werknemer,
                       vn: voornaam van de Werknemer,
                       an: achternaam van de Werknemer
                       credits: credits van de Werknemer

                :return None
                precondition: niks is None
                postcondition: Werknemer toegevoegd
                """

    def __int__(self, id, vn, an, credits):
        self.voornaam = vn
        self.achternaam = an
        self.workload = credits
        #werknemer werkt aan max 1 bestelling tegelijk
        self.huidige_bestelling = None

    def neem_bestelling(self, bestelling):
        """
        :param bestelling
        :return: None
        precondition: bestelling is not None
        postcondition: self.huidige_bestelling == bestelling
        """
        self.huidige_bestelling = bestelling
        print("Werknemer neemt bestelling")

    def werk_1_tijdseenheid(self):
        """
        Werk 1 tijdseenheid aan de huidige bestelling.

        :return: None
        precondition: self.huidige_bestelling is not None
        postcondition:
        """
        if self.huidige_bestelling is None:
            print("werknemer doet niets ")
        else:
            print("Werknemer werkt aan een bestelling")
            return

    def maak_vrij_als_klaar(self):
        """
        Maak werknemer vrij indien bestelling klaar.

        :return: Bestelling|None (klaar bestelde object als die net klaar werd)
        precondition: geen
        postcondition: als bestelling klaar: self.huidige_bestelling wordt None
        """
        if self.huidige_bestelling is None:
            return None

        if self.huidige_bestelling.is_klaar():
            klaar = self.huidige_bestelling
            self.huidige_bestelling = None
            print("Bestelling is klaar")
            return klaar
        return None