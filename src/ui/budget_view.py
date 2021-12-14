from tkinter import ttk, constants
from services.user_service import user_service

class BudgetView:
    def __init__(self, root, add_expense_view):
        self._root = root       
        self._frame = None
        self._budget = user_service.show_budget()
        self._expenselist, self._expenses_categorized = user_service.return_expenses()
        self._add_expense_view = add_expense_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_budget(self):
        intro_text = ttk.Label(master=self._frame, text="Here is your original budget:")
        budget_text = ttk.Label(master=self._frame, text="What you have used so far:")
        amount_text = ttk.Label(master=self._frame, text="Total budget:")
        total_amount_text = ttk.Label(master=self._frame, text=f"{self._budget.amount}")
        used_amount_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[0]}")
        food_text = ttk.Label(master=self._frame, text="Food budget:")
        total_food_text = ttk.Label(master=self._frame, text=f"{self._budget.food}")
        used_food_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[1]}")
        transit_text = ttk.Label(master=self._frame, text="Transit budget:")
        total_transit_text = ttk.Label(master=self._frame, text=f"{self._budget.transit}")
        used_transit_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[2]}")        
        entertainment_text = ttk.Label(master=self._frame, text="Entertainment budget:")
        total_entertainment_text = ttk.Label(master=self._frame, text=f"{self._budget.entertainment}")
        used_entertainment_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[3]}")    
        living_text = ttk.Label(master=self._frame, text="Living budget:")
        total_living_text = ttk.Label(master=self._frame, text=f"{self._budget.living}")
        used_living_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[4]}")    
        utilities_text = ttk.Label(master=self._frame, text="Utilities budget:")
        total_utilities_text = ttk.Label(master=self._frame, text=f"{self._budget.utilities}")
        used_utilities_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[5]}")    
        insurance_text = ttk.Label(master=self._frame, text="Insurance budget:")
        total_insurance_text = ttk.Label(master=self._frame, text=f"{self._budget.insurance}")
        used_insurance_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[6]}")    

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

    def _show_expenses(self):
        expense_label = ttk.Label(master=self._frame, text= "Here are your past expenses")
        expense_label.grid(padx=5, pady=5)
        for expense in self._expenselist:
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
            newexpense_label = ttk.Label(master=self._frame, text=f"{category_name}" \
                f" cost {expense.amount} euros in {expense.date}, comment: {expense.comment}")
            newexpense_label.grid(sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)        
        budget_label = ttk.Label(master=self._frame, text = "Here you can view your budget and add expenses")
        budget_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self._show_budget()
        self._show_expenses()

        add_expense_button = ttk.Button(master=self._frame, text="Add a new expense", command=self._insert_expense_click)
        add_expense_button.grid(padx=5, pady=5)

    def _insert_expense_click(self):
        self._add_expense_view()