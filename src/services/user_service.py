import sys
from entities.budget import Budget
from entities.expense import Expense
from repositories.user_repository import user_repository as default_user_repository
from repositories.budget_repository import budget_repository as default_budget_repository
from repositories.expense_repository import expense_repository as default_expense_repository

class UserService:
    """Sovelluslogiikasta vastaava luokka
    """
    def __init__(self, user_repository=default_user_repository, budget_repository= \
        default_budget_repository, expense_repository=default_expense_repository):
        """Luokan konstruktori

        Args:
            user_repository (optional): Olio, jolla on UserRepository-luokkaa vastaavat metodit.\
                Defaults to default_user_repository.
            budget_repository (optional): Olio, jolla on BudgetRepository-luokkaa vastaavat \
                metodit. Defaults to default_budget_repository.
            expense_repository (optional): Olio, jolla on ExpenseRepository-luokkaa vastaavat \
                metodit. Defaults to default_expense_repository.
        """
        self._user = None
        self._budget = None
        self._user_repository = user_repository
        self._budget_repository = budget_repository
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
            self.find_expenses()
            return self._user
        raise Exception

    def logout(self):
        """Kirjaa käyttäjän ulos.
        """
        self._user = None
        self._budget = None
        self._budget_modify = False

    def exit(self):
        """Lopettaa sovelluksen
        """
        sys.exit()

    def create_budget(self, amount):
        """Luo uuden budjetin

        Args:
            amount (int): budjetin kokonaissumma
        """
        self._budget = self._budget_repository.create_budget(self._user.user_id, amount)

    def show_total(self):
        """Kertoo budjetin kokonaissumman

        Returns:
            Palauttaa budjetin kokonaissumman (int)
        """
        return self._budget.amount

    def show_budget(self):
        """Kertoo käyttäjän budjetin tiedot

        Returns:
            Palauttaa käyttäjän budjetin Budget-oliona
        """
        budget = self._budget_repository.select_budget(self._user.user_id)
        self._budget = Budget(budget[1], budget[2], budget[3], budget[4], budget[5], \
            budget[6], budget[7], budget[8])
        return self._budget

    def modify_budget(self, food, transit, entertainment, living, utilities, insurance):
        """Muokkaa budjettia lisäämäällä siihen kategorioiden valitut summat

        Args:
            food (int): food-kategorian summa.
            transit (int): transit-kategorian summa.
            entertainment (int): entertainment-kategorian summa.
            living (int): living-kategorian summa.
            utilities (int): utilities-kategorian summa.
            insurance (int): insurance-kategorian summa.
        """
        self._budget_repository.modify_budget(self._user.user_id, food, transit,\
            entertainment, living, utilities, insurance)

    def create_expense(self, amount, category, comment, datenow):
        """Luo uuden kulun

        Args:
            amount (int): Kulun summa
            category (int): Kulun kategoria
                (1=food, 2=transit, 3=entertainment, 4=living, 5=utilities, 6=insurance)
            comment (str): Kommentti kulusta
            datenow (date): kulun päivämäärä
        """
        new_expense = Expense(self._user.user_id, amount, category, comment, datenow)
        self._user.add_expense(new_expense)
        self._expense_repository.create_expense(self._user.user_id, \
            amount, category, comment, datenow)

    def find_expenses(self):
        """Hakee käyttäjän kulut ja lisää ne User-luokan oliolle
        """
        expenses = self._expense_repository.find_user_expenses(self._user.user_id)
        for expense in expenses:
            new_expense = Expense(expense[1], expense[2], expense[3], expense[4], expense[5])
            self._user.add_expense(new_expense)

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

    def check_budget(self):
        """Tarkastaa onko käyttäjä tehnyt budjetin itselleen

        Returns:
            boolean: onko budjetti tehty vai ei
        """
        budget_exist = self._budget_repository.select_budget(self._user.user_id)
        if budget_exist is None:
            return False
        return True

    def modify_on(self):
        """Näyttää että budjettia modifioidaan, eikä tehdä ensimmäistä kertaa
        """
        self._budget_modify = True

    def check_modify(self):
        """Kertoo modifioidaanko budjettia, vai tehdäänkö se ensimmäistä kertaa

        Returns:
            boolean: kertoo onko modifiointi päällä
        """
        return self._budget_modify

user_service = UserService()
