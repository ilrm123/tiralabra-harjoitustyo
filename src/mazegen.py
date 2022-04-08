import random
import pygame
import time

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

        if self.height*self.width <= 2:
            return

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
    
    def visualize(self, height, width, walls):
        grid = []
        counter = 1

        for i in range(1, height+1):
            grid.append([*range(counter, counter+width)])
            counter += int(width)
        
        pygame.init()
        screen = pygame.display.set_mode((width*25+8, height*25+8))
        pygame.display.set_caption("Labyrintin visualisointi")
        screen.fill((0, 0, 0))

        x = 4
        y = 4
        coords = {}

        for row in grid:
            for square in row:
                pygame.draw.rect(screen, (0,0,50), pygame.Rect(x, y, 25, 25))
                coords[square] = (x, y)
                x += 25
            y += 25
            x = 4

        pygame.display.flip()
        time.sleep(0.125)

        pygame.draw.rect(screen, (100,180,255), pygame.Rect(coords[walls[0][0]][0]+2, coords[walls[0][0]][1]+2, 21, 21))

        for wall in walls:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
            if wall[1] == wall[0]-1: #vasen seinä
                pygame.draw.rect(screen, (50,130,230), pygame.Rect(coords[wall[1]][0]+23, coords[wall[1]][1]+2, 4, 21))
            elif wall[1] == wall[0]+1: #oikea seinä
                pygame.draw.rect(screen, (50,130,230), pygame.Rect(coords[wall[1]][0]-2, coords[wall[1]][1]+2, 4, 21))
            elif wall[1] == wall[0]-width: #yläseinä
                pygame.draw.rect(screen, (50,130,230), pygame.Rect(coords[wall[1]][0]+2, coords[wall[1]][1]+23, 21, 4))
            elif wall[1] == wall[0]+width: #alaseinä
                pygame.draw.rect(screen, (50,130,230), pygame.Rect(coords[wall[1]][0]+2, coords[wall[1]][1]-2, 21, 4))
            
            pygame.draw.rect(screen, (50,130,230), pygame.Rect(coords[wall[1]][0]+2, coords[wall[1]][1]+2, 21, 21))
            time.sleep(0.125)
            pygame.display.flip()
        

def main():
    """Pääfunktio, joka suorittaa ohjelman

    """

    height = int(input("Anna labyrintin korkeus: "))
    width = int(input("Anna labyrintin leveys: "))
    maze = MazeGeneration(height, width)
    route = maze.random_depthfirst()
    if route == None:
        print("Liian pieni labyrintti")
    else:
        maze.visualize(height, width, route)


if __name__ == "__main__":
    main()
