# 本文件是云计算器的一部分。
#
# 云计算器是自由软件：你可以再分发之和/或依照由自由软件基金会发布的 GNU 通用公共许可证修改之，无论是版本 3 许可证，还是（按你的决定）任何以后版都可以。
#
# 发布云计算器是希望它能有用，但是并无保障;甚至连可销售和符合某个特定的目的都不保证。请参看 GNU 通用公共许可证，了解详情。
#
# 你应该随程序获得一份 GNU 通用公共许可证的复本。如果没有，请看 <https://www.gnu.org/licenses/>.
#
# This file is part of WebCalculator.
#
# WebCalculator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# WebCalculator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with WebCalculator. If not, see <https://www.gnu.org/licenses/>.
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
