import unittest
from repositories.expense_repository import expense_repository

class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        expense_repository.delete_all()
        expense_repository.create_expense(1, 100, 1, "kauppa", 2021-12-10)
        self.expenses = expense_repository.find_user_expenses(1)

    def test_find_user_expenses(self):
        self.assertEqual(len(self.expenses), 1)
        self.assertEqual(self.expenses[0][0], 1)
        self.assertEqual(self.expenses[0][1], 1)
        self.assertEqual(self.expenses[0][2], 100)
        self.assertEqual(self.expenses[0][3], 1)
        self.assertEqual(self.expenses[0][4], "kauppa")
        self.assertEqual(self.expenses[0][5], 2021-12-10)

    def test_create_expense(self):
        new_expense = expense_repository.create_expense(1, 200, 4, "vuokra", 2021-12-12)
        self.assertEqual(new_expense.user_id, 1)
        self.assertEqual(new_expense.amount, 200)
        self.assertEqual(new_expense.category, 4)
        self.assertEqual(new_expense.comment, "vuokra")
        self.assertEqual(new_expense.date, 2021-12-12)