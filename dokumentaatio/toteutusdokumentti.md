# Toteutusdokumentti

Ohjelman yleisrakenne on yksinkertainen, kaikki toiminnallisuus on yhdessä tiedostossa jossa on yksi luokka metodeineen sekä pääfunktio.

Tarkka tieto aika- tai tilavaativuuksista on valitettavasti jäänyt uupumaan, mutta ohjelmaa suorittaessa voi huomata että kolmesta tämänhetkisestä algoritmista satunnaistettu syvyyshaku on huomattavasti nopein, ja Kruskal hitain, etenkin suurilla syötteillä. Satunnaistettu Primin algoritmi on todella hidas jos labyrintin leveys tai korkeus on hyvin suuri, Kruskalin algoritmi taas on äärimmäisen hidas jopa ei-niin-suurilla syötteillä (esim. 100x100). Luotujen labyrinttien rakenteista huomaa sen, että satunnaistetulla syvyyshaulla luoduissa labyrinteissa on runsaasti kahden suunnan ruutuja, vähän umpikujia ja hyvin vähän neljän suunnan ruutuja. Primin ja Kruskalin luomat labyrintit ovat erittäin samanlaisia keskenään; niissä on paljon umpikujia sekä kolmen ja neljän suunnan ruutuja ja vähemmän kahden suunnan ruutuja kuin syvyyshaussa.

Työn puutteita ovat ainakin testauksen vähäisyys ja mahdollisesti hieman "väärin" toteutetut algoritmit mikä mahdollisesti vaikuttaa aikavaativuuteen.

Työtä voisi parannella ainakin joillain hienosäädöillä, kuten virheellisten syötteiden käsittelyllä ja mahdollistamalla todella suurten labyrinttien visualisoinnin (Pygamen ikkuna skaalautuu labyrintin koon mukaan joten isot labyrintit eivät mahdu ruudulle), sekä algoritmien tehokkuuden optimoinnilla.


## Lähteet:

https://en.wikipedia.org/wiki/Maze_generation_algorithm

Tirakirja:
https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/
