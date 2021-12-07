from tkinter import ttk, constants
from services.user_service import user_service

class BudgetChooseView:
    def __init__(self, root, show_budget_view):
        self.root = root
        self.frame = None
        self.show_budget_view = show_budget_view

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def show_remaining(self):
        self.remaining = user_service.show_remaining()
        remaining_label = ttk.Label(master=self.frame, text=f"You have {self.remaining} in your budget")
        remaining_label.grid(padx=5, pady=5)

    def choose_food(self):
        food_label = ttk.Label(master=self.frame, text="Choose food budget:")
        self.food_sum = ttk.Entry(master=self.frame)
        food_label.grid(padx=5, pady=5)
        self.food_sum.grid(row=2, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)     

    def choose_transit(self):
        transit_label = ttk.Label(master=self.frame, text="Choose transit budget:")
        self.transit_sum = ttk.Entry(master=self.frame)
        transit_label.grid(padx=5, pady=5)
        self.transit_sum.grid(row=3, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def choose_entertainment(self):
        entertainment_label = ttk.Label(master=self.frame, text="Choose entertainment budget:")
        self.entertainment_sum = ttk.Entry(master=self.frame)
        entertainment_label.grid(padx=5, pady=5)
        self.entertainment_sum.grid(row=4, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
 
    def choose_living(self):
        living_label = ttk.Label(master=self.frame, text="Choose living budget:")
        self.living_sum = ttk.Entry(master=self.frame)
        living_label.grid(padx=5, pady=5)
        self.living_sum.grid(row=5, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def choose_utilities(self):
        utilities_label = ttk.Label(master=self.frame, text="Choose utilities budget:")
        self.utilities_sum = ttk.Entry(master=self.frame)
        utilities_label.grid(padx=5, pady=5)
        self.utilities_sum.grid(row=6, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def choose_insurance(self):
        insurance_label = ttk.Label(master=self.frame, text="Choose insurance budget:")
        self.insurance_sum = ttk.Entry(master=self.frame)
        insurance_label.grid(padx=5, pady=5)
        self.insurance_sum.grid(row=7, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)        
        budget_label = ttk.Label(master=self.frame, text="Here you can choose your budget")
        budget_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.show_remaining()
        self.choose_food()
        self.choose_transit()
        self.choose_entertainment()
        self.choose_living()
        self.choose_utilities()
        self.choose_insurance()
        create_button = ttk.Button(master=self.frame, text="Create", command=self.createbutton_click)
        create_button.grid(row=8, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def createbutton_click(self):
        food = int(self.food_sum.get())
        transit = int(self.transit_sum.get())
        entertainment = int(self.entertainment_sum.get())
        living = int(self.living_sum.get())
        utilities = int(self.utilities_sum.get())
        insurance = int(self.insurance_sum.get())
        amount = food + transit + entertainment + living + utilities + insurance
        if self.remaining >= amount:
            user_service.modify_budget(food, transit, entertainment, living, utilities, insurance)
            self.show_budget_view()
        else:
            money_label = ttk.Label(master=self.frame, text=f"You have {self.remaining-amount} in your budget")
            money_label.grid(padx=5, pady=5)
            self.initialize()