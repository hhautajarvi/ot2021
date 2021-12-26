class Budget:
    """Luokka joka kertoo käyttäjän budjetin tiedot

    Attributes:
        user_id: Käyttäjän tunnistenumero
        amount: Budjetin kokonaissumma
        food, transit, entertainment, living, utilities, insurance: \
            kyseisten kategorioiden summat budjetissa
        used: käytetty määrä budjetin kokonaissummasta
        remaining: jäljellä oleva määrä budjetin kokonaissummasta
    """

    def __init__(self, user_id, amount, food=0, transit=0, entertainment=0, \
        living=0, utilities=0, insurance=0):
        """Luokan konstruktori joka luo uuden budjetin

        Args:
            user_id (int): Käyttäjän tunnistenumero
            amount (int): Budjetin kokonaissumma
            food (int, optional): kyseisen kategorian summa. Defaults to 0.
            transit (int, optional): kyseisen kategorian summa. Defaults to 0.
            entertainment (int, optional): kyseisen kategorian summa. Defaults to 0.
            living (int, optional): kyseisen kategorian summa. Defaults to 0.
            utilities (int, optional): kyseisen kategorian summa. Defaults to 0.
            insurance (int, optional): kyseisen kategorian summa. Defaults to 0.
        """
        self.user_id = user_id
        self.amount = amount
        self.food = food
        self.transit = transit
        self.entertainment = entertainment
        self.living = living
        self.utilities = utilities
        self.insurance = insurance

    @property
    def used(self):
        """Palauttaa budjetissa käytetyn summan

        Returns:
            int: Palauttaa budjetissa käytetyn summan
        """
        return self.food + self.transit + self.entertainment + self.living \
             + self.utilities + self.insurance

    @property
    def remaining(self):
        """Palauttaa budjetissa jäljellä olevan käyttämättömän summan

        Returns:
            int: Palauttaa budjetissa jäljellä olevan käyttämättömän summan
        """
        return self.amount - self.used
