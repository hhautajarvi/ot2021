from entities.expense import Expense
from database_connection import get_database_connection

class ExpenseRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_expense(self, user_id, amount, category, comment, date):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Expense (user_id, amount, category, comment, date)" \
            " VALUES (?,?,?,?,?)", (user_id, amount, category, comment, date))
        self.connection.commit()
        return Expense(user_id, amount, category, comment, date)

    def find_user_expenses(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Expense WHERE user_id=?", (user_id, ))
        expenses = cursor.fetchall()
        return expenses

    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE from Expense")
        self.connection.commit()

expense_repository = ExpenseRepository(get_database_connection())
