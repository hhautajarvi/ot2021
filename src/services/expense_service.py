from entities.expense import Expense
from repositories.expense_repository import expense_repository as default_expense_repository
from services.user_service import user_service

class ExpenseService:
    """Kuluihin liittyvästä sovelluslogiikasta vastaava luokka
    """
    def __init__(self, expense_repository=default_expense_repository):
        """Luokan konstruktori

        Args:
            expense_repository (optional): Olio, jolla on ExpenseRepository-luokkaa vastaavat \
                metodit. Defaults to default_expense_repository.
        """
        self._expense_repository = expense_repository

    def create_expense(self, amount, category, comment, datenow):
        """Luo uuden kulun

        Args:
            amount (int): Kulun summa
            category (int): Kulun kategoria
                (1=food, 2=transit, 3=entertainment, 4=living, 5=utilities, 6=insurance)
            comment (str): Kommentti kulusta
            datenow (date): kulun päivämäärä
        """
        user_id = user_service.show_id()
        new_expense = Expense(user_id, amount, category, comment, datenow)
        user_service.add_expense(new_expense)
        self._expense_repository.create_expense(user_id, \
            amount, category, comment, datenow)

expense_service = ExpenseService()
