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
        self.remaining = 0
        self.used = 0

    def update_remaining(self):
        self.used = self.food + self.transit + self.entertainment + self.living \
            + self.utilities + self.insurance
        self.remaining = self.amount - self.used

    def change_amount(self, amount):
        self.amount = amount
        self.update_remaining()

    def change_food(self, food):
        self.food = food
        self.update_remaining()

    def change_transit(self, transit):
        self.transit = transit
        self.update_remaining()

    def change_entertainment(self, entertainment):
        self.entertainment = entertainment
        self.update_remaining()

    def change_living(self, living):
        self.living = living
        self.update_remaining()

    def change_utilities(self, utilities):
        self.utilities = utilities
        self.update_remaining()

    def change_insurance(self, insurance):
        self.insurance = insurance
        self.update_remaining()
