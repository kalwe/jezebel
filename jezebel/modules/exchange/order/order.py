class Order:

    _is_open = False
    _are_hit = None
    _is_finish = False

    def __init__(self, otype, currencie, price, amount):
        # self._id =
        self._otype = otype
        self._currencie = currencie
        self._price = price
        self._amount = amount

    def sell(self):
        print("  Sell " + self._otype + " order executed, amount: " + str(self._amount) + " " + self._currencie + " at price" + str(self._price))

    def buy(self):
        print("  Buy " + self._otype + " order executed, amount: " + str(self._amount) + " " + self._currencie + " at price " + str(self._price))

    """Submite order request to exchange api"""
    def execute(self):
        # validate with exchange api responde to set _is_open equal true
        self._is_open = True

    def cancel(self):
        self._is_finish = True
        self._is_open = False
        print("\n  Order canceled.")

    def is_finish(self):
        if self._is_finish == True:
            return self
