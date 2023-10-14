from CalculatorSupport.CalculatorSupport import calc_main, CalcType
from traceback import print_exc

from CalculatorSupport.Logger import test2

if __name__ == '__main__':
    CalcType.set_calc_type(CalcType.Fraction)
    test2()
    while 1:
        try:
            calc_main(input(">>> "))
        except Exception:
            print_exc()
