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
from typing import Generator

from .Operators import *
from .RationalNumber import RationalNumber


class CalcParser:
    """仅用于提供数学表达式解析的实现方式, 不在calc_main中实际使用"""
    @staticmethod
    def generator_parser(expression: str, operators: list[type[Operator]]) -> \
            Generator[tuple[type[Operator] | None, str | None, str | None], None, None]:
        def parse():
            nonlocal expression
            while len(expression):
                # 提取操作符
                for operator in operators:
                    match = operator.part_match(expression)  # 尝试匹配当前操作符
                    if match:  # 匹配成功
                        if isinstance(match, (tuple, list)):
                            operands, expression = match
                        yield (operator,) + match
                    else:  # 匹配失败
                        continue
                # 提取数字
                match = RationalNumber.parse_digits_part(expression)
                if match and not isinstance(match, bool):
                    operands, expression = match
                    yield (None,) + match
            pass

        return parse()

    pass


def test():
    from .CalcFormatter import CalculateFormatter
    expression = CalculateFormatter.format("1+1")
    from .Utils import find_all_subclasses
    operators = find_all_subclasses(Operator)
    # print("\n".join(CalcParser.generator_parser(expression, operators)))
    g = CalcParser.generator_parser(expression, operators)
    while True:
        print(next(g))
