# 编写一个简易的CLI界面用于调试
from interpreter import *


def debug_cli():
    """简易的命令行界面（CLI）用于调试。
    """

    print("欢迎使用云计算器后端调试CLI。输入 'quit' 以退出。")
    while True:
        try:
            input_expr = input("请输入表达式：")
            if input_expr.lower() == 'quit':
                print("退出调试CLI。")
                break
            interpreter = Interpreter(input_expr)
            result = interpreter.calculate()
            print(f"计算结果：{result}")
        except Exception as e:
            print(f"发生错误：{e}")
