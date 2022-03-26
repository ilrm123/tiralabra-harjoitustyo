import unittest
from mazegen import MazeGeneration

class TestMazeGeneration(unittest.TestCase):
    def setUp(self):
        self.generator = MazeGeneration(3, 4)

    def test_verkon_vierekkaiset_oikein(self):
        self.assertEqual(self.generator.graph[1], [False, 2, 5])
