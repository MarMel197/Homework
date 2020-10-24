# Set-up Unittest & import Guest class
import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

# Set up our guest objects from Guest class    
    def setUp(self):
        self.guest1 = Guest("Emma", 50.00)
        self.guest2 = Guest("Simon", 30.00)
        self.guest3 = Guest("Anthony", 40.00)
        self.guest4 = Guest("Lauchy", 10.00)

# Initial Tests
    def test_guest_has_name(self):
        self.assertEqual("Anthony", self.guest3.name)

    def test_another_guest_has__name(self):
        self.assertEqual("Lauchy", self.guest4.name)