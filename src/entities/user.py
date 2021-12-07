class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.budget = None
        self.expenselist = []
        self.expenses_categorized = [0, 0, 0, 0, 0, 0, 0]
        #0= total 1=food, 2=transit, 3=entertainment, 4=living, 5=utilities, 6=insurance

    def add_expense(self, expense):
        self.expenses_categorized[expense.category] += expense.amount
        self.expenses_categorized[0] += expense.amount
        self.expenselist.append(expense)
