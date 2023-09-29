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
