import unittest
from services.user_service import user_service

class TestUserService(unittest.TestCase):
    def setUp(self):
        user_service.budget_repository.delete_all()
        user_service.user_repository.delete_all()
        self.user = user_service.create_new_user("Matti", "salasana2")
        self.budget = user_service.create_budget(2000)

    def test_create_new_user_name(self):
        self.assertEqual(self.user.username, "Matti")

    def test_create_new_user_password(self):
        self.assertEqual(self.user.password, "salasana2")        

    def test_create_budget_user_id(self):
        self.assertEqual(self.budget.user_id, 1)

    def test_create_budget_amount(self):
        self.assertEqual(self.budget.amount, 2000)

    def test_show_remaining(self):
        self.assertEqual(self.budget.remaining, 2000)