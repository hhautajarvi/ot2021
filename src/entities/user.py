from datetime import date

class User:
    """Luokka joka pitää kirjaa käyttäjän tiedoista

    Attributes:
        user_id: käyttäjän tunnistenumero
        username: käyttäjänimi
        password: salasana
        budget: käyttäjän käytössä oleva budjettiolio
        expenselist: käyttäjän kulut eriteltyinä eri listoihin kategorian \
            mukaan
        expenses_categorized: käyttäjän kulut kategorisoituna sanakirjassa \
            kuukausittain listattuna
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
        self.expenselist = [[],[],[],[],[],[],[]]
        self.expenses_categorized = {}
        #0= total 1=food, 2=transit, 3=entertainment, 4=living, 5=utilities, 6=insurance

    def add_expense(self, expense):
        """Lisää kulun käyttäjän kululistoihin, luo kyseiselle kuukaudelle listan
            jos se ei ole valmiina

        Args:
            expense: expense-luokan olio
        """
        expense_date = date.fromisoformat(expense.date)
        if (expense_date.month, expense_date.year) not in self.expenses_categorized:
            self.expenses_categorized[(expense_date.month, expense_date.year)] = \
                [0, 0, 0, 0, 0, 0, 0]
        self.expenses_categorized[(expense_date.month, expense_date.year)][expense.category] \
             += expense.amount
        self.expenses_categorized[(expense_date.month, expense_date.year)][0] += expense.amount
        self.expenselist[expense.category].append(expense)
