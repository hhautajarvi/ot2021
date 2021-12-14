import unittest
from entities.user import User
from entities.expense import Expense

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Matti", "salasana1")
        self.expense1 = Expense(1, 100, 1, "kauppa", 2021-12-10)
        self.expense2 = Expense(1, 400, 4, "vuokra", 2021-12-10)
        self.user.add_expense(self.expense1)
        self.user.add_expense(self.expense2)

    def test_constructor_user_id_works(self):
        self.assertEqual(self.user.user_id, 1)

    def test_constructor_name_works(self):
        self.assertEqual(self.user.username, "Matti")

    def test_constructor_password_works(self):
        self.assertEqual(self.user.password, "salasana1")

    def test_add_expense(self):
        self.assertEqual(len(self.user.expenselist), 2)

    def test_add_expense_sum(self):
        self.assertEqual((self.user.expenselist[0].amount+self.user.expenselist[1].amount), 500)