import unittest
from services.user_service import user_service
from repositories.budget_repository import budget_repository
from repositories.user_repository import user_repository
from repositories.expense_repository import expense_repository

class TestUserService(unittest.TestCase):
    def setUp(self):
        user_service._budget_repository.delete_all()
        user_service._user_repository.delete_all()
        user_service._expense_repository.delete_all()
        user_service.create_new_user("Matti", "salasana2")
        user_service.create_budget(2000)
        user_service.modify_budget(100, 90, 80, 70, 60, 50)
        user_service.create_expense(100, 4, "vuokra")
        user_service.create_expense(200, 1, "kauppalasku")
        self.user = user_repository.find_user("Matti")
        self.budget = budget_repository.select_budget(1)
        self.expenses = expense_repository.find_user_expenses(1)

    def test_create_new_user_name(self):
        self.assertEqual(self.user.username, "Matti")

    def test_create_new_user_password(self):
        self.assertEqual(self.user.password, "salasana2")        

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