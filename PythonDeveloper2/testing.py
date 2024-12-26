import unittest

def calculate(radius):
    return 3.14*radius*radius

class TestCalculate(unittest.TestCase):

    def test_area(self):
        self.assertEqual(calculate(1), 3.14)
        self.assertEqual(calculate(2), 12.56)
        self.assertEqual(calculate(0), 0)

