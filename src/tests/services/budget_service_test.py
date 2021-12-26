import unittest
from repositories.budget_repository import budget_repository
from services.budget_service import budget_service
from services.user_service import user_service

class TestBudgetService(unittest.TestCase):
    def setUp(self):
        budget_service._budget_repository.delete_all()
        user_service._user_repository.delete_all()
        user_service.create_new_user("Matti", "salasana2")
        budget_service.create_budget(2000)
        budget_service.modify_budget(100, 90, 80, 70, 60, 50)
        self.budget = budget_repository.select_budget(1)

    def test_constructor(self):
        self.assertFalse(budget_service._budget_modify)
        self.assertEqual(budget_service._user_id, 1)

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

    def test_show_total(self):
        self.assertEqual(budget_service.show_total(), 2000)

    def test_show_budget(self):
        test_budget = budget_service.show_budget()
        self.assertEqual(self.budget[1], test_budget.user_id)
        self.assertEqual(self.budget[2], test_budget.amount)
        self.assertEqual(self.budget[3], test_budget.food)
        self.assertEqual(self.budget[4], test_budget.transit)
        self.assertEqual(self.budget[5], test_budget.entertainment)
        self.assertEqual(self.budget[6], test_budget.living)
        self.assertEqual(self.budget[7], test_budget.utilities)
        self.assertEqual(self.budget[8], test_budget.insurance)

    def test_check_budget(self):
        self.assertTrue(budget_service.check_budget())
        
    def test_check_budget_false(self):
        user_service._user.user_id = 2
        self.assertFalse(budget_service.check_budget())

    def test_check_modify_off(self):
        self.assertEqual(budget_service._budget_modify, budget_service.check_modify())

    def test_modify_on(self):
        budget_service.modify_on()
        self.assertEqual(budget_service._budget_modify, budget_service.check_modify())

    def test_budget_logout(self):
        budget_service.budget_logout()
        self.assertIsNone(budget_service._budget)
        self.assertFalse(budget_service._budget_modify)