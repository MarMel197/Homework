import unittest
from app.models.game import Game
from app.models.player import Player

class GameTest(unittest.TestCase):
    def setUp(self):
        self.rock = Player('Mark', 'rock')
        self.paper = Player('Rob', 'paper')
        self.scissors = Player('Emma', 'scissors')

    def test_game_has_winner(self):
        self.assertEqual('Player 1 wins', Game.who_won(self.rock,self.scissors))

    def test_game_has_another__winner(self):
        self.assertEqual('Player 2 wins', Game.who_won(self.rock,self.paper))



