import unittest
from services.user_service import user_service
from repositories.budget_repository import budget_repository
from repositories.user_repository import user_repository

class TestUserService(unittest.TestCase):
    def setUp(self):
        user_service.budget_repository.delete_all()
        user_service.user_repository.delete_all()
        user_service.create_new_user("Matti", "salasana2")
        user_service.create_budget(2000)
        self.user = user_repository.find_user("Matti")
        self.budget = budget_repository.select_budget(1)

    def test_create_new_user_name(self):
        self.assertEqual(self.user.username, "Matti")

    def test_create_new_user_password(self):
        self.assertEqual(self.user.password, "salasana2")        

    def test_create_budget_user_id(self):
        self.assertEqual(self.budget[1], 1)

    def test_create_budget_amount(self):
        self.assertEqual(self.budget[2], 2000)
