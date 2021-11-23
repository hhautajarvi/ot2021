from entities.budget import Budget

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.budget = Budget()