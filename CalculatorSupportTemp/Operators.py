import math
import re
from typing import Callable

from Constants import NAN, INF
from StatementSet import *


class Operator:
    full_match_re: list[re.Pattern] = [re.compile(r"^[^\s\S]$")]
    part_match_re: list[re.Pattern] = [re.compile(r"^[^\s\S]")]
    operands_type: type | list[type] | tuple[type] = object
    execute = None

    # @classmethod
    # def full_match(cls, full_expression: str) -> [bool]:
    #     return any((pattern.match(full_expression) for pattern in cls.full_match_re))
    @classmethod
    def full_match(cls, full_expression: str) -> None | list[str] | bool:
        """NotImplemented"""
        match_list = []
        for pattern in cls.full_match_re:
            match = pattern.match(full_expression)
            if match:
                match_list.append(list(match.groups()))
        return None

    # @classmethod
    # def part_match(cls, part_expression: str) -> [bool]:
    #     return any((pattern.match(part_expression) for pattern in cls.part_match_re))
    @classmethod
    def part_match(cls, part_expression: str) -> tuple[None | list[str], str] | bool:
        for pattern in cls.part_match_re:
            match = pattern.match(part_expression)
            if match:
                match_groups = list(match.groups())
                expression = match_groups.pop(-1)
                if match_groups:
                    operand = match_groups
                else:
                    operand = None
                return operand, expression
        return False

    calc_args_count = INF

    @staticmethod
    def calculate(*args) -> object:
        return NAN


class SymbolOperator(Operator):
    @classmethod
    def part_match(cls, part_expression: str) -> tuple[None | list[str], str] | bool:
        result = super().part_match(part_expression)
        if isinstance(result, tuple):
            return None, result[-1]
        else:
            return result

    pass


class UnaryOperator(SymbolOperator):
    calc_args_count = 1


class BinaryOperator(SymbolOperator):
    calc_args_count = 2


class Addition(BinaryOperator):
    full_match_re = [re.compile(r"^.+\+.+$")]
    part_match_re = [re.compile(r"^\+(.+)")]

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 + v2


class Minus(BinaryOperator):
    full_match_re = [re.compile(r"^.+-.+$")]
    part_match_re = [re.compile(r"^-(.+)")]

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 - v2


class Multiplication(BinaryOperator):
    full_match_re = [re.compile(r"^.+\*.+$")]
    part_match_re = [re.compile(r"^\*(.+)")]

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 * v2


class Division(BinaryOperator):
    full_match_re = [re.compile(r"^.+/.+$")]
    part_match_re = [re.compile(r"^/(.+)")]

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 / v2


class Power(BinaryOperator):
    full_match_re = [re.compile(r"^.+\^.+$")]
    part_match_re = [re.compile(r"^\^(.+)")]

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 ** v2


class Mode(BinaryOperator):
    full_match_re = [re.compile(r"^.+%.+$")]
    part_match_re = [re.compile(r"^%(.+)")]

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 % v2


class Divisibility(BinaryOperator):
    full_match_re = [re.compile(r"^.+\|.+$")]
    part_match_re = [re.compile(r"^\|(.+)")]

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 // v2


class Factorial(UnaryOperator):
    full_match_re = [re.compile(r"^.+!.*$")]
    part_match_re = [re.compile(r"^!(.*)")]

    @staticmethod
    def calculate(v1, v2) -> object:
        return math.factorial(v1)


class FunctionOperator(Operator):
    pass


class TrigonometricFunctions(FunctionOperator):
    calc_args_count = 1


