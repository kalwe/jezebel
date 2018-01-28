import unittest
from modules.riskmanager.riskmanager import *
from modules.exchange.balance import *

class TestRiskManager(unittest.TestCase):
    def setUp(self):
        self.balanceusd = Balance('USD', 1000.00)
        self.riskmanager = RiskManager(self.balanceusd)

    def tearDown(self):
        self.balanceusd._pending = 0.0
        self.balanceusd._available = 0.0

    """Should return True if have capital to invest"""
    def test_have_god_limit(self):
        self.balanceusd.add_pending(200.00)
        self.balanceusd.add_pending(50)
        self.assertTrue(self.riskmanager.have_god_limit())

    def test_have_god_limit_negative(self):
        self.balanceusd.add_pending(200.00)
        self.balanceusd.add_pending(500.00)
        self.assertFalse(self.riskmanager.have_god_limit())


    # def test_capital_to_invest(self):
    #     self.assertTrue(True, True)

    # def test_capital_to_altcoin(self):
    #     self.assertTrue(True, True)
