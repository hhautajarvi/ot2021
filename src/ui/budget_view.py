from tkinter import ttk, constants
from services.user_service import user_service

class BudgetView:
    def __init__(self, root, add_expense_view):
        self.root = root       
        self.frame = None
        self.budget = user_service.show_budget()
        self.expenselist, self.expenses_categorized = user_service.return_expenses()
        self.add_expense_view = add_expense_view

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def show_budget(self):
        intro_text = ttk.Label(master=self.frame, text="Here is your original budget:")
        budget_text = ttk.Label(master=self.frame, text="What you have used so far:")
        amount_text = ttk.Label(master=self.frame, text="Total budget:")
        total_amount_text = ttk.Label(master=self.frame, text=f"{self.budget.amount}")
        used_amount_text = ttk.Label(master=self.frame, text=f"{self.expenses_categorized[0]}")
        food_text = ttk.Label(master=self.frame, text="Food budget:")
        total_food_text = ttk.Label(master=self.frame, text=f"{self.budget.food}")
        used_food_text = ttk.Label(master=self.frame, text=f"{self.expenses_categorized[1]}")
        transit_text = ttk.Label(master=self.frame, text="Transit budget:")
        total_transit_text = ttk.Label(master=self.frame, text=f"{self.budget.transit}")
        used_transit_text = ttk.Label(master=self.frame, text=f"{self.expenses_categorized[2]}")        
        entertainment_text = ttk.Label(master=self.frame, text="Entertainment budget:")
        total_entertainment_text = ttk.Label(master=self.frame, text=f"{self.budget.entertainment}")
        used_entertainment_text = ttk.Label(master=self.frame, text=f"{self.expenses_categorized[3]}")    
        living_text = ttk.Label(master=self.frame, text="Living budget:")
        total_living_text = ttk.Label(master=self.frame, text=f"{self.budget.living}")
        used_living_text = ttk.Label(master=self.frame, text=f"{self.expenses_categorized[4]}")    
        utilities_text = ttk.Label(master=self.frame, text="Utilities budget:")
        total_utilities_text = ttk.Label(master=self.frame, text=f"{self.budget.utilities}")
        used_utilities_text = ttk.Label(master=self.frame, text=f"{self.expenses_categorized[5]}")    
        insurance_text = ttk.Label(master=self.frame, text="Insurance budget:")
        total_insurance_text = ttk.Label(master=self.frame, text=f"{self.budget.insurance}")
        used_insurance_text = ttk.Label(master=self.frame, text=f"{self.expenses_categorized[6]}")    

        intro_text.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        budget_text.grid(row=1, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        amount_text.grid(padx=5, pady=5)
        total_amount_text.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        used_amount_text.grid(row=2, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        food_text.grid(padx=5, pady=5)
        total_food_text.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        used_food_text.grid(row=3, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        transit_text.grid(padx=5, pady=5)
        total_transit_text.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        used_transit_text.grid(row=4, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        entertainment_text.grid(padx=5, pady=5)
        total_entertainment_text.grid(row=5, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        used_entertainment_text.grid(row=5, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        living_text.grid(padx=5, pady=5)
        total_living_text.grid(row=6, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        used_living_text.grid(row=6, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        utilities_text.grid(padx=5, pady=5)
        total_utilities_text.grid(row=7, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        used_utilities_text.grid(row=7, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        insurance_text.grid(padx=5, pady=5)
        total_insurance_text.grid(row=8, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        used_insurance_text.grid(row=8, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def show_expenses(self):
        expense_label = ttk.Label(master=self.frame, text= "Here are your past expenses")
        expense_label.grid(padx=5, pady=5)
        for expense in self.expenselist:
            category_number = expense.category
            if category_number == 1:
                category_name = "Food"
            elif category_number == 2:
                category_name = "Transit"
            elif category_number == 3:
                category_name = "Entertainment"
            elif category_number == 4:
                category_name = "Living"
            elif category_number == 5:
                category_name = "Utilities"
            elif category_number == 6:
                category_name = "Insurance"
            newexpense_label = ttk.Label(master=self.frame, text=f"{category_name}" \
                f" cost {expense.amount} euros in {expense.date}, comment: {expense.comment}")
            newexpense_label.grid(sticky=(constants.E, constants.W), padx=5, pady=5)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)        
        budget_label = ttk.Label(master=self.frame, text = "Here you can view your budget and add expenses")
        budget_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self.show_budget()
        self.show_expenses()

        add_expense_button = ttk.Button(master=self.frame, text="Add a new expense", command=self.insert_expense_click)
        add_expense_button.grid(padx=5, pady=5)

    def insert_expense_click(self):
        self.add_expense_view()