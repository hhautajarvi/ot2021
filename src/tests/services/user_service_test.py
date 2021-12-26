import unittest
from entities.expense import Expense
from services.user_service import user_service
from repositories.user_repository import user_repository
from datetime import date

class TestUserService(unittest.TestCase):
    def setUp(self):
        user_service._user_repository.delete_all()
        user_service._expense_repository.delete_all()
        user_service.create_new_user("Matti", "salasana2")
        expense1 = Expense(1, 100, 4, "vuokra", "2012-12-26")
        expense2 = Expense(1, 200, 1, "kauppalasku", "2012-12-26")
        user_service.add_expense(expense1)
        user_service.add_expense(expense2)
        self.user = user_repository.find_user("Matti")

    def test_create_new_user_name(self):
        self.assertEqual(self.user.username, "Matti")

    def test_create_new_user_password(self):
        self.assertEqual(self.user.password, "salasana2")  
        
    def test_create_new_user_duplicate_username(self):
        self.assertRaises(Exception, user_service.create_new_user, "Matti", "sala")  

    def test_login_user(self):
        login_user = user_service.login("Matti", "salasana2")
        self.assertEqual(login_user.username, self.user.username)
        self.assertEqual(login_user.password, self.user.password)

    def test_login_user_wrong_username(self):
        self.assertRaises(Exception, user_service.login, "Masa", "salasana2")

    def test_login_user_wrong_password(self):
        self.assertRaises(Exception, user_service.login, "Matti", "sala")

    def test_find_expenses(self):
        user_service._find_expenses()
        expense_date = date.fromisoformat("2012-12-26")
        self.assertEqual(len(user_service._user.expenselist[0]), 0)
        self.assertEqual(len(user_service._user.expenselist[1]), 1)
        self.assertEqual(len(user_service._user.expenselist[4]), 1)
        self.assertEqual(user_service._user.expenses_categorized[(expense_date.month, expense_date.year)][0], 300)
        self.assertEqual(user_service._user.expenses_categorized[(expense_date.month, expense_date.year)][1], 200)
        self.assertEqual(user_service._user.expenses_categorized[(expense_date.month, expense_date.year)][4], 100)

    def test_return_expenses(self):
        expenselist, expenselistcat = user_service.return_expenses()
        self.assertEqual(len(expenselist[1]), 1)
        self.assertEqual(len(expenselist[4]), 1)
        self.assertEqual(len(expenselist[0]), 0)
        expense_date = date.fromisoformat("2012-12-26")
        self.assertEqual(expenselistcat[(expense_date.month, expense_date.year)][0], 300)
        self.assertEqual(expenselistcat[(expense_date.month, expense_date.year)][1], 200)
        self.assertEqual(expenselistcat[(expense_date.month, expense_date.year)][4], 100)

    def test_show_id(self):
        self.assertEqual(self.user.user_id, user_service.show_id())

    def test_month_check(self):
        user_service.month_check(11, 2021)
        expense_date = date.fromisoformat("2012-11-26")
        self.user.expenses_categorized[(expense_date.month, expense_date.year)] = [0, 0, 0, 0, 0, 0, 0]

    def test_logout(self):
        user_service.logout()
        self.assertIsNone(user_service._user)
