class Chocoladeshot:
    """check Chocoladeshot
            :param id: id van shot
                   verval: vervaldatum van de shot

            :return True/False

            precondition: is niet None
            Postcondition: 1 shot minder van de Stock"""

    def __int__(self, id, kleur_melk, verval_data):
        self.prijs = 1

        self.datum_slecht = verval_data
        self.zoeksleutel = id

        if kleur_melk == "zwarte" or "melk" or "bruine" or "witte":
            self.kleur = kleur_melk
            return self.kleur



