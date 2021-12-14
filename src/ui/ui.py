from ui.login import LoginView
from ui.budget_view import BudgetView
from ui.budget_create_view import BudgetCreateView
from ui.budget_choose_view import BudgetChooseView
from ui.add_expense_view import AddExpenseView

class UI:
    def __init__(self, root):
        self._root = root
        self._view = None

    def start(self):
        self._show_login()

    def _show_login(self):
        self._hide_view()
        self._view = LoginView(self._root, self._show_budget_create_view, self._show_budget_view)
        self._view.pack()

    def _show_budget_view(self):
        self._hide_view()
        self._view = BudgetView(self._root, self._show_add_expense_view)
        self._view.pack()

    def _show_budget_create_view(self):
        self._hide_view()
        self._view = BudgetCreateView(self._root, self._choose_budget_view)     
        self._view.pack()   

    def _choose_budget_view(self):
        self._hide_view()
        self._view = BudgetChooseView(self._root, self._show_budget_view)
        self._view.pack()

    def _show_add_expense_view(self):
        self._hide_view()
        self._view = AddExpenseView(self._root, self._show_budget_view)
        self._view.pack()

    def _hide_view(self):
        if self._view:
            self._view.destroy()

        self._view = None