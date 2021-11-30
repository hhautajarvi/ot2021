import unittest
from entities.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Matti", "salasana1")

    def test_constructor_user_id_works(self):
        self.assertEqual(self.user.user_id, 1)

    def test_constructor_name_works(self):
        self.assertEqual(self.user.username, "Matti")

    def test_constructor_password_works(self):
        self.assertEqual(self.user.password, "salasana1")