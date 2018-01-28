import unittest
from modules.exchange.balance import *

class TestBalance(unittest.TestCase):
    def setUp(self):
        self.balanceusd = Balance('USD', 1000.00)

    def tearDown(self):
        self.balanceusd._available = 0.0
        self.balanceusd._pending = 0.0
        # self.balanceusd._total_amount = 0.0

    def test_add_pending(self):
        pending_amount = 250.00
        self.balanceusd.add_pending(pending_amount)
        self.assertEqual(self.balanceusd.total_pending(), pending_amount)

    def test_total_amount(self):
        self.balanceusd.add_pending(200.00)
        self.assertEqual(self.balanceusd.total_amount(), 1000.00)
