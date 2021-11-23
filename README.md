# Ohjelmistotuotanto harjoitustyö

Tälle sivulle tulee Helsingin yliopiston ohjelmistotuotanto-kurssin harjoitustyö, sekä laskuharjoitustehtävien vastauksia.

# Budjetointisovellus

Sovelluksen avulla käyttäjät voivat hallinnoida ja suunnitella rahankäyttöään sekä tarkastella tilastoja toteutuneista kuluista.

## Dokumentaatio

[Vaativuusmäärittely](https://github.com/hhautajarvi/ot2021/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/hhautajarvi/ot2021/blob/master/dokumentaatio/tyoaikakirjanpito.md)

## Python versiot

Toimivuus testattu Pythonin versiolla 3.8.10.

## Ohjelman tilanne

Projektissa toimii tällä hetkellä käyttäjän luominen ja kirjautuminen, sekä budjetin luominen.

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Tietokannan alustaminen toimii komennolla:

```bash
poetry run invoke build
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```