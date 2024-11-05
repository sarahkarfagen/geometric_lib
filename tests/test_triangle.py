# python -m unittest .\tests\test_triangle.py
import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):

    def test_area_positive_values(self):
        self.assertEqual(area(10, 5), 25)
        self.assertEqual(area(6, 3), 9)

    def test_area_zero_base_or_height(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(10, 0), 0)

    def test_area_negative_values(self):
        self.assertEqual(area(-10, 5), -25)
        self.assertEqual(area(10, -5), -25)
        self.assertEqual(area(-6, -3), 9)

    def test_perimeter_positive_values(self):
        self.assertEqual(perimeter(10, 8, 6), 24)
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0, 8, 6), 14)
        self.assertEqual(perimeter(10, 0, 6), 16)
        self.assertEqual(perimeter(10, 8, 0), 18)

    def test_perimeter_negative_values(self):
        self.assertEqual(perimeter(-10, 8, 6), 4)
        self.assertEqual(perimeter(10, -8, 6), 8)
        self.assertEqual(perimeter(10, 8, -6), 12)

if __name__ == '__main__':
    unittest.main()
