class Stack:  # 栈
    stake_list = []  # 栈列表，用于存储元素
    top = size = 0  # 栈顶指针和长度

    def push(self, obj):
        stake, top, lenght = self.stake_list, self.top, self.size

        # 如果栈顶指针大于等于栈的长度减1，表示栈已满，需要扩展栈的长度
        if top >= lenght - 1:
            stake.append(obj)  # 将 obj 添加到栈的末尾
            top, lenght = lenght, lenght + 1  # 更新栈顶指针和栈的长度
        else:
            top += 1  # 栈顶指针加1
            stake[top] = obj  # 将 obj 放入栈中的指定位置

        self.stake_list, self.top, self.size = stake, top, lenght  # 更新类属性
        return obj  # 返回被入栈的对象 obj

    def pop(self):
        stake, top = self.stake_list, self.top

        # 如果栈顶指针小于0，表示栈为空，无法出栈，返回 None
        if top < 0:
            return None
        else:
            _result = stake[top]  # 从栈中取出栈顶元素
            top -= 1  # 栈顶指针减1
            self.top = top  # 更新类属性中的栈顶指针
            return _result  # 返回被出栈的元素

    def mul_pop(self, n: int = 0):
        """stack[1,2,3].mul_pop(2)==[2,3]"""
        _result = [self.pop()] * n
        _result.reverse()
        return _result

    def top_element(self):
        return self.stake_list[self.top]
