#!/usr/bin/python3

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_attributes_initialized(self):
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_unique_ids(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

if __name__ == '__main__':
    unittest.main()
