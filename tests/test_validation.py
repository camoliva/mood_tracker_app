import unittest
from mood_tracker import validate_rating

class TestValidation(unittest.TestCase):
    def test_valid_rating(self):
        self.assertTrue(validate_rating(3))
                        
    def test_invalid_rating_low(self):
        self.assertFalse(validate_rating(0))
        
    def test_invalid_rating_high(self):
        self.assertFalse(validate_rating(6))

if __name__ == '__main__':
    unittest.main()

# This code is a unit test for the validate_rating function in the mood_tracker module.

