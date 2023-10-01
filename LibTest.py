# from CalculatorSupportBeta import calc_main

from CalculatorSupport import calc_main, log


# @pysnooper.snoop(depth=2)
# @pysnooper.snoop(os.path.abspath(r".\log.log"), depth=2)
def main():
    io = log.create_string_io()
    calc_main("1+(1)")
    io.write("test")
    io.seek(0)
    print(io.read())


# print(main())
# print(calc_main("sin(1)"))
# print(calc_main("sin(1+1)"))
# print(Utils.debug(calc_main, ("log2(1+1)",)))
if __name__ == '__main__':
    main()
