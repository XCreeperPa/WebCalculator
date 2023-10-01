import io


class Logger:
    def __init__(self, output=None):
        """
        初始化 SimpleLogger 类。

        :param output: 输出流对象，如文件对象。如果为 None，则默认使用 print 输出。
        """
        self._output: io.IOBase | None = output

    def log(self, message):
        """
        记录日志消息。

        :param message: 要记录的消息。
        :return: None
        """
        if self._output:
            self._output.write(message + "\n")
            self._output.flush()
        else:
            print(message)

    def setIO(self, output=None):
        """
        设置或重置输出流对象。

        :param output: 新的输出流对象，如文件对象。如果为 None，则将输出重置为默认的 print 输出。
        :return: None
        """
        self._output = output

    def currentIO(self):
        """
        获取当前的输出流对象。如果没有指定输出流对象，则返回默认的 print 输出。

        :return: 当前的输出流对象或 None（代表默认的 print 输出）。
        """
        return self._output

    def create_string_io(self):
        """
        创建自定义内存输出流实例。

        :return: io.StringIO
        """
        _io = io.StringIO()
        # _io.write("test")
        self.setIO(_io)
        return _io

    def create_file_io(self, file: str, mode: str = 'w', encoding: str = None, newline: str = None):
        """
        创建自定义文件输出流实例。

        :param file: 文件路径。
        :param mode: 打开文件模式，默认为 'w'。
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
            self._output.seek(0)
            return self._output.read()
        else:
            return ""

    def readline(self):
        """
        readline读取日志IO

        :return: str
        """
        if self._output:
            return self._output.readline()
        else:
            return ""

    def readlines(self):
        """
        按行读取日志IO，返回一个包含所有行的列表。

        :return: List[str]
        """
        if self._output:
            self._output.seek(0)
            return self._output.readlines()
        else:
            return []

    def __call__(self, message):
        """
        记录日志消息。

        :param message: 要记录的消息。
        :return: None
        """
        self.log(message)
