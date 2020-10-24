# Set-up Unittest & import Room class
import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room()

    # Paramenerers required above

