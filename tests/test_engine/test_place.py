#!/usr/bin/env python3
"""Unit tests for the Place class in the models module"""

import unittest
from models.place import Place
from models import BaseModel

class TestPlace(unittest.TestCase):
    """Test case for the Place class"""

    def test_inheritance(self):
        """Test if Place inherits from BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_attribute_creation(self):
        """Test if attributes are created in Place class"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_attribute_values(self):
        """Test if attributes have the correct default values"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.amenity_ids, [])

    def test_attribute_types(self):
        """Test the data types of attributes in Place class"""
        place = Place()
        self.assertTrue(type(place.city_id) == str)
        self.assertTrue(type(place.user_id) == str)
        self.assertTrue(type(place.name) == str)
        self.assertTrue(type(place.description) == str)
        self.assertTrue(type(place.number_rooms) == int)
        self.assertTrue(type(place.number_bathrooms) == int)
        self.assertTrue(type(place.max_guest) == int)
        self.assertTrue(type(place.price_by_night) == int)
        self.assertTrue(type(place.latitude) == float)
        self.assertTrue(type(place.longitude) == float)
        self.assertTrue(type(place.amenity_ids) == list)

if __name__ == "__main__":
    unittest.main()
