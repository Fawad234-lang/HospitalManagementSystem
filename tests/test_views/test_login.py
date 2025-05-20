import unittest
from app.services.auth import authenticate_user

class TestLogin(unittest.TestCase):
    def test_valid_login(self):
        self.assertTrue(authenticate_user("admin", "admin123"))

    def test_invalid_login(self):
        self.assertFalse(authenticate_user("wrong", "123"))
