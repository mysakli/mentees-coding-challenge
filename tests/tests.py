import unittest
from main import MenteeSummary
import os, json


class TestMenteeSummary(unittest.TestCase):
    def setUp(self):
        self.summary = MenteeSummary('./tests/test-list.csv')
        self.file_path = './tests/test_summary.json'
    
    def test_count_mentees(self):
        self.assertEqual(self.summary.get_count(), 4)
    
    def test_avg_name_length(self):
        self.assertEqual(self.summary.get_avg_name_length(), 13.75)

    def test_unique_languages(self):
        self.assertEqual(self.summary.get_unique_languages(), ['English', 'German', 'Japanese', 'Spanish'])

    def test_shortest_name(self):
        self.assertEqual(self.summary.get_shortest_name(), ['Ron Weasley'])

    def test_longest_name(self):
        self.assertEqual(self.summary.get_longest_name(), ['Albus Dumbledore', 'Hermione Granger'])
    
    def test_file_created(self):
        self.summary.create_summary_json('tests/test_summary.json')
        self.assertTrue(os.path.isfile(self.file_path))
    
    def test_file_contents(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        
        self.assertEqual(data, {
    "nr_of_mentees": 4,
    "languages": [
        "English",
        "German",
        "Japanese",
        "Spanish"
    ],
    "avg_name_length": 13.75,
    "shortest_names": [
        "Ron Weasley"
    ],
    "longest_names": [
        "Albus Dumbledore",
        "Hermione Granger"
    ]
    })

