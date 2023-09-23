import re

from Constants import *


class Operator:
    full_match_re: list[re.Pattern] = [re.compile(r"^(?![\s\S])$")]
    part_match_re: list[re.Pattern] = [re.compile(r"^(?![\s\S])")]

    @classmethod
    def full_match(cls, full_expression: str) -> [bool]:
        # return cls.full_match_re.match(full_expression)
        return any((pattern.match(full_expression) for pattern in cls.full_match_re))

    @classmethod
    def part_match(cls, part_expression: str) -> [bool]:
        # return cls.part_match_re.match(part_expression)
        return any((pattern.match(part_expression) for pattern in cls.part_match_re))

    calculate_arguments_count = INF

    @staticmethod
    def calculate(*args) -> object:
        return NAN


class SymbolOperator(Operator):
    pass


class Addition(SymbolOperator):
    full_match_re = [re.compile(r"^.+\+.+$")]
    part_match_re = [re.compile(r"^\+.+")]
    calculate_arguments_count = 2

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 + v2


class Minus(SymbolOperator):
    full_match_re = [re.compile(r"^.+-.+$")]
    part_match_re = [re.compile(r"^-.+")]
    calculate_arguments_count = 2

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 - v2


class Multiplication(SymbolOperator):
    full_match_re = [re.compile(r"^.+\*.+$")]
    part_match_re = [re.compile(r"^\*.+")]
    calculate_arguments_count = 2

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 * v2


class Division(SymbolOperator):
    full_match_re = [re.compile(r"^.+/.+$")]
    part_match_re = [re.compile(r"^/.+")]
    calculate_arguments_count = 2

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 / v2


class Power(SymbolOperator):
    full_match_re = [re.compile(r"^.+\^.+$")]
    part_match_re = [re.compile(r"^\^.+")]
    calculate_arguments_count = 2

    @staticmethod
    def calculate(v1, v2) -> object:
        return v1 ** v2


class Factorial(SymbolOperator):
    full_match_re = [re.compile(r"^.+!.*$")]
    part_match_re = [re.compile(r"^!.*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1, v2) -> object:
        return math.factorial(v1)


class FunctionOperator(Operator):
    pass


class TrigonometricFunctions(FunctionOperator):
    calculate_arguments_count = 1


class Sine(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*sin(.+).*$")]
    part_match_re = [re.compile(r"^sin(.+).*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.sin(v1)


class Cosine(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*cos(.+).*$")]
    part_match_re = [re.compile(r"^cos(.+).*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.cos(v1)


class Tangent(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*tan(.+).*$")]
    part_match_re = [re.compile(r"^tan(.+).*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.tan(v1)


class Cosecant(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*csc(.+).*$")]
    part_match_re = [re.compile(r"^csc(.+).*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.sin(v1)


class Secant(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*sec(.+).*$")]
    part_match_re = [re.compile(r"^sec(.+).*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.cos(v1)


class Cotangent(TrigonometricFunctions):
    full_match_re = [re.compile(r"^.*cot(.+).*$")]
    part_match_re = [re.compile(r"^cot(.+).*")]
    calculate_arguments_count = 1


class InverseTrigonometricFunctions(TrigonometricFunctions):
    pass


class Arcsine(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*asin(.+).*$")]
    part_match_re = [re.compile(r"^asin(.+).*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.asin(v1)


class Arccosine(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*acos(.+).*$")]
    part_match_re = [re.compile(r"^acos(.+).*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.acos(v1)


class Arctangent(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*atan(.+).*$")]
    part_match_re = [re.compile(r"^atan(.+).*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return math.atan(v1)


class Arccotangent(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*acot(.+).*$")]
    part_match_re = [re.compile(r"^acot(.+).*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.atan(v1)


class Arccosecant(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*acsc(.+).*$")]
    part_match_re = [re.compile(r"^acsc(.+).*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.asin(v1)


class Arcsecant(InverseTrigonometricFunctions):
    full_match_re = [re.compile(r"^.*asec(.+).*$")]
    part_match_re = [re.compile(r"^asec(.+).*")]
    calculate_arguments_count = 1

    @staticmethod
    def calculate(v1) -> object:
        return 1 / math.acos(v1)
