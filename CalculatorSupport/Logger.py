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
import io
from typing import Callable


class Message(str):
    INFO = 0
    WARNING = 1
    CALC_ERROR = 2
    PYTHON_ERROR = 3
    DEBUG = -1

    DEFAULT = INFO

    def __init__(self, _object, tag: (INFO, WARNING, CALC_ERROR, PYTHON_ERROR, DEBUG) = DEFAULT):
        super().__init__()
        self.tag: (Message.INFO, Message.WARNING, Message.CALC_ERROR, Message.PYTHON_ERROR, Message.DEBUG) = tag

    def __new__(cls, _object, *args, **kwargs):
        return str.__new__(cls, _object)

    def is_INFO(self):
        return self.tag == Message.INFO

    def is_WARNING(self):
        return self.tag == Message.WARNING

    def is_CALC_ERROR(self):
        return self.tag == Message.CALC_ERROR

    def is_PYTHON_ERROR(self):
        return self.tag == Message.PYTHON_ERROR

    def is_DEBUG(self):
        return self.tag == Message.DEBUG

    # @property
    # def __class__(self):
    #     return super().__class__


# noinspection GrazieInspection
class Logger:
    MESSAGE_TYPE = Message
    DEFAULT_LOG_FUNCTION: Callable = lambda *args, **kwargs: print(*args, **kwargs)

    def __init__(self, output=None):
        """
        初始化 SimpleLogger 类

        :param output: 输出流对象，如文件对象。如果为 None，则默认使用 print 输出
        """
        self._output: io.IOBase | None = output
        self.info_output: io.IOBase | None = None
        self.warning_output: io.IOBase | None = None
        self.calc_error_output: io.IOBase | None = None
        self.python_error_output: io.IOBase | None = None
        self.debug_output: io.IOBase | None = None

        self.position: int = 0

    def log(self, message,
            tag: (Message.INFO,
                  Message.WARNING,
                  Message.CALC_ERROR,
                  Message.PYTHON_ERROR,
                  Message.DEBUG) = Message.DEFAULT,
            end: str = "\n"):
        """
        记录日志消息

        :param message: 要记录的消息
        :param tag: 日志级别
        :param end: 换行符
        :return: None
        """
        message = self.MESSAGE_TYPE(str(message) + end, tag=tag)
        if self._output is not None:
            self._output.write(message)
            self._output.flush()
        else:
            self.DEFAULT_LOG_FUNCTION(message)
        if self.info_output is not None and message.is_INFO():
            self.info_output.write(message)
            self.info_output.flush()
        if self.warning_output is not None and message.is_WARNING():
            self.warning_output.write(message)
            self.warning_output.flush()
        if self.calc_error_output is not None and message.is_CALC_ERROR():
            self.calc_error_output.write(message)
            self.calc_error_output.flush()
        if self.python_error_output is not None and message.is_PYTHON_ERROR():
            self.python_error_output.write(message)
            self.python_error_output.flush()
        if self.debug_output is not None and message.is_DEBUG():
            self.debug_output.write(message)
            self.debug_output.flush()

    def log_info(self, message):
        """
        记录INFO日志消息
        """
        self.log(message, tag=Message.INFO)

    def log_warning(self, message):
        """
        记录WARNING日志消息
        """
        self.log(message, tag=Message.WARNING)

    def log_calc_error(self, message):
        """
        记录CALC_ERROR日志消息
        """
        self.log(message, tag=Message.CALC_ERROR)

    def log_python_error(self, message):
        """
        记录PYTHON_ERROR日志消息
        """
        self.log(message, tag=Message.PYTHON_ERROR)

    def log_debug(self, message):
        """
        记录DEBUG日志消息
        """
        self.log(message, tag=Message.DEBUG)

    def setIO(self, output=None):
        """
        设置或重置输出流对象

        :param output: 新的输出流对象，如文件对象。如果为 None，则将输出重置为默认的 print 输出
        :return: None
        """
        self._output = output

    def currentIO(self):
        """
        获取当前的输出流对象。如果没有指定输出流对象，则返回默认的 print 输出

        :return: 当前的输出流对象或 None（代表默认的 print 输出）
        """
        return self._output

    def create_string_io(self):
        """
        创建自定义内存输出流实例

        :return: io.StringIO
        """
        _io = io.StringIO()
        self.setIO(_io)
        return _io

    def create_file_io(self, file: str, mode: str = 'w', encoding: str = None, newline: str = None):
        """
        创建自定义文件输出流实例

        :param file: 文件路径
        :param mode: 打开文件模式，默认为 'w'
        :param encoding: 编码
        :param newline: 换行符
        :return: io.IOBase
        """
        _io = open(file, mode, encoding=encoding, newline=newline)
        self.setIO(_io)
        return _io

    def read(self):
        """
        读取日志IO

        :return: str
        """
        if self._output:
            if isinstance(self._output, io.StringIO):
                content = self._output.getvalue()
            elif isinstance(self._output, io.FileIO):
                content = self._output.readall()
            else:
                content = self._output.read()
            position = self.position
            self.position = len(content)
            return content[position:]
        else:
            return ""

    def __call__(self, message):
        """
        记录日志消息

        :param message: 要记录的消息
        :return: None
        """
        self.log(message)


class CustomLogIO(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = 0

    def write(self, message):
        self.append(message)

    def flush(self):
        pass

    def __call__(self, message):
        self.write(message)

    def read(self):
        position = self.position
        self.position = len(self)
        return "".join(self[position:])

    def readline(self):
        position = self.position
        self.position += 1
        return self[position]

    def readlines(self):
        position = self.position
        self.position = len(self)
        return self[position:]


def test():
    log = Logger()
    log.create_string_io()
    log.info_output = io.StringIO()
    log.warning_output = io.StringIO()
    log.calc_error_output = io.StringIO()
    log.python_error_output = io.StringIO()
    log.debug_output = io.StringIO()
    log("line1")
    log.log("line2")
    log.log_info("line: info")
    log.log_warning("line: warning")
    log.log_calc_error("line: calc_error")
    log.log_python_error("line: python_error")
    log.log_debug("line: debug")
    print(f"log: {log.read()}")
    log.info_output.seek(0)
    print(f"info: {log.info_output.read()}")
    log.warning_output.seek(0)
    print(f"warning: {log.warning_output.read()}")
    log.calc_error_output.seek(0)
    print(f"calc_error: {log.calc_error_output.read()}")
    log.python_error_output.seek(0)
    print(f"python_error: {log.python_error_output.read()}")
    log.debug_output.seek(0)
    print(f"debug: {log.debug_output.read()}")


def test2():
    log = Logger()
    log.setIO(CustomLogIO())
    log("line1")
    log.log("line2")
    log.log_info("line: info")
    log.log_warning("line: warning")
    log.log_calc_error("line: calc_error")
    log.log_python_error("line: python_error")
    log.log_debug("line: debug")
    for line in log.currentIO().readlines():
        line: Message
        print(line, line.tag)
