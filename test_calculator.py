import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test add method
    def test_add_1(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_2(self):
        self.assertEqual(self.calc.add(1, -1), 0)

    def test_add_3(self):
        self.assertEqual(self.calc.add(-5, 2), -3)

    def test_add_4(self):
        self.assertEqual(self.calc.add(-4, -2), -6)

    # Test subtract method
    def test_subtract_1(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)

    def test_subtract_3(self):
        self.assertEqual(self.calc.subtract(-2, 1), -3)

    def test_subtract_4(self):
        self.assertEqual(self.calc.subtract(1, -2), 3)

    # Test multiply method
    def test_multiply_1(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(2, -3), -6)

    def test_multiply_3(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiply_4(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiply_5(self):
        self.assertEqual(self.calc.multiply(0, 1), 0)

    def test_multiply_6(self):
        self.assertEqual(self.calc.multiply(0, -3), 0)

    def test_multiply_7(self):
        self.assertEqual(self.calc.multiply(1, 0), 0)

    def test_multiply_8(self):
        self.assertEqual(self.calc.multiply(-3, 0), 0)

    # Test divide method
    def test_divide_1(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_3(self):
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_divide_4(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_5(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_6(self):
        self.assertEqual(self.calc.divide(0, 10), 0)

    # Test modulo method
    def test_modulo_1(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(10, 0)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_3(self):
        self.assertEqual(self.calc.modulo(10, -3), 1)

    def test_modulo_4(self):
        self.assertEqual(self.calc.modulo(-10, 3), -1)

    def test_modulo_5(self):
        self.assertEqual(self.calc.modulo(-10, -3), -1)

    def test_modulo_6(self):
        self.assertEqual(self.calc.modulo(0, 10), 0)


if __name__ == "__main__":
    unittest.main()
