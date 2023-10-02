from .CalcFormatter import *

class CalcFormatterOperatorPrecedence:
    pass


class PriorityTreeForFormatters:
    def __init__(self):
        self.graph = {"InfinityHigh": []}

    def add_higher_priority(self, existing_operator, new_operators):
        """为已存在的运算符添加优先级更高的新运算符。"""
        if existing_operator not in self.graph:
            raise ValueError(f"运算符 {existing_operator} 不存在!")

        if not isinstance(new_operators, (list, tuple)):
            new_operators = [new_operators]

        # 对于 InfinityHigh，我们直接设置新运算符为其子节点
        if existing_operator == "InfinityHigh":
            self.graph[existing_operator].append(new_operators[0])
            self.graph[new_operators[0]] = []
            current_parent = new_operators[0]
        else:
            # 查找现有运算符的父节点
            parent_of_existing = self.find_parent(existing_operator)
            # 移除父节点与现有运算符之间的连接
            self.graph[parent_of_existing].remove(existing_operator)
            # 设置新运算符的父节点为现有运算符的父节点
            self.graph[parent_of_existing].append(new_operators[0])
            # 将现有运算符设置为第一个新运算符的子节点
            self.graph[new_operators[0]] = [existing_operator]
            current_parent = new_operators[0]

        # 为其他新运算符设置父节点
        for i in range(1, len(new_operators)):
            self.graph[current_parent].append(new_operators[i])
            self.graph[new_operators[i]] = []
            current_parent = new_operators[i]

    def add_lower_priority(self, existing_operator, new_operators):
        """为已存在的运算符添加优先级更低的新运算符。"""
        if existing_operator not in self.graph:
            raise ValueError(f"运算符 {existing_operator} 不存在!")

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


