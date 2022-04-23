import unittest
from mazegen import MazeGeneration

class TestMazeGeneration(unittest.TestCase):
    def setUp(self):
        self.generator = MazeGeneration(3, 4)
        self.graph1 = self.generator.create_graph()
        self.graph2 = self.generator.create_graph()
        self.graph3 = self.generator.create_graph()

    def test_verkon_vasen_ylakulma_oikein(self):
        self.assertEqual(self.graph1[1], [False, 2, 5])

    def test_verkon_vasen_alakulma_oikein(self):
        self.assertEqual(self.graph1[9], [False, 10, 5])

    def test_verkon_oikea_ylakulma_oikein(self):
        self.assertEqual(self.graph1[4], [False, 3, 8])

    def test_verkon_oikea_alakulma_oikein(self):
        self.assertEqual(self.graph1[12], [False, 11, 8])

    def test_verkon_keskiosa_oikein(self):
        self.assertEqual(self.graph1[6], [False, 5, 7, 2, 10])

    def test_verkon_ylakeskiosa_oikein(self):
        self.assertEqual(self.graph1[3], [False, 2, 4, 7])

    def test_verkon_alakeskiosa_oikein(self):
        self.assertEqual(self.graph1[10], [False, 9, 11, 6])

    def test_verkon_vasen_keskiosa_oikein(self):
        self.assertEqual(self.graph1[5], [False, 6, 1, 9])

    def test_verkon_oikea_keskiosa_oikein(self):
        self.assertEqual(self.graph1[8], [False, 7, 4, 12])

    def test_kaikissa_solmuissa_kaydaan_syvyyshaku(self):
        route = self.generator.random_depthfirst(self.graph1)

        visited = []
        realamount =[*range(1, 13, 1)]

        for edge in route:
            if edge[0] not in visited:
                visited.append(edge[0])
            if edge[1] not in visited:
                visited.append(edge[1])

        self.assertEqual(sorted(visited), realamount)

    def test_kaikissa_solmuissa_kaydaan_prim(self):
        route = self.generator.random_prim(self.graph2)

        visited = []
        realamount =[*range(1, 13, 1)]

        for edge in route:
            if edge[0] not in visited:
                visited.append(edge[0])
            if edge[1] not in visited:
                visited.append(edge[1])

        self.assertEqual(sorted(visited), realamount)

    def test_kaikissa_solmuissa_kaydaan_kruskal(self):
        route = self.generator.random_prim(self.graph3)

        visited = []
        realamount =[*range(1, 13, 1)]

        for edge in route:
            if edge[0] not in visited:
                visited.append(edge[0])
            if edge[1] not in visited:
                visited.append(edge[1])

        self.assertEqual(sorted(visited), realamount)
