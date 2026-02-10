class Chocoladeshot:
    def __init__(self, id, vervaldatum, type):
        self.Prijs = 1.00
        self.Vervaldatum = vervaldatum
        self.Zoeksleutel = id

        self.Wit = False
        self.Zwart = False
        self.Melk = False
        self.Puur = False

        if type == "wit":
            self.Wit = True
        elif type == "zwart":
            self.Zwart = True
        elif type == "melk":
            self.Melk = True
        elif type == "puur":
            self.Puur = True
