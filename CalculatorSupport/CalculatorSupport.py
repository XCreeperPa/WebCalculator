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
import decimal
import fractions

from .CalcFormatter import CalculateFormatter
from .CalcTracker import calc_tracker
from .Constants import *
from .ExpressionOperateInscriber import ExpressionOperateInscriber
from .Logger import Logger, Message
from .LoopFlags import LoopFlagsGroup
from .OperatorPrecedence import operator_precedence, OperatorPrecedence
from .Operators import *
from .RationalNumber import *
from .Stack import *
from .Utils import find_all_subclasses, capture_print_to_file

decimal_context = decimal.getcontext()
decimal_context.prec = 30  # 设置全局精度(单位:小数点后的位数)

Pi = PiApproximation()
E = EulerNumber()


# Decimal = decimal.Decimal
# Fraction = fractions.Fraction
# DefaultCalcType: type = decimal.Decimal
#
#
# def set_DefaultCalcType(v: type):
#     global DefaultCalcType
#     DefaultCalcType = v
class CalcType:
    Decimal = decimal.Decimal
    Fraction = fractions.Fraction
    calc_type = Decimal

    @classmethod
    def set_calc_type(cls, v: type):
        cls.calc_type = v

    @classmethod
    def set_decimal(cls):
        cls.set_calc_type(cls.Decimal)

    @classmethod
    def set_fraction(cls):
        cls.set_calc_type(cls.Fraction)

    def __new__(cls, *args, **kwargs):
        return cls.calc_type(*args, **kwargs)


operator_precedence = OperatorPrecedence(operator_precedence)  # 构造优先级
log = Logger()


