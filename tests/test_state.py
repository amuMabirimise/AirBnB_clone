class TestState(unittest.TestCase):
    """Test case for the State class"""

    def test_inheritance(self):
        """Test if State class inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_attributes(self):
        """Test if State class attributes are present and initialized"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    unittest.main()
