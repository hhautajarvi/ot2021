from tkinter import ttk, constants
from ui.plotting.plot_view import PlotView
from services.user_service import user_service
from datetime import date

class BudgetView:
    def __init__(self, root, add_expense_view, login_view, choose_budget):
        self._root = root
        self._frame = None
        self._budget = user_service.show_budget()
        self._expenselist, self._expenses_categorized = user_service.return_expenses()
        self._add_expense_view = add_expense_view
        self._login_view = login_view
        self._choose_budget_view = choose_budget
        self._month = date.today().month
        self._year = date.today().year

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_budget(self):
        month_text = ttk.Label(master=self._frame, text=f"Month/year: {self._month}/{self._year}")
        intro_text = ttk.Label(master=self._frame, text="Your original budget:")
        budget_text = ttk.Label(master=self._frame, text="This months expenditures:")

        amount_text = ttk.Label(master=self._frame, text="Total budget:")
        total_amount_text = ttk.Label(master=self._frame, text=f"{self._budget.amount}")
        used_amount_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[(self._month, self._year)][0]}")

        food_text = ttk.Label(master=self._frame, text="Food budget:")
        total_food_text = ttk.Label(master=self._frame, text=f"{self._budget.food}")
        used_food_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[(self._month, self._year)][1]}")

        transit_text = ttk.Label(master=self._frame, text="Transit budget:")
        total_transit_text = ttk.Label(master=self._frame, text=f"{self._budget.transit}")
        used_transit_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[(self._month, self._year)][2]}")  

        entertainment_text = ttk.Label(master=self._frame, text="Entertainment budget:")
        total_entertainment_text = ttk.Label(master=self._frame, text=f"{self._budget.entertainment}")
        used_entertainment_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[(self._month, self._year)][3]}")

        living_text = ttk.Label(master=self._frame, text="Living budget:")
        total_living_text = ttk.Label(master=self._frame, text=f"{self._budget.living}")
        used_living_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[(self._month, self._year)][4]}")   

        utilities_text = ttk.Label(master=self._frame, text="Utilities budget:")
        total_utilities_text = ttk.Label(master=self._frame, text=f"{self._budget.utilities}")
        used_utilities_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[(self._month, self._year)][5]}")   

        insurance_text = ttk.Label(master=self._frame, text="Insurance budget:")
        total_insurance_text = ttk.Label(master=self._frame, text=f"{self._budget.insurance}")
        used_insurance_text = ttk.Label(master=self._frame, text=f"{self._expenses_categorized[(self._month, self._year)][6]}")    

        month_text.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
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
        expense_label = ttk.Label(master=self._frame, text= "Your past expenses")
        expense_label.grid(column=1, padx=5, pady=5)
        category_number = 1
        for list in self._expenselist[1:]:
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
            cat_name_label = ttk.Label(master=self._frame, text=f"{category_name} costs:")
            cat_name_label.grid(column=0, padx=5, pady=5)
            category_number += 1
            for expense in list:
                expense_date = date.fromisoformat(expense.date)
                if expense_date.month == self._month and expense_date.year == self._year:         
                    newexpense_label = ttk.Label(master=self._frame, text=f"{expense.amount} " \
                        f"euros in {expense.date}, comment: {expense.comment}")
                    newexpense_label.grid(column=1, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        previous_month_button = ttk.Button(master=self._frame, text="Previous month", command=self._previous_month_click)
        previous_month_button.grid(row=0, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        
        next_month_button = ttk.Button(master=self._frame, text="Next month", command=self._next_month_click)
        next_month_button.grid(row=0, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        logout_button = ttk.Button(master=self._frame, text="Logout", command=self._logout_click)
        logout_button.grid(row=0, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        exit_button = ttk.Button(master=self._frame, text="Exit", command=self._exit)
        exit_button.grid(row=0, column=3, sticky=(constants.E, constants.W), padx=5, pady=5)

        user_service.month_check(self._month, self._year)
        self._show_budget()
        self._show_expenses()
        plots = PlotView(self._frame, self._month, self._year)
        plots.plot()

        modify_budget_button = ttk.Button(master=self._frame, text="Modify budget", command=self._modify_budget_click)
        modify_budget_button.grid(row=9, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        add_expense_button = ttk.Button(master=self._frame, text="Add a new expense", command=self._add_expense_view)
        add_expense_button.grid(row=9, column=1, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

    def _logout_click(self):
        user_service.logout()
        self._login_view()

    def _exit(self):
        user_service.exit()
        
    def _previous_month_click(self):
        if self._month == 1:
            self._month = 12
            self._year -= 1
        else:
            self._month -= 1
        self.destroy()
        self._initialize()
        self.pack()

    def _next_month_click(self):
        if self._month == 12:
            self._month = 1
            self._year += 1
        else:
            self._month += 1
        self.destroy()
        self._initialize()
        self.pack()

    def _modify_budget_click(self):
        user_service.modify_on()
        self._choose_budget_view()
