# -*- coding: utf-8 -*-
# |=========================|
# |      Coded by Noob_0    |
# | Noob_0-main@outlook.com |
# |=========================|
__author__ = "Noob_0"
__version__ = "1.0"
__license__ = "MIT"

# import Constants
# import LoopFlags
# import OperatorPrecedence
# import Operators
# import RationalNumber
# import Stack
# import Utils

# import sys
# import os

# sys.path.append(os.path.abspath(r"..\.."))
# print(sys.path)

from . import CalculatorSupport
from . import Constants
from . import OperatorPrecedence
from . import Operators
from . import RationalNumber
from .CalculatorSupport import (calc_main, calc_format,
                                CalcType, decimal_context,
                                log
                                )

# set_DefaultCalcType, Decimal, decimal_context, Fraction,

__all__ = ["calc_main", "calc_format", "CalcType", "log",
           "Operators",
           "CalcParser",
           "OperatorPrecedence",
           "RationalNumber",
           "Constants",
           ]
