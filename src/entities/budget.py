class Budget:
    def __init__(self, user_id, amount, food=0, transit=0, entertainment=0, \
        living=0, utilities=0, insurance=0):
        self.user_id = user_id
        self.amount = amount
        self.food = food
        self.transit = transit
        self.entertainment = entertainment
        self.living = living
        self.utilities = utilities
        self.insurance = insurance

    @property
    def used(self):
        return self.food + self.transit + self.entertainment + self.living + self.utilities + self.insurance

    @property
    def remaining(self):
        return self.amount - self.used

    def change_amount(self, amount):
        self.amount = amount

    def change_food(self, food):
        self.food = food

    def change_transit(self, transit):
        self.transit = transit

    def change_entertainment(self, entertainment):
        self.entertainment = entertainment

    def change_living(self, living):
        self.living = living

    def change_utilities(self, utilities):
        self.utilities = utilities

    def change_insurance(self, insurance):
        self.insurance = insurance
