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
