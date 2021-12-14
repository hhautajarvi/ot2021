from entities.expense import Expense
from database_connection import get_database_connection

class ExpenseRepository:
    """Expense-luokkaan liittyvistä tietokantaoperaatioista vastaava luokka
    """
    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden Connection-olio
        """
        self.connection = connection

    def create_expense(self, user_id, amount, category, comment, date):
        """Luo uuden kulun tietokantaan käyttäjän antamilla tiedoilla

        Args:
            user_id (int): Käyttäjän tunnistenumero
            amount (int): Kulun summa
            category (int): Kulun kategoria
                (1=food, 2=transit, 3=entertainment, 4=living, 5=utilities, 6=insurance)
            comment (str): Kommentti kulusta
            date (str/date): Kulun päivämäärä jolloin se on syötetty

        Returns:
            Palauttaa Expense-luokan olion
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Expense (user_id, amount, category, comment, date)" \
            " VALUES (?,?,?,?,?)", (user_id, amount, category, comment, date))
        self.connection.commit()
        return Expense(user_id, amount, category, comment, date)

    def find_user_expenses(self, user_id):
        """Hakee valitun käyttäjän kulut tietokannasta

        Args:
            user_id (int): käyttäjän tunnistenumero

        Returns:
            palauttaa kulujen tiedot listana
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Expense WHERE user_id=?", (user_id, ))
        expenses = cursor.fetchall()
        return expenses

    def delete_all(self):
        """Poistaa kaikki kulut tietokannasta
        """
        cursor = self.connection.cursor()
        cursor.execute("DELETE from Expense")
        self.connection.commit()

expense_repository = ExpenseRepository(get_database_connection())
