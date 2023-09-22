import unittest
from module import Expression, RationalNumber


# 测试用例
class TestExpression(unittest.TestCase):

    # 测试加法
    def test_addition(self):
        self.assertEqual(Expression.calculate("3 + 4"), RationalNumber(7, 1))
        self.assertEqual(Expression.calculate("-3 + 4"), RationalNumber(1, 1))
        self.assertEqual(Expression.calculate("3 + -4"), RationalNumber(-1, 1))
        self.assertEqual(Expression.calculate("-3 + -4"), RationalNumber(-7, 1))
        self.assertEqual(Expression.calculate("0 + 0"), RationalNumber(0, 1))

    # 测试减法
    def test_subtraction(self):
        self.assertEqual(Expression.calculate("5 - 2"), RationalNumber(3, 1))
        self.assertEqual(Expression.calculate("-5 - 2"), RationalNumber(-7, 1))
        self.assertEqual(Expression.calculate("5 - -2"), RationalNumber(7, 1))
        self.assertEqual(Expression.calculate("-5 - -2"), RationalNumber(-3, 1))
        self.assertEqual(Expression.calculate("0 - 0"), RationalNumber(0, 1))

    # 测试乘法
    def test_multiplication(self):
        self.assertEqual(Expression.calculate("3 * 2"), RationalNumber(6, 1))
        self.assertEqual(Expression.calculate("-3 * 2"), RationalNumber(-6, 1))
        self.assertEqual(Expression.calculate("3 * -2"), RationalNumber(-6, 1))
        self.assertEqual(Expression.calculate("-3 * -2"), RationalNumber(6, 1))
        self.assertEqual(Expression.calculate("0 * 0"), RationalNumber(0, 1))

    # 测试除法
    def test_division(self):
        self.assertEqual(Expression.calculate("8 / 2"), RationalNumber(4, 1))
        self.assertEqual(Expression.calculate("-8 / 2"), RationalNumber(-4, 1))
        self.assertEqual(Expression.calculate("8 / -2"), RationalNumber(-4, 1))
        self.assertEqual(Expression.calculate("-8 / -2"), RationalNumber(4, 1))

        with self.assertRaises(ZeroDivisionError):
            Expression.calculate("8 / 0")

    # 测试括号
    def test_parentheses(self):
        self.assertEqual(Expression.calculate("2 * ( 3 + 1 )"), RationalNumber(8, 1))
        self.assertEqual(Expression.calculate("2 * ( - 3 + 1 )"), RationalNumber(-4, 1))
        self.assertEqual(Expression.calculate("( 3 + 1 ) * 2"), RationalNumber(8, 1))
        self.assertEqual(Expression.calculate("( - 3 + 1 ) * 2"), RationalNumber(-4, 1))
        self.assertEqual(Expression.calculate("0 * ( 0 + 0 )"), RationalNumber(0, 1))

    # 测试异常处理
    def test_exception_handling(self):
        with self.assertRaises(ZeroDivisionError):
            Expression.calculate("8 / 0")
        with self.assertRaises(ZeroDivisionError):
            Expression.calculate("( 8 / 0 ) + 1")
        with self.assertRaises(ZeroDivisionError):
            Expression.calculate("1 + ( 8 / 0 )")
        with self.assertRaises(ZeroDivisionError):
            Expression.calculate("( 0 / 0 )")
        with self.assertRaises(ZeroDivisionError):
            Expression.calculate("1 / ( 2 - 2 )")

    # 测试压力测试
    def test_stress_test(self):
        large_number = 10 ** 12  # 一兆
        self.assertEqual(Expression.calculate(f"{large_number} + {large_number}"), RationalNumber(2 * large_number, 1))
        self.assertEqual(Expression.calculate(f"{large_number} - {large_number}"), RationalNumber(0, 1))
        self.assertEqual(Expression.calculate(f"{large_number} * {large_number}"),
                         RationalNumber(large_number ** 2, 1))
        self.assertEqual(Expression.calculate(f"{large_number} / {large_number}"), RationalNumber(1, 1))
        self.assertEqual(Expression.calculate(f"{large_number} / 1"), RationalNumber(large_number, 1))
