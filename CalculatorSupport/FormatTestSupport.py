import re

from CalcFormatter import SingleTimeFormatter


class TestFormatter(SingleTimeFormatter):
    regex_list = [re.compile(r"^.*$")]
    replacement = r"Hello World"
