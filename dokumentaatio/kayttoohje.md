# Käyttöohje

Ohjelma käyttää Poetrya.

Ohjelman suorituksen vaiheet:

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


Muut toiminnot virtuaaliympäristössä:

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
