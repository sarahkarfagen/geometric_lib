# python -m unittest .\tests\test_rectangle.py
import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):

    def test_area_positive_values(self):
        self.assertEqual(area(10, 5), 50)
        self.assertEqual(area(3, 7), 21)

    def test_area_zero_side(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(10, 0), 0)

    def test_area_negative_values(self):
        self.assertEqual(area(-5, 4), -20)
        self.assertEqual(area(6, -3), -18)

    def test_perimeter_positive_values(self):
        self.assertEqual(perimeter(10, 5), 30)
        self.assertEqual(perimeter(3, 7), 20)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_negative_values(self):
        self.assertEqual(perimeter(-5, 4), -2)
        self.assertEqual(perimeter(6, -3), 6)

if __name__ == '__main__':
    unittest.main()
