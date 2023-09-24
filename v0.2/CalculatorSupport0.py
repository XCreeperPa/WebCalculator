import math

NAN = float('NaN')
INF = float('Inf')


class RationalNumber:
    def __init__(self):
        pass


class Int:
    NaN = float('NaN')  # 用于表示非法结果
    __value = 0  # 初始值为0

    def __init__(self, value=None):
        # 初始化整数对象
        # value: 整数值或其他可转化为整数的对象
        if value is None:
            value = 0
        try:
            self.__value = int(value)
        except (ValueError, TypeError):
            self.__value = NAN  # 处理非法输入

    def sum(self, *args):
        # 整数求和接口，支持多个整数相加
        result = self.__value
        for arg in args:
            try:
                result += int(arg)
            except (ValueError, TypeError):
                return NAN  # 处理非法输入
        return Int(result)

    def difference(self, *args):
        # 整数求差接口，支持多个整数相减
        result = self.__value
        for arg in args:
            try:
                result -= int(arg)
            except (ValueError, TypeError):
                return NAN  # 处理非法输入
        return Int(result)

    def product(self, *args):
        # 整数求积接口，支持多个整数相乘
        result = self.__value
        for arg in args:
            try:
                result *= int(arg)
            except (ValueError, TypeError):
                return NAN  # 处理非法输入
        return Int(result)

    def quotient(self, *args):
        # 整数求商接口，支持多个整数相除
        result = self.__value
        for arg in args:
            try:
                arg_value = int(arg)
                if arg_value == 0:
                    return NAN  # 处理除以0的情况
                result //= arg_value
            except (ValueError, TypeError):
                return NAN  # 处理非法输入
        return Int(result)

    @property
    def value(self):
        # 获取整数值
        return self.__value

    def __int__(self):
        # 转换为整数
        return self.__value

    def __float__(self):
        # 转换为浮点数
        return float(self.__value)

    def __floor__(self):
        # 下舍整数
        return int(self.__value)

    def __abs__(self):
        # 绝对值
        return Int(abs(self.__value))

    def __neg__(self):
        # 取负数
        return Int(-self.__value)

    def __pos__(self):
        # 取正数
        return Int(self.__value)

    def __add__(self, other):
        # 加法运算
        return self.sum(other)

    def __sub__(self, other):
        # 减法运算
        return self.difference(other)

    def __mul__(self, other):
        # 乘法运算
        return self.product(other)

    def __truediv__(self, other):
        # 除法运算
        return self.quotient(other)

    def __floordiv__(self, other):
        # 整除运算
        return Int(self.__value // int(other))

    def __mod__(self, other):
        # 取模运算
        try:
            other_value = int(other)
            if other_value == 0:
                return NAN  # 处理取模0的情况
            return Int(self.__value % other_value)
        except (ValueError, TypeError):
            return NAN  # 处理非法输入

    def __eq__(self, other):
        # 等于运算
        try:
            other_value = int(other)
            return self.__value == other_value
        except (ValueError, TypeError):
            return False  # 处理非法输入

    def __ne__(self, other):
        # 不等于运算
        return not self.__eq__(other)

    def __lt__(self, other):
        # 小于运算
        try:
            other_value = int(other)
            return self.__value < other_value
        except (ValueError, TypeError):
            return False  # 处理非法输入

    def __le__(self, other):
        # 小于等于运算
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        # 大于运算
        try:
            other_value = int(other)
            return self.__value > other_value
        except (ValueError, TypeError):
            return False  # 处理非法输入

    def __ge__(self, other):
        # 大于等于运算
        return self.__eq__(other) or self.__gt__(other)

    def __invert__(self):
        # 求整数的倒数
        if self.__value != 0:
            return Int(1) / self
        return NAN

    def __repr__(self):
        # 返回整数的字符串表示
        return str(self.__value)

    def __str__(self):
        # 返回整数的字符串表示
        return str(self.__value)

    def print(self, _type=None):
        # 根据指定类型输出整数
        if _type is None:
            _type = str
        if _type == int:
            return self.__value
        if _type == str:
            return str(self.__value)
        if _type == Int:
            return Int(self.__value)


class Float:
    NaN = float('NaN')  # 用于表示非法结果
    __value = 0.0  # 初始值为0.0

    def __init__(self, value=None):
        # 初始化浮点数对象
        # value: 浮点数值或其他可转化为浮点数的对象
        if value is None:
            value = 0.0
        try:
            self.__value = float(value)
        except (ValueError, TypeError):
            self.__value = NAN  # 处理非法输入

    def sum(self, *args):
        # 浮点数求和接口，支持多个浮点数相加
        result = self.__value
        for arg in args:
            try:
                result += float(arg)
            except (ValueError, TypeError):
                return Float(NAN)  # 处理非法输入
        return Float(result)

    def difference(self, *args):
        # 浮点数求差接口，支持多个浮点数相减
        result = self.__value
        for arg in args:
            try:
                result -= float(arg)
            except (ValueError, TypeError):
                return Float(NAN)  # 处理非法输入
        return Float(result)

    def product(self, *args):
        # 浮点数求积接口，支持多个浮点数相乘
        result = self.__value
        for arg in args:
            try:
                result *= float(arg)
            except (ValueError, TypeError):
                return Float(NAN)  # 处理非法输入
        return Float(result)

    def quotient(self, *args):
        # 浮点数求商接口，支持多个浮点数相除
        result = self.__value
        for arg in args:
            try:
                arg_value = float(arg)
                if arg_value == 0.0:
                    return Float(NAN)  # 处理除以0的情况
                result /= arg_value
            except (ValueError, TypeError):
                return Float(NAN)  # 处理非法输入
        return Float(result)

    @property
    def value(self):
        # 获取浮点数值
        return self.__value

    def __float__(self):
        # 转换为浮点数
        return self.__value

    def __int__(self):
        # 转换为整数
        return int(self.__value)

    def __floor__(self):
        # 下舍整数
        return int(self.__value)

    def __abs__(self):
        # 绝对值
        return Float(abs(self.__value))

    def __neg__(self):
        # 取负数
        return Float(-self.__value)

    def __pos__(self):
        # 取正数
        return Float(self.__value)

    def __add__(self, other):
        # 加法运算
        return self.sum(other)

    def __sub__(self, other):
        # 减法运算
        return self.difference(other)

    def __mul__(self, other):
        # 乘法运算
        return self.product(other)

    def __truediv__(self, other):
        # 除法运算
        return self.quotient(other)

    def __floordiv__(self, other):
        # 整除运算
        return Float(self.__value // float(other))

    def __mod__(self, other):
        # 取模运算
        try:
            other_value = float(other)
            if other_value == 0.0:
                return Float(NAN)  # 处理取模0的情况
            return Float(self.__value % other_value)
        except (ValueError, TypeError):
            return Float(NAN)  # 处理非法输入

    def __eq__(self, other):
        # 等于运算
        try:
            other_value = float(other)
            return self.__value == other_value
        except (ValueError, TypeError):
            return False  # 处理非法输入

    def __ne__(self, other):
        # 不等于运算
        return not self.__eq__(other)

    def __lt__(self, other):
        # 小于运算
        try:
            other_value = float(other)
            return self.__value < other_value
        except (ValueError, TypeError):
            return False  # 处理非法输入

    def __le__(self, other):
        # 小于等于运算
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        # 大于运算
        try:
            other_value = float(other)
            return self.__value > other_value
        except (ValueError, TypeError):
            return False  # 处理非法输入

    def __ge__(self, other):
        # 大于等于运算
        return self.__eq__(other) or self.__gt__(other)

    def __invert__(self):
        # 求浮点数的倒数
        if self.__value != 0.0:
            return Float(1.0) / self
        return Float(NAN)

    def __repr__(self):
        # 返回浮点数的字符串表示
        return str(self.__value)

    def __str__(self):
        # 返回浮点数的字符串表示
        return str(self.__value)

    def print(self, _type=None):
        # 根据指定类型输出浮点数
        if _type is None:
            _type = str
        if _type == float:
            return self.__value
        if _type == int:
            return int(self.__value)
        if _type == str:
            return str(self.__value)
        if _type == Float:
            return Float(self.__value)


class Fraction(RationalNumber):
    NaN = float('NaN')
    __m = 0
    __d = 1

    def __init__(self, molecular=None, denominator=None, is_fraction: bool = True):
        # molecular分子,denominator分母
        self.is_fraction = is_fraction
        if not is_fraction:
            return
        if molecular is None:
            molecular = 0
        if denominator is None:
            denominator = 1
        if type(denominator) == Fraction:
            self.is_fraction = False
            _fraction = self.quotient(molecular, denominator)
            molecular, denominator = _fraction._molecular, _fraction._denominator
            self.is_fraction = _fraction.is_fraction
            if not _fraction.is_fraction:
                return
        elif type(molecular) == Fraction:
            _fraction = molecular
            if _fraction.is_fraction:
                molecular, denominator = _fraction.molecular, _fraction.denominator
            else:
                self.is_fraction = False
                return
        try:
            molecular, denominator = float(molecular), float(denominator)
        except TypeError:
            pass
        self._molecular, self._denominator = float(molecular), float(denominator)
        self.reduction()

        super().__init__()

    def reduction(self):  # 约分
        _NaN = NAN
        if self._molecular == self.__m and self._denominator == self.__d:
            return
        molecular, denominator = self._molecular, self._denominator
        if molecular != NAN and denominator != NAN and denominator != 0:
            while molecular % 1 != 0 or denominator % 1 != 0:
                molecular, denominator = molecular * 10, denominator * 10
            r = self.gcd()
            self._molecular, self._denominator = molecular // r, denominator // r
        else:
            self._molecular = _NaN
            self._denominator = _NaN
        self.__m, self.__d = self._molecular, self._denominator

    def gcd(self, _x=None, _y=None):  # 求最大公约数
        if _x and _y:
            _x, _y = int(_x), int(_y)
        else:
            _x, _y = self._molecular, self._denominator
        while _y:
            _x, _y = _y, _x % _y
        return _x

    def sum(self, *_obj):  # 分数求和
        _NaN = NAN
        if self.is_fraction:
            self.reduction()
            _obj = iter([self] + list(_obj))
        else:
            _obj = iter(_obj)
        _x = next(_obj)
        if type(_x) != Fraction:
            _x = Fraction(_x)
        elif not _x.is_fraction:
            return Fraction(is_fraction=False)
        while True:
            try:
                _y = next(_obj)
            except StopIteration:
                break
            if _x._molecular == _NaN:
                break
            if type(_y) != Fraction:
                _y = Fraction(_y)
            elif not _y.is_fraction:
                return Fraction(is_fraction=False)
            molecular = _x._molecular * _y._denominator + _y._molecular * _x._denominator
            denominator = _x._denominator * _y._denominator
            _x = Fraction(molecular=molecular, denominator=denominator)
        return _x

    def difference(self, *_obj):  # 分数求差
        _NaN = NAN
        if self.is_fraction:
            self.reduction()
            _obj = iter([self] + list(_obj))
        else:
            _obj = iter(_obj)
        _x = next(_obj)
        if type(_x) != Fraction:
            _x = Fraction(_x)
        elif not _x.is_fraction:
            return Fraction(is_fraction=False)
        while True:
            try:
                _y = next(_obj)
            except StopIteration:
                break
            if _x._molecular == _NaN:
                break
            if type(_y) != Fraction:
                _y = Fraction(_y)
            elif not _y.is_fraction:
                return Fraction(is_fraction=False)
            molecular = _x._molecular * _y._denominator - _y._molecular * _x._denominator
            denominator = _x._denominator * _y._denominator
            _x = Fraction(molecular=molecular, denominator=denominator)
        return _x

    def product(self, *_obj):  # 分数求积
        _NaN = NAN
        if self.is_fraction:
            self.reduction()
            _obj = iter([self] + list(_obj))
        else:
            _obj = iter(_obj)
        _x = next(_obj)
        if type(_x) != Fraction:
            _x = Fraction(_x)
        elif not _x.is_fraction:
            return Fraction(is_fraction=False)
        while True:
            try:
                _y = next(_obj)
            except StopIteration:
                break
            if _x._molecular == _NaN:
                break
            if type(_y) != Fraction:
                _y = Fraction(_y)
            elif not _y.is_fraction:
                return Fraction(is_fraction=False)
            else:
                _y.reduction()
            molecular = _x._molecular * _y._molecular
            denominator = _x._denominator * _y._denominator
            _x = Fraction(molecular=molecular, denominator=denominator)
        return _x

    def quotient(self, *_obj):  # 分数求商
        _NaN = NAN
        if self.is_fraction:
            self.reduction()
            _obj = iter([self] + list(_obj))
        else:
            _obj = iter(_obj)
        _x = next(_obj)
        if type(_x) != Fraction:
            _x = Fraction(_x)
        elif not _x.is_fraction:
            return Fraction(is_fraction=False)
        while True:
            try:
                _y = next(_obj)
            except StopIteration:
                break
            if _x._molecular == _NaN:
                break
            if type(_y) != Fraction:
                _y = Fraction(_y)
            elif not _y.is_fraction:
                return Fraction(is_fraction=False)
            molecular = _x._molecular * _y._denominator
            denominator = _x._denominator * _y._molecular
            _x = Fraction(molecular=molecular, denominator=denominator)
        return _x

    @property
    def molecular(self):
        return self._molecular

    @molecular.setter
    def molecular(self, molecular):
        try:
            self._molecular = float(molecular)
        except (ValueError, TypeError):
            raise ValueError('%s can\'t be molecular' % molecular)
        else:
            self.reduction()

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        try:
            self._denominator = float(denominator)
        except (ValueError, TypeError):
            raise ValueError('%s can\'t be denominator' % denominator)
        else:
            self.reduction()

    def __int__(self):  # 求整形数
        return int(self._molecular // self._denominator)

    def __float__(self):  # 求近似值
        return self._molecular / self._denominator

    def __floor__(self):  # 下舍整数
        return int(self._molecular // self._denominator)

    def __abs__(self):  # 求绝对值
        fraction = Fraction(self._molecular, self._denominator)
        fraction._molecular = abs(fraction._molecular)
        return fraction

    # 运算符

    def __add__(self, other):  # + 加运算
        return self.sum(other)

    def __sub__(self, other):  # - 减运算
        return self.difference(other)

    def __mul__(self, other):  # * 乘运算
        return self.product(other)

    def __truediv__(self, other):  # / 分数除法运算(返回分数)
        return self.quotient(other)

    def __floordiv__(self, other):  # // 分数整除运算(返回整数)
        return int(self.quotient(other))

    def __mod__(self, other):  # % 取模运算(返回整数)
        return self.difference(self, int(self.quotient(other)))

    # 一元运算符

    def __neg__(self):  # - 取负
        return Fraction(-self._molecular, self._denominator, is_fraction=self.is_fraction)

    def __pos__(self):  # + 取正
        return Fraction(self._molecular, self._denominator, is_fraction=self.is_fraction)

    # 比较运算符

    def __eq__(self, other):  # ==
        if type(other) != Fraction:
            other = Fraction(other)
        elif not self.is_fraction:
            return False
        else:
            self.reduction()
        if not other.is_fraction:
            return False
        else:
            other.reduction()
        if self._molecular * other._denominator == self._denominator * other._molecular:
            return True
        return False

    def __ne__(self, other):  # !=
        return bool(~self.__eq__(other) + 2)

    def __lt__(self, other):  # <
        if type(other) != Fraction:
            other = Fraction(other)
        elif not self.is_fraction:
            return False
        else:
            self.reduction()
        if not other.is_fraction:
            return False
        else:
            other.reduction()
        if self._molecular * other._denominator < self._denominator * other._molecular:
            return True
        return False

    def __le__(self, other):  # <=
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):  # >
        if type(other) != Fraction:
            other = Fraction(other)
        elif not self.is_fraction:
            return False
        if not other.is_fraction:
            return False
        if self._molecular * other._denominator > self._denominator * other._molecular:
            return True
        return False

    def __ge__(self, other):  # >=
        return self.__eq__(other) or self.__gt__(other)

    def __invert__(self):  # ~ 取倒数
        return Fraction(self._denominator, self._molecular, is_fraction=self.is_fraction)

    def __repr__(self):
        if self.is_fraction:
            return '%d/%d' % (self._molecular, self._denominator)
        else:
            return 'NaF'

    def __str__(self):
        if self.is_fraction:
            return '%d/%d' % (self._molecular, self._denominator)
        else:
            return 'NaF'

    def print(self, _type=None):
        if _type is None:
            _type = str
        if _type == int:
            return self._molecular, self._denominator
        if _type == str:
            return '%d/%d' % (self._molecular, self._denominator)
        if _type == Fraction:
            return Fraction(self)


class Stake:
    stake = []  # 栈列表，用于存储元素
    top = lenght = 0  # 栈顶指针和长度

    def push(self, obj):
        stake, top, lenght = self.stake, self.top, self.lenght

        # 如果栈顶指针大于等于栈的长度减1，表示栈已满，需要扩展栈的长度
        if top >= lenght - 1:
            stake.append(obj)  # 将 obj 添加到栈的末尾
            top, lenght = lenght, lenght + 1  # 更新栈顶指针和栈的长度
        else:
            top += 1  # 栈顶指针加1
            stake[top] = obj  # 将 obj 放入栈中的指定位置

        self.stake, self.top, self.lenght = stake, top, lenght  # 更新类属性
        return obj  # 返回被入栈的对象 obj

    def pop(self):
        stake, top = self.stake, self.top

        # 如果栈顶指针小于0，表示栈为空，无法出栈，返回 None
        if top < 0:
            return None
        else:
            _result = stake[top]  # 从栈中取出栈顶元素
            top -= 1  # 栈顶指针减1
            self.top = top  # 更新类属性中的栈顶指针
            return _result  # 返回被出栈的元素


def calc_format(obj: str):
    # 去掉字符串末尾的等号字符 '='
    while obj[-1] == '=':
        obj = obj[:-1]

    # 将字符串中的 'log10' 替换为 'logX'
    obj = obj.replace('log10', 'logX')

    # 将字符串中的 'log2' 替换为 'logII'
    obj = obj.replace('log2', 'logII')

    # 在整个字符串外加上圆括号 '(' 和 ')'
    obj = '(' + obj + ')'

    i = 0
    while i < len(obj) - 1:
        # 处理数字后面跟着小数点的情况，补充缺失的零
        if obj[i] not in '1234567890' and obj[i + 1] == '.':
            obj = obj[:i + 1] + '0' + obj[i + 1:]

        # 处理小数点后面不是数字的情况，补充缺失的零
        if obj[i] == '.' and obj[i + 1] not in '1234567890':
            obj = obj[:i + 1] + '0' + obj[i + 1:]

        # 将连续的两个乘号 '**' 替换为 '^'
        if obj[i] == obj[i + 1] == '*':
            obj = obj[:i] + '^' + obj[i + 2:]

        # 将连续的两个除号 '//' 替换为 '|'
        if obj[i] == obj[i + 1] == '/':
            obj = obj[:i] + '|' + obj[i + 2:]

        # 将方括号 '[' 或 '{' 替换为 '('
        if obj[i] in '[{':
            obj = obj[:i] + '(' + obj[i + 1:]

        # 将方括号 ']' 或 '}' 替换为 ')'
        if obj[i] in ']}':
            obj = obj[:i] + ')' + obj[i + 1:]

        # 处理连续的两个减号 '--'，将其替换为加号 '+'
        if obj[i] == obj[i + 1] == '-':
            obj = obj[:i] + '+' + obj[i + 2:]

            # 如果前一个字符和当前字符都是加号 '+'
            # 则将前一个加号去除，并继续处理下一个字符
            if obj[i - 1] == obj[i] == '+':
                obj = obj[:i] + obj[i + 1:]
                continue

        # 处理连续的两个加号 '++'，将其替换为空字符 ''
        if obj[i] == obj[i + 1] == '+':
            obj = obj[:i] + obj[i + 1:]
            continue

        # 处理加号 '+' 和减号 '-' 之间的情况，将加号去除
        if obj[i] == '+' and obj[i + 1] == '-':
            obj = obj[:i] + obj[i + 1:]
            continue

        # 处理操作符前面是左括号并且后面是减号 '-' 的情况，
        # 将减号替换为零 '0'
        if obj[i] in '([{' and obj[i + 1] == '-':
            obj = obj[:i + 1] + '0' + obj[i + 1:]

        # 处理减号 '-' 后面不是括号或数字的情况，
        # 在减号后添加一个零 '0'，然后补全括号
        if obj[i + 1] == '-' and not obj[i] in '()[]{}1234567890':
            obj = obj[:i + 1] + '(0' + obj[i + 1:]
            j = i + 4
            parentheses = 0
            while True:
                j += 1
                if j >= len(obj):
                    break
                if obj[j] in '([{':
                    parentheses += 1
                if obj[j] in ')]}':
                    parentheses -= 1
                if obj[j] in '+-' and not parentheses:
                    break
            obj = obj[:j] + ')' + obj[j:]

        # 处理百分号 '%' 前面是数字而后面不是括号或数字的情况，
        # 将百分号替换为乘号 '*' 和 0.01，然后补全括号
        if i > 0 and obj[i - 1] in '1234567890' and obj[i] == '%' and not obj[i + 1] in '([{1234567890':
            obj = obj[:i] + '*0.01)' + obj[i + 1:]
            j, i = i - 2, i - 1
            while obj[j] in '1234567890.':
                j -= 1
                if j < 0:
                    break
            obj = obj[:j + 1] + '(' + obj[j + 1:]

        # 处理连续的感叹号 '!' 和数字的情况，将感叹号替换为乘号 '*'
        elif obj[i] == '!' and obj[i + 1] in '1234567890':
            obj = obj[:i + 1] + '*' + obj[i + 1:]

        # 处理右括号、右方括号和右大括号之后紧跟左括号、左方括号和左大括号的情况，
        # 在右括号后添加乘号 '*'
        if obj[i] in ')]}' and obj[i + 1] in '([{':
            obj = obj[:i + 1] + '*' + obj[i + 1:]

        # 处理右括号、右方括号和右大括号之后紧跟数字的情况，
        # 在右括号后添加乘号 '*'
        if obj[i] in ')]}' and obj[i + 1] in '1234567890':
            obj = obj[:i + 1] + '*' + obj[i + 1:]

        # 处理 'pi' 后面的情况，根据前一个字符是数字还是其他字符来添加乘号 '*'
        if i > 0 and obj[i] + obj[i + 1] == 'pi':
            if obj[i - 1] in '1234567890':
                obj = obj[:i] + '*' + str(math.pi) + obj[i + 2:]
            else:
                obj = obj[:i] + str(math.pi) + obj[i + 2:]

        # 处理 'e' 后面的情况，根据前一个字符是数字还是其他字符来添加乘号 '*'
        if obj[i + 1] == 'e':
            if obj[i] in '1234567890':
                obj = obj[:i + 1] + '*' + str(math.e) + obj[i + 2:]
            else:
                obj = obj[:i + 1] + str(math.e) + obj[i + 2:]

        i += 1  # 移动到下一个字符继续处理

    return obj  # 返回格式化后的字符串


def calc_check(obj: str, keys: list):
    obj = list(obj)  # 将输入的字符串转换为字符列表以便逐个字符处理
    numbers = '1234567890.'  # 数字的字符集合
    symbol_set = set(''.join(keys))  # 将操作符列表合并为一个字符集合
    parentheses = 0  # 用于跟踪括号的数量

    # 遍历输入字符串中的每个字符
    for t in obj:
        # 如果字符不在操作符集合或数字字符集合中，返回 False
        if t not in symbol_set and t not in numbers:
            return False

        # 统计左括号的数量
        if t == '(':
            parentheses += 1

        # 统计右括号的数量，并检查括号的匹配性
        if t == ')':
            parentheses -= 1
            if parentheses < 0:  # 如果出现多余的右括号，返回 False
                return False

    # 如果最终左右括号数量不匹配，返回 False
    if parentheses != 0:
        return False

    i = 0
    while i < len(obj):
        j = ''

        # 遍历数字字符并将它们组合成一个数字
        while i < len(obj) and obj[i] in numbers:
            j += obj[i]
            i += 1

        # 如果 j 不为空，尝试将其转换为浮点数，如果不能转换则返回 False
        if j != '':
            try:
                float(j)
            except ValueError:
                return False

        j = ''

        # 继续遍历非数字字符
        while i < len(obj) and obj[i] not in numbers:
            j += obj[i]
            i += 1

        t = ''

        # 对 j 进行操作符匹配检查
        while len(j):
            for k in keys:
                if ''.join(j[:len(k)]) == k:
                    t = k

            # 如果没有找到匹配的操作符，返回 False
            if t == '':
                return False

            j = j[len(t):]  # 从 j 中去除已匹配的操作符

    # 如果通过了所有检查，返回 True，表示输入字符串合法
    return True


def calc_calculation(number_stake, top_n, symbol):
    __x = 0

    # 检查 symbol 是否是支持的运算符
    if symbol in ('+', '-', '*', '/', '%', '^', '|'):
        # 如果是二元运算符（+、-、*、/、%、^、|），则从操作数栈取出两个操作数
        number2 = number_stake[top_n]
        top_n -= 1
        number1 = number_stake[top_n]

        # 根据运算符计算结果并赋值给 __x
        if symbol == '+':
            __x = number1 + number2
        elif symbol == '-':
            __x = number1 - number2
        elif symbol == '*':
            __x = number1 * number2
        elif symbol == '/':
            if number2 == 0:
                __x = 'nan'  # 处理除以零的情况，结果为 'nan'（非数值）
            else:
                __x = number1 / number2
        elif symbol == '%':
            if number2 == 0:
                __x = 'nan'  # 处理模除零的情况，结果为 'nan'
            else:
                __x = number1 % number2
        elif symbol == '^':
            if number1 == number2 == 0:
                __x = 'nan'  # 处理 0^0 的情况，结果为 'nan'
            else:
                __x = number1 ** number2
        elif symbol == '|':
            if number2 == 0:
                __x = 'nan'  # 处理整除零的情况，结果为 'nan'
            else:
                __x = number1 // number2  # 整数除法

    else:
        # 如果是一元运算符，从操作数栈取出一个操作数
        number1 = number_stake[top_n]

        # 根据运算符计算结果并赋值给 __x
        if symbol == '!':
            __x = math.factorial(number1)  # 阶乘运算
        elif symbol == 'sin':
            __x = math.sin(number1)  # 正弦函数
        elif symbol == 'cos':
            __x = math.cos(number1)  # 余弦函数
        elif symbol == 'tan':
            __x = math.tan(number1)  # 正切函数
        elif symbol == 'logII':
            __x = math.log2(number1)  # 以2为底的对数
        elif symbol == 'logX':
            __x = math.log10(number1)  # 以10为底的对数

    # 将计算结果 __x 存入操作数栈
    number_stake[top_n] = __x

    # 返回更新后的操作数栈和栈顶指针
    return number_stake, top_n


def calc_stringBoom(obj: str, keys: list):
    _list = []  # 用于存储分割后的字符串片段
    t = ''  # 临时变量，用于存储匹配的操作符

    while len(obj):
        for i in keys:
            if obj[:len(i)] == i:  # 如果字符串以当前操作符开头
                t = i  # 将匹配到的操作符赋值给 t
        _list.append(t)  # 将匹配到的操作符添加到列表 _list
        obj = obj[len(t):]  # 从原字符串中移除已匹配的操作符

    return _list  # 返回包含操作符的列表


def calc_main(obj, _format=True, check=True, format_in_return=False):
    if _format:
        if format_in_return:
            obj = format_in_return = calc_format(obj=obj)  # 格式化输入字符串，并根据需要更新返回值
        else:
            obj = calc_format(obj=obj)  # 仅格式化输入字符串

    symbol_list = ['(', ')', '+', '-', '*', '/', '%', '^', '|', '!', 'sin', 'cos', 'tan', 'logII', 'logX']

    # 如果启用检查，并且输入字符串中存在不支持的操作符，则返回错误
    if check and not calc_check(obj=obj, keys=symbol_list):
        return 'Error'

    # 定义运算符的优先级和关联性
    symbol_tuple = (
        ['(', ')'],
        ['+', '-'],
        ['*', '/', '%', '|'],
        ['^'],
        ['!', 'sin', 'cos', 'tan', 'logII', 'logX']
    )
    symbol_dict = {}

    # 构建运算符字典，用于比较优先级
    for i in range(len(symbol_tuple)):
        for t in symbol_tuple[i]:
            symbol_dict[t] = i

    numbers = '1234567890.'
    number_stake, symbol_stake = [], []
    i = top_n = len_n = top_s = len_s = 0

    while i < len(obj):
        n = ''
        while i < len(obj) and obj[i] in numbers:
            n += obj[i]
            i += 1
        if n != '':
            if top_n >= len_n - 1:
                number_stake.append(float(n))
                top_n, len_n = len_n, len_n + 1
            else:
                top_n += 1
                number_stake[top_n] = float(n)

        s = ''
        while i < len(obj) and obj[i] not in numbers:
            s += obj[i]
            i += 1
        s = calc_stringBoom(s, symbol_list)

        for j in s:
            if len_s == 0:
                symbol_stake.append(j)
                top_s, len_s = len_s, len_s + 1
                continue

            if j == '(':
                if top_s >= len_s - 1:
                    symbol_stake.append(j)
                    top_s, len_s = len_s, len_s + 1
                else:
                    top_s += 1
                    symbol_stake[top_s] = j
                continue

            # 处理运算符优先级，确保正确地计算顺序
            while symbol_dict[symbol_stake[top_s]] >= symbol_dict[j]:
                if j == ')' and symbol_stake[top_s] == '(':
                    top_s -= 1
                    break

                # 执行计算并更新操作数栈
                number_stake, top_n = calc_calculation(number_stake, top_n, symbol_stake[top_s])

                # 如果结果包含 'nan'，则返回 'nan'
                if 'nan' in number_stake:
                    return 'nan'
                top_s -= 1

            if j != ')':
                if top_s >= len_s - 1:
                    symbol_stake.append(j)
                    top_s, len_s = len_s, len_s + 1
                else:
                    top_s += 1
                    symbol_stake[top_s] = j

    if format_in_return:
        return number_stake[:top_n + 1] + [format_in_return]  # 返回结果列表，包含格式化后的字符串
    else:
        return number_stake[:top_n + 1]  # 返回结果列表，不包含格式化后的字符串


def calculate(__obj: str, _format: bool = True, check: bool = True, format_in_return: bool = False):
    """
    计算数学表达式的值

    Parameters:
        __obj (str): 要计算的数学表达式。
        _format (bool, optional): 是否对输入表达式进行格式化，默认为True。
        check (bool, optional): 是否进行语法检查，默认为True。
        format_in_return (bool, optional): 是否在返回结果中包含格式化后的字符串，默认为False。

    Returns:
        list or str: 计算结果。如果格式化后的字符串在结果中，则返回包含格式化字符串的列表，否则返回计算结果的列表

    Example:
        expression_list = ["1+1*2", "(1+1)*2", "2pi", "e^4", "sin(1)", "cos(1)", "tan(1)", "log2(2)", "log10(2)"]
        # 批量计算数学表达式
        for _e in expression_list:
            result = calculate(__obj=_e, format_in_return=True)
            if type(result[0]) == str:
                print(result[0])
            else:
                for value in result:
                    print(value)
    """
    return calc_main(obj=__obj, _format=_format, check=check, format_in_return=format_in_return)


def test():
    expression_list = ["1+1*2", "(1+1)*2", "2pi", "e^4", "sin(1)", "cos(1)", "tan(1)", "log2(2)", "log10(2)"]
    # 批量计算数学表达式
    for _e in expression_list:
        result = calculate(__obj=_e, format_in_return=True)
        if type(result[0]) == str:
            print(result[0])
        else:
            for value in result:
                print(value)


# 实装部分
if __name__ == '__main__':
    a = 'e'
    print(a)
    x = calculate(__obj=a, format_in_return=True)
    if type(x[0]) == str:
        print(x)
    else:
        for x in x:
            print(x)
    a = 'pi'
    print(a)
    x = calculate(__obj=a, format_in_return=True)
    if type(x[0]) == str:
        print(x)
    else:
        for x in x:
            print(x)
    while True:
        a = input()
        if a == '':
            break
        x = calculate(__obj=a, format_in_return=True)
        if type(x[0]) == str:
            print(x)
        else:
            for x in x:
                print(x)
