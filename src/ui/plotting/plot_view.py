import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import constants
import numpy as np
from services.user_service import user_service
from services.budget_service import budget_service

class PlotView:
    """Piirtää kuvaajat BudgetView-luokkaan
    """
    def __init__(self, frame, month, year):
        """Luokan konstruktori

        Args:
            frame: Frame-komponentti johon kuvaajat piirretään
            month (int): haluttu kuukausi joka tiedot piirretään
            year (int): haluttu vuosi joka tiedot piirretään
        """
        self._frame = frame
        self._budget = budget_service.show_budget()
        self._expenselist, self._expenses_categorized = user_service.return_expenses()
        self._month = month
        self._year = year

    def plot(self):
        """Piirtää kuvaajat
        """
        budgetlist = [self._budget.amount, self._budget.food, self._budget.transit, \
             self._budget.entertainment, self._budget.living, self._budget.utilities, self._budget.insurance]
        
        fig = plt.figure(figsize=(7, 7), facecolor='lightgrey')
        ind = np.arange(len(budgetlist)) 
        width = 0.35       
        plt.bar(ind, budgetlist, width, label='Budgeted')
        plt.bar(ind + width, self._expenses_categorized[(self._month, self._year)], width, label='Spent')
        plt.ylabel('Amount')
        plt.title("Budgeted expenses versus realized expenses")
        plt.xticks(ind + width / 2, ('total', 'food', 'transit', 'entertainment', 'living', 'utilities', 'insurance'))
        plt.legend(loc='best')

        canvas = FigureCanvasTkAgg(fig, master=self._frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1,rowspan=20,sticky=(constants.E, constants.W), column=3, columnspan=2, ipadx=5, ipady=5)

    def close(self):
        """Sulkee kuvaajat (ilman tätä kuvaajat jäävät pyörimään mainlooppiin eikä sovellus sulkeudu)
        """
        plt.close('all')