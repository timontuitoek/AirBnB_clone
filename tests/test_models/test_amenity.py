#!/usr/bin/python3
"""
test class amenity
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import models


class TestAmenity(unittest.TestCase):
    """
    test cases
    """
    def test_class(self):
        """
        Tests if the class is named correctly.
        """
        amenity1 = Amenity()
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_parent_class(self):
        """
        Tests if class inherits from BaseModel.
        """
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))

    def test_module_Docs(self):
        """
        test module docs
        """
        moduleDoc = (
                __import__("models.amenity")
                .amenity.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_class_Docs(self):
        """
        test documentation
        """
        classDoc = (
                __import__("models.amenity")
                .amenity.Amenity.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_name_Type(self):
        """
        test name type
        """
        amenity = Amenity()
        self.assertIs(type(amenity.name), str)
