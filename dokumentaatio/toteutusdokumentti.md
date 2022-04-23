## Toteutusdokumentti

Ohjelman yleisrakenne on yksinkertainen, kaikki toiminnallisuus on yhdessä tiedostossa jossa on yksi luokka metodeineen sekä pääfunktio.

Tarkoista aika- tai tilavaativuuksista ei ole tällä hetkellä tietoa, mutta ohjelmaa suorittaessa voi huomata että kolmesta tämänhetkisestä algoritmista satunnaistettu syvyyshaku on huomattavasti nopein, ja Kruskal hitain, etenkin suurilla syötteillä. Satunnaistettu Primin algoritmi on todella hidas jos labyrintin leveys tai korkeus on hyvin suuri, Kruskalin algoritmi taas on äärimmäisen hidas jopa ei-niin-suurilla syötteillä (esim. 100x100). 

Työn tämänhetkisiä puutteita ovat ainakin suorituskykytestauksen puute ja mahdollisesti hieman "väärin" toteutetut algoritmit mikä mahdollisesti vaikuttaa aikavaativuuteen.

Työtä voisi parannella ainakin joillain hienosäädöillä, kuten virheellisten syötteiden käsittelyllä ja mahdollistamalla todella suurten labyrinttien visualisoinnin (Pygamen ikkuna skaalautuu labyrintin koon mukaan joten isot labyrintit eivät mahdu ruudulle)

Lähteet:

https://en.wikipedia.org/wiki/Maze_generation_algorithm
