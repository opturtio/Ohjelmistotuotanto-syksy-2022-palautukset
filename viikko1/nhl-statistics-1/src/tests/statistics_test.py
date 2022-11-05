import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_None(self):
        player = self.statistics.search("Pena")
        self.assertEqual(player, None)

    def test_search_works(self):
        self.assertEqual(self.statistics.search("Kurri").name, "Kurri")

    def test_team_module(self):
        player = self.statistics.team("PIT")
        self.assertEqual((player[0].name, player[0].team, player[0].goals, player[0].assists),("Lemieux", "PIT", 45, 54))

    def test_team_module_EDM(self):
        players = self.statistics.team("EDM")
        self.assertEqual((players[0].name, players[1].name, players[2].name), ("Semenko","Kurri","Gretzky"))

    def test_module_top(self):
        self.assertEqual(str(self.statistics.top(1)[0]), "Gretzky EDM 35 + 89 = 124")
            