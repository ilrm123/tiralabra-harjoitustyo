import random

class MazeGeneration:
    """Luokka, jolla labyrintti ja sen reitti/reitit luodaan

    Attributes:
        height: labyrintin korkeus
        width: labyrintin leveys
    """

    def __init__(self, height, width):
        """Luokan konstruktori, joka luo labyrintin pohjan

        Args:
            height: labyrintin korkeus
            width: labyrintin leveys
        """

        self.height = height
        self.width = width

        #verkko labyrintille
        self.graph = {}

        #vieruslistaesitys verkolle
        for i in range(1, height*width+1):
            self.graph[i] = []

        #lisätään kaaret viereisiin solmuihin
        for node in self.graph:
            #onko vierailtu
            self.graph[node].append(False)

            #lisää kaaret vasemmalle, oikealla, ylös ja alas
            if node-1 in range(1, height*width+1):
                self.graph[node].append(node-1)
            if node+1 in range(1, height*width+1):
                self.graph[node].append(node+1)
            if node-width in range(1, height*width+1):
                self.graph[node].append(node-width)
            if node+width in range(1, height*width+1):
                self.graph[node].append(node+width)

        #poistetaan ylimääräiset kaaret jotka muodostuivat ylläolevasta
        counter = int(width)
        while True:
            copylist1 = self.graph[counter].copy()
            copylist1.remove(counter+1)
            self.graph[counter] = copylist1
            copylist2 = self.graph[counter+1].copy()
            copylist2.remove(counter)
            self.graph[counter+1] = copylist2
            counter += int(width)
            if counter == height*width:
                break

    def random_depthfirst(self):
        """Luo labyrintin satunnaistetulla syvyyshakualgoritmilla

        Returns:
            Lista, joka kertoo kaikki poistetut seinät, eli kaikki kuljetut kaaret
        """

        #alustetaan pino (lista) ja valitaan satunnainen aloitussolmu
        stack = []
        startnode = random.choice(range(1, self.height*self.width+1))
        self.graph[startnode][0] = True
        stack.append(startnode)
        self.removedwalls = []

        #silmukka jossa valitaan aina jokin ei-vierailtu solmu kunnes niitä ei enää ole
        while len(stack) != 0:
            current = stack[-1]
            stack.pop(-1)

            unvisited = []
            for node in self.graph[current][1:]:
                if self.graph[node][0] == False:
                    unvisited.append(node)

            if len(unvisited) != 0:
                stack.append(current)
                new = random.choice(unvisited)
                self.removedwalls.append((current, new))
                self.graph[new][0] = True
                unvisited.remove(new)
                stack.append(new)
                current = int(new)

        return self.removedwalls


def main():
    """Pääfunktio, joka suorittaa ohjelman

    """
    height = int(input("Anna labyrintin korkeus: "))
    width = int(input("Anna labyrintin leveys: "))
    if height*width < 4:
        print("Liian pieni labyrintti")
    else:
        maze = MazeGeneration(height, width)
        route = maze.random_depthfirst()

        #tulostaa listan tupleja jotka kertovat järjestyksessä algoritmin luoman reitin
        print(route)


if __name__ == "__main__":
    main()
