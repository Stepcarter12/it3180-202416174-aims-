import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation", cost=19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", cost=24.95),
        ]
        result = search_by_title(items, "Star")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Star Wars")

    def test_search_by_title_case_insensitive(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation", cost=19.95),
        ]
        result = search_by_title(items, "lion")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "The Lion King")


if __name__ == "__main__":
    unittest.main()
