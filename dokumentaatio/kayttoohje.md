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

Ohjelma pyytää komentorivillä kahta syötettä: labyrintin korkeutta ja leveyttä. Syötteen tulee olla jokin kokonaisluku siten että kumpikaan ei ole 1 ja labyrintti on vähintään kokoa 2x2. Näiden jälkeen ohjelma pyytää käyttäjää valitsemaan toiminnon listalta ja kysyy jokaisen algoritmin kohdalla haluaako käyttäjä visualisoida algoritmien toiminnan. Visualisoinnin pyöriessä painamalla ylöspäin-nuolinäppäintä visualisointia voi nopeuttaa korkeintaan viisinkertaiseksi. Kun ainakin yhtä algoritmia on käytetty, niin toiminnoista voi valita labyrinttien vertailun, joka tulostaa tietoa labyrinteista. Kun generoi labyrintin uudestaan samalla algoritmilla, niin edellinen tällä algoritmilla luotu labyrintti korvataan uudella.

Huom. erittäin suurten labyrinttien generoinnissa voi kestää Primin algoritmilla varsin pitkään ja Kruskalin algoritmilla TODELLA pitkään, 100x100 kokoisen labyrintin generoimiseen Kruskalin algoritmilla kesti koneellani 21 sekuntia.
Suuria labyrintteja ei myöskään välttämättä kannata visualisoida sillä Pygame-ikkuna skaalantuu labyrintin koon mukaan.

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
