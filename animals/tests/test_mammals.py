import unittest
from unittest.mock import Mock
from animals.animals.mammals import MammalsSet


class TestMammalsSet(unittest.TestCase):
    def test_return_empty_list_if_no_mammals(self):
        self.assertEqual(0, len(MammalsSet(None).mammals))

    def test_refresh_list_generates_call_to_database(self):
        """
        Make sure that the set of mammals is updated with a request to the database
        when the refresh message is sent.
        """
        db = Mock()
        MammalsSet(db).refresh()
        db.animals.assert_called()


if __name__ == "__main__":
    unittest.main()
