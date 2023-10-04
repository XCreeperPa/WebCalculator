from CalculatorSupport import Fraction
from CalculatorSupport.CalculatorSupport import calc_main, set_DefaultCalcType
from traceback import print_exc

if __name__ == '__main__':
    set_DefaultCalcType(Fraction)
    while 1:
        try:
            calc_main(input(">>> "))
        except Exception:
            print_exc()
