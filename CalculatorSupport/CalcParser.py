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
