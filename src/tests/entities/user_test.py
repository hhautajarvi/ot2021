import unittest
from entities.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Matti", "salasana1")

    def test_constructor_name_works(self):
        self.assertEqual(self.user.username, "Matti")

    def test_constructor_password_works(self):
        self.assertEqual(self.user.password, "salasana1")