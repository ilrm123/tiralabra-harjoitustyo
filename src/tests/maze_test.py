import unittest
from mazegen import MazeGeneration

class TestMazeGeneration(unittest.TestCase):
    def setUp(self):
        self.generator = MazeGeneration(3, 4)

    def test_verkon_vierekkaiset_oikein(self):
        self.assertEqual(self.generator.graph[1], [False, 2, 5])

    def test_kaikissa_solmuissa_kaydaan(self):
        route = self.generator.random_depthfirst()

        visited = []
        realamount =[*range(1, 13, 1)]

        for edge in route:
            if edge[0] not in visited:
                visited.append(edge[0])
            if edge[1] not in visited:
                visited.append(edge[1])

        self.assertEqual(sorted(visited), realamount)
