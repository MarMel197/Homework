# Set-up Unittest & import Guest class
import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

# Set up our guest objects from Guest class    
    def setUp(self):
        self.guest1 = Guest("Emma")
        self.guest2 = Guest("Simon")
        self.guest3 = Guest("Anthony")
        self.guest4 = Guest("Lauchy")

# Initial Tests
    def test_guest_has_name(self):
        self.assertEqual("Anthony", self.guest3.name)

    def test_another_guest_has__name(self):
        self.assertEqual("Lauchy", self.guest4.name)