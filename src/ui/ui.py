from ui.login import LoginView
from ui.budget_view import BudgetView
from ui.budget_create_view import BudgetCreateView
from ui.budget_choose_view import BudgetChooseView

class UI:
    def __init__(self, root):
        self.root = root
        self.view = None

    def start(self):
        self.show_login()

    def show_login(self):
        self.hide_view()
        self.view = LoginView(self.root, self.show_budget_create_view, self.show_budget_view)
        self.view.pack()

    def show_budget_view(self):
        self.hide_view()
        self.view = BudgetView(self.root)
        self.view.pack()

    def show_budget_create_view(self):
        self.hide_view()
        self.view = BudgetCreateView(self.root, self.choose_budget_view)     
        self.view.pack()   

    def choose_budget_view(self):
        self.hide_view()
        self.view = BudgetChooseView(self.root, self.show_budget_view)

    def hide_view(self):
        if self.view:
            self.view.destroy()

        self.view = None