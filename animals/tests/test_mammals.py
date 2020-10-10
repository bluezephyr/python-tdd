import unittest
from unittest.mock import Mock
from animals.animals.mammals import MammalsSet


class DatabaseMock(Mock):
    @staticmethod
    def animals():
        return [Mock()]


class TestMammalsSet(unittest.TestCase):
    def test_return_empty_list_if_no_mammals(self):
        """Test 1"""
        self.assertEqual(0, len(MammalsSet(None).mammals))

    @unittest.skip
    def test_refresh_generates_call_to_database(self):
        """
        Test 2
        Make sure that the set of mammals is updated with a request to the database
        when the refresh message is sent.
        """
        db = Mock()
        MammalsSet(db).refresh()
        db.animals.assert_called()

    def test_return_list_with_one_item_if_database_contains_one_mammal(self):
        """Test 3"""
        mammals_set = MammalsSet(DatabaseMock())
        mammals_set.refresh()
        self.assertEqual(1, len(mammals_set.mammals))


if __name__ == "__main__":
    unittest.main()
