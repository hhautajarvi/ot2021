class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.budget = None
        self.expenselist = []

    def add_expense(self, expense):
        self.expenselist.append(expense)
