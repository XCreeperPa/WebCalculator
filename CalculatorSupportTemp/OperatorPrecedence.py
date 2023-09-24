from Operators import *

precedence = [
    RightBracket,
    [Addition, Minus],
    [Multiplication, Division],
    [Power],
    [Factorial],
    LeftBracket,
    FunctionOperator,
    Mark,
    SpaceOperator,
]
