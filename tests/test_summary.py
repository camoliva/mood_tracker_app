import unittest
import json
import os
from mood_tracker import show_mood_summary

class TestMoodSummary(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_moods_summary.json"
        self.test_data = [
            {"rating": 5, "note": "Feeling great!", "date": "2025-07-01"},
            {"rating": 3, "note": "Could be better", "date": "2025-07-02"},
            {"rating": 1, "note": "Doing okay", "date": "2025-07-03"},
        ]
        with open(self.test_file, "w") as file:
            json.dump(self.test_data, file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_summary_returns_correct_data(self):
        summary = show_mood_summary(self.test_file)
        self.assertEqual(summary["total"], 3)
        self.assertEqual(summary["average"], 3.0)
        self.assertEqual(summary["highest"], 5)
        self.assertEqual(summary["lowest"], 1)

if __name__ == '__main__':
    unittest.main()
         
#Ttest for the show_mood_summary function in the mood_tracker module