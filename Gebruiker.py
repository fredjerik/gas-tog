class gebruiker:
    """ Gebruiker toevoegen
            :param id: id van de gebruiker,
                   vn: voornaam van de gebruiker,
                   an: achternaam van de gebruiker
                   e-mail: e-mail van de gebruiker

            :return None
            precondition: niks is None
            postcondition: Gebruiker toegevoegd aan de klanten
            """

    def __int__(self, id, vn, an, e_mail):
        self.voor_naam = vn
        self.achter_naam = an
        self.email = e_mail
        self.zoeksleutel = id

    def bestel(self, chocolademelk):
        """
        Plaats een bestelling voor een gegeven chocolademelk

        :param Chocolademelk
        :return: None
        precondition: chocolademelk is not None
        postcondition: bestelling is aangemaakt en stock verlaagd
        """
        print("Gebruiker bestelt chocolademelk ")
