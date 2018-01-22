class Balance:
    # available is a non amount in order
    def __init__(self, currencie, available=0, pending=0):
        self.currencie = currencie
        self.available = available
        self.pending = pending

    def total(self):
        return self.available + self.pending

    # should make api request
    def update_balance(self):
        print("  Updating balance " + self.currencie)
