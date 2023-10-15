class TestAmenity(unittest.TestCase):
    """Test suite for the Amenity class"""

    def test_inheritance(self):
        """Test if the Amenity class inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Test if Amenity class attributes are present"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name')

    def test_attr_type(self):
        """Test the data type of the 'name' attribute"""
        amenity = Amenity()
        self.assertTrue(type(amenity.name) == str)

    def test_attr_values(self):
        """Test if 'name' attribute has the correct default value"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
