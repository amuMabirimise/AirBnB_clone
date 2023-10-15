#!/usr/bin/env python3
"""Test case for the FileStorage class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import models.engine
import models.engine.file_storage

class TestFileStorage(unittest.TestCase):
    """Unit tests for the file storage methods"""

    def test_attr(self):
        """Test the proper initialization of attributes in the FileStorage class"""
        file_store = FileStorage()
        self.assertIsInstance(file_store, FileStorage)
        self.assertTrue(hasattr(file_store, "__file_path"))
        self.assertTrue(hasattr(file_store, "__objects")

    def test_attr_type(self):
        """Verify the data types of attributes in the FileStorage class"""
        file_store = FileStorage()
        self.assertEqual(file_store.__file_path, "file.json")
        self.assertTrue(type(file_store.__objects) == dict)

    def test_all(self):
        """Evaluate the 'all' method functionality in the FileStorage class"""
        file_store = FileStorage()
        all_instance = file_store.all()
        self.assertIsInstance(all_instance, dict)
        self.assertIs(all_instance, file_store.__objects)

    def test_new(self):
        """Examine the functionality of the 'new' method in the FileStorage class"""
        file_store = FileStorage()
        base_model = BaseModel()
        file_store.new(base_model)
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, file_store.__objects)

if __name__ == "__main__":
    unittest.main()
