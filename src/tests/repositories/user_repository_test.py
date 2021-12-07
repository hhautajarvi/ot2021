import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user = user_repository.create_user("Pekka", "salasana1")

    def test_create_user(self):        
        newuser = user_repository.find_user("Pekka")
        self.assertEqual(newuser.username, "Pekka")
        self.assertEqual(newuser.password, "salasana1")

    def test_create_same_username(self):
        self.assertRaises(Exception, user_repository.create_user("Pekka", "salasana1"))