import random

class MazeGeneration:

    def __init__(self, height, width):
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
        stack = []
        startnode = random.choice(range(1, self.height*self.width+1))
        stack.append(startnode)


def main():
    height = int(input("Anna labyrintin korkeus: "))
    width = int(input("Anna labyrintin leveys: "))
    maze = MazeGeneration(height, width)
    
    print(maze.graph)


if __name__ == "__main__":
    main()