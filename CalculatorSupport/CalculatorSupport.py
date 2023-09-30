import decimal
import logging

import CalcFormatter
from Constants import *
from LoopFlags import LoopFlagsGroup
from OperatorPrecedence import precedence, Precedence
from Operators import *
from RationalNumber import *
from Stack import *
from Utils import *

decimal_context = decimal.getcontext()
decimal_context.prec = 30  # 设置全局精度(单位:小数点后的位数)

Pi = PiApproximation()
E = EulerNumber()

DefaultCalcType: type = decimal.Decimal

precedence = Precedence(precedence)  # 构造优先级


def calc_main(expression: str, _format=True, _print=True):
    """主处理函数"""

    def set_operator(_v: type[Operator]):
        nonlocal operator
        operator = _v

    # 格式化输入字符串，并根据需要更新返回值
    if _format:
        expression = calc_format(expression=expression)

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

    # if format_in_return:
    #     return [nums.top_element(), format_in_return]
    # else:
    #     return [nums.top_element()]
    # 返回结果
    if nums.size() == 1:
        print(f"output:{nums.top_element()}")
        return str(nums.top_element())
    else:
        print(nums.stack)
        return str(nums.stack)


# def calc_format(expression: str):
#     """语法糖解释函数"""
#     # 去掉字符串末尾的等号字符 '='
#     while expression[-1] == '=':
#         expression = expression[:-1]
#
#     # 将字符串中的 'log10' 替换为 'logX'
#     expression = expression.replace('log10', 'logX')
#
#     # 将字符串中的 'log2' 替换为 'logII'
#     expression = expression.replace('log2', 'logII')
#
#     # 在整个字符串外加上圆括号 '(' 和 ')'
#     expression = '(' + expression + ')'
#
#     i = 0
#     while i < len(expression) - 1:
#         # 处理数字后面跟着小数点的情况，补充缺失的零
#         if expression[i] not in '1234567890' and expression[i + 1] == '.':
#             expression = expression[:i + 1] + '0' + expression[i + 1:]
#
#         # 处理小数点后面不是数字的情况，补充缺失的零
#         if expression[i] == '.' and expression[i + 1] not in '1234567890':
#             expression = expression[:i + 1] + '0' + expression[i + 1:]
#
#         # 将连续的两个乘号 '**' 替换为 '^'
#         if expression[i] == expression[i + 1] == '*':
#             expression = expression[:i] + '^' + expression[i + 2:]
#
#         # 将连续的两个除号 '//' 替换为 '|'
#         if expression[i] == expression[i + 1] == '/':
#             expression = expression[:i] + '|' + expression[i + 2:]
#
#         # 将方括号 '[' 或 '{' 替换为 '('
#         if expression[i] in '[{':
#             expression = expression[:i] + '(' + expression[i + 1:]
#
#         # 将方括号 ']' 或 '}' 替换为 ')'
#         if expression[i] in ']}':
#             expression = expression[:i] + ')' + expression[i + 1:]
#
#         # 处理连续的两个减号 '--'，将其替换为加号 '+'
#         if expression[i] == expression[i + 1] == '-':
#             expression = expression[:i] + '+' + expression[i + 2:]
#
#             # 如果前一个字符和当前字符都是加号 '+'
#             # 则将前一个加号去除，并继续处理下一个字符
#             if expression[i - 1] == expression[i] == '+':
#                 expression = expression[:i] + expression[i + 1:]
#                 continue
#
#         # 处理连续的两个加号 '++'，将其替换为空字符 ''
#         if expression[i] == expression[i + 1] == '+':
#             expression = expression[:i] + expression[i + 1:]
#             continue
#
#         # 处理加号 '+' 和减号 '-' 之间的情况，将加号去除
#         if expression[i] == '+' and expression[i + 1] == '-':
#             expression = expression[:i] + expression[i + 1:]
#             continue
#
#         # 处理操作符前面是左括号并且后面是减号 '-' 的情况，
#         # 将减号替换为零 '0'
#         if expression[i] in '([{' and expression[i + 1] == '-':
#             expression = expression[:i + 1] + '0' + expression[i + 1:]
#
#         # 处理减号 '-' 后面不是括号或数字的情况，
#         # 在减号后添加一个零 '0'，然后补全括号
#         if expression[i + 1] == '-' and not expression[i] in '()[]{}1234567890':
#             expression = expression[:i + 1] + '(0' + expression[i + 1:]
#             j = i + 4
#             parentheses = 0
#             while True:
#                 j += 1
#                 if j >= len(expression):
#                     break
#                 if expression[j] in '([{':
#                     parentheses += 1
#                 if expression[j] in ')]}':
#                     parentheses -= 1
#                 if expression[j] in '+-' and not parentheses:
#                     break
#             expression = expression[:j] + ')' + expression[j:]
#
#         # 处理百分号 '%' 前面是数字而后面不是括号或数字的情况，
#         # 将百分号替换为乘号 '*' 和 0.01，然后补全括号
#         if i > 0 and expression[i - 1] in '1234567890' and expression[i] == '%' and not expression[
#                                                                                             i + 1] in '([{1234567890':
#             expression = expression[:i] + '*0.01)' + expression[i + 1:]
#             j, i = i - 2, i - 1
#             while expression[j] in '1234567890.':
#                 j -= 1
#                 if j < 0:
#                     break
#             expression = expression[:j + 1] + '(' + expression[j + 1:]
#
#         # 处理连续的感叹号 '!' 和数字的情况，将感叹号替换为乘号 '*'
#         elif expression[i] == '!' and expression[i + 1] in '1234567890':
#             expression = expression[:i + 1] + '*' + expression[i + 1:]
#
#         # 处理右括号、右方括号和右大括号之后紧跟左括号、左方括号和左大括号的情况，
#         # 在右括号后添加乘号 '*'
#         if expression[i] in ')]}' and expression[i + 1] in '([{':
#             expression = expression[:i + 1] + '*' + expression[i + 1:]
#
#         # 处理右括号、右方括号和右大括号之后紧跟数字的情况，
#         # 在右括号后添加乘号 '*'
#         if expression[i] in ')]}' and expression[i + 1] in '1234567890':
#             expression = expression[:i + 1] + '*' + expression[i + 1:]
#
#         # 处理 'pi' 后面的情况，根据前一个字符是数字还是其他字符来添加乘号 '*'
#         if i > 0 and expression[i] + expression[i + 1] == 'pi':
#             if expression[i - 1] in '1234567890':
#                 expression = expression[:i] + '*' + str(Pi) + expression[i + 2:]
#             else:
#                 expression = expression[:i] + str(Pi) + expression[i + 2:]
#
#         # 处理 'e' 后面的情况，根据前一个字符是数字还是其他字符来添加乘号 '*'
#         if expression[i + 1] == 'e':
#             if expression[i] in '1234567890':
#                 expression = expression[:i + 1] + '*' + str(E) + expression[i + 2:]
#             else:
#                 expression = expression[:i + 1] + str(E) + expression[i + 2:]
#
#         i += 1  # 移动到下一个字符继续处理
#
#     return expression  # 返回格式化后的字符串
def calc_format(expression: str):
    return CalcFormatter.CalculateFormatter.format(expression)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG

