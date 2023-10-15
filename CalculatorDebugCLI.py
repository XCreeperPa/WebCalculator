from CalculatorSupport.CalculatorSupport import calc_main, CalcType
from traceback import print_exc
import CalculatorSupport
import time


if __name__ == '__main__':
    CalcType.set_calc_type(CalcType.Fraction)
    while 1:
        try:
            # 使用后端 API 计算结果
            io = CalculatorSupport.log.create_string_io()  # 创建io对象
            result = calc_main(input("(calc)>>> "))  # 使用后端 API 计算结果
            io.seek(0)
            log = io.read()  # 获取日志结果
            print("result:", result)
            print("log:", log)
        except Exception:
            print_exc()
