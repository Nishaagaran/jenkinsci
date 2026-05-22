import unittest
import math
from calculator import Calculator


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_mixed_signs(self):
        self.assertEqual(self.calc.add(-5, 3), -2)

    def test_zero(self):
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_floats(self):
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=10)

    def test_large_numbers(self):
        self.assertEqual(self.calc.add(10**18, 10**18), 2 * 10**18)


class TestSubtract(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_positive_result(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_same_numbers(self):
        self.assertEqual(self.calc.subtract(5, 5), 0)

    def test_negative_operands(self):
        self.assertEqual(self.calc.subtract(-3, -5), 2)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(7, 0), 7)


class TestMultiply(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_by_zero(self):
        self.assertEqual(self.calc.multiply(999, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_mixed_signs(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_by_one(self):
        self.assertEqual(self.calc.multiply(42, 1), 42)

    def test_floats(self):
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.5), 0.25)


class TestDivide(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_exact_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_float_result(self):
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333, places=9)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_zero_dividend(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_negative_numerator(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_negative_denominator(self):
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_both_negative(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_float_operands(self):
        self.assertAlmostEqual(self.calc.divide(1.0, 4.0), 0.25)


class TestPower(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_positive_exponent(self):
        self.assertEqual(self.calc.power(2, 10), 1024)

    def test_zero_exponent(self):
        self.assertEqual(self.calc.power(99, 0), 1)

    def test_exponent_one(self):
        self.assertEqual(self.calc.power(42, 1), 42)

    def test_negative_exponent(self):
        self.assertAlmostEqual(self.calc.power(2, -1), 0.5)

    def test_zero_base(self):
        self.assertEqual(self.calc.power(0, 5), 0)

    def test_negative_base_even_exp(self):
        self.assertEqual(self.calc.power(-2, 2), 4)

    def test_negative_base_odd_exp(self):
        self.assertEqual(self.calc.power(-2, 3), -8)

    def test_fractional_exponent(self):
        self.assertAlmostEqual(self.calc.power(4, 0.5), 2.0)


class TestModulo(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_basic(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_even_division(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(5, 0)

    def test_zero_dividend(self):
        self.assertEqual(self.calc.modulo(0, 5), 0)

    def test_negative_dividend(self):
        self.assertEqual(self.calc.modulo(-7, 3), 2)

    def test_larger_divisor(self):
        self.assertEqual(self.calc.modulo(3, 10), 3)


class TestSquareRoot(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_perfect_square(self):
        self.assertEqual(self.calc.square_root(9), 3.0)

    def test_zero(self):
        self.assertEqual(self.calc.square_root(0), 0.0)

    def test_one(self):
        self.assertEqual(self.calc.square_root(1), 1.0)

    def test_non_perfect_square(self):
        self.assertAlmostEqual(self.calc.square_root(2), math.sqrt(2))

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

    def test_large_number(self):
        self.assertAlmostEqual(self.calc.square_root(1e10), 1e5)

    def test_float_input(self):
        self.assertAlmostEqual(self.calc.square_root(0.25), 0.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
