import unittest
from mazegen import MazeGeneration

class TestMazeGeneration(unittest.TestCase):
    def setUp(self):
        self.generator = MazeGeneration(3, 4)
        self.graph1 = self.generator.create_graph()
        self.graph2 = self.generator.create_graph()

    def test_verkon_vierekkaiset_oikein(self):
        self.assertEqual(self.graph1[1], [False, 2, 5])

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

