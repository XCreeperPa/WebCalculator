# from typing import Type
# import Operators
# from Constants import *
# from OperatorPrecedence import precedence
# from RationalNumber import *
# from Stack import Stack

from CalculatorSupport0 import *


def get_precedence(operator: Type[Operators.Operator], precedence_dict) -> int | None:
    for index, sub in precedence_dict.items():
        if isinstance(sub, list):
            for sub_op in sub:
                if operator == sub_op:
                    return index
        else:
            if operator == sub:
                return index
    return None


def calc_main(expression: str, _format=True, check=True, format_in_return=False):
    precedence_dict = {}
    for index, sublist in enumerate(precedence):
        for op in sublist:
            precedence_dict[op] = index

    if _format:
        if format_in_return:
            expression = format_in_return = calc_format(obj=expression)  # 格式化输入字符串，并根据需要更新返回值
        else:
            expression = calc_format(obj=expression)  # 仅格式化输入字符串

    original_expression = expression
    number_stack = Stack()
    operators_stack = Stack()
    operators: list[Type[Operators.Operator]] = list()
    for _class in Operators.__dict__.values():
        if issubclass(_class, Operators.Operator):
            operators.append(_class)
    while True:
        for operator in operators:
            match = operator.part_match(expression)
            if match:
                operand, expression = match
                if operand is not None:
                    number_stack.push(operand)
                if operators_stack.size() == 0:
                    operators_stack.push(operator)
                else:
                    operator_precedence = get_precedence(operator, precedence_dict)
                    while True:
                        if operators_stack.size < 1:
                            operators_stack.push(operator)
                            break
                        elif operator_precedence <= get_precedence(operators_stack.top_element(), precedence_dict):
                            calc_operator: Type[Operators.Operator] = operators_stack.pop()
                            if issubclass(calc_operator, Operators.Mark) and calc_operator.execute is not None:
                                exec(calc_operator.execute)
                            calc_operand = number_stack.mul_pop(calc_operator.calculate_arguments_count)
                            calc_result = calc_operator.calculate(*calc_operand)
                            if calc_result is not None:
                                number_stack.push(calc_result)
                        else:
                            operators_stack.push(operator)
                            break
        _result = RationalNumber.parse_digits_part(expression)
        if _result and not isinstance(_result, bool):
            operand, expression = _result
            number_stack.push(operand)
        break
    if format_in_return:
        return [number_stack.top_element(), format_in_return]
    else:
        return [number_stack.top_element()]

    pass
