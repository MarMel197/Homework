# Set-up Unittest and import Song Class
import unittest 
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Rock a bye your bear")
        self.song2 = Song("Apples and Bananas")
        self.song3 = Song("Do the propeller")
        self.song4 = Song("Captains magic buttons")

# Initial tests    
    def test_check_song_has_name(self):
        self.assertEqual("Rock a bye your bear", self.song1.song)
    
    def test_check_another_song__name(self):
        self.assertEqual("Captains magic buttons", self.song4.song)
