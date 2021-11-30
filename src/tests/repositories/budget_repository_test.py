import unittest
from repositories.budget_repository import budget_repository

class TestBudgetRepository(unittest.TestCase):
    def setUp(self):
        budget_repository.delete_all()
        self.budget = budget_repository.create_budget(1, 1000)

    def test_create_budget_user_id(self):
        self.assertEqual(self.budget.user_id, 1)

    def test_create_budget_amount(self):
        self.assertEqual(self.budget.amount, 1000)