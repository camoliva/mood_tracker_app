import unittest
import json
import os
from unittest.mock import patch
from mood_tracker import get_user_name

class TestUserName(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_user.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
            
    @patch('builtins.input', return_value = 'Cameron')
    def test_prompt_and_save_name(self, mock_input):
        name = get_user_name(self.test_file)
        self.assertEqual(name, 'Cameron')
        with open(self.test_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data['name'], 'Cameron')

    def test_load_name_from_exists(self):
        with open(self.test_file, "w") as f:
            json.dump({"name": "cameron"}, f)

        name = get_user_name(self.test_file)
        self.assertEqual(name, "cameron")

if __name__ == '__main__':
    unittest.main()

