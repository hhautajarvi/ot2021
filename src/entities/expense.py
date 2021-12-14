class Expense:
    """Luokka joka luo uuden kulun käyttäjän budjettiin

    Attributes:
        user_id: Käyttäjän tunnistenumero
        amount: Kulun summa
        category: Kulun kategoria
            (1=food, 2=transit, 3=entertainment, 4=living, 5=utilities, 6=insurance)
        comment: Kommentti kulusta
        date: Kulun päivämäärä jolloin se on syötetty
    """

    def __init__(self, user_id, amount, category, comment, date):
        """Luokan konstruktori joka luo uuden kulun

        Args:
            user_id (int): Käyttäjän tunnistenumero
            amount (int): Kulun summa
            category (int): Kulun kategoria
                (1=food, 2=transit, 3=entertainment, 4=living, 5=utilities, 6=insurance)
            comment (str): Kommentti kulusta
            date (str/date): Kulun päivämäärä jolloin se on syötetty
        """
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.comment = comment
        self.date = date
