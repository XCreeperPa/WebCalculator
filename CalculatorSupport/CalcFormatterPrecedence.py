from .CalcFormatter import *

class CalcFormatterOperatorPrecedence:
    pass


class PriorityTreeForFormatters:
    def __init__(self):
        self.graph = {"InfinityHigh": []}


    def add_lower_priority(self, existing_operator, new_operators):
        """为已存在的运算符添加优先级更低的新运算符。"""
        if not isinstance(new_operators, (list, tuple)):
            new_operators = [new_operators]

        # 将新运算符设置为现有运算符的子节点
        self.graph[existing_operator].extend(new_operators)

        # 初始化新运算符的子节点列表
        for new_operator in new_operators:
            self.graph[new_operator] = []

    def add_formatters(self, formatters):
        """添加运算符到树中，确保它们是CalculateFormatter的子类。"""
        if not isinstance(formatters, (list, tuple)):
            formatters = [formatters]

        for formatter in formatters:
            if not issubclass(formatter, CalculateFormatter) or formatter == CalculateFormatter:
                raise ValueError(f"{formatter} 不是 CalculateFormatter 的子类!")
            if formatter.__name__ not in self.graph:
                self.graph[formatter.__name__] = []

    def find_parent(self, node):
        """查找给定节点的父节点。"""
        for parent, children in self.graph.items():
            if node in children:
                return parent
        return None

    def get_priority_list(self):
        """返回一个列表，其中包含按优先级排序的运算符。"""
        result = []
        stack = ["InfinityHigh"]
        while stack:
            node = stack.pop()
            result.append(node)
            for child in self.graph[node]:
                stack.append(child)
        return result[1:]  # 排除 InfinityHigh


