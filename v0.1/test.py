# 定义测试模块
import unittest
from interpreter import *


# 测试用例
class TestOnlineCalculatorBackendComprehensive(unittest.TestCase):

    # 测试加法
    def test_addition(self):
        self.assertEqual(Expression("3 + 4").evaluate(), RationalNumber(7, 1))
        self.assertEqual(Expression("-3 + 4").evaluate(), RationalNumber(1, 1))
        self.assertEqual(Expression("3 + -4").evaluate(), RationalNumber(-1, 1))
        self.assertEqual(Expression("-3 + -4").evaluate(), RationalNumber(-7, 1))
        self.assertEqual(Expression("0 + 0").evaluate(), RationalNumber(0, 1))

    # 测试减法
    def test_subtraction(self):
        self.assertEqual(Expression("5 - 2").evaluate(), RationalNumber(3, 1))
        self.assertEqual(Expression("-5 - 2").evaluate(), RationalNumber(-7, 1))
        self.assertEqual(Expression("5 - -2").evaluate(), RationalNumber(7, 1))
        self.assertEqual(Expression("-5 - -2").evaluate(), RationalNumber(-3, 1))
        self.assertEqual(Expression("0 - 0").evaluate(), RationalNumber(0, 1))

    # 测试乘法
    def test_multiplication(self):
        self.assertEqual(Expression("3 * 2").evaluate(), RationalNumber(6, 1))
        self.assertEqual(Expression("-3 * 2").evaluate(), RationalNumber(-6, 1))
        self.assertEqual(Expression("3 * -2").evaluate(), RationalNumber(-6, 1))
        self.assertEqual(Expression("-3 * -2").evaluate(), RationalNumber(6, 1))
        self.assertEqual(Expression("0 * 0").evaluate(), RationalNumber(0, 1))

    # 测试除法
    def test_division(self):
        self.assertEqual(Expression("8 / 2").evaluate(), RationalNumber(4, 1))
        self.assertEqual(Expression("-8 / 2").evaluate(), RationalNumber(-4, 1))
        self.assertEqual(Expression("8 / -2").evaluate(), RationalNumber(-4, 1))
        self.assertEqual(Expression("-8 / -2").evaluate(), RationalNumber(4, 1))

        with self.assertRaises(ZeroDivisionError):
            Expression("8 / 0").evaluate()

    # 测试括号
    def test_parentheses(self):
        self.assertEqual(Expression("2 * ( 3 + 1 )").evaluate(), RationalNumber(8, 1))
        self.assertEqual(Expression("2 * ( - 3 + 1 )").evaluate(), RationalNumber(-4, 1))
        self.assertEqual(Expression("( 3 + 1 ) * 2").evaluate(), RationalNumber(8, 1))
        self.assertEqual(Expression("( - 3 + 1 ) * 2").evaluate(), RationalNumber(-4, 1))
        self.assertEqual(Expression("0 * ( 0 + 0 )").evaluate(), RationalNumber(0, 1))

    # 测试异常处理
    def test_exception_handling(self):
        with self.assertRaises(ZeroDivisionError):
            Expression("8 / 0").evaluate()
        with self.assertRaises(ZeroDivisionError):
            Expression("( 8 / 0 ) + 1").evaluate()
        with self.assertRaises(ZeroDivisionError):
            Expression("1 + ( 8 / 0 )").evaluate()
        with self.assertRaises(ZeroDivisionError):
            Expression("( 0 / 0 )").evaluate()
        with self.assertRaises(ZeroDivisionError):
            Expression("1 / ( 2 - 2 )").evaluate()

    # 测试压力测试
    def test_stress_test(self):
        large_number = 10 ** 12  # 一兆
        self.assertEqual(Expression(f"{large_number} + {large_number}").evaluate(), RationalNumber(2 * large_number, 1))
        self.assertEqual(Expression(f"{large_number} - {large_number}").evaluate(), RationalNumber(0, 1))
        self.assertEqual(Expression(f"{large_number} * {large_number}").evaluate(),
                         RationalNumber(large_number ** 2, 1))
        self.assertEqual(Expression(f"{large_number} / {large_number}").evaluate(), RationalNumber(1, 1))
        self.assertEqual(Expression(f"{large_number} / 1").evaluate(), RationalNumber(large_number, 1))
