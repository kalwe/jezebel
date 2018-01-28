class Balance:

    _available = 0.0
    _pending = 0.0
    _amount_total = 0.0

    def __init__(self, currencie, available=0.0):
        self._currencie = currencie
        self._available = available # available is a non amount in order
        # self._pending = pending
        # self._amount_total = self.amount_total()

    def total_amount(self):
        return self._available + self._pending

    def add_pending(self, val):
        self._pending += val
        self._available -= val

    def total_pending(self):
        return self._pending

    # should make api request
    def update_balance(self):
        print("  Updating balance " + self._currencie)
