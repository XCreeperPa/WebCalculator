from Constants import *


class RationalNumber:
    def __init__(self):
        pass


class Int(RationalNumber):
    __value = 0  # 初始值为0

    def __init__(self, value):
        # 初始化整数对象
        # value: int或其他可转化为整数的对象
        if value is None:
            value = 0
        try:
            self.__value = int(value)
        except (ValueError, TypeError):
            self.__value = NAN  # 处理非法输入
        super().__init__()

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


class Float(RationalNumber):
    def __init__(self, value=None):
        # 初始化浮点数对象
        # value: 浮点数值或其他可转化为浮点数的对象
        if value is None:
            value = 0.0
        try:
            self.__value = float(value)
        except (ValueError, TypeError):
            self.__value = NAN  # 处理非法输入
        super().__init__()

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
        return Int(self.__value)

    def __floor__(self):
        # 下舍整数
        return Int(self.__value)

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
        if _type == Int:
            return Int(self.__value)
        if _type == Fraction:
            return Fraction(self.__value)
        if _type == int:
            return int(self.__value)
        if _type == str:
            return str(self.__value)
        if _type == Float:
            return Float(self.__value)


class Fraction(RationalNumber):
    __m = 0
    __d = 1

    def __init__(self, molecular=None, denominator=None):
        # molecular分子,denominator分母
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
        self._molecular, self._denominator = Float(molecular), Float(denominator)
        self.reduction()

        super().__init__()

    def reduction(self):  # 约分
        if self._molecular == self.__m and self._denominator == self.__d:
            return
        molecular, denominator = self._molecular, self._denominator
        if molecular != NAN and denominator != NAN and denominator != 0:
            while molecular % 1 != 0 or denominator % 1 != 0:
                molecular, denominator = molecular * 10, denominator * 10
            r = self.gcd()
            self._molecular, self._denominator = molecular // r, denominator // r
        else:
            self._molecular = NAN
            self._denominator = NAN
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
        if self.is_fraction:
            self.reduction()
            _obj = iter([self] + list(_obj))
        else:
            _obj = iter(_obj)
        _x = next(_obj)
        if type(_x) != Fraction:
            _x = Fraction(_x)
        while True:
            try:
                _y = next(_obj)
            except StopIteration:
                break
            if _x._molecular == NAN:
                break
            if type(_y) != Fraction:
                _y = Fraction(_y)
            molecular = _x._molecular * _y._denominator + _y._molecular * _x._denominator
            denominator = _x._denominator * _y._denominator
            _x = Fraction(molecular=molecular, denominator=denominator)
        return _x

    def difference(self, *_obj):  # 分数求差
        if self.is_fraction:
            self.reduction()
            _obj = iter([self] + list(_obj))
        else:
            _obj = iter(_obj)
        _x = next(_obj)
        if type(_x) != Fraction:
            _x = Fraction(_x)
        while True:
            try:
                _y = next(_obj)
            except StopIteration:
                break
            if _x._molecular == NAN:
                break
            if type(_y) != Fraction:
                _y = Fraction(_y)
            molecular = _x._molecular * _y._denominator - _y._molecular * _x._denominator
            denominator = _x._denominator * _y._denominator
            _x = Fraction(molecular=molecular, denominator=denominator)
        return _x

    def product(self, *_obj):  # 分数求积
        if self.is_fraction:
            self.reduction()
            _obj = iter([self] + list(_obj))
        else:
            _obj = iter(_obj)
        _x = next(_obj)
        if type(_x) != Fraction:
            _x = Fraction(_x)
        while True:
            try:
                _y = next(_obj)
            except StopIteration:
                break
            if _x._molecular == NAN:
                break
            if type(_y) != Fraction:
                _y = Fraction(_y)
            else:
                _y.reduction()
            molecular = _x._molecular * _y._molecular
            denominator = _x._denominator * _y._denominator
            _x = Fraction(molecular=molecular, denominator=denominator)
        return _x

    def quotient(self, *_obj):  # 分数求商
        if self.is_fraction:
            self.reduction()
            _obj = iter([self] + list(_obj))
        else:
            _obj = iter(_obj)
        _x = next(_obj)
        if type(_x) != Fraction:
            _x = Fraction(_x)
        while True:
            try:
                _y = next(_obj)
            except StopIteration:
                break
            if _x._molecular == NAN:
                break
            if type(_y) != Fraction:
                _y = Fraction(_y)
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
        return Int(self._molecular // self._denominator)

    def __float__(self):  # 求近似值
        return self._molecular / self._denominator

    def __floor__(self):  # 下舍整数
        return Int(self._molecular // self._denominator)

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
        return Int(self.quotient(other))

    def __mod__(self, other):  # % 取模运算(返回整数)
        return self.difference(self, Int(self.quotient(other)))

    # 一元运算符

    def __neg__(self):  # - 取负
        return Fraction(-self._molecular, self._denominator)

    def __pos__(self):  # + 取正
        return Fraction(self._molecular, self._denominator)

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
        return Fraction(self._denominator, self._molecular)

    def __repr__(self):
        return f'{self._molecular}/{self._denominator}'

    def __str__(self):
        return f'{self._molecular}/{self._denominator}'

    def print(self, _type=None):
        if _type is None:
            _type = str
        if _type == Int:
            return self.__int__()
        if _type == Float:
            return self.__float__()
        if _type == int:
            return self._molecular, self._denominator
        if _type == float:
            return self.__float__()
        if _type == str:
            return self.__str__()
        if _type == Fraction:
            return Fraction(self)
