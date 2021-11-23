import unittest
from services.user_service import user_service

class TestUserService(unittest.TestCase):

    def test_create_new_user(self):
        newuser = user_service.create_new_user("Matti", "salasana2")
        self.assertEqual(newuser.username, "Matti")
        self.assertEqual(newuser.password, "salasana2")        