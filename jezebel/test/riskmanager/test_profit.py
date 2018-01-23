import unittest
from modules.riskmanager.profit import *

class TestProfit(unittest.TestCase):
    def test_calc_prt(self):
        self.assertEqual(profit_to_gain(100, 1, 0.4), 101.4)

    def test_profit_to_gain(self):
        self.assertEqual(profit_to_gain(100, 3, 0.4), 103.4)

    def test_profit_to_loss(self):
        self.assertEqual(profit_to_loss(100, 1, 0.4), 98.6)

    def test_profit_gain_without_fees(self):
        self.assertEqual(profit_gain_without_fees(100, 1), 101)

    def test_profit_loss_without_fees(self):
        self.assertEqual(profit_loss_without_fees(100, 1), 99)

    def test_profit_one_prct(self):
        self.assertEqual(profit_one_prct(100, 0.4), 101.4)
