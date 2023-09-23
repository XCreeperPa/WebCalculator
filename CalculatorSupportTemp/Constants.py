import math

NAN = math.nan
INF = math.inf


class PiApproximation(float):
    DEFAULT = math.pi

    def __new__(cls):
        super().__new__(cls, cls.DEFAULT)

    @staticmethod
    def calculate_pi_leibniz(iterations=100):
        """莱布尼茨公式"""
        pi_estimate = 0
        sign = 1

        for i in range(iterations):
            term = 1 / (2 * i + 1)
            pi_estimate += sign * term
            sign *= -1

        return 4 * pi_estimate

    @staticmethod
    def chudnovsky_formula(iterations=100):
        """楚德诺夫斯基算法"""
        k = 0
        sum_term = 0
        while k < iterations:
            numerator = (-1) ** k * math.factorial(6 * k) * (545140 - 11380 * k)
            denominator = math.factorial(k) ** 3 * math.factorial(3 * k) * 640320 ** (3 * k + 3 / 2)
            term = numerator / denominator
            sum_term += term
            k += 1

        pi_approximation = 1 / (12 * sum_term)
        return pi_approximation

    def calculate(self):
        """计算pi的近似值"""
        return self.chudnovsky_formula()


class EulerNumber(float):
    DEFAULT = math.e

    def __new__(cls, _value):
        return super().__new__(cls, cls.DEFAULT)

    @staticmethod
    def calculate_e_taylor(iterations=100):
        """泰勒级数法计算"""
        e_estimate = 1
        factorial = 1

        for i in range(1, iterations):
            factorial *= i
            e_estimate += 1 / factorial

        return e_estimate

    def calculate(self):
        """计算e的近似值"""
        return self.calculate_e_taylor()
