from tkinter import StringVar, ttk, constants

class BudgetChooseView:
    def __init__(self, root, show_budget_view):
        self.show_budget_view = show_budget_view
        self.root = root
        self.frame = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)        
        budget_label = ttk.Label(master=self.frame, text = "Here you can choose your budget")
        budget_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)