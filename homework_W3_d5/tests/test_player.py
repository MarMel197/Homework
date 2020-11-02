import unittest
from app.models.player import Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player('Mark', 'rock')
        self.player1 = Player('Cammy', 'paper')
        self.player2 = Player('Sophie', 'scissors')

    def test_game_has_player(self):
        self.assertEqual('Mark', self.player.name)

    def test_game_has_another__player(self):
        self.assertEqual('Sophie', self.player2.name)