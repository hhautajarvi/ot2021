class Budget:
    def __init__(self):
        self.amount = 0
        self.food = 0
        self.transit = 0
        self.entertainment = 0
        self.living = 0
        self.utilities = 0
        self.insurance = 0
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
