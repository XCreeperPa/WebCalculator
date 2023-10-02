import difflib


class ExpressionInscriber:
    def __init__(self, original_expression):
        self.original_expression = original_expression
        self.latest_expression = self.original_expression
        self.differ = difflib.Differ()
        self.former_increase_differ_list: list[str] = list()
        # self.former_decrease_differ_list: list[str] = list()
        self.latter_increase_differ_list: list[str] = list()
        # self.latter_decrease_differ_list: list[str] = list()

    def __call__(self, expression: str):
        differ = list(self.differ.compare(expression, self.latest_expression))

        former_increase_differ_expression = str()
        char_index = 0
        while char_index < len(differ) and differ[char_index].startswith('+ '):
            former_increase_differ_expression += differ[char_index][2:]
            char_index += 1
        self.former_increase_differ_list.append(former_increase_differ_expression)

        latter_increase_differ_expression = str()
        char_index = -1
        while -char_index <= len(differ) and differ[char_index].startswith('+ '):
            latter_increase_differ_expression = differ[char_index][2:] + latter_increase_differ_expression
            char_index -= 1
        self.latter_increase_differ_list.append(latter_increase_differ_expression)

        self.latest_expression = expression
        return self
    @property
    def size(self):
        return len(self.former_increase_differ_list)
    def get_former_differ_expression(self, start_index: int, end_index: int = None) -> str:
        if end_index is None:
            return self.former_increase_differ_list[start_index]
        else:
            return "".join(self.former_increase_differ_list[start_index:end_index])

    def get_latter_differ_expression(self, start_index: int, end_index: int = None) -> str:
        if end_index is None:
            return self.latter_increase_differ_list[start_index]
        else:
            return "".join(self.latter_increase_differ_list[start_index:end_index])

    def __getitem__(self, index):
        pass

    def __str__(self):
        return self.original_expression

# def test():
#     inscriber = ExpressionInscriber("(1+1)")
#     # inscriber('(1+1)')
#     # inscriber('1+1)')
#     # inscriber('+1)')
#     # inscriber('1)')
#     # inscriber(')')
#     inscriber('')
#     print(f"former: {inscriber.former_increase_differ_list}")
#     print(f"latter: {inscriber.latter_increase_differ_list}")
#
#
# test()
