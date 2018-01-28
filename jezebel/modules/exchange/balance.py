class Balance:

    _available = 0.0
    _pending = 0.0
    _total_amount = 0.0

    def __init__(self, currencie, available=0.0):
        self._currencie = currencie
        self._available = float(available) # available is a non amount in order
        self._total_amount = self.total_amount()
        # self._pending = pending
        # self._amount_total = self.amount_total()

    def total_amount(self):
        return self._available + self._pending

    def add_pending(self, val):
        self._pending += float(val)
        self._available -= float(val)

    def sub_pending(self, val):
        self._pending -= float(val)

    def total_pending(self):
        return self._pending

    # should make api request
    def update_balance(self):
        print("  Updating balance " + self._currencie)
