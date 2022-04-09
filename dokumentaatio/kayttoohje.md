# Käyttöohje

Ohjelma käyttää Poetrya.

## Ohjelman suorituksen vaiheet:

1.  Asenna riippuvuudet

```bash
poetry install
```

2. Siirry virtuaaliympäristöön

```bash
poetry shell
```

3. Suorita ohjelma

```bash
python3 src/mazegen.py
```
## Ohjelman käyttö

Ohjelma pyytää komentorivillä kahta syötettä: labyrintin korkeutta ja leveyttä. Syötteen tulee olla jokin kokonaisluku siten että kumpikaan ei ole 1 ja labyrintti on vähintään kokoa 2x2. Näiden jälkeen ohjelma kysyy järjestyksessä haluatko visualisoida algoritmien toiminnan. Syöttämällä 1 visualisointi aukeaa Pygame-ikkunassa ja syöttämällä 2 visualisointi ohitetaan. Visualisoinnin pyöriessä painamalla ylöspäin-nuolinäppäintä visualisointia voi nopeuttaa korkeintaan viisinkertaiseksi.

## Muut toiminnot virtuaaliympäristössä:

Testit:

```bash
pytest src
```

Pylint:

```bash
pylint src
```

Coverage testikattavuus:

```bash
coverage run --branch -m pytest src; coverage report -m
```
