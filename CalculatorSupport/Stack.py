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
        self.stack.extend(args)
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

    def __str__(self):
        """返回栈的字符串表示"""
        return str(self.stack)


# class MixStack(Stack):
#     pass


class OperandStack(Stack):
    def __init__(self):
        super().__init__()


class OperatorStack(Stack):
    def __init__(self):
        super().__init__()
