class RiskManager(object):

    SAFETY = 70/100
    PRINCIPAL = 30/100
    ALTERNATIVE = 20/100

    def __init__(self, balance):
        self._balance = balance # Class with currencie and amount
        # self._principal = principal # Value in percent to calc for principal currencie
        # self._alternative = alternative # Value in percent to calc alternative coin
        # self._safety = safety # Reservatoin or safety margin to save

    """Leave you alive to fight anoter day,
    save 70% of total capital, not allow invest if pending value is above this limit"""
    def have_god_limit(self):
    #     print(str(self._balance._pending))
    #     print(str(self._balance._available))
        if self._balance._pending < (self._balance.total_amount() * (self.SAFETY)):
            return True
        else:
            return False

    """Return 1/3 of your capital to security invest"""
    def capital_to_invest(self):
        if self.have_god_limit():
            return self._balance.amount_total/self.SAFETY

    """Return safe capital to invest in altcoins"""
    def capital_to_altcoin(self):
        if self._balance._available > 0:
            return self._balance._abailable * (self.ALTERNATIVE/100)
