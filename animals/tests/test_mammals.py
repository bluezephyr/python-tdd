import unittest
from unittest.mock import Mock, call
from animals.animals.mammals import MammalsSet


class TestMammalsSet(unittest.TestCase):
    def test_return_empty_list_if_no_mammals(self):
        """Test 1"""
        self.assertEqual(0, len(MammalsSet(None).mammals))

    def test_refresh_generates_call_to_database(self):
        """
        Test 2
        Make sure that the set of mammals is updated with a request to the database
        when the refresh message is sent.
        """
        db = Mock()
        db.animals.return_value = []
        MammalsSet(db).refresh()
        db.animals.assert_called()

    def test_add_mammal_to_mammals_set_at_refresh(self):
        """Test 3"""
        horse = Mock()
        db = Mock()
        db.animals.return_value = [horse]
        mammals_set = MammalsSet(db)
        mammals_set.refresh()
        self.assertEqual(1, len(mammals_set.mammals))

    def test_only_add_mammals_to_the_mammals_set(self):
        db = Mock()
        horse = Mock()
        trout = Mock()
        db.animals.return_value = [horse, trout]
        mammals_set = MammalsSet(db)
        mammals_set.refresh()
        db.assert_has_calls([call.animals()])
        horse.is_mammal.assert_called_once()
        trout.is_mammal.assert_called_once()


if __name__ == "__main__":
    unittest.main()
