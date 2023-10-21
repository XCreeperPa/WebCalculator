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
from .Operators import *
from .Utils import *

operator_precedence = [
    RightBracket,
    [Addition, Minus],
    [Multiplication, Division, Divisibility, Mode],
    [Power],
    [Factorial],
    FunctionOperator,
    LeftBracket,
    Mark,
    SpaceOperator,
]


class OperatorPrecedence(list):
    """OperatorPrecedence(operator_precedence)构造优先级"""
    def __init__(self, original_precedence: list):
        super().__init__(self.build(original_precedence))

    @staticmethod
    def build(original_precedence: list) -> list[set]:
        def build_item_process(op) -> set:
            if isinstance(op, list):
                op_set = set()
                for sub_op in op:
                    op_set.update(build_item_process(sub_op))
                return op_set
            elif issubclass(op, Operator):
                op_set = set(find_all_subclasses(op))
                op_set.add(op)
                return op_set
            else:
                raise ValueError(f"Operator {op} is not a subclass of Operator")

        precedence_list = [build_item_process(op) for op in original_precedence]
        # 去除重复项
        for _index, _obj in enumerate(precedence_list):
            if not isinstance(_obj, list):
                _obj = [_obj]
            for op in _obj:
                for _level_index, level in enumerate(precedence_list):
                    if op in level and _index != _level_index:
                        precedence_list[_level_index].remove(op)
        return precedence_list

    def get(self, cls) -> int | None:
        for _index, _obj in enumerate(self):
            if cls in _obj:
                return _index
        return None