console_handler = logging.StreamHandler()  # 控制台日志
console_handler.setLevel(logging.INFO)  # 设置控制台日志的级别为INFO

console_debug_handler = logging.StreamHandler()  # 控制台debug日志
console_debug_handler.setLevel(logging.DEBUG)  # 设置控制台debug日志的级别为DEBUG

# 创建一个格式化器，定义日志消息的格式
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(log_formatter)
console_debug_handler.setFormatter(log_formatter)

logger.addHandler(console_handler)


# logger.addHandler(console_debug_handler)


def log(_str):
    # logger.info(_str)
    print(_str)


def test():
    import traceback
    import time
    import concurrent.futures

    sleep_time = 0.8
    repeat_time = 1

    class ThreadPoolExecutorWrapper:
        def __init__(self, max_workers=None):
            self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

        def submit(self, func, *args, **kwargs):
            return self.executor.submit(func, *args, **kwargs)

        def map(self, func, *iterables, timeout=None, chunksize=1):
            return self.executor.map(func, *iterables, timeout=timeout, chunksize=chunksize)

        def shutdown(self):
            self.executor.shutdown()

    thread_pool = ThreadPoolExecutorWrapper(max_workers=8)

    # 使用函数，传递日志文件名
    close_log = capture_print_to_file(r'.\test\CalcMainTestLog.txt')

    with open(r".\test\test_expression.txt", "r", encoding="utf-8") as f:
        # print(f.read())
        for line in f.read().split():
            if line.isspace():
                continue
            elif line.strip().startswith("#"):
                print(line.strip())
                continue
            else:
                for i in range(repeat_time):
                    try:
                        print("original_input:" + line.strip())
                        thread_pool.submit(calc_main, line.strip())
                    except Exception:
                        log(traceback.format_exc())
                    time.sleep(sleep_time)
            print("\n", end="")
    log("test done")
    # 在结束时关闭文件并恢复sys.stdout
    close_log()


if __name__ == '__main__':
    # test()

    while True:
        log(calc_main(input("(Calc)>> ")))
