import random
import time
import pygame

class MazeGeneration:
    """Luokka, jolla labyrintti ja sen reitti/reitit luodaan

    Attributes:
        height: labyrintin korkeus
        width: labyrintin leveys
    """

    def __init__(self, height, width):
        """Luokan konstruktori, joka vastaanottaa korkeuden ja leveyden

        Args:
            height: labyrintin korkeus
            width: labyrintin leveys
        """

        self.height = height
        self.width = width

    def create_graph(self):
        """Luo oikeanlaisen verkon labyrintin muodostusta varten

        Returns:
            Sanakirja, jonka avaimet ovat solmuja ja arvot listoja, joiden ensimmäinen
            alkio kertoo onko solmussa vierailtu ja loput alkiot ovat solmun naapureita
        """

        # verkko labyrintille
        graph = {}

        # vieruslistaesitys verkolle
        for i in range(1, self.height*self.width+1):
            graph[i] = []

        # lisätään kaaret viereisiin solmuihin
        for node in graph:
            # onko vierailtu
            graph[node].append(False)

            # lisää kaaret vasemmalle, oikealla, ylös ja alas
            if node-1 in range(1, self.height*self.width+1):
                graph[node].append(node-1)
            if node+1 in range(1, self.height*self.width+1):
                graph[node].append(node+1)
            if node-self.width in range(1, self.height*self.width+1):
                graph[node].append(node-self.width)
            if node+self.width in range(1, self.height*self.width+1):
                graph[node].append(node+self.width)

        # poistetaan ylimääräiset kaaret jotka muodostuivat ylläolevasta
        counter = int(self.width)
        while True:
            copylist1 = graph[counter].copy()
            copylist1.remove(counter+1)
            graph[counter] = copylist1
            copylist2 = graph[counter+1].copy()
            copylist2.remove(counter)
            graph[counter+1] = copylist2
            counter += int(self.width)
            if counter == self.height*self.width:
                break

        return graph

    def random_depthfirst(self, graph):
        """Luo labyrintin satunnaistetulla syvyyshakualgoritmilla

        Args:
            graph: Verkko jolla labyrintti muodostetaan

        Returns:
            Lista, joka kertoo kaikki poistetut seinät, eli kaikki kuljetut kaaret
        """

        # alustetaan pino (lista) ja valitaan satunnainen aloitussolmu
        stack = []
        startnode = random.choice(range(1, self.height*self.width+1))
        graph[startnode][0] = True
        stack.append(startnode)
        removedwalls = []

        # silmukka jossa valitaan aina jokin ei-vierailtu solmu kunnes niitä ei enää ole
        while len(stack) != 0:
            current = stack[-1]
            stack.pop(-1)

            # lisätään tämänhetkisen solmun ei-vieraillut naapurit listaan
            unvisited = []
            for node in graph[current][1:]:
                if graph[node][0] is False:
                    unvisited.append(node)

            # jos solmulla on vierailemattomia naapureita niin valitaan satunnainen naapuri,
            # lisätään poistettu seinä listaan ja lisätään uusi solmu pinoon
            if len(unvisited) != 0:
                stack.append(current)
                new = random.choice(unvisited)
                removedwalls.append((current, new))
                graph[new][0] = True
                unvisited.remove(new)
                stack.append(new)
                current = int(new)

        return removedwalls

    def random_prim(self, graph):
        """Luo labyrintin satunnaistetulla Primin algoritmilla

        Args:
            graph: Verkko jolla labyrintti muodostetaan

        Returns:
            Lista, joka kertoo kaikki poistetut seinät, eli kaikki kuljetut kaaret
        """

        # Luodaan lista seinille, valitaan aloitussolmu ja merkitään se vierailluksi
        walls = []
        startnode = random.choice(range(1, self.height*self.width+1))
        graph[startnode][0] = True
        removedwalls = []

        # Lisätään aloitussolmun seinät listaan
        for neighbor in graph[startnode][1:]:
            walls.append((startnode, neighbor))

        # Silmukka jossa valitaan seinälistasta satunnainen seinä,
        # poistetaan seinä jos toisessa solmussa on käyty, merkitään toinenkin käydyksi
        # ja jatketaan kunnes seinälista on tyhjä
        while len(walls) != 0:
            randwall = random.choice(walls)

            if (graph[randwall[0]][0] is True and graph[randwall[1]][0] is False) or (graph[randwall[1]][0] is True and graph[randwall[0]][0] is False):
                removedwalls.append(randwall)

                for node in randwall:
                    if graph[node][0] is False:
                        graph[node][0] = True

                        for neighbor in graph[node][1:]:
                            walls.append((node, neighbor))

            walls.remove(randwall)

        return removedwalls

    def random_kruskal(self, graph):
        """Luo labyrintin satunnaistetulla Kruskalin algoritmilla

        Args:
            graph: Verkko jolla labyrintti muodostetaan

        Returns:
            Lista, joka kertoo kaikki poistetut seinät, eli kaikki kuljetut kaaret
        """

        # Luodaan lista seinille, lista solmujoukoille ja lista poistettaville seinille
        walls = []
        nodesets = []
        removedwalls = []

        # Lisätään kaikki seinät eli verkon kaaret seinälistaan
        for node in graph:
            for neighbor in graph[node][1:]:
                if (node, neighbor) not in walls and (neighbor, node) not in walls:
                    walls.append((node, neighbor))

        # Lisätään kaikki solmut omissa joukoissaan solmujoukkolistaan
        for node in graph:
            nodesets.append([node])

        # Sekoitetaan seinien järjestys listassa
        random.shuffle(walls)

        # Käydään seinät läpi siten, että jos seinän erottamat solmut ovat eri joukoissa,
        # niin nämä joukot yhdistetään
        for wall in walls:
            distinct = True
            for nodeset in nodesets:
                if wall[0] in nodeset and wall[1] in nodeset:
                    distinct = False
                    break

            if distinct == False:
                continue

            removedwalls.append(wall)

            # Etsitään solmujoukoista ne joukot joissa kumpikin solmu on
            for nodeset in nodesets:
                if wall[0] in nodeset:
                    set1 = nodeset.copy()
                if wall[1] in nodeset:
                    set2 = nodeset.copy()

            # Yhdistetään joukot
            if set1 != set2:
                nodesets.remove(set1)
                nodesets.remove(set2)

                set1.extend(set2)
                nodesets.append(set1)

        return removedwalls

    def visualize(self, walls):
        """Visualisoi luodun labyrintin

        Args:
            walls: Seinät jotka poistettiin algoritmin avulla, eli verkossa kuljetut kaaret
        """

        # Lista johon muodostetaan ruudukko
        grid = []

        # Lisätään listaan oikea määrä oikean pituisia rivejä
        counter = 1
        for i in range(1, self.height+1):
            grid.append([*range(counter, counter+self.width)])
            counter += int(self.width)

        # Alustetaan pygame visualisointia varten, näytön koko riippuu labyrintin koosta
        pygame.init()
        screen = pygame.display.set_mode((self.width*25+8, self.height*25+8))
        pygame.display.set_caption("Labyrintin visualisointi")
        screen.fill((0, 0, 0))

        # Koordinaattimuuttujat joiden avulla luodaan ruudukko ja lisätään kaikkien solmujen
        # koordinaatit coords-sanakirjaan
        x = 4
        y = 4
        coords = {}

        # Ruudukon luonti ja koordinaattien lisäys
        for row in grid:
            for square in row:
                pygame.draw.rect(screen, (0,0,50), pygame.Rect(x, y, 25, 25))
                coords[square] = (x, y)
                x += 25
            y += 25
            x = 4

        pygame.display.flip()
        time.sleep(0.125)

        # Visualisoinnin suoritussilmukka
        counter = 0 # kerroin jolla voidaan nopeuttaa visualisointia
        for wall in walls:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if counter < 5:
                            counter += 1

                if event.type == pygame.QUIT:
                    exit()

            # seinien poistot
            if wall[1] == wall[0]-1: # vasen seinä
                pygame.draw.rect(screen, (50,130,230), pygame.Rect(coords[wall[1]][0]+23, coords[wall[1]][1]+2, 4, 21))
            elif wall[1] == wall[0]+1: # oikea seinä
                pygame.draw.rect(screen, (50,130,230), pygame.Rect(coords[wall[1]][0]-2, coords[wall[1]][1]+2, 4, 21))
            elif wall[1] == wall[0]-self.width: # yläseinä
                pygame.draw.rect(screen, (50,130,230), pygame.Rect(coords[wall[1]][0]+2, coords[wall[1]][1]+23, 21, 4))
            elif wall[1] == wall[0]+self.width: # alaseinä
                pygame.draw.rect(screen, (50,130,230), pygame.Rect(coords[wall[1]][0]+2, coords[wall[1]][1]-2, 21, 4))

            # seinän erottamien ruutujen värjääminen
            pygame.draw.rect(screen, (50,130,230), pygame.Rect(coords[wall[1]][0]+2, coords[wall[1]][1]+2, 21, 21))
            pygame.draw.rect(screen, (50,130,230), pygame.Rect(coords[wall[0]][0]+2, coords[wall[0]][1]+2, 21, 21))

            time.sleep(0.125-(counter*0.025))
            pygame.display.flip()

        # Väritetään aloitus- ja lopetusruudut
        pygame.draw.rect(screen, (100,180,255), pygame.Rect(coords[walls[0][0]][0]+2, coords[walls[0][0]][1]+2, 21, 21))
        pygame.draw.rect(screen, (100,180,255), pygame.Rect(coords[wall[1]][0]+2, coords[wall[1]][1]+2, 21, 21))
        pygame.display.flip()


