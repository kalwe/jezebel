import unittest
from modules.riskmanager.profit import *

class TestProfit(unittest.TestCase):
    def test_calc_prt(self):
        self.assertEqual(profit_to_gain(100, 0, 0.4), 100.4)
