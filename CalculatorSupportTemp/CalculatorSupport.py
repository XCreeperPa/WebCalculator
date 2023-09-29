import logging

from CalculatorSupport0 import calc_format  #
from Constants import *
from LoopFlags import LoopFlagsGroup
from OperatorPrecedence import precedence, Precedence
from Operators import *
from RationalNumber import *
from Stack import *
from Utils import *

Pi = PiApproximation()
E = EulerNumber()
precedence = precedence
DefaultCalcType: type = float
precedence = Precedence(precedence)


def calc_main(expression: str, _format=True, check=True, format_in_return=False):
    def set_operator(_v: type[Operator]):
        nonlocal operator
        operator = _v

    # 格式化输入字符串，并根据需要更新返回值
    if _format:
        if format_in_return:
            expression = format_in_return = calc_format(obj=expression)
        else:
            expression = calc_format(obj=expression)

    # 存储原表达式
    original_expression = expression
    log(expression)
    # 初始化数字和操作符栈
    nums = OperandStack()
    ops = OperatorStack()
    # 获取所有的操作符类
    operators: list[type[Operator]] = find_all_subclasses(Operator)
    loop_flags = LoopFlagsGroup()

    loop_flag0 = loop_flags.new()
    while loop_flag0:  # 循环处理整个表达式
        loop_flag1 = loop_flags.new()
        for operator in operators:  # 遍历所有的操作符
            match = operator.part_match(expression)  # 尝试匹配当前操作符

            if execute_check(match):
                execute_complete(match)(globals(), locals())  # 执行Mark
            if not match:  # 匹配失败
                continue

            operands, expression = match  # 提取操作数和剩余的表达式
            if operands is not None:  # 矫正操作数格式
                operands = [DefaultCalcType(operand) if not isinstance(operand, DefaultCalcType) else operand
                            for operand in operands]

            if ops.is_empty():  # 如果操作符栈为空
                ops.push(operator)  # 直接将操作符压入操作符栈
            else:  # 否则，需要根据优先级来决定如何处理操作符
                loop_flag2 = loop_flags.new()
                # 如果当前操作符的优先级小于或等于栈顶的操作符的优先级
                while precedence.get(operator) <= precedence.get(ops.top_element()) and loop_flag2:
                    if operator is RightBracket:
                        pass
                    calc_operator: type[Operator] = ops.pop()  # 弹出栈顶的操作符

                    # if issubclass(calc_operator, Mark) and calc_operator.execute is not None:
                    #     exec(calc_operator.execute)  # 执行Mark
                    if execute_check(calc_operator):
                        execute_complete(calc_operator)(globals(), locals())  # 执行Mark

                    calc_args_count = calc_operator.calc_args_count
                    calc_operand = nums.mul_pop(calc_args_count)  # 获取足够数量的操作数

                    operands_type: type | list[type] | tuple[type] = calc_operator.operands_type
                    if not isinstance(operands_type, (list, tuple)):
                        operands_type = [operands_type] * calc_args_count
                    _index = 0
                    loop_flag3 = loop_flags.new()
                    while _index < calc_args_count and loop_flag3:
                        # noinspection PyTypeHints
                        if not isinstance(calc_operand[_index], operands_type[_index]):
                            calc_operand[_index] = operands_type[_index](calc_operand[_index])
                        _index += 1
                    loop_flag3.end()

                    product = calc_operator.calculate(*calc_operand)  # 执行计算

                    if calc_args_count:
                        _seq = ", "
                        log(f"{calc_operator.__name__}({_seq.join(map(str, calc_operand))}) = {product}")

                    if execute_check(product):
                        execute_complete(product)(globals(), locals())  # 执行Mark
                    # if isinstance(product, type) and issubclass(product, Mark) and product.execute is not None:
                    #     execute: Callable = execute_complete(product)
                    #     execute(globals(), locals())  # 执行Mark
                    #     print(operator)
                    elif product is not None:  # 如果计算结果存在
                        nums.push(product)  # 将计算结果压入数字栈
                    if ops.is_empty():  # 如果操作符栈为空
                        break
                loop_flag2.end()
                ops.push(operator)
                if operands is not None:
                    nums.mul_push(*operands)
            if loop_flag1.break_flag:
                break
        loop_flag1.end()

        # 提取数字
        match = RationalNumber.parse_digits_part(expression)  # 尝试从表达式中提取数字
        if match and not isinstance(match, bool):  # 如果成功提取了数字
            operands, expression = match  # 提取操作数和剩余的表达式
            nums.push(DefaultCalcType(operands))  # 将操作数压入数字栈
        if ops.is_empty():  # 如果操作符栈为空，说明表达式处理完成
            break
    loop_flag0.end()

    # 返回结果
    if format_in_return:
        return [nums.top_element(), format_in_return]
    else:
        return [nums.top_element()]

    pass


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG

console_handler = logging.StreamHandler()  # 控制台日志
console_handler.setLevel(logging.INFO)  # 设置控制台日志的级别为INFO

console_debug_handler = logging.StreamHandler()  # 控制台debug日志
console_debug_handler.setLevel(logging.DEBUG)  # 设置控制台debug日志的级别为DEBUG

# 创建一个格式化器，定义日志消息的格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)
console_debug_handler.setFormatter(formatter)

logger.addHandler(console_handler)


# logger.addHandler(console_debug_handler)


def log(_str):
    # logger.info(_str)
    print(_str)


if __name__ == '__main__':
    # 构建运算符优先级字典

    # log(calc_main("1+(1+1)*2"))
    while True:
        log(calc_main(input()))
