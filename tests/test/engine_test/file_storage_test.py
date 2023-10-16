#!/usr/bin/python3
""" Tests for FileStorage"""

import unittest
from models.engine.file_storage import FileStorage


class TestFilestorage(unittest.TestCase):
    """Test if the 'all' method returns a dictionary"""
    def test_all(self):
        storage = FileStorage()
        result = storage.all()
         self.assertIsInstance(result, dict)
