from module import *


# 定义解释器类（Interpreter）
class Interpreter:
    """用于解释用户输入的表达式，并返回计算结果或错误信息。
    """
    def __init__(self, input_expr: str):
        """
        参数:
            input_expr (str): 输入的字符串表达式
        """
        self.input_expr = input_expr

    def parse(self) -> Expression:
        """解析输入的表达式，生成 Expression 对象。
        返回:
            Expression: 表达式对象
        """
        return Expression(self.input_expr)

    def calculate(self) -> RationalNumber:
        """调用 Expression 对象的 evaluate 方法，并返回结果。
        返回:
            RationalNumber: 计算结果
        """

        expr = self.parse()
        return expr.evaluate()