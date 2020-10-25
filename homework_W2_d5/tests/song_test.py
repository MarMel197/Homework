# Set-up Unittest and import Song Class
import unittest 
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.test_song1 = Song("Infinite Dreams", "Iron Maiden") 
        self.test_song2 = Song("The Fly", "U2") 

# Initial tests    
    def test_check_song_has_name(self):
        self.assertEqual("Infinite Dreams", self.test_song1.song)

    def test_check_another_song__name(self):
        self.assertEqual("The Fly", self.test_song2.song)
    
    def test_check_song_has_artist(self):
        self.assertEqual("Iron Maiden", self.test_song1.artist)

    def test_check_another_song__artist(self):
        self.assertEqual("U2", self.test_song2.artist)