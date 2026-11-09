import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_haku_loytyy(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_haku_ei_loydy(self):
        player = self.stats.search("Tuntematon")
        self.assertIsNone(player)

    def test_joukkue(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        names = [p.name for p in edm_players]
        self.assertIn("Semenko", names)
        self.assertIn("Kurri", names)
        self.assertIn("Gretzky", names)

    def test_parhaat_pistemiehet(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
