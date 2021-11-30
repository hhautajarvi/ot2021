from entities.budget import Budget
from database_connection import get_database_connection

class BudgetRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_budget(self, user_id, amount):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Budget (user_id, amount) VALUES (?,?)", (user_id, amount))
        self.connection.commit()
        return Budget(user_id, amount)

    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE from Budget")
        self.connection.commit()


budget_repository = BudgetRepository(get_database_connection())