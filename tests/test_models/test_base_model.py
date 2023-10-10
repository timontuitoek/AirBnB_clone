#!/usr/bin/python3
"""
import modules
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    """
    parent class module to test for various instances
    of class basemodel
    """
    def test_id_length(self):
        """
        test length
        """
        obj = BaseModel()
        self.assertEqual(len(obj.id), 36)

    def test_id_type(self):
        """
        test type
        """
        obj = BaseModel()
        self.assertIs(type(obj.id), str)

if __name__ == "__main__":
    unittest.main()
