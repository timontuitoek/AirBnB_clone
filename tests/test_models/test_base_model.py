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

    def test_created_at_type(self):
        """
        test type
        """
        obj = BaseModel()
        self.assertIs(type(obj.created_at), datetime)

    def test_updated_at_type(self):
        """
        test type
        """
        obj = BaseModel()
        self.assertIs(type(obj.updated_at), datetime)

    def test_to_dict_type(self):
        """
        test type
        """
        obj = BaseModel()
        to_dict_dict = obj.to_dict()
        self.assertIn("__class__", to_dict_dict)
        self.assertIs(type(to_dict_dict["__class__"]), str)

if __name__ == "__main__":
    unittest.main()
