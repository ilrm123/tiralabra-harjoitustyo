## Toteutusdokumentti

Ohjelman yleisrakenne on yksinkertainen, kaikki toiminnallisuus on yhdessä tiedostossa jossa on yksi luokka metodeineen sekä pääfunktio.

Tarkoista aika- tai tilavaativuuksista ei ole tällä hetkellä tietoa, mutta ohjelmaa suorittaessa voi huomata että kahdesta tämänhetkisestä algoritmista satunnaistettu syvyyshaku on huomattavasti nopeampi kuin satunnaistettu Primin algoritmi, etenkin suurilla syötteillä. Satunnaistettu Primin algoritmi on todella hidas jos labyrintin leveys tai korkeus on hyvin suuri, tämä voi tosin johtua omasta toteutustavastani eikä välttämättä ole Primin algoritmille ominainen asia.

Työn tämänhetkisiä puutteita ovat ainakin testauksen vähäisyys ja mahdollisesti hieman "väärin" toteutetut algoritmit mikä mahdollisesti vaikuttaa aikavaativuuteen.

Työtä voisi parannella ainakin joillain hienosäädöillä, kuten virheellisten syötteiden käsittelyllä ja mahdollistamalla todella suurien labyrinttien visualisoinnin (Pygamen ikkuna skaalautuu labyrintin koon mukaan joten isot labyrintit eivät mahdu ruudulle)

