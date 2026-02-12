class Honing:
    """check Honing
            :param id: id van Honinh
                   verval: vervaldatum van de Honing

            :return True/False

            precondition: is niet None
            Postcondition: 1 Honing minder van de Stock"""

    def __init__(self, id, verval):
        self.prijs  = 0.5
        self.vervaldatum = verval
        self.zoeksleutel = id