class Sine(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*sin\((.+?)\).*$")]
    part_match_re = [re.compile(r"^sin\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.sin(float(v1))


class Cosine(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*cos\((.+?)\).*$")]
    part_match_re = [re.compile(r"^cos\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.cos(float(v1))


class Tangent(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*tan\((.+?)\).*$")]
    part_match_re = [re.compile(r"^tan\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.tan(float(v1))


class Cosecant(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*csc\((.+?)\).*$")]
    part_match_re = [re.compile(r"^csc\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.sin(float(v1))


class Secant(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*sec\((.+?)\).*$")]
    part_match_re = [re.compile(r"^sec\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.cos(float(v1))


class Cotangent(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*cot\((.+?)\).*$")]
    part_match_re = [re.compile(r"^cot\((.+?)\)(.*)")]
    calc_args_count = 1


class InverseTrigonometricFunctions(TrigonometricFunctions):
    pass


class Arcsine(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*asin\((.+?)\).*$")]
    part_match_re = [re.compile(r"^asin\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.asin(float(v1))


class Arccosine(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*acos\((.+?)\).*$")]
    part_match_re = [re.compile(r"^acos\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.acos(float(v1))


class Arctangent(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*atan\((.+?)\).*$")]
    part_match_re = [re.compile(r"^atan\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.atan(float(v1))


class Arccotangent(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*acot\((.+?)\).*$")]
    part_match_re = [re.compile(r"^acot\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.atan(float(v1))


class Arccosecant(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*acsc\((.+?)\).*$")]
    part_match_re = [re.compile(r"^acsc\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.asin(float(v1))


class Arcsecant(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*asec\((.+?)\).*$")]
    part_match_re = [re.compile(r"^asec\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.acos(float(v1))


class LogarithmicFunction(FunctionOperator):
    pass


class CommonLogarithm(LogarithmicFunction):
    full_match_re = [re.compile(r"^.*log(\d*?)\((.+?)\).*$")]
    part_match_re = [re.compile(r"^log(\d*?)\((.+?)\)(.*)")]
    calc_args_count = 2
    DEFAULT_BASE = 10

    @classmethod
    def full_match(cls, full_expression: str) -> None | list[str] | bool:
        result = super().full_match(full_expression)
        if isinstance(result, tuple):
            return result[::-1]  # 反转列表
        else:
            return result

    @classmethod
    def part_match(cls, part_expression: str) -> None | list[str] | bool:
        result = super().part_match(part_expression)
        if isinstance(result, tuple):
            return result[::-1]  # 反转列表
        else:
            return result

    @staticmethod
    def calculate(_x, _base=DEFAULT_BASE) -> object:
        return math.log(float(_x), _base)


class DefaultLogarithm(CommonLogarithm):
    full_match_re = [re.compile(r"^.*log\((.+?)\).*$")]
    part_match_re = [re.compile(r"^log\((.+?)\)(.*)")]
    calc_args_count = 1


class NaturalLogarithm(LogarithmicFunction):
    full_match_re = [re.compile(r"^.*ln\((.+?)\).*$")]
    part_match_re = [re.compile(r"^ln\((.+?)\)(.*)")]
    calc_args_count = 1

    @staticmethod
    def calculate(_x) -> object:
        return math.log(float(_x))


class Mark(Operator):
    calc_args_count = 0


class EndMark(Mark):
    execute = "loop_flags.break_all()"


class EmptyMark(Mark):
    execute = f"{Statements.pass_}"

    @classmethod
    def calculate(cls, *args) -> object:
        return cls


class SetEmptyMark(EmptyMark):
    @staticmethod
    def execute(_globals, _locals) -> None:
        _locals["set_operator"](EmptyMark)
        _locals["loop_flags"].break_loop()


# class BracketActionMark(SetEmptyMark):
#     @staticmethod
#     def execute(_globals: dict, _locals: dict) -> None:
#         if _locals["operator"] is RightBracket:
#             _locals["set_operator"](EmptyMark)
#         else:
#             _locals["ops"].push(BracketActionMark)
#         _locals["loop_flags"].break_top()


class BreakMark(Mark):
    execute = Statements.break_


class FunctionalOperator(Operator):  # bracket and so on
    @staticmethod
    def calculate(*args) -> object | type[Mark]:
        return super().calculate(*args)


class SpaceBreakMark(BreakMark):
    execute = f"""{Statements.break_}"""


class SpaceOperator(FunctionalOperator):
    full_match_re = [re.compile(r"^.* .*$")]
    part_match_re = [re.compile(r"^ (.*)")]
    execute = 0

    @staticmethod
    def calculate(*args) -> object | type[Mark]:
        return SpaceBreakMark


class Bracket(FunctionalOperator):
    calc_args_count = 0


class LeftBracket(Bracket, Mark):
    full_match_re = [re.compile(r"^.*\(.*\).*$")]
    part_match_re = [re.compile(r"^\((.*\).*)")]

    @classmethod
    def execute(cls, _globals: dict, _locals: dict) -> None:
        if _locals["loop_flag2"].state is False:
            return
        if _locals["operator"] is RightBracket:
            if _locals["ops"].is_empty():
                _locals["set_operator"](EndMark)
                _locals["loop_flags"].break_all()
            else:
                _locals["set_operator"](EmptyMark)
        else:
            _locals["ops"].push(cls)
        _locals["loop_flags"].break_top()

    @classmethod
    def calculate(cls) -> type[Mark]:
        return EmptyMark


class RightBracket(Bracket):
    full_match_re = [re.compile(r"^.*\(.*\).*$")]
    part_match_re = [re.compile(r"^\)(.*)")]
    calc_args_count = 0

    @staticmethod
    def calculate():
        return None


def execute_check(obj) -> bool:
    return isinstance(obj, type) and issubclass(obj, Mark) and obj.execute is not None


def execute_complete(obj, check=True) -> Callable:
    def none(*args, **kwargs):
        return *args, *kwargs.values()

    if (not check) or execute_check(obj):
        return _execute_complete(obj)
    else:
        return none


def _execute_complete(operator: type[Operator]) -> Callable:
    def execute_exec(*args, **kwargs):
        exec(operator.execute, *args, **kwargs)
        return *args, *kwargs.values()

    def execute_callable(*args, **kwargs):
        return operator.execute(*args, **kwargs)

    if isinstance(operator.execute, str):
        return execute_exec
    elif callable(operator):
        return execute_callable
    else:
        raise ValueError(f"{operator} is not a executable string or callable object")
