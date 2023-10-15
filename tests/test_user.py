class TestUser(unittest.TestCase):
    """Test suite for the User class"""
    
    def test_inheritance(self):
        """Test User class inheritance from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_attr(self):
        """Test if User class attributes are created"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_attr_value(self):
        """Test User class attribute default values"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_att_type(self):
        """Test the data type of User class attributes"""
        user = User()
        self.assertTrue(type(user.email) == str)
        self.assertTrue(type(user.password) == str)
        self.assertTrue(type(user.first_name) == str)
        self.assertTrue(type(user.last_name) == str)

if __name__ == "__main__":
    unittest.main()
