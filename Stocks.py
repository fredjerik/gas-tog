class Stocks:
    def __init__(self, product_type):
        """
        Algemene stock voor één type product.

        :param product_type: naam van het product
        postcondition: lege lijst van producten
        """
        self.product_type = product_type
        self.items = []

    def voeg_toe(self, item):
        """
        Voeg een item toe aan de stock.

        :param item: object van het juiste type
        precondition: item is not None
        postcondition: item zit in items
        """
        print("Item is toegevoegd aan stock")
        self.items.append(item)

    def neem_uit_stock(self):
        """
        Neem één item uit stock

        :return: item of None
        postcondition: stock is 1 item kleiner indien niet leeg
        """
        if len(self.items) == 0:
            print("stock is leeg")
            return None

        item = self.items.pop(0)
        print("item is eruitgenomen")
        return item
