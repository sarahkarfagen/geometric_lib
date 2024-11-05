#python -m unittest test_square.py
import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):

    def test_area_positive_value(self):
        self.assertEqual(area(10), 100)
        self.assertEqual(area(5), 25)

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_area_negative_value(self):
        self.assertEqual(area(-5), 25)
        self.assertEqual(area(-3), 9)

    def test_perimeter_positive_value(self):
        self.assertEqual(perimeter(10), 40)
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative_value(self):
        self.assertEqual(perimeter(-5), -20)
        self.assertEqual(perimeter(-3), -12)

if __name__ == '__main__':
    unittest.main()
