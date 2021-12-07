import unittest
from entities.expense import Expense

class TestExpense(unittest.TestCase):
    def setUp(self):
        self.expense = Expense(1, 100, 1, "kauppa", 2021-12-10)

    def test_constructor_user_id_works(self):
        self.assertEqual(self.expense.user_id, 1)

    def test_constructor_amount_works(self):
        self.assertEqual(self.expense.amount, 100)

    def test_constructor_category_works(self):
        self.assertEqual(self.expense.category, 1)

    def test_constructor_comment_works(self):
        self.assertEqual(self.expense.comment, "kauppa")
    
    def test_constructor_date_works(self):
        self.assertEqual(self.expense.date, 2021-12-10)
    