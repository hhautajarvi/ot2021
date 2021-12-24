from tkinter import ttk, constants, IntVar, StringVar
from services.user_service import user_service

class BudgetChooseView:
    def __init__(self, root, show_budget_view):
        self._root = root
        self._frame = None
        self._show_budget_view = show_budget_view
        self._food = IntVar()
        self._transit = IntVar()
        self._entertainment = IntVar()
        self._living = IntVar()
        self._utilities = IntVar()
        self._insurance = IntVar()
        self._food.trace_add("write", self.calculate_sum)
        self._transit.trace_add("write", self.calculate_sum)
        self._entertainment.trace_add("write", self.calculate_sum)
        self._living.trace_add("write", self.calculate_sum)
        self._utilities.trace_add("write", self.calculate_sum)
        self._insurance.trace_add("write", self.calculate_sum)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _view_remaining(self):
        self._remaining = user_service.show_remaining()
        remaining_label = ttk.Label(master=self._frame, text="You have total of in your budget: ")
        remaining_sum_label = ttk.Label(master=self._frame, text=f"{self._remaining}")
        self._result_label = ttk.Label(master=self._frame, text=self._food.get() + self._transit.get() + self._entertainment.get() \
            + self._living.get() + self._utilities.get() + self._insurance.get())
        money_label = ttk.Label(master=self._frame, text="You have left in your budget: ")
        remaining_label.grid(padx=5, pady=5)
        remaining_sum_label.grid(row=2, column=2, sticky=(constants.E, constants.W), padx=5, pady=5) 
        money_label.grid(padx=5, pady=5)
        self._result_label.grid(row=3, column=2, sticky=(constants.E, constants.W), padx=5, pady=5) 

    def _choose_food(self):
        food_label = ttk.Label(master=self._frame, text="Choose food budget:")
        self._food_sum = ttk.Entry(master=self._frame, textvariable=self._food)
        food_label.grid(padx=5, pady=5)
        self._food_sum.grid(row=4, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)     

    def _choose_transit(self):
        transit_label = ttk.Label(master=self._frame, text="Choose transit budget:")
        self._transit_sum = ttk.Entry(master=self._frame, textvariable=self._transit)
        transit_label.grid(padx=5, pady=5)
        self._transit_sum.grid(row=5, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _choose_entertainment(self):
        entertainment_label = ttk.Label(master=self._frame, text="Choose entertainment budget:")
        self._entertainment_sum = ttk.Entry(master=self._frame, textvariable=self._entertainment)
        entertainment_label.grid(padx=5, pady=5)
        self._entertainment_sum.grid(row=6, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
 
    def _choose_living(self):
        living_label = ttk.Label(master=self._frame, text="Choose living budget:")
        self._living_sum = ttk.Entry(master=self._frame, textvariable=self._living)
        living_label.grid(padx=5, pady=5)
        self._living_sum.grid(row=7, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _choose_utilities(self):
        utilities_label = ttk.Label(master=self._frame, text="Choose utilities budget:")
        self._utilities_sum = ttk.Entry(master=self._frame, textvariable=self._utilities)
        utilities_label.grid(padx=5, pady=5)
        self._utilities_sum.grid(row=8, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _choose_insurance(self):
        insurance_label = ttk.Label(master=self._frame, text="Choose insurance budget:")
        self._insurance_sum = ttk.Entry(master=self._frame, textvariable=self._insurance)
        insurance_label.grid(padx=5, pady=5)
        self._insurance_sum.grid(row=9, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)        

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable,foreground='red')
        self._error_label.grid(padx=5, pady=5)

        budget_label = ttk.Label(master=self._frame, text="Here you can choose your budget")
        budget_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        exit_button = ttk.Button(master=self._frame, text="Exit", command=self._exit)
        exit_button.grid(row=1, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._view_remaining()
        self._choose_food()
        self._choose_transit()
        self._choose_entertainment()
        self._choose_living()
        self._choose_utilities()
        self._choose_insurance()
        
        create_button = ttk.Button(master=self._frame, text="Create", command=self._createbutton_click)
        create_button.grid(row=10, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        
        self._frame.grid_columnconfigure(1, weight=1, minsize=170)
        self._hide_error()

    def _createbutton_click(self):
        try:
            food = int(self._food_sum.get())
            transit = int(self._transit_sum.get())
            entertainment = int(self._entertainment_sum.get())
            living = int(self._living_sum.get())
            utilities = int(self._utilities_sum.get())
            insurance = int(self._insurance_sum.get())
        except:
            self._show_error(f"The amounts should be entered in numbers")
            return
        amount = food + transit + entertainment + living + utilities + insurance
        if self._remaining >= amount:
            user_service.modify_budget(food, transit, entertainment, living, utilities, insurance)
            self._show_budget_view()
        else:
            self.destroy()
            self._initialize()
            self.pack()
            self._show_error(f"The sum of the categories should be under the total budget")

    def calculate_sum(self, *args):
        try:
            food = self._food.get()
        except:
            food = 0
        try:
            transit = self._transit.get()
        except:
            transit = 0
        try:
            entertainment = self._entertainment.get()
        except:
            entertainment = 0
        try:
            living = self._living.get()
        except:
            living = 0
        try:
            utilities = self._utilities.get()
        except:
            utilities = 0
        try:
            insurance = self._insurance.get()
        except:
            insurance = 0
        self._result_label['text'] = self._remaining - (food + transit + entertainment + living + utilities + insurance)

    def _exit(self):
        user_service.exit()
        