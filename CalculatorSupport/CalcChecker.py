# import re
# from .Operators import *
from .Stack import ExpressionStack


class CalcChecker:
    def expression_stack_checker(self):
        pass


class StaticChecker(CalcChecker):
    pass


class DynamicChecker(CalcChecker):
    pass


class ExpressionStackChecker(DynamicChecker):
    def stack_checker(self, expression_stack) -> None | Exception:
        return None


class DoubleBinaryChecker(ExpressionStackChecker):
    def stack_checker(self, expression_stack: ExpressionStack) -> None | Exception:
        return None
