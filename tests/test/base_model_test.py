#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):

    def test_init(self):
        """test method"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
