import sys
from entities.expense import Expense
from repositories.user_repository import user_repository as default_user_repository
from repositories.expense_repository import expense_repository as default_expense_repository

class UserService:
    """Käyttäjään liittyvästä sovelluslogiikasta vastaava luokka
    """
    def __init__(self, user_repository=default_user_repository, expense_repository=default_expense_repository):
        """Luokan konstruktori

        Args:
            user_repository (optional): Olio, jolla on UserRepository-luokkaa vastaavat metodit.\
                Defaults to default_user_repository.
            expense_repository (optional): Olio, jolla on ExpenseRepository-luokkaa vastaavat \
                metodit. Defaults to default_expense_repository.
        """
        self._user = None
        self._budget = None
        self._user_repository = user_repository
        self._expense_repository = expense_repository
        self._budget_modify = False

    def create_new_user(self, username, password):
        """Luo uuden käyttäjän

        Args:
            username (str): käyttäjänimi
            password (str): salasana

        Raises:
            Exception: Virhe jos käyttäjänimi on jo käytössä

        Returns:
            Palauttaa luodun käyttäjän User-oliona
        """
        usercheck = self._user_repository.find_user(username)

        if usercheck is not None:
            if username == usercheck.username:
                raise Exception
        self._user = self._user_repository.create_user(username, password)
        return self._user

    def login(self, username, password):
        """Kirjaa käyttäjän sisään

        Args:
            username (str): käyttäjänimi
            password (str): salasana

        Raises:
            Exception: Virhe jos käyttäjänimi ja salasana eivät täsmää

        Returns:
            Palauttaa käyttäjän User-oliona
        """
        usercheck = self._user_repository.find_user(username)
        if username == usercheck.username and password == usercheck.password:
            self._user = usercheck
            self._find_expenses()
            return self._user
        raise Exception

    def _find_expenses(self):
        """Hakee käyttäjän kulut kirjautuessa ja lisää ne User-luokan oliolle
        """
        expenses = self._expense_repository.find_user_expenses(self._user.user_id)
        for expense in expenses:
            new_expense = Expense(expense[1], expense[2], expense[3], expense[4], expense[5])
            user_service.add_expense(new_expense)

    def logout(self):
        """Kirjaa käyttäjän ulos.
        """
        self._user = None

    def exit(self):
        """Lopettaa sovelluksen
        """
        sys.exit()

    def show_id(self):
        """Kertoo käyttäjän id-numeron

        Returns:
            int: käyttäjän id-numero
        """
        return self._user.user_id

    def add_expense(self, expense):
        """Lisää kulun käyttäjän kululistaan

        Args:
            expense: lisättävä kulu
        """
        self._user.add_expense(expense)

    def return_expenses(self):
        """Hakee käyttäjän kulut user-olion listasta

        Returns:
            Palauttaa käyttäjän expenselist ja expenses_categorized -listat
        """
        return self._user.expenselist, self._user.expenses_categorized

    def month_check(self, month, year):
        """Tarkastaa onko haettu kuukausi kululistassa.
        Jos ei ole, luo siihen tyhjän kululistan.

        Args:
            month (int): haettu kuukausi
            year (int): haettu vuosi
        """
        if (month, year) not in self._user.expenses_categorized:
            self._user.expenses_categorized[(month, year)] = [0, 0, 0, 0, 0, 0, 0]

user_service = UserService()
