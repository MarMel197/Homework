# Set-up Unittest & import Room class
import unittest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
# Set up song and room objecs
        self.song1 = Song("Bohemian Rhapsody", "Queen")
        self.song2 = Song("Can't get you out of my head", "Kylie Minogue")
        self.song3 = Song("I wanna dance with sombody", "Whitney Houston")
        self.song4 = Song("Build me up buttercup", "The Foundations")
        self.song5 = Song("Achy breaky heart", "Billy Ray Sirus")
        self.song6 = Song("Baggy Trousers", "Madness")
        self.song7 = Song("I believe in a thing called love", "The Darkness")
        self.song8 = Song("Video games", "Lana Del Rey")
        self.song9 = Song("Hurt", "Christina Aguilera")
        self.song10 = Song("Let it go", "Frozen")
        self.song11 = Song("Shake it off", "Taylor Swift")
        self.song12 = Song("Baby shark", "Pink Fong")



        self.room1 = Room("Popular Songs", [self.song1, self.song2, self.song3])
        self.room2 = Room("Easy Songs",[self.song4, self.song5, self.song6])
        self.room3 = Room("Hard Songs", [self.song7, self.song8, self.song9])
        self.room4 = Room("Kids Songs", [self.song10, self.song11, self.song12])

# Initial Tests
    def test_room_has_name(self):
        self.assertEqual("Easy Songs", self.room2.name)

    def test_another_room__number(self):
        self.assertEqual("Kids Songs", self.room4.name)

