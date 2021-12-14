from datetime import date
from entities.budget import Budget
from entities.expense import Expense
from repositories.user_repository import user_repository as default_user_repository
from repositories.budget_repository import budget_repository as default_budget_repository
from repositories.expense_repository import expense_repository as default_expense_repository

class UserService:
    def __init__(self, user_repository=default_user_repository, budget_repository= \
        default_budget_repository, expense_repository=default_expense_repository):
        self._user = None
        self._budget = None
        self._user_repository = user_repository
        self._budget_repository = budget_repository
        self._expense_repository = expense_repository

    def create_new_user(self, username, password):
        usercheck = self._user_repository.find_user(username)

        if usercheck is not None:
            if username == usercheck.username:
                raise Exception
        self._user = self._user_repository.create_user(username, password)
        return self._user

    def login(self, username, password):
        usercheck = self._user_repository.find_user(username)
        if username == usercheck.username and password == usercheck.password:
            self._user = usercheck
            self.find_expenses()
            return self._user
        raise Exception

    def create_budget(self, amount):
        self._budget = self._budget_repository.create_budget(self._user.user_id, amount)

    def show_remaining(self):
        return self._budget.remaining

    def show_budget(self):
        budget = self._budget_repository.select_budget(self._user.user_id)
        self._budget = Budget(budget[1], budget[2], budget[3], budget[4], budget[5], \
            budget[6], budget[7], budget[8])
        return self._budget

    def modify_budget(self, food, transit, entertainment, living, utilities, insurance):
        self._budget_repository.modify_budget(self._user.user_id, food, transit,\
            entertainment, living, utilities, insurance)

    def create_expense(self, amount, category, comment):
        now = date.today()
        datenow = now.isoformat()
        new_expense = Expense(self._user.user_id, amount, category, comment, datenow)
        self._user.add_expense(new_expense)
        self._expense_repository.create_expense(self._user.user_id, \
            amount, category, comment, datenow)

    def find_expenses(self):
        expenses = self._expense_repository.find_user_expenses(self._user.user_id)
        for expense in expenses:
            new_expense = Expense(expense[1], expense[2], expense[3], expense[4], expense[5])
            self._user.add_expense(new_expense)

    def return_expenses(self):
        return self._user.expenselist, self._user.expenses_categorized

user_service = UserService()
