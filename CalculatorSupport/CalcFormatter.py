import re

from .LoopFlags import LoopFlagsGroup
from .Utils import *


class CalculateFormatter:
    @staticmethod
    def format(expression: str) -> str:
        for formatter in find_all_subclasses(SingleTimeFormatter):
            expression = formatter.format(expression)
        loop_flags = LoopFlagsGroup()
        loop_flag = loop_flags.new()
        while loop_flag:
            loop_flag.break_loop()
            for formatter in find_all_subclasses(MultiTimeFormatter):
                new_expression = formatter.format(expression)
                if new_expression != expression:
                    expression = new_expression
                    loop_flag.resume()
        return expression

    test_input: list[str] = ["1+1="]
    test_expected: list[str] = ["(1+1)"]

    @classmethod
    def test(cls):
        for _input, _expected in zip(cls.test_input, cls.test_expected):
            output = cls.format(_input)
            print(f"input: {_input}\nexpected: {_expected}\noutput: {output}\n")
            assert output == _expected, (f"\nclass: {cls.__name__}\n"
                                         f"input: {_input}\n"
                                         f"expected: {_expected}\n"
                                         f"output: {output}")
        return True


class RegexFormatter(CalculateFormatter):
    regex_list: list[re.Pattern] = [re.compile(r"^(^\s\S)$")]
    replacement: str = r"\g<1>"

    @classmethod
    def format(cls, expression: str) -> str:
        for regex in cls.regex_list:
            expression = regex.sub(cls.replacement, expression)
        return expression


class SingleTimeFormatter(RegexFormatter):
    """单次格式化"""


class MultiTimeFormatter(RegexFormatter):
    """多次格式化"""


class Strip(RegexFormatter):
    replacement = r""


class StripEquality(SingleTimeFormatter, Strip):
    """移除表达式末位等号:\"1+1=\"==\"1+1\""""
    regex_list = [re.compile(r"=+$")]
    test_input = ["1+1="]
    test_expected = ["1+1"]


class AddShellBracket(SingleTimeFormatter):
    """表达式最外层加括号:\"1+1=\"==\"(1+1)\""""
    regex_list = [re.compile(r"^(.*)$")]
    replacement = r'(\g<1>)'
    test_input = ["1+1", "(1+1)", "1+(1)"]
    test_expected = ["(1+1)", "(1+1)", "(1+(1))"]

    @classmethod
    def format(cls, expression: str) -> str:
        expression = StripEquality.format(expression)
        if re.match(r"^\(.*\)$", expression):
            return expression
        return super().format(expression)


class DecimalPointFormatter(SingleTimeFormatter):
    """(1.)==(1.0)"""
    regex_list = [
        re.compile(r'(\d+\.)\D'),
        re.compile(r'(\d+\.)$'),
    ]
    replacement = r'\g<1>0'
    test_input = ["1."]
    test_expected = ["1.0"]


class ExponentFormatter(SingleTimeFormatter):
    """2**2==2^2"""
    regex_list = [re.compile(r'\*\*')]
    replacement = r'^'
    test_input = ["2**2"]
    test_expected = ["2^2"]


class DivideFormatter(SingleTimeFormatter):
    """3//2==3|2"""
    regex_list = [re.compile(r'//')]
    replacement = r'|'
    test_input = ["3//2"]
    test_expected = ["3|2"]


class ModeOrPercentFormatter(SingleTimeFormatter):
    """'%'后跟数字为mode模运算，'%'后不跟数字为percent百分号: 2%*100==(2/100)*100"""
    regex_list = [
        re.compile(r'([\d.]+)%(\D)'),
        re.compile(r'([\d.]+)%(\D)*$'),
    ]
    replacement = r'(\g<1>/100)\g<2>'
    test_input = ["2%*100", "20%"]
    test_expected = ["(2/100)*100", "(20/100)"]


class ExclamationFormatter(SingleTimeFormatter):
    """阶乘'!'后面跟数字，向'!'后添加'*': 2!3==2!*3"""
    regex_list = [re.compile(r'!(\d)')]
    replacement = r'!*\g<1>'
    test_input = ["2!3"]
    test_expected = ["2!*3"]


