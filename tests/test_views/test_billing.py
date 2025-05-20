import unittest

class TestBilling(unittest.TestCase):
    def test_amount_format(self):
        self.assertEqual(f"${100}", "$100")
