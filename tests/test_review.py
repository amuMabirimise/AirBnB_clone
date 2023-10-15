class TestReview(unittest.TestCase):
    """Test case for the Review class"""

    def test_inheritance(self):
        """Test if Review class inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_attributes(self):
        """Test if Review class attributes are created"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_attr_value(self):
        """Test if Review class attribute default values"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_att_type(self):
        """Test the data type of Review class attributes"""
        review = Review()
        self.assertTrue(type(review.place_id) == str)
        self.assertTrue(type(review.user_id) == str)
        self.assertTrue(type(review.text) == str)

if __name__ == "__main__":
    unittest.main()
