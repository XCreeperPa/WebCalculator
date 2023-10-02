# from CalculatorSupportBeta import calc_main

from CalculatorSupport import calc_main, log


# @pysnooper.snoop(depth=2)
# @pysnooper.snoop(os.path.abspath(r".\log.log"), depth=2)
def main():
    _io = log.create_string_io()
    _result = calc_main("1+1")
    print(log.read())


def calc_main_user_test():
    while True:
        calc_main(input("(Calc)>> "))


# print(main())
# print(calc_main("sin(1)"))
# print(calc_main("sin(1+1)"))
# print(Utils.debug(calc_main, ("log2(1+1)",)))
if __name__ == '__main__':
    main()
    # calc_main_user_test()
