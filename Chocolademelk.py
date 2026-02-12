class Chocolademelk:
    """check Chocolademelk
            :param id: id van melk


            :return True/False

            precondition: is niet None
            Postcondition: 1 Chocolademelk minder van de Stock"""
    def __init__(self, id):
        self.basisprijs = 2
        self.zoeksleutel = id
        self.toevoegingen = []

    def voeg_toe(self, toevoeging):
        """
        voeg_toe
        :param toevoeging: Honing, chilipeper...
        :return: None
        precondition: toevoeging is not None
        postcondition: toevoeging zit in self.toevoegingen
        """

        self.toevoegingen.append(toevoeging)
        print("Er is iets toegevoegd in de chocolademelk")

    def workload(self):
        """
               Workload: 5 credits per chocolademelk + 1 per toevoeging.

               :return: credits
               precondition: geen
               postcondition: resultaat >= 5
               """
        print("Workload voor chocolademelk")
        return 5 + len(self.toevoegingen)


    def prijs(self):
        """
                Bereken prijs op basis van basisprijs + toevoegingen.

                :return: totale prijs
                precondition: alle items in lijsten hebben een .prijs
                postcondition: resultaat >= basisprijs
                """
        print("Prijs voor chocolademelk")
        return self.basisprijs + len(self.toevoegingen)
