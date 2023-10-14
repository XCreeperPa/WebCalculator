from CalculatorSupport.CalculatorSupport import calc_main, CalcType
from traceback import print_exc

from CalculatorSupport.RationalNumber import Fraction

if __name__ == '__main__':
    CalcType.set_calc_type(CalcType.Fraction)
    while 1:
        try:
            calc_main(input(">>> "))
        except Exception:
            print_exc()
