import unittest
from services.budget_service import budget_service
from services.user_service import user_service
from services.expense_service import expense_service
from repositories.expense_repository import expense_repository

class TestExpenseService(unittest.TestCase):
    def setUp(self):
        user_service._user_repository.delete_all()
        user_service._expense_repository.delete_all()
        user_service.create_new_user("Matti", "salasana2")
        budget_service.create_budget(2000)
        budget_service.modify_budget(100, 90, 80, 70, 60, 50)
        expense_service.create_expense(100, 4, "vuokra", "2012-12-26")
        expense_service.create_expense(200, 1, "kauppalasku", "2012-12-26")
        self.expenses = expense_repository.find_user_expenses(1)

    def test_create_expense(self):
        self.assertEqual(len(self.expenses), 2)

    def test_expense_sum(self):
        self.assertEqual((self.expenses[0][2]+self.expenses[1][2]), 300)