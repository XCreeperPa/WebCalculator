# 本文件是云计算器的一部分。
#
# 云计算器是自由软件：你可以再分发之和/或依照由自由软件基金会发布的 GNU 通用公共许可证修改之，无论是版本 3 许可证，还是（按你的决定）任何以后版都可以。
#
# 发布云计算器是希望它能有用，但是并无保障;甚至连可销售和符合某个特定的目的都不保证。请参看 GNU 通用公共许可证，了解详情。
#
# 你应该随程序获得一份 GNU 通用公共许可证的复本。如果没有，请看 <https://www.gnu.org/licenses/>.
#
# This file is part of WebCalculator.
#
# WebCalculator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# WebCalculator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with WebCalculator. If not, see <https://www.gnu.org/licenses/>.
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

    def __new__(cls):
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
