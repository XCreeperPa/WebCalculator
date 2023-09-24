import math
import re

from Constants import NAN, INF
from StatementSet import *


class Operator:
    full_match_re: list[re.Pattern] = [re.compile(r"^[^\s\S]$")]
    part_match_re: list[re.Pattern] = [re.compile(r"^[^\s\S]")]
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
                operand = match_groups
                return operand, expression
        return False

    calculate_arguments_count = INF

    @staticmethod
    def calculate(*args) -> object:
        return NAN


class SymbolOperator(Operator):
    @classmethod
    def part_match(cls, part_expression: str) -> tuple[None | list[str], str] | bool:
        operand, expression = super().part_match(part_expression)
        return None, expression

    pass


class UnaryOperator(SymbolOperator):
    calculate_arguments_count = 1


class BinaryOperator(SymbolOperator):
    calculate_arguments_count = 2


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


class Factorial(UnaryOperator):
    full_match_re = [re.compile(r"^.+!.*$")]
    part_match_re = [re.compile(r"^!(.*)")]

    @staticmethod
    def calculate(v1, v2) -> object:
        return math.factorial(v1)


class FunctionOperator(Operator):
    pass


class TrigonometricFunctions(FunctionOperator):
    calculate_arguments_count = 1


class Sine(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*sin\((.+)\).*$")]
    part_match_re = [re.compile(r"^sin\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.sin(float(v1))


class Cosine(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*cos\((.+)\).*$")]
    part_match_re = [re.compile(r"^cos\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.cos(float(v1))


class Tangent(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*tan\((.+)\).*$")]
    part_match_re = [re.compile(r"^tan\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.tan(float(v1))


class Cosecant(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*csc\((.+)\).*$")]
    part_match_re = [re.compile(r"^csc\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.sin(float(v1))


class Secant(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*sec\((.+)\).*$")]
    part_match_re = [re.compile(r"^sec\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.cos(float(v1))


class Cotangent(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*cot\((.+)\).*$")]
    part_match_re = [re.compile(r"^cot\((.+)\)(.*)")]
    calculate_arguments_count = 1


class InverseTrigonometricFunctions(TrigonometricFunctions):
    pass


class Arcsine(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*asin\((.+)\).*$")]
    part_match_re = [re.compile(r"^asin\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.asin(float(v1))


class Arccosine(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*acos\((.+)\).*$")]
    part_match_re = [re.compile(r"^acos\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.acos(float(v1))


class Arctangent(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*atan\((.+)\).*$")]
    part_match_re = [re.compile(r"^atan\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.atan(float(v1))


class Arccotangent(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*acot\((.+)\).*$")]
    part_match_re = [re.compile(r"^acot\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.atan(float(v1))


class Arccosecant(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*acsc\((.+)\).*$")]
    part_match_re = [re.compile(r"^acsc\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.asin(float(v1))


class Arcsecant(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*asec\((.+)\).*$")]
    part_match_re = [re.compile(r"^asec\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.acos(float(v1))


class LogarithmicFunction(FunctionOperator):
    pass


class CommonLogarithm(LogarithmicFunction):
    full_match_re = [re.compile(r"^.*log(\d*)\((.+)\).*$")]
    part_match_re = [re.compile(r"^log(\d*)\((.+)\)(.*)")]
    calculate_arguments_count = 2
    DEFAULT_BASE = 10

    @classmethod
    def full_match(cls, full_expression: str) -> None | list[str] | bool:
        return super().full_match(full_expression)[::-1]  # 反转列表

    @classmethod
    def part_match(cls, part_expression: str) -> None | list[str] | bool:
        return super().part_match(part_expression)[::-1]

    @staticmethod
    def calculate(_x, _base=DEFAULT_BASE) -> object:
        return math.log(float(_x), _base)


class DefaultLogarithm(CommonLogarithm):
    full_match_re = [re.compile(r"^.*log\((.+)\).*$")]
    part_match_re = [re.compile(r"^log\((.+)\)(.*)")]
    calculate_arguments_count = 1


class NaturalLogarithm(LogarithmicFunction):
    full_match_re = [re.compile(r"^.*ln\((.+)\).*$")]
    part_match_re = [re.compile(r"^ln\((.+)\)(.*)")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(_x) -> object:
        return math.log(float(_x))


class Mark(Operator):
    pass


class BreakMark(Mark):
    execute = Statements.break_


class FunctionalOperator(Operator):  # bracket and so on
    pass


class BracketBreakMark(BreakMark):
    execute = f"""
{Statements.if_} expression[index]==")":
    {Statements.break_}
"""


class Bracket(FunctionalOperator):
    calculate_arguments_count = 0


class LeftBracket(Bracket):
    full_match_re = [re.compile(r"^.*\(.*\).*$")]
    part_match_re = [re.compile(r"^\((.*)\).*")]
    execute = BracketBreakMark

    @staticmethod
    def calculate():
        return BracketBreakMark


class RightBracket(Bracket):
    full_match_re = [re.compile(r"^.*\(.*\).*$")]
    part_match_re = [re.compile(r"^\)(.*)")]
    calculate_arguments_count = 0

    @staticmethod
    def calculate():
        return None
