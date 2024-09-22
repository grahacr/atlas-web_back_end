import unittest
from calculator import Calculator
from unittest.mock import patch

class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2), 3)
        self.assertEqual(self.calculator.add(-1, -2), -3)
        self.assertEqual(self.calculator.add(-1, 2), 1)
    
    def test_division(self):
        self.assertEqual(self.calculator.divide(21, 7), 3)
        self.assertEqual(self.calculator.divide(-12, -4), -3)
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
