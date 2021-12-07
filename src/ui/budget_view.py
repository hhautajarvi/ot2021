from tkinter import ttk, constants
from services.user_service import user_service

class BudgetView:
    def __init__(self, root):
        self.root = root       
        self.frame = None
        self.budget = user_service.show_budget()

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def show_budget(self):
        intro_text = ttk.Label(master=self.frame, text="Here is your budget:")
        amount_text = ttk.Label(master=self.frame, text=f"You have {self.budget.amount} in your budget")
        food_text = ttk.Label(master=self.frame, text=f"You have {self.budget.food} in your food budget")
        transit_text = ttk.Label(master=self.frame, text=f"You have {self.budget.transit} in your transit budget")
        entertainment_text = ttk.Label(master=self.frame, text=f"You have {self.budget.entertainment} in your entertainment budget")
        living_text = ttk.Label(master=self.frame, text=f"You have {self.budget.living} in your living budget")
        utilities_text = ttk.Label(master=self.frame, text=f"You have {self.budget.utilities} in your utilities budget")
        insurance_text = ttk.Label(master=self.frame, text=f"You have {self.budget.insurance} in your insurance budget")

        intro_text.grid(padx=5, pady=5)
        amount_text.grid(padx=5, pady=5)
        food_text.grid(padx=5, pady=5)
        transit_text.grid(padx=5, pady=5)
        entertainment_text.grid(padx=5, pady=5)
        living_text.grid(padx=5, pady=5)
        utilities_text.grid(padx=5, pady=5)
        insurance_text.grid(padx=5, pady=5)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)        
        budget_label = ttk.Label(master=self.frame, text = "Here you can view your budget")
        budget_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.show_budget()