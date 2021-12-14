# Arkkitehtuurikuvaus

## Rakenne

Kuvassa on esitelty koodin pakkausrakenne ja luokat. Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria.

![Luokkakaavio](./kuvat/luokkakaavio.jpg)

Pakkaus Ui sisältää käyttöliittymästä vastavaa koodin, services sovelluslogiikan ja repositories tietokantatoiminnoista vastavan koodin. Pakkaus entities sisältää taas luokkia jotka kuvaavat ohjelman tietokohteita.


Services-luokan UserServices mahdollisesti pilkotaan User-, Budget- ja Expense-service luokkiin.

## Käyttöliittymä

Käyttöliittymässä on kuusi erillistä näkymää:

* Kirjautuminen ja rekisteröinti
* Budjetin summan valinta
* Budjetin kategorioiden summien valinta
* Budjetin tarkastelu
* Kulun lisäys
* Budjetin graafinen tarkastelu

Nämä on toteutettu omina luokkinaan ja näistä jokainen on yksi kerrallaan näkyvillä. Ainoastaan budjetin graafinen tarkastelu aukeaa erilliseen ikkunaan, joka pitää sulkea päästäkseen takaisin budjetin tarkastelun näkymään. Näkyminen näyttämisestä vastaa UI-luokka. Käyttöliittymä on pyritty eristämään sovelluslogiikasta ja se vain kutsuu UserService-luokan metodeja.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat User, Budget ja Expense, jotka kuvaavat käyttäjiä ja heidän tekemiä budjetteja ja niihin liittyviä sovellukseen syötettyjä kuluja.

Sovelluksen toimintalogiikasta vastaa UserService-luokan olio joka tarjoaa kaikille käyttöliittymän toiminnoille omat metodit. Näitä ovat esimerkiksi:
* create_new_user(username, password)
* create_budget(amount)
* find_expenses()

UserService pääsee myös käsiksi tietokantoihin liittyviin BudgetRepository, ExpenseRepository ja UserRepository -luokkiin, jotka annetaan UserService-luokalle konstruktorikutsun yhteydessä. Näin sovelluslogiikka voi hoitaa käyttäjiin, budjetteihin ja kuluihin liittyvien tietojen tallennuksen.

## Toiminnallisuudet

Kuvassa on esitetty käyttäjän rekisteröinnin sekvenssikaavio

![Rekisteröinti](./kuvat/register_sequence.png)