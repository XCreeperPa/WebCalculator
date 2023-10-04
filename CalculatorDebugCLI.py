from CalculatorSupport.CalculatorSupport import calc_main
from traceback import print_exc

if __name__ == '__main__':
    while 1:
        try:
            calc_main(input(">>> "))
        except Exception:
            print_exc()
