import unittest
from services.user_service import user_service
from repositories.budget_repository import budget_repository
from repositories.user_repository import user_repository
from repositories.expense_repository import expense_repository
from datetime import date

class TestUserService(unittest.TestCase):
    def setUp(self):
        user_service._budget_repository.delete_all()
        user_service._user_repository.delete_all()
        user_service._expense_repository.delete_all()
        user_service.create_new_user("Matti", "salasana2")
        user_service.create_budget(2000)
        user_service.modify_budget(100, 90, 80, 70, 60, 50)
        user_service.create_expense(100, 4, "vuokra", "2012-12-26")
        user_service.create_expense(200, 1, "kauppalasku", "2012-12-26")
        self.user = user_repository.find_user("Matti")
        self.budget = budget_repository.select_budget(1)
        self.expenses = expense_repository.find_user_expenses(1)

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

    def test_create_budget_user_id(self):
        self.assertEqual(self.budget[1], 1)

    def test_create_budget_amount(self):
        self.assertEqual(self.budget[2], 2000)

    def test_modify_budget_food(self):        
        self.assertEqual(self.budget[3], 100)

    def test_modify_budget_transit(self):
        self.assertEqual(self.budget[4], 90)

    def test_modify_budget_entertainment(self):        
        self.assertEqual(self.budget[5], 80)

    def test_modify_budget_living(self):
        self.assertEqual(self.budget[6], 70)

    def test_modify_budget_utilities(self):
        self.assertEqual(self.budget[7], 60)

    def test_modify_budget_insurance(self):
        self.assertEqual(self.budget[8], 50)

    def test_create_expense(self):
        self.assertEqual(len(self.expenses), 2)

    def test_expense_sum(self):
        self.assertEqual((self.expenses[0][2]+self.expenses[1][2]), 300)

    def test_show_remaining(self):
        self.assertEqual(user_service.show_total(), 2000)

    def test_return_expenses(self):
        expenselist, expenselistcat = user_service.return_expenses()
        self.assertEqual(len(expenselist[1]), 1)
        self.assertEqual(len(expenselist[4]), 1)
        self.assertEqual(len(expenselist[0]), 0)
        expense_date = date.fromisoformat("2012-12-26")
        self.assertEqual(expenselistcat[(expense_date.month, expense_date.year)][0], 300)
        self.assertEqual(expenselistcat[(expense_date.month, expense_date.year)][1], 200)
        self.assertEqual(expenselistcat[(expense_date.month, expense_date.year)][4], 100)

    def test_logout(self):
        user_service.logout()
        self.assertIsNone(user_service._user)
