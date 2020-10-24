# Set-up Unittest and import Song Class
import unittest 
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song()

    # Paramenerers required above
