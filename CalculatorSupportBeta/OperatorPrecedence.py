from .Operators import *
from .Utils import *

precedence = [
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
