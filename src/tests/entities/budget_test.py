import unittest
from entities.budget import Budget

class TestUser(unittest.TestCase):
    def setUp(self):
        self.budget = Budget(1, 200)

    def test_constructor_user_id(self):
        self.assertEqual(self.budget.user_id, 1)

    def test_constructor_budget_amount(self):
        self.assertEqual(self.budget.amount, 200)

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