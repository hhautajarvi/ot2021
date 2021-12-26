from tkinter import Radiobutton, ttk, constants, IntVar, StringVar
from services.user_service import user_service
from services.expense_service import expense_service
from tkcalendar import DateEntry
from datetime import date

class AddExpenseView:
    """Ui-luokka jonka avulla tehdään uusi kulu
    """
    def __init__(self, root, show_budget_view):
        self._root = root
        self._frame = None
        self._show_budget_view = show_budget_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _enter_amount(self):
        amount_label = ttk.Label(master=self._frame, text="Enter expense amount:")
        self._amount_sum = ttk.Entry(master=self._frame)
        amount_label.grid(padx=5, pady=5)
        self._amount_sum.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)  

    def _choose_category(self):
        category_label = ttk.Label(master=self._frame, text="Choose category")
        self._category = IntVar(value= 1)
        
        food_button = Radiobutton(master=self._frame, text="Food", variable=self._category, value=1)
        transit_button = Radiobutton(master=self._frame, text="Transit", variable=self._category, value=2)
        entertainment_button = Radiobutton(master=self._frame, text="Entertainment", variable=self._category, value=3)
        living_button = Radiobutton(master=self._frame, text="Living", variable=self._category, value=4)
        utilities_button = Radiobutton(master=self._frame, text="Utilities", variable=self._category, value=5)
        insurance_button = Radiobutton(master=self._frame, text="Insurance", variable=self._category, value=6)
        
        category_label.grid(padx=5, pady=5)
        food_button.grid(padx=5, pady=5)
        transit_button.grid(padx=5, pady=5)
        entertainment_button.grid(padx=5, pady=5)
        living_button.grid(padx=5, pady=5)
        utilities_button.grid(padx=5, pady=5)
        insurance_button.grid(padx=5, pady=5)

    def _write_comment(self):
        comment_label = ttk.Label(master=self._frame, text="Write a comment of the expense:")
        self._comment = ttk.Entry(master=self._frame)
        comment_label.grid(padx=5, pady=5)
        self._comment.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _choose_date(self):
        date_label = ttk.Label(master=self._frame, text="Choose a date for the expense:")
        self._calendar = DateEntry(master=self._frame)
        self._calendar.set_date(date.today())
        date_label.grid(padx=5, pady=5)
        self._calendar.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

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

        budget_label = ttk.Label(master=self._frame, text="Enter a new expense")
        budget_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        exit_button = ttk.Button(master=self._frame, text="Exit", command=self._exit)
        exit_button.grid(row=1, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._enter_amount()
        self._write_comment()
        self._choose_date()
        self._choose_category()

        add_button = ttk.Button(master=self._frame, text="Add", command=self._addbutton_click)
        add_button.grid(padx=5, pady=5)
        
        self._frame.grid_columnconfigure(1, weight=1, minsize=170)
        self._hide_error()

    def _addbutton_click(self):
        try:
            amount = int(self._amount_sum.get())
        except:
            self._show_error(f"Amount is required in numbers")
            return
        comment = self._comment.get()
        calendar = self._calendar.get_date()
        datenow = calendar.isoformat()
        if len(comment) > 50:
            self._show_error(f"Comment too long, max length is 50 characters")
            return
        category = int(self._category.get())
        expense_service.create_expense(amount, category, comment, datenow)
        self._show_budget_view()

    def _exit(self):
        user_service.exit()
        