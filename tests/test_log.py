import unittest
from unittest.mock import patch
from mood_tracker import log_mood

class TestLogMood(unittest.TestCase):
    @patch('builtins.input', side_effect=['4', 'Feeling good'])
    def test_log_mood_valid(self, mock_input):
        mood_entry = log_mood()
        self.assertEqual(mood_entry['rating'], 4)
        self.assertEqual(mood_entry['comment'], 'Feeling good')
        self.assertIn('date', mood_entry)

if __name__ == '__main__':
    unittest.main()

# Test for the log_mood function in the mood_tracker module.              
