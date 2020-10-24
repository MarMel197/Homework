# Set-up Unittest & import Guest class
import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest()

    # Paramenerers required above