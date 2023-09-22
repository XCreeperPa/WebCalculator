from math import gcd


# 定义有理数类（RationalNumber）
class RationalNumber:
    """有理数类，支持基本的数学运算。
    """
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("分母不能为0")
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common
        # 进一步化简，以确保结果总是最简形式
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other: 'RationalNumber') -> 'RationalNumber':
        return RationalNumber(self.numerator * other.denominator + self.denominator * other.numerator,
                              self.denominator * other.denominator)

    def __sub__(self, other: 'RationalNumber') -> 'RationalNumber':
        return RationalNumber(self.numerator * other.denominator - self.denominator * other.numerator,
                              self.denominator * other.denominator)

    def __mul__(self, other: 'RationalNumber') -> 'RationalNumber':
        return RationalNumber(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other: 'RationalNumber') -> 'RationalNumber':
        if other.numerator == 0:
            raise ZeroDivisionError("除数不能为0")
        return RationalNumber(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other: 'RationalNumber') -> bool:
        """判断两个 RationalNumber 对象是否相等。
        """
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"


class Expression:
    """用于存储和处理数学表达式。
    """

    @classmethod
    def calculate(cls, expression):
        return cls.evaluate(cls.generate_rpn(cls.lexical_analysis(expression)))

    @classmethod
    def lexical_analysis(cls, original_expr):
        """词法分析阶段，用于处理负数。
        返回:
            List[str]: 词法单元列表
        """
        tokens = []
        elements = original_expr.split()
        # 定义合法的字符集
        valid_tokens = set('0123456789+-*/() ')

        # 检查每一个词法单元
        for token in original_expr:
            for char in token:
                if char not in valid_tokens:
                    raise ValueError(f"发现无法处理的字符: {char}")

        # 如果表达式以负号开头，自动在前面添加一个 "0"
        if elements and elements[0] == '-':
            _elements = elements
            elements = ["0", *elements]

        i = 0

        while i < len(elements):
            token = elements[i]
            if token == '-' and (i == 0 or elements[i - 1] in ['+', '-', '*', '/', '(']):
                next_token = elements[i + 1]
                tokens.append(f"-{next_token}")
                i += 2  # 跳过下一个元素，因为它已经被合并为一个负数
            else:
                tokens.append(token)
                i += 1
        return tokens

    @classmethod
    def generate_rpn(cls, tokens):
        """生成逆波兰式（Reverse Polish Notation）。
        返回:
            List[str]: 逆波兰式表达式的列表表示
        """

        output = []
        operators = []
        operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        for token in tokens:
            if token.lstrip('-').isnumeric():
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if operators:  # 检查是否还有左括号，以避免 IndexError
                    operators.pop()  # 移除左括号 '('
            else:
                while operators and operators[-1] in operator_precedence and operator_precedence[
                    operators[-1]] >= operator_precedence.get(token, 0):
                    output.append(operators.pop())
                operators.append(token)
        while operators:
            output.append(operators.pop())
        return output

    @classmethod
    def evaluate(cls, rpn_expr) -> RationalNumber:
        """计算逆波兰式的值，并返回结果。
        返回:
            RationalNumber: 计算结果
        """

        stack = []

        for token in rpn_expr:
            if token.lstrip('-').isnumeric():
                stack.append(RationalNumber(int(token), 1))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b.numerator == 0:
                        raise ZeroDivisionError("除数不能为0")
                    stack.append(a / b)

        return stack[0]
