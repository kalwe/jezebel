class Exchange(object):

    _orders = []
    _balances = []

    def __init__(self, name, url, api):
        self._name = name
        self._url = url
        self._api = api

    # ajust to concat name and url
    def info(self):
        print(self._name)
        print(self._url)

    def append_balance(self, balance):
        self._balances.append(balance)

    def create_order(self, order):
        order.execute()
        if order._is_open:
            self._orders.append(order)

    def list_orders(self):
        if self._orders.__len__() != 0:
            return self._orders

    def open_orders(self):
        orders = []
        for order in self._orders:
            if order._is_open:
                orders.append(order)
        return orders
