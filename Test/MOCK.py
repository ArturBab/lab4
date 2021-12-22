from main import *
from unittest import TestCase
from unittest.mock import patch

class TestCost(TestCase):
    @patch('main.sum_cost', return_value= 193840)
    def test_sum_cost(self, x):
        self.assertEqual(sum_cost(0), 193840)