import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk, constants
import numpy as np
from services.user_service import user_service

class PlotView:
    def __init__(self, root, budget_view):
        self._root = root
        self._frame = None
        self._budget = user_service.show_budget()
        self._expenselist, self._expenses_categorized = user_service.return_expenses()
        self._budget_view = budget_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _plot(self):
        budgetlist = [self._budget.amount, self._budget.food, self._budget.transit, \
             self._budget.entertainment, self._budget.living, self._budget.utilities, self._budget.insurance]
        
        fig = Figure(figsize=(7,7), dpi=100)

        ind = np.arange(len(budgetlist)) 
        width = 0.35       
        plt.bar(ind, budgetlist, width, label='Budgeted')
        plt.bar(ind + width, self._expenses_categorized, width, label='Spent')
        plt.ylabel('Amount')
        plt.title("Budgeted expenses versus realized expenses")
        plt.xticks(ind + width / 2, ('total', 'food', 'transit', 'entertaiment', 'living', 'utilities', 'insurance'))
        plt.legend(loc='best')
        plt.show()

        canvas = FigureCanvasTkAgg(fig, master=self._frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._plot()
        self.destroy()
        self._budget_view()
        self.pack()
