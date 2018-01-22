class OrderType:

    limit = 'LIMIT'
    limit_oco = 'LIMIT-OCO'
    market = 'MARKET'
    stop = 'STOP'
    trailling_stop = 'TRAILLING-STOP'

    def limit(self):
        self.otype = 'LIMIT'
        return self.otype

    def limit_oco(self):
        self.otype = 'LIMIT-OCO'
        return self.otype

    def market(self):
        self.otype = 'MARKET'
        return self.otype

    def stop(self):
        self.otype = 'STOP'
        return self.otype

    def trailling_stop(self):
        self.otype = 'TRAILLING-STOP'
        return self.otype
