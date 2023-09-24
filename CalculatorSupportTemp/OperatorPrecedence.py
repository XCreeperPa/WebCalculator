from Operators import *

precedence = [
    Bracket,
    [Addition, Minus],
    [Multiplication, Division],
    [Power],
    [Factorial],
    FunctionOperator,
    Mark,
]
