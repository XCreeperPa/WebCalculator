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
# from CalculatorSupportBeta import calc_main

from CalculatorSupport import calc_main, log, CalcType


# @pysnooper.snoop(depth=2)
# @pysnooper.snoop(os.path.abspath(r".\log.log"), depth=2)
def main():
    _io = log.create_string_io()
    # _result = calc_main("(1+1-1)/0+1")
    # print(log.read())
    # _result = calc_main("1+0/0+1")
    # print(log.read())
    _result = calc_main("()(1/0)")
    print(log.read())


# def calc_fraction_test():
#     from CalculatorSupport import calc_main, set_DefaultCalcType, Fraction
#     set_DefaultCalcType(Fraction)
#     calc_main("1/2+1")


def pre_test():
    print(0.1 + 0.2)
    print(calc_main("0.1+0.2"))


def formatter_test():
    from CalculatorSupport import CalcFormatter
    CalcFormatter.test_log_with_docstring(_f=None)


def calc_main_user_test():
    log.create_string_io()
    while True:
        calc_main(input("(Calc)>> "))
        print(log.read())


# print(cards())
# print(calc_main("sin(1)"))
# print(calc_main("sin(1+1)"))
# print(Utils.debug(calc_main, ("log2(1+1)",)))
if __name__ == '__main__':
    CalcType.set_fraction()
    # cards()
    # calc
    # _fraction_test()
    # pre_test()
    # formatter_test()
    calc_main_user_test()
