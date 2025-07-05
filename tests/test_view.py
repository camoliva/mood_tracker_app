import unittest
import json
import os
from mood_tracker import view_moods

class TestViewMoods(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_moods.json"
        self.test_data = [
            { "rating": 3, "note": "Could be better", "date": "2025-07-02"},
            {"rating": 5, "note": "Feeling great!", "date": "2025-07-03"}
        ]
        with open(self.test_file, "w") as file:
            json.dump(self.test_data, file)

        def tearDown(self):
            if os.path.exists(self.test_file):
                os.remove(self.test_file)

        def test_view_moods_returns_correct_data(self):
            moods = view_moods(self.test_file)
            self.assertEqual(len(moods), 2)
            self.assertEqual(moods[0]["note"], "Could be better")
            self.assertEqual(moods[1]["rating"], 5)

        def test_view_moods_handles_empty_file(self):
            with open(self.test_file, "w") as f:
                f.write("")

            result = view_moods(self.test_file)
            self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()

#this is a test for the view_moods function in the mood_tracker module.       