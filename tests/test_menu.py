import unittest
from unittest.mock import patch
from mood_tracker import get_user_choice

class TestMenu(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_choice_log_mood(self, mock_input):
        self.assertEqual(get_user_choice(), '1')

    @patch('builtins.input', side_effect=['x','2'])
    def test_invalid_choice_then_valid_choice(self, mock_input):
        self.assertEqual (get_user_choice(), '2')

if __name__ == '__main__':
    unittest.main()
# This code is a test for the get_user_choice function in the mood_tracker module.