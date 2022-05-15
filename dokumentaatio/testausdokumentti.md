# Testausdokumentti

## Yksikkötestaus

Coveragen tuottama yksikkötestauksen kattavuusraportti:
![alt text](https://github.com/ilrm123/tiralabra-harjoitustyo/blob/main/dokumentaatio/testikattavuus.png?raw=true)

Kattavuudesta on jätetty pois visualisointi, käyttöliittymä ja main-funktio. Kattavuudessa on pieniä aukkoja sillä yksikkötestejä ei ole aivan jokaiselle erilaiselle tapaukselle, jonka seurauksena muutamassa eri if-haarautumassa ei käydä yksikkötestauksessa lainkaan. 

Yksikkötestejä on 13. Testeissä 1-9 testataan onko luodun verkon solmut yhdistetty kaarilla oikeisiin solmuihin, testeissä 10-12 testataan käykö satunnaistettu syvyyshakualgoritmi kaikissa solmuissa, käykö satunnaistettu Primin algoritmi kaikissa solmuissa ja käykö satunnaistettu Kruskalin algoritmi kaikissa solmuissa, ja viimeinen on testi testaa get_stats funktiota joka palauttaa umpikujien yms. määrän.

Yksikkötestit viimeistä testiä lukuunottamatta tehtiin syötteillä 3 ja 4, eli luotu labyrintti on erittäin pieni, mutta soveltuu kuitenkin näiden testien tarkoitukseen. Viimeisessä testissä on käytetty erikseen luotua listaa.

Yksikkötestit voidaan suorittaa virtuaaliympäristössä seuraavalla komennolla:

```bash
pytest src
```

## Suorituskyky

Suorituskykytestausta ei ole varsinaisesti omana eriytettynä testauksenaan mutta suorituskykyä voi testailla suorittamalla itse ohjelmaa. Labyrinttien luominen erikokoisilla syötteillä antaa seuraavanlaisia tuloksia:

### 50x50

Satunnaistettu syvyyshaku: 0.005 sekuntia
Primin algoritmi: 0.065 sekuntia
Kruskalin algoritmi: 1.259 sekuntia

### 100x100

Satunnaistettu syvyyshaku: 0.019 sekuntia
Primin algoritmi: 0.404 sekuntia
Kruskalin algoritmi: 20.354 sekuntia


### 150x150

Satunnaistettu syvyyshaku: 0.039 sekuntia
Primin algoritmi: 1.771 sekuntia
Kruskalin algoritmi: 104.405 sekuntia


Näistä voi huomata että satunnaistettu syvyyshaku on selvästi algoritmeista tehokkain, kun taas Kruskalin algoritmi on selvästi vähiten tehokas. Algoritmit ovat kuitenkin tässä projektissa toteutettu varsin improvisoidusti ja vapaamuotoisesti, etenkin Kruskalin algoritmi, joka on äärimmäisen hidas sillä sen toteutuksessa ei ole käytetty suositeltuja tietorakenteita vaan ne on toteutettu itse Pythonin valmiilla tietorakenteilla. Nämä algoritmien suorituskyvyt eivät siis vastaa niiden niin sanottuja "virallisia" suorityskykyjä.
