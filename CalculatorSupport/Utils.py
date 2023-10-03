def debug(func, func_args: (list, tuple) = None, func_kwargs: dict = None,
          snooper_args: (list, tuple) = None, snooper_kwargs: dict = None):
    """Power by PySnooper(pysnooper.snoop)"""
    import pysnooper
    if func_args is None:
        func_args = []
    if func_kwargs is None:
        func_kwargs = {}
    if snooper_args is None:
        snooper_args = []
    if snooper_kwargs is None:
        snooper_kwargs = {}
    return pysnooper.snoop(*snooper_args, **snooper_kwargs)(func)(*func_args, **func_kwargs)


class FindHeadMatchingParentheses:
    bracket = {"(": ")", "[": "]", "{": "}"}

    def __init__(self, _str: str):
        self.last_bracket_index: int | None = None
        self.sub_str: str | None = None
        stack = []
        for i, _char in enumerate(_str):
            if _char in self.bracket:
                stack.append(_char)
            elif _char in self.bracket.values() and self.bracket[stack[-1]] == _char:
                stack.pop()
                if len(stack) <= 0:
                    self.last_bracket_index = i
                    self.sub_str = _str[:i + 1]
                    return


def find_all_subclasses(cls) -> list:
    subclasses = list(cls.__subclasses__())
    for subclass in subclasses:
        # Recursively call to get all subclasses
        subclasses.extend(find_all_subclasses(subclass))
    return subclasses


def capture_print_to_file(log_filename):
    """
    # 使用函数，传递日志文件名
    close_log = capture_print_to_file('my_log_file.txt')
    # 使用print打印消息，将同时输出到控制台和文件
    print("This message will be captured by both console and file.")
    # 在结束时关闭文件并恢复sys.stdout
    close_log()
    """
    import sys

    # 打开文件以捕获print输出
    log_file = open(log_filename, 'w', encoding='utf-8')

    # 自定义输出流，将输出同时发送到控制台和文件
    class DualOutput:
        def __init__(self, *outputs):
            self.outputs = outputs

        def write(self, text):
            for output in self.outputs:
                output.write(text)

        def flush(self):
            for output in self.outputs:
                output.flush()

    # 创建自定义输出流实例
    dual_output = DualOutput(sys.stdout, log_file)

    # 将sys.stdout重定向到自定义输出流
    sys.stdout = dual_output

    # 返回关闭文件的函数，以便在结束时关闭文件
    def close_log_file():
        log_file.close()
        # 恢复sys.stdout到原始状态
        sys.stdout = sys.__stdout__

    return close_log_file
