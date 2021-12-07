import unittest
from repositories.expense_repository import expense_repository

class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        expense_repository.delete_all()
        expense_repository.create_expense(1, 100, 1, "kauppa", 2021-12-10)
        self.expenses = expense_repository.find_user_expenses(1)

    def test_find_user_expenses(self):
        self.assertEqual(len(self.expenses), 1)

    def test_find_user_expenses_amount(self):
        self.assertEqual(self.expenses[0][2], 100)