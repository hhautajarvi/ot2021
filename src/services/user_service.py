from entities.user import User
from repositories.user_repository import user_repository as default_user_repository

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self.user = None
        self.user_repository = user_repository

    def create_new_user(self, username, password):
        usercheck = self.user_repository.find_user(username)

        if usercheck is not None:
            if username == usercheck.username:
                raise Exception

        return self.user_repository.create_user(username, password)

    def login(self, username, password):
        usercheck = self.user_repository.find_user(username)
        if username == usercheck.username and password == usercheck.password:
            self.user = usercheck
            return self.user
        raise Exception

user_service = UserService()
