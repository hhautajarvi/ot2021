import unittest
from repositories.budget_repository import budget_repository

class TestBudgetRepository(unittest.TestCase):
    def setUp(self):
        budget_repository.delete_all()
        budget_repository.create_budget(1, 1000)
        self.budget1 = budget_repository.select_budget(1)
        budget_repository.modify_budget(1, 50, 40, 30, 20, 10, 5)
        self.budget2 = budget_repository.select_budget(1)

    def test_create_budget_user_id(self):        
        self.assertEqual(self.budget1[1], 1)

    def test_create_budget_amount(self):
        self.assertEqual(self.budget1[2], 1000)

    def test_modify_budget_food(self):
        self.assertEqual(self.budget2[3], 50)

    def test_modify_budget_transit(self):
        self.assertEqual(self.budget2[4], 40)

    def test_modify_budget_entertainment(self):
        self.assertEqual(self.budget2[5], 30)

    def test_modify_budget_living(self):
        self.assertEqual(self.budget2[6], 20)
    
    def test_modify_budget_utilities(self):
        self.assertEqual(self.budget2[7], 10)

    def test_modify_budget_insurance(self):
        self.assertEqual(self.budget2[8], 5)