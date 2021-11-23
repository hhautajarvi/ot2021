import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()

    def test_create_user(self):
        user_repository.create_user("Pekka", "salasana1")
        newuser = user_repository.find_user("Pekka")
        self.assertEqual(newuser.username, "Pekka")
        self.assertEqual(newuser.password, "salasana1")