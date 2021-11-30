from tkinter import StringVar, ttk, constants
from services.user_service import user_service

class BudgetCreateView:
    def __init__(self, root, choose_budget_view):
        self.root = root
        self.frame = None
        self.choose_budget_view = choose_budget_view

        self.initialize()


    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def choose_budget_sum(self):
        sum_label = ttk.Label(master=self.frame, text="Enter budget sum:")
        self.budget_sum = ttk.Entry(master=self.frame)
        sum_label.grid(padx=5, pady=5)
        self.budget_sum.grid(row=1, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        
        create_button = ttk.Button(master=self.frame, text="Create", command=self.createbutton_click)
        create_button.grid(row=2, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)        
        budget_label = ttk.Label(master=self.frame, text = "Here you can make your budget")
        budget_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.choose_budget_sum()

    def createbutton_click(self):
        sum = self.budget_sum.get()
        user_service.create_budget(sum)
        self.choose_budget_view()

