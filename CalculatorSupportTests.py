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
import unittest
from CalculatorSupport.CalculatorSupport import calc_main

BasicTests = {
        # 加法
        "-1+1": "0",
        "1+1": "2",
        "10+20": "30",
        "100+200": "300",
        "-10+-20": "-30",
        "-100+-200": "-300",
        "0+0": "0",
        "1234+5678": "6912",
        "-1234+-5678": "-6912",
        "9999+1": "10000",

        # 减法
        "1-1": "0",
        "10-20": "-10",
        "100-200": "-100",
        "-1-1": "-2",
        "-10--20": "10",
        "-100--200": "100",
        "0-0": "0",
        "1234-5678": "-4444",
        "-1234-5678": "-6912",
        "9999-1": "9998",

        # 乘法
        "1*1": "1",
        "10*20": "200",
        "100*200": "20000",
        "-1*1": "-1",
        "-10*-20": "200",
        "-100*-200": "20000",
        "0*0": "0",
        "1234*5678": "7006652",
        "-1234*5678": "-7006652",
        "9999*1": "9999",

        # 除法
        "1/1": "1",
        "10/20": "0.5",
        "100/200": "0.5",
        "-1/1": "-1",
        "-10/-20": "0.5",
        "-100/-200": "0.5",
        "0/1": "0",

    }
BracketTests = {
    # 加法与括号
    "(1+1)": "2",
    "10+(20+30)": "60",
    "100+(200+300)": "600",
    "-1+(1+2)": "2",
    "(-10+20)+-30": "-20",

    # 减法与括号
    "(1-1)": "0",
    "10-(20-30)": "20",
    "100-(200-300)": "200",
    "-1-(1-2)": "0",
    "(-10-20)-30": "-60",

    # 乘法与括号
    "(1*1)": "1",
    "10*(20*2)": "400",
    "100*(2*3)": "600",
    "-1*(1*2)": "-2",
    "(-10*2)*3": "-60",

    # 除法与括号
    "(1/1)": "1",
    "10/(20/2)": "1",
    "100/(4/2)": "50",
    "-1/(1/2)": "-2",

    # 嵌套括号
    "((1+2)+(3+4))": "10",
    "10*((20-10)*(3-1))": "200",
    "100/((50/2)/5)": "20",
    "-(1+(2-(3+(4-5))))": "-1",
    "(-10-(20-(30-(40-50))))": "10",
    "1/(-1)": "-1"
}

TestsList = [BasicTests, BracketTests]


class MyTestCase(unittest.TestCase):
    def test(self):
        for tests_dict in TestsList:
            for key in tests_dict:
                self.assertEqual(calc_main(key), tests_dict[key])
                print()


if __name__ == '__main__':
    unittest.main()