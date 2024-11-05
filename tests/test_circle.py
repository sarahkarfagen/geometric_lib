# python -m unittest .\tests\test_circle.py
import unittest
import math
from circle import area, perimeter

class TestCircle(unittest.TestCase):

    def test_area_positive_radius(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(3), math.pi * 3 * 3)
        self.assertAlmostEqual(area(0.5), math.pi * 0.5 * 0.5)

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_area_negative_radius(self):
        self.assertAlmostEqual(area(-1), math.pi)
        self.assertAlmostEqual(area(-3), math.pi * 3 * 3)

    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3)
        self.assertAlmostEqual(perimeter(0.5), 2 * math.pi * 0.5)

    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative_radius(self):
        self.assertAlmostEqual(perimeter(-1), -2 * math.pi)
        self.assertAlmostEqual(perimeter(-3), -2 * math.pi * 3)

if __name__ == '__main__':
    unittest.main()
