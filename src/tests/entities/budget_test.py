import unittest
from entities.budget import Budget

class TestUser(unittest.TestCase):
    def setUp(self):
        self.budget = Budget(1, 200)
        self.budget2 = Budget(2, 1300, 50, 100, 150, 200, 300, 400)

    def test_constructor_only_amount(self):
        self.assertEqual(self.budget.user_id, 1)
        self.assertEqual(self.budget.amount, 200)
        self.assertEqual(self.budget.food, 0)
        self.assertEqual(self.budget.transit, 0)
        self.assertEqual(self.budget.entertainment, 0)
        self.assertEqual(self.budget.living, 0)
        self.assertEqual(self.budget.utilities, 0)
        self.assertEqual(self.budget.insurance, 0)

    def test_used(self):
        self.assertEqual(self.budget.used, 0)

    def test_remaining(self):
        self.assertEqual(self.budget.remaining, 200)

    def test_constructor_all_attributes(self):
        self.assertEqual(self.budget2.user_id, 2)
        self.assertEqual(self.budget2.amount, 1300)
        self.assertEqual(self.budget2.food, 50)
        self.assertEqual(self.budget2.transit, 100)
        self.assertEqual(self.budget2.entertainment, 150)
        self.assertEqual(self.budget2.living, 200)     
        self.assertEqual(self.budget2.utilities, 300)
        self.assertEqual(self.budget2.insurance, 400)

    def test_used(self):
        self.assertEqual(self.budget2.used, 1200)

    def test_remaining(self):
        self.assertEqual(self.budget2.remaining, 100)