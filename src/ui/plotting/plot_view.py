import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import constants
import numpy as np
from services.user_service import user_service

class PlotView:
    def __init__(self, root, month, year):
        self._frame = root
        self._budget = user_service.show_budget()
        self._expenselist, self._expenses_categorized = user_service.return_expenses()
        self._month = month
        self._year = year

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def plot(self):
        budgetlist = [self._budget.amount, self._budget.food, self._budget.transit, \
             self._budget.entertainment, self._budget.living, self._budget.utilities, self._budget.insurance]
        
        self._fig = plt.figure(figsize=(7, 7), dpi=100)
        ind = np.arange(len(budgetlist)) 
        width = 0.35       
        plt.bar(ind, budgetlist, width, label='Budgeted')
        plt.bar(ind + width, self._expenses_categorized[(self._month, self._year)], width, label='Spent')
        plt.ylabel('Amount')
        plt.title("Budgeted expenses versus realized expenses")
        plt.xticks(ind + width / 2, ('total', 'food', 'transit', 'entertainment', 'living', 'utilities', 'insurance'))
        plt.legend(loc='best')

        canvas = FigureCanvasTkAgg(self._fig, master=self._frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1,rowspan=20,sticky=(constants.E, constants.W), column=3, columnspan=2, ipadx=5, ipady=5)

    def close(self):
        plt.close('all')