from tkinter import ttk, constants, StringVar
from services.user_service import user_service
from services.budget_service import budget_service

class BudgetCreateView:
    """Ui-luokka jossa valitaan budjetin kokonaissumma
    """
    def __init__(self, root, choose_budget_view):
        self._root = root
        self._frame = None
        self._choose_budget_view = choose_budget_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _choose_budget_sum(self):
        sum_label = ttk.Label(master=self._frame, text="Enter budget sum:")
        self._budget_sum = ttk.Entry(master=self._frame)
        sum_label.grid(padx=5, pady=5)
        self._budget_sum.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        
        create_button = ttk.Button(master=self._frame, text="Create", command=self._createbutton_click)
        create_button.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable,foreground='red')
        self._error_label.grid(columnspan=2, padx=5, pady=5)
    
        budget_label = ttk.Label(master=self._frame, text = "Here you can make your budget")
        budget_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        exit_button = ttk.Button(master=self._frame, text="Exit", command=self._exit)
        exit_button.grid(row=1, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._choose_budget_sum()

        self._frame.grid_columnconfigure(1, weight=1, minsize=170)
        self._hide_error()

    def _createbutton_click(self):
        sum = self._budget_sum.get()
        try:
            budget_service.create_budget(int(sum))
            self._choose_budget_view()
        except:
            self._show_error('The amount should be entered in numbers')

    def _exit(self):
        user_service.exit()
        