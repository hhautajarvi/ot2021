from tkinter import ttk, constants
from entities.user import User
from entities.budget import Budget

class BudgetCreateView:
    def __init__(self, root):
        self.root = root
        self.frame = None

        self.initialize()


    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)        
        budget_label = ttk.Label(master=self.frame, text = "Here you can make your budget")
        budget_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)