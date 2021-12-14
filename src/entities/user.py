class User:
    """Luokka joka pitää kirjaa käyttäjän tiedoista

    Attributes:
        user_id: käyttäjän tunnistenumero
        username: käyttäjänimi
        password: salasana
        budget: käyttäjän käytössä oleva budjettiolio
        expenselist: käyttäjän kulut listassa
        expenses_categorized: käyttäjän kulut kategorisoituna listassa
    """
    def __init__(self, user_id, username, password):
        """Luokan konstruktori joka luo käyttäjän tiedot

        Args:
            user_id (int): käyttäjän tunnistenumero
            username (str): käyttäjänimi
            password (str): salasana
        """
        self.user_id = user_id
        self.username = username
        self.password = password
        self.budget = None
        self.expenselist = []
        self.expenses_categorized = [0, 0, 0, 0, 0, 0, 0]
        #0= total 1=food, 2=transit, 3=entertainment, 4=living, 5=utilities, 6=insurance

    def add_expense(self, expense):
        """Lisää kulun käyttäjän kululistoihin

        Args:
            expense: expense-luokan olio
        """
        self.expenses_categorized[expense.category] += expense.amount
        self.expenses_categorized[0] += expense.amount
        self.expenselist.append(expense)
