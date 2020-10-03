import unittest
from animals.animals.mammals import MammalsSet


class TestMammalsSet(unittest.TestCase):
    def test_refresh_list_generates_call_to_database(self):
        mammals = MammalsSet()


if __name__ == "__main__":
    unittest.main()
