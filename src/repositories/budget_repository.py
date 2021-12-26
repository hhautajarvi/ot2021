from entities.budget import Budget
from database_connection import get_database_connection

class BudgetRepository:
    """Budget-luokkaan liittyvistä tietokantaoperaatioista vastaava luokka
    """
    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden Connection-olio
        """
        self.connection = connection

    def create_budget(self, user_id, amount):
        """Luo uuden käyttäjälle uuden budjetin tietokantaan valitulla summalla

        Args:
            user_id (int): käyttäjän tunnistenumero
            amount (int): budjetin kokonaissumma

        Returns:
            Palauttaa Budget-luokan olion
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Budget (user_id, amount, food, transit, entertainment, living,\
            utilities, insurance) VALUES (?,?,?,?,?,?,?,?)", (user_id, amount, 0, 0, 0, 0, 0, 0))
        self.connection.commit()
        return Budget(user_id, amount)

    def modify_budget(self, user_id, food, transit, entertainment, living, utilities, insurance):
        """Muokkaa budjettia lisäämäällä siihen kategorioiden valitut summat

        Args:
            user_id (int): Käyttäjän tunnistenumero
            food (int): food-kategorian summa.
            transit (int): transit-kategorian summa.
            entertainment (int): entertainment-kategorian summa.
            living (int): living-kategorian summa.
            utilities (int): utilities-kategorian summa.
            insurance (int): insurance-kategorian summa.
        """
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Budget SET food=?, transit=?, entertainment=?, living=?," \
            "utilities=?, insurance=? WHERE user_id=?", \
                (food, transit, entertainment, living, utilities, insurance, user_id))
        self.connection.commit()

    def select_budget(self, user_id):
        """Valitsee halutun käyttäjän budjetin

        Args:
            user_id (int): käyttäjän tunnistenumero

        Returns:
            Palauttaa budjetin tiedot tuplena tai 'None' jos haluttua budjettia ei löydy
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Budget WHERE user_id=?", (user_id, ))
        budget = cursor.fetchone()
        if budget is None:
            return None
        return budget

    def delete_all(self):
        """Poistaa kaikki budjetit tietokannasta
        """
        cursor = self.connection.cursor()
        cursor.execute("DELETE from Budget")
        self.connection.commit()


budget_repository = BudgetRepository(get_database_connection())
