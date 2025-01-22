import unittest
from app import calculate_addition, calculate_subtraction, app

class TestApp(unittest.TestCase):
    def test_calculate_addition(self):
        self.assertEqual(calculate_addition(2, 3), 5)

    def test_calculate_subtraction(self):
        self.assertEqual(calculate_subtraction(5, 3), 2)

if __name__ == "__main__":
    unittest.main()
