#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_attribute_initialized(self):
        """Tests that the name attribute of a new `State` 
        object is initialized to an empty string."""
        state = State()
        self.assertEqual(state.name, "")

    def test_unique_ids(self):
        """This function tests if two instantiated 
        objects of `State` have different IDs."""
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

if __name__ == '__main__':
    unittest.main()

