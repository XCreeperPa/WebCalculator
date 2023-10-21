# 本文件是云计算器的一部分。
#
# 云计算器是自由软件：你可以再分发之和/或依照由自由软件基金会发布的 GNU 通用公共许可证修改之，无论是版本 3 许可证，还是（按你的决定）任何以后版都可以。
#
# 发布云计算器是希望它能有用，但是并无保障;甚至连可销售和符合某个特定的目的都不保证。请参看 GNU 通用公共许可证，了解详情。
#
# 你应该随程序获得一份 GNU 通用公共许可证的复本。如果没有，请看 <https://www.gnu.org/licenses/>.
#
# This file is part of WebCalculator.
#
# WebCalculator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# WebCalculator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with WebCalculator. If not, see <https://www.gnu.org/licenses/>.
class Stack:
    def __init__(self):
        self.stack = []

    def __iter__(self):
        return iter(self.stack[::-1])

    def __getitem__(self, index):
        return self.stack[::-1][index]

    def get(self, index):
        return self.__getitem__(index)

    def push(self, obj):
        """将元素压入栈"""
        self.stack.append(obj)
        return obj

    def mul_push(self, *args):
        """将多个元素压入栈"""
        for _obj in args:
            self.push(_obj)
        return self

    def pop(self):
        """从栈中弹出顶部元素并返回"""
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def mul_pop(self, n: int = 0):
        """从栈中弹出多个元素，返回弹出的元素组成的列表"""
        if n < 0:
            raise ValueError("Invalid argument: n cannot be negative")
        if n == 0:
            return []
        if n > len(self.stack):
            n = len(self.stack)
        popped_elements = self.stack[-n:]
        self.stack = self.stack[:-n]
        return popped_elements

    def top_element(self):
        """返回栈顶元素，不弹出"""
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        """检查栈是否为空"""
        return len(self.stack) == 0

    def size(self):
        """返回栈的当前大小"""
        return len(self.stack)

    def clear(self):
        """清空栈"""
        self.stack.clear()

    def __str__(self):
        """返回栈的字符串表示"""
        return str(self.stack)


class CalcStack(Stack):
    def __init__(self, expression_stack=None):
        super().__init__()
        self.expression_stack: ExpressionStack = expression_stack

    def push(self, obj):
        super().push(obj)
        if self.expression_stack is not None:
            self.expression_stack.push(self)

    def pop(self):
        _obj = super().pop()
        if self.expression_stack is not None:
            self.expression_stack.update()
        return _obj

    def mul_pop(self, n: int = 0):
        _objs = super().mul_pop(n)
        if self.expression_stack is not None:
            self.expression_stack.update()
        return _objs


class OperandStack(CalcStack):
    def __init__(self, expression_stack=None):
        super().__init__(expression_stack)


class OperatorStack(CalcStack):
    def __init__(self, expression_stack=None):
        super().__init__(expression_stack)


class ExpressionStack(Stack):
    class StackPointer:
        def __init__(self, index, stack: Stack):
            self.index = index
            self.stack = stack

        def get(self):
            return self.stack.stack[self.index]

    def __init__(self, original_expression=None):
        super().__init__()
        self.original_expression = original_expression

    def push(self, stack: Stack):
        super().push(self.StackPointer(stack.size() - 1, stack))

    def mul_push(self, *args):
        for arg in args:
            self.push(arg)
        return self

    def pop(self, *_):
        raise NotImplementedError

    def mul_pop(self, *_):
        raise NotImplementedError

    def get(self, index):
        self.update()
        return super().get(index).get()

    def get_all(self):
        self.update()
        return [p.get() for p in self.stack]

    def update(self):
        i = 0
        while i < self.size():
            try:
                self.stack[i].get()
            except IndexError:
                self.stack.pop(i)
            else:
                i += 1
