from tkinter import StringVar, ttk, constants
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

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)        
        budget_label = ttk.Label(master=self.frame, text="Here you can choose your budget")
        budget_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)


        self.show_remaining()
