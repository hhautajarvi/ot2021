# Käyttöohje

Lataa projekti viimeisimmän releasen koodi Assets-osiosta kohdasta Source Code.

## Konfigurointi

Tietokantatiedoston nimen voi halutessaan muuttaa .env-tiedostossa. Tietokanta luodaan automaattisesti data-hakemistoon.


## Ohjelman käynnistys

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Ja alusta tietokanta komennolla:

```bash
poetry run invoke build
```

Ohjelman voi sitten käynnistää komennolla:

```bash
poetry run invoke start
```

## Kirjautuminen ja rekisteröityminen

Sovellus käynnistyy kirjaumis/rekisteröitymisnäkymään. Tässä käyttäjä voi kirjautua jo luodulla käyttäjätunnuksella sisään sovellukseen syöttämällä käyttäjänimen ja salasanan Login-kohtaan ja painamalla 'Login'-painiketta. Tai käyttäjä voi luoda uuden käyttäjän syöttämällä uuden käyttäjänimen ja salasanan 'Make a new user' -kohtaan ja painamalla 'Register'-painiketta.

## Uuden budjetin luominen

Jos käyttäjä loi uuden käyttäjän, hänet siirretään uuden budjetin luomisen tilaan. Samoin jos käyttäjä on luonut jo aikasemmin käyttäjän, mutta ei ole luonut budjettia, hänet siirretään tähän tilaan kirjautuessaan sisään. Ensimmäisessä valintaruudussa käyttäjä syöttää budjetilleen haluamansa kokonaissumman ja painaa 'Create'-painiketta. Näin käyttäjä siirtyy uuteen näkymään valitsemaan summat eri budjetin kategorioille. Tässä valintaruudussa käyttäjä syöttää halumansa summat eri budjetin kategorioille, samalla hän näkee kuinka paljon budjettia on jäljellä. Jos valitun budjetin kokonaissumman ylittää kategorioissa, budjettia ei voi luoda. Kun kategoroiden summat on hyväksyttävästi valittu, budjetin voi luoda painamalla 'Create'-painiketta.

## Budjetin tarkastelu

Kun käyttäjä joko kirjautuu jo luodulla käyttäjällä sisään tai luo budjetin uudella käyttäjällä, käyttäjä siirretään budjetin tarkastelun tilaan. Tässä tilassa käyttäjä näkee luomansa budjetin summat, sekä kirjaamiensa kulujen yhteissummat, sekä kirjatut kulut eriteltynä sekä numeraalisesti että graafisesti. Numeraalisen listauksen alla käyttäjä näkee kategorioittain jaoteltuna syöttämänsä kulut ja niiden tiedot kyseiselle kuukaudelle.

Näytön yläreunassa on 'Previous month' ja 'Next month' -näppäimet joita painamalla käyttäjä voi nähdä edellisen tai seuraavan kuukauden budjettinsa. Alempaa löytyy 'Modify budget' ja 'Add a new expense'-painikeet. 'Modify budget'-painiketta painamalla käyttäjä pääsee samaan tilaan jossa valittiin budjettia luotaessa valittiin kategorioille summat ja nyt käyttäjä voi muokata näitä summia. 'Add a new expense'-painiketta painamalla käyttäjä pääsee tilaan josta käyttäjä voi luoda uuden kulun budjettiin. Yläreunan 'Logout'-painikkeesta käyttäjä voi kirjautua ulos ja palata takaisin kirjautumis- ja rekisteröintinäkymään.

## Uuden kulun luominen

Tässä näkymässä käyttäjä voi luoda toteutuneen kulun budjettiinsa. Käyttäjän pitää syöttää kulun summa 'Enter expense amount'-ruutuun ja valita jokin budjettikategorioista johon kulu liittyy. Käyttäjä voi myös valita haluamansa päivämäärän kululle 'Choose a date for the expense'-kohdasta. Oletuspäivänä on tämä päivä, mutta sen oikealta puolelta pientä nuolta painamalla esille tulee kalenteri josta käyttäjä voi valita jonkin toisen päivämäärän. Halutessaan käyttäjä voi myös kirjoittaa kommentin kulusta. Kulun lisäys onnistuu painamalla 'Add'-näppäintä. Tämän jälkeen käyttäjä palaa takaisin budjetin tarkastelu-näkymään.

## Ohjelmasta poistuminen

Ohjelmasta voi poistua joka ruudulta painamalla oikean yläkulman 'Exit'-näppäintä.