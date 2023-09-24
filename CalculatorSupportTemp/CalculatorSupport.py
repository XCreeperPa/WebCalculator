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


def annotated_calc_main(expression: str, _format=True, check=True, format_in_return=False):
    # 构建运算符优先级字典
    precedence_dict = {}
    for index, sublist in enumerate(precedence):
        for op in sublist:
            precedence_dict[op] = index

    # 格式化输入字符串，并根据需要更新返回值
    if _format:
        if format_in_return:
            expression = format_in_return = calc_format(obj=expression)
        else:
            expression = calc_format(obj=expression)

    # 存储原表达式
    original_expression = expression
    # 初始化数字和操作符栈
    number_stack = Stack()
    operators_stack = Stack()
    operators: list[Type[Operators.Operator]] = list()
    # 获取所有的操作符类
    for _class in Operators.__dict__.values():
        if issubclass(_class, Operators.Operator):
            operators.append(_class)
    while True:  # 循环处理整个表达式
        for operator in operators:  # 遍历所有的操作符
            match = operator.part_match(expression)  # 尝试匹配当前操作符
            if match:  # 如果匹配成功
                operand, expression = match  # 提取操作数和剩余的表达式
                if operand is not None:  # 如果操作数存在
                    number_stack.push(operand)  # 将操作数压入数字栈
                if operators_stack.size() == 0:  # 如果操作符栈为空
                    operators_stack.push(operator)  # 直接将操作符压入操作符栈
                else:  # 否则，需要根据优先级来决定如何处理操作符
                    operator_precedence = get_precedence(operator, precedence_dict)  # 获取当前操作符的优先级
                    while True:  # 循环处理栈顶的操作符
                        if operators_stack.size() < 1:  # 如果操作符栈为空
                            operators_stack.push(operator)  # 将当前操作符压入操作符栈
                            break
                        elif operator_precedence <= get_precedence(operators_stack.top_element(),
                                                                   precedence_dict):  # 如果当前操作符的优先级小于或等于栈顶的操作符的优先级
                            calc_operator: Type[Operators.Operator] = operators_stack.pop()  # 弹出栈顶的操作符
                            if issubclass(calc_operator,
                                          Operators.Mark) and calc_operator.execute is not None:  # 如果需要执行特定的操作
                                exec(calc_operator.execute)
                            calc_operand = number_stack.mul_pop(calc_operator.calculate_arguments_count)  # 获取足够数量的操作数
                            calc_result = calc_operator.calculate(*calc_operand)  # 执行计算
                            if calc_result is not None:  # 如果计算结果存在
                                number_stack.push(calc_result)  # 将计算结果压入数字栈
                        else:  # 如果当前操作符的优先级大于栈顶的操作符的优先级
                            operators_stack.push(operator)  # 将当前操作符压入操作符栈
                            break
        _result = RationalNumber.parse_digits_part(expression)  # 尝试从表达式中提取数字
        if _result and not isinstance(_result, bool):  # 如果成功提取了数字
            operand, expression = _result  # 提取操作数和剩余的表达式
            number_stack.push(operand)  # 将操作数压入数字栈
        if operators_stack.size() == 0:  # 如果操作符栈为空，说明表达式处理完成
            break

    # 返回结果
    if format_in_return:
        return [number_stack.top_element(), format_in_return]
    else:
        return [number_stack.top_element()]

    pass