def main():
    """Pääfunktio, joka suorittaa ohjelman

    """

    height = int(input("Anna labyrintin korkeus: "))
    width = int(input("Anna labyrintin leveys: "))

    if height == 1 or width == 1 or height*width < 4:
        print("Liian pienet mitat labyrintille")
    else:
        maze = MazeGeneration(height, width)
        graph1 = maze.create_graph()
        graph2 = maze.create_graph()
        graph3 = maze.create_graph()

        start = time.time()
        depth = maze.random_depthfirst(graph1)
        end = time.time()
        print(f"Satunnaistettuun syvyyshakuun kulunut aika: {end-start} s")
        ans = int(input("Haluatko visualisoida syvyyshaun? 1 = Kyllä tai 2 = Ei: "))
        if ans == 1:
            maze.visualize(depth)

        start = time.time()
        prim = maze.random_prim(graph2)
        end = time.time()
        print(f"Satunnaistettuun Primin algoritmiin kulunut aika: {end-start} s")
        ans = int(input("Haluatko visualisoida Primin algoritmin? 1 = Kyllä tai 2 = Ei: "))
        if ans == 1:
            maze.visualize(prim)

        start = time.time()
        kruskal = maze.random_kruskal(graph3)
        end = time.time()
        print(f"Satunnaistettuun Kruskalin algoritmiin kulunut aika: {end-start} s")
        ans = int(input("Haluatko visualisoida Kruskalin algoritmin? 1 = Kyllä tai 2 = Ei: "))
        if ans == 1:
            maze.visualize(kruskal)


if __name__ == "__main__":
    main()
