# from CalculatorSupportBeta import calc_main

from CalculatorSupport import calc_main, log, CalcType


# @pysnooper.snoop(depth=2)
# @pysnooper.snoop(os.path.abspath(r".\log.log"), depth=2)
def main():
    _io = log.create_string_io()
    # _result = calc_main("(1+1-1)/0+1")
    # print(log.read())
    # _result = calc_main("1+0/0+1")
    # print(log.read())
    _result = calc_main("()(1/0)")
    print(log.read())


# def calc_fraction_test():
#     from CalculatorSupport import calc_main, set_DefaultCalcType, Fraction
#     set_DefaultCalcType(Fraction)
#     calc_main("1/2+1")


def pre_test():
    print(0.1 + 0.2)
    print(calc_main("0.1+0.2"))


def formatter_test():
    from CalculatorSupport import CalcFormatter
    CalcFormatter.test_log_with_docstring(_f=None)


def calc_main_user_test():
    log.create_string_io()
    while True:
        calc_main(input("(Calc)>> "))
        print(log.read())


# print(main())
# print(calc_main("sin(1)"))
# print(calc_main("sin(1+1)"))
# print(Utils.debug(calc_main, ("log2(1+1)",)))
if __name__ == '__main__':
    CalcType.set_fraction()
    # main()
    # calc
    # _fraction_test()
    # pre_test()
    # formatter_test()
    calc_main_user_test()
