import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *

class TestCost(unittest.TestCase):

    def test_cost(self):
        self.assertEqual(check_cost("Xbox series X / XSX"), 50000)

    def test_cost1(self):
        self.assertEqual(check_cost("PlayStation 5 / PS5"), 105000)

    def test_cost2(self):
        self.assertEqual(check_cost("Nintendo Switch / NS"), 38840)

if __name__ == "__main__":
    unittest.main()