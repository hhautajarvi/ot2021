from entities.budget import Budget
from repositories.user_repository import user_repository as default_user_repository
from repositories.budget_repository import budget_repository as default_budget_repository

class UserService:
    def __init__(self, user_repository=default_user_repository,\
        budget_repository= default_budget_repository):
        self.user = None
        self.budget = None
        self.user_repository = user_repository
        self.budget_repository = budget_repository

    def create_new_user(self, username, password):
        usercheck = self.user_repository.find_user(username)

        if usercheck is not None:
            if username == usercheck.username:
                raise Exception
        self.user = self.user_repository.create_user(username, password)
        return self.user

    def login(self, username, password):
        usercheck = self.user_repository.find_user(username)
        if username == usercheck.username and password == usercheck.password:
            self.user = usercheck
            return self.user
        raise Exception

    def create_budget(self, amount):
        user_id = self.user.user_id
        self.budget = self.budget_repository.create_budget(user_id, amount)

    def show_remaining(self):
        return self.budget.remaining

    def show_budget(self):
        budget = self.budget_repository.select_budget(self.user.user_id)
        self.budget = Budget(budget[1], budget[2], budget[3], budget[4], budget[5], \
            budget[6], budget[7], budget[8])
        return self.budget

    def modify_budget(self, food, transit, entertainment, living, utilities, insurance):
        self.budget_repository.modify_budget(self.user.user_id, food, transit,\
            entertainment, living, utilities, insurance)

user_service = UserService()
