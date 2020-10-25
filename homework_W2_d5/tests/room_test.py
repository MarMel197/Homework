# Set-up Unittest & import Room class
import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
# Set up song and room objecs
        self.guest = Guest("Santa")
        self.guest1 = Guest("Emma")
        self.guest2 = Guest("Simon")
        self.guest3 = Guest("Anthony")
        self.guest4 = Guest("Lauchy")

        self.song =Song("Always look on the bright side of life", "Monty Python")
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
# Set up playlist for rooms
        self.room1_playlist = [self.song1, self.song2]
        self.room2_playlist = [self.song4, self.song5]
        self.room3_playlist = [self.song7, self.song8]
        self.room4_playlist = [self.song10, self.song11]

        self.room1 = Room("Popular Songs", self.room1_playlist,[], self.song, self.guest)
        self.room2 = Room("Easy Songs", self.room2_playlist, [self.guest2, self.guest3], self.song, self.guest)
        self.room3 = Room("Hard Songs", self.room3_playlist, [], self.song, self.guest)
        self.room4 = Room("Kids Songs", self.room4_playlist, [], self.song, self.guest)

        

# Initial Tests
    def test_room_has_name(self):
        self.assertEqual("Easy Songs", self.room2.name)

    def test_another_room__number(self):
        self.assertEqual("Kids Songs", self.room4.name)


    def test_check_room_has_guestlidt(self):
        self.assertEqual(0, len(self.room1.guestlist))

    def test_check_add_guest_to_guestlist(self):
        self.room1.add_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guestlist))

    def test_remove_guest_from_room(self):
        self.room2.remove_guest(self.guest3)
        self.assertEqual(1, len(self.room2.guestlist))

    def test_room_has_playlist(self):
        self.assertEqual(2, len(self.room3.playlist))

    def test_add_song_to_playlist(self):
        self.room3.playlist_add(self.song9)
        self.assertEqual(3, len(self.room3.playlist))

