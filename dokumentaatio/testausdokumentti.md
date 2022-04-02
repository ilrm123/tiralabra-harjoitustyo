# Testausdokumentti

Coveragen tuottama yksikkötestauksen kattavuusraportti

Name                     Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------
src/mazegen.py              60      8     28      1    88%   97-106, 110
src/tests/__init__.py        0      0      0      0   100%
src/tests/maze_test.py      17      0      8      1    96%   20->17
--------------------------------------------------------------------
TOTAL                       77      8     36      2    89%


Testejä on tähän mennessä vasta kaksi. Ensimmäisessä testataan onko luodun verkon solmut yhdistetty kaarilla oikeisiin solmuihin, ja toisessa testataan käykö satunnaistettu syvyyshakualgoritmi kaikissa solmuissa. Testit ovat siinä mielessä puutteellisia, että ne testaavat vain yhdenlaista tapausta.

Testaus tehtiin syötteillä 3 ja 4, eli luotu labyrintti on erittäin pieni, joten testit eivät testaa vielä tehokkuutta ja testaavat vain tätä yhtä tapausta.
