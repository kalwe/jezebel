class RiskManager(object):

    SAFETY = 70/100
    PRINCIPAL = 30/100
    ALTERNATIVE = 20/100

    def __init__(self, balance, principal, alternative, safety):
        self._balance = balance
        self._principal = principal
        self._alternative = alternative
        self._safety = safety

    """Leave you alive to fight anoter day,
    save 70% of total capital, not allow invest if pending value is above this limit"""
    def have_god_limit(self):
        if self._balance.pending > (self._balance.amount_total * (SAFETY/100))
            return True
        else:
            return False

    """Return 1/3 of your capital to security invest"""
    def capital_to_invest(self):
        if self.have_god_limit():
            return balance.amount_total/SAFETY

    """Return safe capital to invest in altcoins"""
    def capital_to_altcoin(self)
        if self._balance.available > 0:
            return balance.abailable * (ALTERNATIVE/100)
