import unittest
import os
import json
from mood_tracker import save_mood_to_file

class TestSaveMood(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_moods.json"
        self.test_entry = {
            "rating": 5,
            "comment": "Feeling greet!",
            "date": "2023-10-01"
        }

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_mood_to_file(self):
        save_mood_to_file(self.test_entry, self.test_file)

        with open(self.test_file, 'r') as file:
            data = json.load(file)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0], self.test_entry)

if __name__ == '__main__':
    unittest.main()
# test for the save_mood_to_file function in the mood_tracker