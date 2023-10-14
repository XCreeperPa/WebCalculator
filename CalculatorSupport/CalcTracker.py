from .ExpressionOperateInscriber import ExpressionOperateInscriber
from .Logger import Logger
from .OperatorPrecedence import OperatorPrecedence
from .Operators import *


# @pysnooper.snoop(depth=2)
def calc_tracker(track_operator: type[Operator], record: ExpressionOperateInscriber,
                 operator_precedence: OperatorPrecedence, log: Logger):
    bracket_count = 0
    index = -1
    # while -index <= len(record.operate_log) and track_operator != record.operate_log[index].operator:
    #     index -= 1
    # index -= 1
    while -index <= len(record.operate_log):
        operator = record.operate_log[index].operator
        if operator is not None:
            if issubclass(operator, Bracket) or bracket_count != 0:
                if issubclass(operator, RightBracket):
                    bracket_count += 1
                elif issubclass(operator, LeftBracket):
                    bracket_count -= 1
                if bracket_count < 0:
                    break
            elif operator_precedence.get(track_operator) > operator_precedence.get(operator):
                break
        index -= 1
    former_skip: int = len(record.get_former_differ_expression(0, record.size + index + 1))
    latter_skip: int = len(record.original_expression) - record.size
    log.log_calc_error(record.original_expression)
    log.log_calc_error(
        "~" * former_skip +
        "^" * len(record.get_former_differ_expression(record.size + index, record.size - 1)) +
        "~" * latter_skip
    )
