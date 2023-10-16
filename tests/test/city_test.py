#!/usr/bin/python3

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_attributes_initialized(self):
        """Test that the `name` and `state_id` 
        attributes of a new `City` object are initialized 
        to empty strings."""
        city = City()
        self.assertEqual(city.name, '')
        self.assertEqual(city.state_id, '')

if __name__ == '__main__':
    unittest.main()
