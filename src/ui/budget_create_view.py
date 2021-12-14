from tkinter import ttk, constants
from services.user_service import user_service

class BudgetCreateView:
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
        self._budget_sum.grid(row=1, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        
        create_button = ttk.Button(master=self._frame, text="Create", command=self.createbutton_click)
        create_button.grid(row=2, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)        
        budget_label = ttk.Label(master=self._frame, text = "Here you can make your budget")
        budget_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self._choose_budget_sum()

    def createbutton_click(self):
        sum = self._budget_sum.get()
        user_service.create_budget(int(sum))
        self._choose_budget_view()

