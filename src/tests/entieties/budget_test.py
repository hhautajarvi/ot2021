import unittest
from entities.budget import Budget

class TestUser(unittest.TestCase):
    def setUp(self):
        self.budget = Budget()

    def test_change_amount(self):
        self.budget.change_amount(100)
        self.assertEqual(self.budget.amount, 100)

    def test_change_food(self):
        self.budget.change_food(10)
        self.assertEqual(self.budget.food, 10)

    def test_change_transit(self):
        self.budget.change_transit(10)
        self.assertEqual(self.budget.transit, 10)

    def test_change_entertainment(self):
        self.budget.change_entertainment(10)
        self.assertEqual(self.budget.entertainment, 10)

    def test_change_living(self):
        self.budget.change_living(10)
        self.assertEqual(self.budget.living, 10)

    def test_change_utilities(self):
        self.budget.change_utilities(10)
        self.assertEqual(self.budget.utilities, 10)

    def test_change_insurance(self):
        self.budget.change_insurance(10)
        self.assertEqual(self.budget.insurance, 10)

    def test_used_sum(self):
        self.budget.change_food(10)
        self.budget.change_transit(10)
        self.budget.change_entertainment(10)
        self.budget.change_living(10)
        self.budget.change_insurance(10)
        self.budget.change_utilities(10)
        self.assertEqual(self.budget.used, 60)

    def test_remaining_sum(self):
        self.budget.change_amount(100)        
        self.budget.change_food(10)
        self.budget.change_transit(10)
        self.budget.change_entertainment(10)
        self.budget.change_living(10)
        self.budget.change_insurance(10)
        self.budget.change_utilities(10)
        self.assertEqual(self.budget.remaining, 40)