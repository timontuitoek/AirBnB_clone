#!/usr/bin/python3
"""
test place
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
import unittest
import models


class TestPlace(unittest.TestCase):
    """
    test places
    """
    def test_create_place(self):
        """
        test create place
        """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_attributes_default(self):
        """
        test place attributes default
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_set_place_attributes(self):
        """
        test set place attributes
        """
        place = Place()
        place.city_id = "city_123"
        place.user_id = "user_456"
        place.name = "Cozy Cabin"
        place.description = "A peaceful retreat"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 100
        place.latitude = 35.1234
        place.longitude = -97.5678
        place.amenity_ids = [1, 2, 3]

        self.assertEqual(place.city_id, "city_123")
        self.assertEqual(place.user_id, "user_456")
        self.assertEqual(place.name, "Cozy Cabin")
        self.assertEqual(place.description, "A peaceful retreat")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 35.1234)
        self.assertEqual(place.longitude, -97.5678)
        self.assertEqual(place.amenity_ids, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