class ConsecutiveSubtractFormatter(MultiTimeFormatter):
    """处理连续的减号 '--'，将其替换为加号 '+': 1--1==1+1"""
    regex_list = [re.compile(r'--')]
    replacement = r'+'
    test_input = ["1--1"]
    test_expected = ["1+1"]


class ConsecutivePlusFormatter(MultiTimeFormatter):
    """处理连续的加号 '++'，将其替换为一个 '+': 1++1=1+1"""
    regex_list = [re.compile(r'\+\+')]
    replacement = r'+'
    test_input = ["1++1"]
    test_expected = ["1+1"]


class PlusMinusFormatter(MultiTimeFormatter):
    """处理加号 '+' 和减号 '-' 之间的情况，将加号去除: 1+-1==1-1"""
    regex_list = [re.compile(r'\+-')]
    replacement = r'-'
    test_input = ["1+-1"]
    test_expected = ["1-1"]


class MinusPlusFormatter(MultiTimeFormatter):
    """处理减号 '-' 和加号 '+' 之间的情况，将减号去除: 1-+1==1-1"""
    regex_list = [re.compile(r'-\+')]
    replacement = r'-'
    test_input = ["1-+1"]
    test_expected = ["1-1"]


class NegativePositiveFormatter(SingleTimeFormatter):
    """正负数处理/左括号后跟减号 '(-''[-''{-'，将减号替换为零减 '0-: (-1)==(0-1)'"""
    regex_list = [re.compile(r'([(\[{])([-+])')]
    replacement = r'\g<1>0\g<2>'
    test_input = ["(-1)", "(+1)"]
    test_expected = ["(0-1)", "(0+1)"]


class LeftBracketMultipleFormatter(SingleTimeFormatter):
    """在数字与左括号之间添加乘号 '*': 2(e)==2*(e)"""
    # 特殊情况log2(e)!=log2*(e)
    regex_list = [re.compile(r'(\d+)([(\[{])')]
    # replacement = r'\g<1>*\g<2>'
    replacement = r'\g<1>*\g<2>'
    raw_exception_list = [r"(?<!(?:{exceptions}))(\d+)([(\[{{])"]
    exception_list = ["log"]
    test_input = ["2(e)", "log2(e)"]
    test_expected = ["2*(e)", "log2(e)"]

    @classmethod
    def format(cls, expression: str) -> str:
        for _index, raw_exception in enumerate(cls.raw_exception_list):
            regex = raw_exception.format(exceptions="|".join(cls.exception_list))
            cls.regex_list[_index] = re.compile(regex)
        return super().format(expression)


class RightBracketMultipleFormatter(SingleTimeFormatter):
    """在数字与右括号之间添加乘号 '*': (e)2==(e)*2"""
    regex_list = [re.compile(r'([)\]}])(\d)')]
    replacement = r'\g<1>*\g<2>'
    test_input = ["(e)2"]
    test_expected = ["(e)*2"]


class BracketMultiplierFormatter(SingleTimeFormatter):
    """在左括号和右括号之间后添加乘号 '*': (e1)(e2)==(e1)*(e2)"""
    regex_list = [re.compile(r'([)\]}])([(\[{])')]
    replacement = r'\g<1>*\g<2>'
    test_input = ["(e1)(e2)"]
    test_expected = ["(e1)*(e2)"]


def test(_f: str = None, doc: bool = False):
    if _f is not None:
        close_log = capture_print_to_file(f'{_f}')
    else:
        close_log = capture_print_to_file(r".\test\FormatterTestLog.txt")
    import time
    sleep_time = 0.2
    for formatter in (find_all_subclasses(SingleTimeFormatter) + find_all_subclasses(MultiTimeFormatter)):
        formatter: CalculateFormatter
        print(formatter.__name__)
        if doc and len(formatter.__doc__.strip()):
            print(formatter.__doc__.strip())
        formatter.test()
        time.sleep(sleep_time)
    print("test done")
    close_log()


def test_log_with_docstring():
    _f = r".\test\FormatterTestWithDocLog.txt"
    test(_f, doc=True)


if __name__ == '__main__':
    test_log_with_docstring()