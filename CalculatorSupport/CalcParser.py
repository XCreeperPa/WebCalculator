# import re
# from .Operators import *
class CalcParser:
    pass

    @staticmethod
    def generator_parser(expression):
        def parse():
            nonlocal expression
            yield expression
            pass

        return parse
