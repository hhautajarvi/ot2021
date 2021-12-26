from entities.budget import Budget
from repositories.budget_repository import budget_repository as default_budget_repository
from services.user_service import user_service

class BudgetService:
    """Budjettiin liittyvästä sovelluslogiikasta vastaava luokka
    """
    def __init__(self, budget_repository= default_budget_repository):
        """Luokan konstruktori

        Args:
            budget_repository (optional): Olio, jolla on BudgetRepository-luokkaa vastaavat \
                metodit. Defaults to default_budget_repository.
        """
        self._budget = None
        self._budget_repository = budget_repository
        self._budget_modify = False
        self._user_id = None

    def create_budget(self, amount):
        """Luo uuden budjetin

        Args:
            amount (int): budjetin kokonaissumma
        """
        self._user_id = user_service.show_id()
        self._budget = self._budget_repository.create_budget(self._user_id, amount)

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
        budget = self._budget_repository.select_budget(self._user_id)
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
        self._budget_repository.modify_budget(self._user_id, food, transit,\
            entertainment, living, utilities, insurance)

    def check_budget(self):
        """Tarkastaa onko käyttäjä tehnyt budjetin itselleen

        Returns:
            boolean: onko budjetti tehty vai ei
        """
        self._user_id = user_service.show_id()
        budget_exist = self._budget_repository.select_budget(self._user_id)
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

    def budget_logout(self):
        """Kirjaa myös käyttäjän budjetin ulos
        """
        self._budget = None
        self._budget_modify = False


budget_service = BudgetService()