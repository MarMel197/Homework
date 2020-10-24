# Set-up Unittest & import Room class
import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room(1)
        self.room2 = Room(2)
        self.room3 = Room(3)
        self.room4 = Room(4)

# Initial Tests
    def test_room_has_number(self):
        self.assertEqual(2, self.room2.number)

    def test_another_room__number(self):
        self.assertEqual(4, self.room4.number)

