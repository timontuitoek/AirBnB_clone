#!/usr/bin/python3
"""
import modules
"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    parent class module for test cases
    """
    def test_file_path(self):
        """
        check for correct path of file
        """
        file_storage = FileStorage()
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

if __name__ == "__main__":
    unittest.main()
