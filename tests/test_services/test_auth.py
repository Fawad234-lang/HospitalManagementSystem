import unittest
from app.services.auth import register_user, authenticate_user

class TestAuth(unittest.TestCase):
    def test_register_new_user(self):
        self.assertTrue(register_user("testuser", "test123"))

    def test_register_duplicate(self):
        register_user("testuser2", "abc")
        self.assertFalse(register_user("testuser2", "abc"))

    def test_authenticate_existing(self):
        register_user("authuser", "pass")
        self.assertTrue(authenticate_user("authuser", "pass"))