def calc_main(expression: str, _format=True, _print=True, repeat_times: int = 3):
    """主处理函数"""

    def set_operator(_v: type[Operator]):
        nonlocal operator
        operator = _v

    loop_flags.clear()
    # 格式化输入字符串，并根据需要更新返回值
    if _format:
        try:
            expression = calc_format(expression=expression)
        except Exception as e:
            log.log_python_error(e)

    if not len(expression):
        return 0

    # 存储原表达式
    original_expression = expression
    log(expression)
    record = ExpressionOperateInscriber(original_expression)
    # 初始化数字和操作符栈
    # expression_stack = ExpressionStack(original_expression)
    nums = OperandStack()
    ops = OperatorStack()
    # 获取所有的操作符类
    operators: list[type[Operator]] = find_all_subclasses(Operator)

    repeat_count = 0  # 防止死循环
    over_repeat: Exception | None = None  # loop over repeat flag
    loop_flag0 = loop_flags.new("loop_flag0")
    while loop_flag0:  # 循环处理整个表达式
        if repeat_count > repeat_times:
            operate_log = f"{record.get_former_differ_expression(0, record.size)}"
            log.log_calc_error(original_expression)
            log.log_calc_error("~" * len(operate_log) + "^" * (len(original_expression) - len(operate_log)))
            over_repeat = SyntaxError("语法错误: 无法识别")
            loop_flags.break_all()
            break
        loop_flag1 = loop_flags.new("loop_flag1")
        for operator in operators:  # 遍历所有的操作符
            match = operator.part_match(expression)  # 尝试匹配当前操作符

            if execute_check(match):
                execute_complete(match)(globals(), locals())  # 执行Mark
            if not match:  # 匹配失败
                continue

            repeat_count = 0
            operands, expression = match  # 提取操作数和剩余的表达式
            if operands is not None:  # 矫正操作数格式
                operands = [CalcType(operand) if not isinstance(operand, CalcType) else operand
                            for operand in operands]
            match_operator: type[Operator] = operator  # for record 记录运算符
            match_operands = operands  # for record 记录运算子

            if ops.is_empty():  # 如果操作符栈为空
                ops.push(operator)  # 直接将操作符压入操作符栈
            else:  # 否则，需要根据优先级来决定如何处理操作符
                loop_flag2 = loop_flags.new("loop_flag2")
                # 如果当前操作符的优先级小于或等于栈顶的操作符的优先级
                while operator_precedence.get(operator) <= operator_precedence.get(ops.top_element()) and loop_flag2:
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
                    loop_flag3 = loop_flags.new("loop_flag3")
                    while _index < calc_args_count and loop_flag3:
                        if _index >= len(calc_operand) or _index >= len(operands_type):
                            operate_log = f"{record.get_former_differ_expression(0, record.size)}"
                            log.log_calc_error(original_expression)
                            log.log_calc_error("~" * len(operate_log) + "^" * (len(original_expression) - len(operate_log)))
                            over_repeat = SyntaxError("语法错误: 无法识别")
                            loop_flags.break_all()
                            break
                        # noinspection PyTypeHints
                        if not isinstance(calc_operand[_index], operands_type[_index]):
                            calc_operand[_index] = operands_type[_index](calc_operand[_index])
                        _index += 1
                    loop_flag3.end()

                    try:
                        product = calc_operator.calculate(*calc_operand)  # 执行计算
                    except Exception as e:
                        if calc_args_count:
                            operator_log = f"{calc_operator.__name__}({', '.join(map(str, calc_operand))})"
                            log.log_calc_error(operator_log)
                            log.log_calc_error("^" * len(operator_log))
                        else:
                            operator_log = f"{calc_operator.__name__}"
                            log.log_calc_error(operator_log)
                            log.log_calc_error("^" * len(operator_log))
                        # log(e.__repr__())
                        log.log_calc_error(e.__repr__())
                        # log(traceback.format_exc())
                        calc_tracker(calc_operator, record, operator_precedence, log)
                        return e

                    if calc_args_count:
                        log(f"{calc_operator.__name__}({', '.join(map(str, calc_operand))}) = {product}")

                    if execute_check(product):
                        execute_complete(product)(globals(), locals())  # 执行Mark
                    elif product is not None:  # 如果计算结果存在
                        nums.push(product)  # 将计算结果压入数字栈
                    if ops.is_empty():  # 如果操作符栈为空
                        break
                loop_flag2.end()
                ops.push(operator)
                if operands is not None:
                    nums.mul_push(*operands)
            if match_operands is None:
                record(expression, match_operator)
            else:
                record(expression, match_operator, match_operands)
            if loop_flag1.break_flag:
                break
        loop_flag1.end()
        repeat_count += 1

        # 提取数字
        match = RationalNumber.parse_digits_part(expression)  # 尝试从表达式中提取数字
        if match and not isinstance(match, bool):  # 如果成功提取了数字
            repeat_count = 0
            operands, expression = match  # 提取操作数和剩余的表达式
            nums.push(CalcType(operands))  # 将操作数压入数字栈
            record(expression, operands=operands)
        if ops.is_empty():  # 如果操作符栈为空，说明表达式处理完成
            break
    loop_flag0.end()

    # if format_in_return:
    #     return [nums.top_element(), format_in_return]
    # else:
    #     return [nums.top_element()]
    # 返回结果
    log.log_debug("nums:"+str(nums))
    if over_repeat:
        # operate_log = f"{record.get_former_differ_expression(0, record.size)}"
        # log(original_expression)
        # log("~" * len(operate_log) + "^" * (len(original_expression) - len(operate_log)))
        log.log_calc_error(over_repeat.__repr__())
        return
    if nums.size() == 1:
        log(f"output:{nums.top_element()}")
        return str(nums.top_element())
    else:
        log(f"{nums.stack}")
        return str(nums.stack)


def calc_format(expression: str):
    """语法糖处理"""
    return CalculateFormatter.format(expression)


# def log(_str):
#     # logger.info(_str)
#     print(_str)


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


loop_flags = LoopFlagsGroup()

if __name__ == '__main__':
    # test()

    while True:
        log(calc_main(input("(Calc)>> ")))
