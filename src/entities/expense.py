class Expense:
    def __init__(self, user_id, amount, category, comment, date):
        self.user_id = user_id
        self.amount = amount
        self.category = category
        # 1=food, 2=transit, 3=entertainment, 4=living, 5=utilities, 6=insurance
        self.comment = comment
        self.date = date
